# Build the bounded PowerPC payload using the supported retail binding and selected
# transport mode. Link addresses, cache ranges and guarded instruction metadata must stay
# aligned with the loader. Boundary names here: RelocatedRuntimeBuildResult, parse_args,
# build_prime3_runtime_payload, main.
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import os
import subprocess
import sys
from pathlib import Path
from typing import Any

if __package__ in {None, ""}:
    _repository_root = Path(__file__).resolve().parents[2]
    _repository_root_str = os.fspath(_repository_root)
    if _repository_root_str not in sys.path:
        sys.path.insert(0, _repository_root_str)

from nullphaze_network.prime3_wii_runtime.protocol import (
    CRC_SIZE,
    DEFAULT_RUNTIME_BUILD_ID,
    GAME_IDENTITY_FIELD_OFFSETS,
    GAME_IDENTITY_PAYLOAD_SIZE,
    GAME_IDENTITY_SCHEMA_VERSION,
    HEADER_SIZE,
    INVENTORY_FIELD_OFFSETS,
    INVENTORY_FRAME_SIZE,
    INVENTORY_ITEM_IDS,
    INVENTORY_PAYLOAD_SIZE,
    INVENTORY_RECORD_COUNT,
    INVENTORY_RECORD_SIZE,
    INVENTORY_SCHEMA_VERSION,
    PRIME3_NTSC_RETAIL_PROFILE_FINGERPRINT,
    PRIME3_NTSC_RETAIL_PROFILE_ID,
    PROTOCOL_MAGIC,
    PROTOCOL_VERSION,
    Prime3WiiAvailability,
    Prime3WiiCapability,
    Prime3WiiCommand,
    Prime3WiiGameId,
    Prime3WiiInventoryAvailability,
    Prime3WiiPlatformId,
    Prime3WiiRegionId,
    Prime3WiiRevisionId,
)
from nullphaze_network.prime3_wii_runtime.runtime_payload import (
    PRIME3_RUNTIME_CONTINUE_MODES,
    PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES,
    PRIME3_RUNTIME_ENTRY_SYMBOL,
    PRIME3_RUNTIME_HALT_MODES,
    PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_CONTINUE,
    PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL,
    PRIME3_RUNTIME_PAYLOAD_MODE_PROBE,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT,
    PRIME3_RUNTIME_PAYLOAD_SCHEMA_VERSION,
    PRIME3_RUNTIME_RELOCATED_MODES,
    PRIME3_RUNTIME_REQUIRED_ALIGNMENT,
    PRIME3_RUNTIME_TARGET_ABI,
    PRIME3_RUNTIME_TARGET_ARCHITECTURE,
    PRIME3_RUNTIME_TARGET_ENDIANNESS,
    LegacyPrime3RuntimeTransportMetadata,
    Prime3EntryBootstrapMetadata,
    Prime3RelocatedRuntimeMetadata,
    Prime3RetailIosWrapperMetadata,
    Prime3RuntimeAbiProbeMetadata,
    Prime3RuntimeDiagnosticMetadata,
    Prime3RuntimeGameIdentityMetadata,
    Prime3RuntimeInventoryMetadata,
    Prime3RuntimePayloadManifest,
    Prime3RuntimePayloadPatchField,
    Prime3RuntimeTransportMetadata,
    compute_cache_range,
    compute_source_digest,
)
from randovania.games.prime3.exporter.runtime_toolchain import resolve_prime3_runtime_toolchain

ROOT = Path(__file__).resolve().parents[2]
SCRIPT_ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT_DIR = ROOT.joinpath("build", "prime3_wii_runtime")
SOURCE_FILES = (
    Path("payload.S"),
    Path("payload.ld"),
    Path("../prime3_tcp_runtime_clean/runtime.c"),
    Path("../prime3_tcp_runtime_clean/runtime.S"),
    Path("../prime3_tcp_runtime_clean/runtime.ld"),
    Path("build_payload.py"),
)
PROBE_CANARY_START_SYMBOL = "payload_canary_start"
PROBE_CANARY_END_SYMBOL = "payload_canary_end"
PROBE_COUNTER_SYMBOL = "payload_execution_counter"
BOOTSTRAP_SAVE_AREA_START_SYMBOL = "payload_save_area_start"
BOOTSTRAP_SAVE_AREA_END_SYMBOL = "payload_save_area_end"
BOOTSTRAP_HALT_LOOP_SYMBOL = "payload_halt_loop"
EMBEDDED_RUNTIME_START_SYMBOL = "payload_embedded_runtime_start"
EMBEDDED_RUNTIME_END_SYMBOL = "payload_embedded_runtime_end"
BOOTSTRAP_STAGING_ADDRESS = 0x806843C0
BOOTSTRAP_ORIGINAL_ENTRY_INSTRUCTION = 0x4800016D
BOOTSTRAP_ORIGINAL_BRANCH_TARGET = 0x8000648C
BOOTSTRAP_ORIGINAL_CONTINUATION_ADDRESS = 0x80006324
BOOTSTRAP_DIAGNOSTIC_BLOCK_SIZE = 0x40
BOOTSTRAP_CANARY_BYTES = b"P3BOOTSTRAPCANRY"
BOOTSTRAP_CANARY_OFFSET = 0x00
BOOTSTRAP_MARKER_OFFSET = 0x14
BOOTSTRAP_COUNTER_OFFSET = 0x18
BOOTSTRAP_ORIGINAL_80000034_OFFSET = 0x1C
BOOTSTRAP_ORIGINAL_80003110_OFFSET = 0x20
BOOTSTRAP_REPLACEMENT_VALUE_OFFSET = 0x24
BOOTSTRAP_STATUS_OFFSET = 0x28
BOOTSTRAP_MARKER_VALUE = 0x50334254
BOOTSTRAP_HALT_STATUS_VALUE = 0xB0070001
BOOTSTRAP_CONTINUE_STATUS_VALUE = 0xB0070002
RELOCATED_COPY_HALT_STATUS_VALUE = 0xB0071001
RELOCATED_RETURN_HALT_STATUS_VALUE = 0xB0071002
RELOCATED_CONTINUE_STATUS_VALUE = 0xB0071003
RELOCATED_RUNTIME_DESTINATION = 0x817E1000
RELOCATED_RUNTIME_CACHE_LINE_SIZE = 0x20
RELOCATED_RUNTIME_CANARY_BYTES = b"P3HIRUNTIMECANAR"
RELOCATED_COPY_COMPLETE_MARKER_VALUE = 0x434F5059
RELOCATED_EXECUTED_MARKER_VALUE = 0x52554E21
RELOCATED_SUCCESS_STATUS_VALUE = 0x52544F4B
RELOCATED_BOOTSTRAP_RETURN_MARKER_VALUE = 0x4252544E
PRIME3_NTSC_RETAIL_DOL_SHA256 = "6b550f221602074747a2e61b0aa064203fd493f6865dfb3b1a912682065e6104"
PRIME3_NTSC_IOS_OPEN_ASYNC_ADDRESS = 0x80504668
PRIME3_NTSC_IOS_OPEN_ADDRESS = 0x80504780
PRIME3_NTSC_IOS_CLOSE_ASYNC_ADDRESS = 0x805048A0
PRIME3_NTSC_IOS_CLOSE_ADDRESS = 0x80504960
PRIME3_NTSC_IOS_READ_ASYNC_ADDRESS = 0x80504A08
PRIME3_NTSC_IOS_READ_SYNC_ADDRESS = 0x80504B08
PRIME3_NTSC_IOS_WRITE_ASYNC_ADDRESS = 0x80504C10
PRIME3_NTSC_IOS_WRITE_SYNC_ADDRESS = 0x80504D10
PRIME3_NTSC_IOS_SEEK_ASYNC_ADDRESS = 0x80504E18
PRIME3_NTSC_IOS_SEEK_SYNC_ADDRESS = 0x80504EF8
PRIME3_NTSC_CONFIRMED_IOS_IOCTL_ASYNC_ADDRESS = 0x80504FE0
PRIME3_NTSC_CONFIRMED_IOS_IOCTL_SYNC_ADDRESS = 0x80505118
PRIME3_NTSC_CONFIRMED_IOS_IOCTLV_ASYNC_ADDRESS = 0x80505384
PRIME3_NTSC_CONFIRMED_IOS_IOCTLV_SYNC_ADDRESS = 0x80505468
PRIME3_NTSC_IOS_SUBMIT_HELPER_ADDRESS = 0x8050441C
PRIME3_NTSC_IOS_REQUEST_ALLOCATOR_ADDRESS = 0x80505960
# Legacy native-readiness names are not verified service identities. The
# 2026-10-20 retail audit attributes the bootstrap below to /dev/es and its
# claimed SO field to /dev/fs. Do not use them to infer retail IP ownership.
PRIME3_NTSC_NWC24_OPEN_LIB_ADDRESS = 0x805541B8
PRIME3_NTSC_NETWORK_BOOTSTRAP_ADDRESS = 0x80508DD4
PRIME3_NTSC_SO_FD_SDA_OFFSET = -26024
DEFAULT_NATIVE_BEACON_IPV4 = 0xC0A832F8
DEFAULT_NATIVE_BEACON_PORT = 43674
PRIME3_NTSC_IOS_OPEN_ASYNC_GUARD_WORDS = (
    0x9421FFD0,
    0x7C0802A6,
    0x90010034,
    0x39610030,
)
RUNTIME_ENTRY_SYMBOL = "runtime_entry"
RUNTIME_POLL_ENTRY_SYMBOL = "runtime_poll_entry"
RUNTIME_POLL_HOOK_WRAPPER_SYMBOL = "runtime_poll_hook_wrapper"
CP3C_CONFIG_START_SYMBOL = "__cp3c_config_start"
CP3C_CONFIG_END_SYMBOL = "__cp3c_config_end"
CP3C_SERVER_IPV4_SYMBOL = "__cp3c_server_ipv4"
CP3C_SERVER_PORT_SYMBOL = "__cp3c_server_port"
FORBIDDEN_RENDERER_SYMBOL_FRAGMENTS = (
    "overlay",
    "post_copy",
    "xfb",
    "kpad",
    "end_scene",
    "endscene",
    "imgui",
    "gsn1",
    "stt1",
    "rcv1",
    "receive_submission_diagnostics",
)
RUNTIME_RETAIL_IOS_OPEN_VENEER_SYMBOL = "runtime_call_retail_ios_open_async"
RUNTIME_RETAIL_IOS_CLOSE_VENEER_SYMBOL = "runtime_call_retail_ios_close_async"
RUNTIME_RETAIL_READ_ASYNC_VENEER_SYMBOL = "runtime_call_retail_read_async"
RUNTIME_RETAIL_WRITE_ASYNC_VENEER_SYMBOL = "runtime_call_retail_write_async"
RUNTIME_RETAIL_IOS_IOCTL_ASYNC_VENEER_SYMBOL = "runtime_call_retail_ios_ioctl_async"
RUNTIME_RETAIL_IOS_IOCTLV_ASYNC_VENEER_SYMBOL = "runtime_call_retail_ios_ioctlv_async"
RUNTIME_RETAIL_NWC24_OPEN_LIB_VENEER_SYMBOL = "runtime_call_retail_nwc24_open_lib"
RUNTIME_RETAIL_NETWORK_BOOTSTRAP_VENEER_SYMBOL = "runtime_call_retail_network_bootstrap"
RUNTIME_RETAIL_VENEER_SELFTEST_SYMBOL = "runtime_call_retail_veneer_selftest"
RUNTIME_RETAIL_VENEER_SELFTEST_TARGET_SYMBOL = "runtime_local_veneer_selftest_target"
RUNTIME_RETAIL_VENEER_SELFTEST_CALLER_SYMBOL = "runtime_run_retail_veneer_selftest"
RUNTIME_ABI_PROBE_SUPPLIED_ARGS_SYMBOL = "runtime_abi_probe_supplied_args"
RUNTIME_ABI_PROBE_PRE_CALL_ARGS_SYMBOL = "runtime_abi_probe_pre_call_args"
RUNTIME_ABI_PROBE_TARGET_ARGS_SYMBOL = "runtime_abi_probe_target_args"
RUNTIME_ABI_PROBE_RETURN_VALUE_SYMBOL = "runtime_abi_probe_return_value"
RUNTIME_ABI_PROBE_RESULT_FLAGS_SYMBOL = "runtime_abi_probe_result_flags"
RUNTIME_ABI_PROBE_STACK_POINTER_BEFORE_SYMBOL = "runtime_abi_probe_stack_pointer_before"
RUNTIME_ABI_PROBE_STACK_POINTER_AFTER_SYMBOL = "runtime_abi_probe_stack_pointer_after"
RUNTIME_ABI_PROBE_SAVED_LR_SYMBOL = "runtime_abi_probe_saved_lr"
RUNTIME_ABI_PROBE_RESTORED_LR_SYMBOL = "runtime_abi_probe_restored_lr"
RUNTIME_ABI_PROBE_SAVED_R2_SYMBOL = "runtime_abi_probe_saved_r2"
RUNTIME_ABI_PROBE_RESTORED_R2_SYMBOL = "runtime_abi_probe_restored_r2"
RUNTIME_ABI_PROBE_SAVED_R13_SYMBOL = "runtime_abi_probe_saved_r13"
RUNTIME_ABI_PROBE_RESTORED_R13_SYMBOL = "runtime_abi_probe_restored_r13"
RUNTIME_ABI_PROBE_TARGET_CTR_SYMBOL = "runtime_abi_probe_target_ctr"
RUNTIME_ABI_PROBE_AFTER_CALL_FLAG_SYMBOL = "runtime_abi_probe_after_call_flag"
RUNTIME_ABI_PROBE_EXPECTED_RETURN_VALUE_SYMBOL = "runtime_abi_probe_expected_return_value"
RUNTIME_CODE_START_SYMBOL = "runtime_code_start"
RUNTIME_CODE_END_SYMBOL = "runtime_code_end"
RUNTIME_STATE_START_SYMBOL = "runtime_state_start"
RUNTIME_STATE_END_SYMBOL = "runtime_state_end"
RUNTIME_NETWORK_DIAGNOSTICS_SYMBOL = "runtime_network_diagnostics_block"
RUNTIME_CANARY_START_SYMBOL = "runtime_canary_start"
RUNTIME_CANARY_END_SYMBOL = "runtime_canary_end"
RUNTIME_COPY_COMPLETE_MARKER_SYMBOL = "runtime_copy_complete_marker"
RUNTIME_EXECUTED_MARKER_SYMBOL = "runtime_executed_marker"
RUNTIME_EXECUTION_COUNTER_SYMBOL = "runtime_execution_counter"
RUNTIME_STATUS_SYMBOL = "runtime_status"
RUNTIME_BOOTSTRAP_RETURN_MARKER_SYMBOL = "runtime_bootstrap_return_marker"
RUNTIME_POLL_COUNTER_SYMBOL = "runtime_poll_counter"
RUNTIME_POLL_HEARTBEAT_SYMBOL = "runtime_poll_heartbeat"
RUNTIME_POLL_LAST_SEQUENCE_SYMBOL = "runtime_poll_last_sequence"
RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_ENTRY_COUNT_SYMBOL = "runtime_hook_wrapper_entry_count"
RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_BEFORE_POLL_COUNT_SYMBOL = "runtime_hook_wrapper_before_poll_count"
RUNTIME_DIAGNOSTIC_POLL_ENTRY_COUNT_SYMBOL = "runtime_poll_entry_count"
RUNTIME_DIAGNOSTIC_POLL_EXIT_COUNT_SYMBOL = "runtime_poll_exit_count"
RUNTIME_DIAGNOSTIC_STATE_MACHINE_ENTRY_COUNT_SYMBOL = "runtime_state_machine_entry_count"
RUNTIME_DIAGNOSTIC_STATE_MACHINE_EXIT_COUNT_SYMBOL = "runtime_state_machine_exit_count"
RUNTIME_DIAGNOSTIC_C_BEFORE_VENEER_CALL_COUNT_SYMBOL = "runtime_c_before_veneer_call_count"
RUNTIME_DIAGNOSTIC_RETAIL_VENEER_ENTRY_COUNT_SYMBOL = "runtime_retail_veneer_entry_count"
RUNTIME_DIAGNOSTIC_RETAIL_TARGET_RETURN_COUNT_SYMBOL = "runtime_retail_target_return_count"
RUNTIME_DIAGNOSTIC_RETAIL_VENEER_EXIT_COUNT_SYMBOL = "runtime_retail_veneer_exit_count"
RUNTIME_DIAGNOSTIC_C_AFTER_VENEER_CALL_COUNT_SYMBOL = "runtime_c_after_veneer_call_count"
RUNTIME_DIAGNOSTIC_IOS_SUBMIT_ATTEMPT_COUNT_SYMBOL = "runtime_ios_submit_attempt_count"
RUNTIME_DIAGNOSTIC_IOS_SUBMIT_RETURN_COUNT_SYMBOL = "runtime_ios_submit_return_count"
RUNTIME_DIAGNOSTIC_IOS_SUBMIT_RETURN_VALUE_SYMBOL = "runtime_ios_submit_return_value"
RUNTIME_DIAGNOSTIC_CALLBACK_ENTRY_COUNT_SYMBOL = "runtime_callback_entry_count"
RUNTIME_DIAGNOSTIC_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_callback_exit_count"
RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_AFTER_POLL_COUNT_SYMBOL = "runtime_hook_wrapper_after_poll_count"
RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_EXIT_COUNT_SYMBOL = "runtime_hook_wrapper_exit_count"
RUNTIME_DIAGNOSTIC_LAST_EXECUTION_MARKER_SYMBOL = "runtime_last_execution_marker"
RUNTIME_DIAGNOSTIC_LAST_PHASE_BEFORE_STEP_SYMBOL = "runtime_last_transport_phase_before_step"
RUNTIME_DIAGNOSTIC_LAST_PHASE_AFTER_STEP_SYMBOL = "runtime_last_transport_phase_after_step"
RUNTIME_DIAGNOSTIC_CALLBACK_RESULT_SYMBOL = "runtime_callback_result"
RUNTIME_VERIFIED_GAME_R2_SYMBOL = "runtime_verified_game_r2"
RUNTIME_VERIFIED_GAME_R13_SYMBOL = "runtime_verified_game_r13"
RUNTIME_TRANSPORT_PHASE_SYMBOL = "runtime_transport_phase"
RUNTIME_NATIVE_BEACON_IPV4_SYMBOL = "runtime_native_beacon_ipv4"
RUNTIME_TRANSPORT_LAST_ERROR_SYMBOL = "runtime_transport_last_error"
RUNTIME_TRANSPORT_LAST_SOCKET_ERROR_SYMBOL = "runtime_transport_last_socket_error"
RUNTIME_TRANSPORT_LAST_IOS_RESULT_SYMBOL = "runtime_transport_last_ios_result"
RUNTIME_TRANSPORT_PENDING_OPERATION_SYMBOL = "runtime_transport_pending_operation"
RUNTIME_TRANSPORT_PENDING_GENERATION_SYMBOL = "runtime_transport_pending_generation"
RUNTIME_TRANSPORT_CALLBACK_GENERATION_SYMBOL = "runtime_transport_callback_generation"
RUNTIME_TRANSPORT_CALLBACK_COUNT_SYMBOL = "runtime_transport_callback_count"
RUNTIME_TRANSPORT_REJECTED_CALLBACK_COUNT_SYMBOL = "runtime_transport_rejected_callback_count"
RUNTIME_TRANSPORT_CALLBACK_PENDING_SYMBOL = "runtime_transport_callback_pending"
RUNTIME_TRANSPORT_OPEN_KD_SUBMIT_COUNT_SYMBOL = "runtime_transport_open_kd_submit_count"
RUNTIME_TRANSPORT_OPEN_KD_CALLBACK_COUNT_SYMBOL = "runtime_transport_open_kd_callback_count"
RUNTIME_TRANSPORT_OPEN_KD_SUBMIT_RESULT_SYMBOL = "runtime_transport_open_kd_submit_result"
RUNTIME_TRANSPORT_OPEN_KD_CALLBACK_RESULT_SYMBOL = "runtime_transport_open_kd_callback_result"
RUNTIME_TRANSPORT_OPEN_KD_SUBMIT_GENERATION_SYMBOL = "runtime_transport_open_kd_submit_generation"
RUNTIME_TRANSPORT_OPEN_KD_CALLBACK_GENERATION_SYMBOL = "runtime_transport_open_kd_callback_generation"
RUNTIME_TRANSPORT_NWC24_SUBMIT_COUNT_SYMBOL = "runtime_transport_nwc24_submit_count"
RUNTIME_TRANSPORT_NWC24_CALLBACK_COUNT_SYMBOL = "runtime_transport_nwc24_callback_count"
RUNTIME_TRANSPORT_NWC24_SYNCHRONOUS_RESULT_SYMBOL = "runtime_transport_nwc24_synchronous_result"
RUNTIME_TRANSPORT_NWC24_CALLBACK_RESULT_SYMBOL = "runtime_transport_nwc24_callback_result"
RUNTIME_TRANSPORT_NWC24_OUTPUT_BUFFER_SYMBOL = "runtime_transport_nwc24_output_buffer"
RUNTIME_TRANSPORT_NWC24_OUTPUT_DIGEST_SYMBOL = "runtime_transport_nwc24_output_digest"
RUNTIME_TRANSPORT_NWC24_SUBMIT_GENERATION_SYMBOL = "runtime_transport_nwc24_submit_generation"
RUNTIME_TRANSPORT_NWC24_CALLBACK_GENERATION_SYMBOL = "runtime_transport_nwc24_callback_generation"
RUNTIME_TRANSPORT_OPEN_IP_SUBMIT_COUNT_SYMBOL = "runtime_transport_open_ip_submit_count"
RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_COUNT_SYMBOL = "runtime_transport_open_ip_callback_count"
RUNTIME_TRANSPORT_OPEN_IP_SUBMIT_RESULT_SYMBOL = "runtime_transport_open_ip_submit_result"
RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_RESULT_SYMBOL = "runtime_transport_open_ip_callback_result"
RUNTIME_TRANSPORT_OPEN_IP_SUBMIT_GENERATION_SYMBOL = "runtime_transport_open_ip_submit_generation"
RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_GENERATION_SYMBOL = "runtime_transport_open_ip_callback_generation"
RUNTIME_TRANSPORT_OPEN_IP_PATH_POINTER_SYMBOL = "runtime_transport_open_ip_path_pointer"
RUNTIME_TRANSPORT_OPEN_IP_PATH_LENGTH_SYMBOL = "runtime_transport_open_ip_path_length"
RUNTIME_TRANSPORT_OPEN_IP_MODE_VALUE_SYMBOL = "runtime_transport_open_ip_mode_value"
RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_POINTER_SYMBOL = "runtime_transport_open_ip_callback_pointer"
RUNTIME_TRANSPORT_OPEN_IP_CONTEXT_POINTER_SYMBOL = "runtime_transport_open_ip_context_pointer"
RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_transport_open_ip_callback_exit_count"
RUNTIME_TRANSPORT_OPEN_IP_STALE_CALLBACK_COUNT_SYMBOL = "runtime_transport_open_ip_stale_callback_count"
RUNTIME_TRANSPORT_OPEN_IP_DUPLICATE_CALLBACK_COUNT_SYMBOL = "runtime_transport_open_ip_duplicate_callback_count"
RUNTIME_TRANSPORT_IP_FD_BEFORE_OPEN_IP_SYMBOL = "runtime_transport_ip_fd_before_open_ip"
RUNTIME_TRANSPORT_KD_CLOSE_SUBMIT_COUNT_SYMBOL = "runtime_transport_kd_close_submit_count"
RUNTIME_TRANSPORT_KD_CLOSE_CALLBACK_COUNT_SYMBOL = "runtime_transport_kd_close_callback_count"
RUNTIME_TRANSPORT_KD_CLOSE_SUBMIT_RESULT_SYMBOL = "runtime_transport_kd_close_submit_result"
RUNTIME_TRANSPORT_KD_CLOSE_CALLBACK_RESULT_SYMBOL = "runtime_transport_kd_close_callback_result"
RUNTIME_TRANSPORT_KD_CLOSE_SUBMIT_GENERATION_SYMBOL = "runtime_transport_kd_close_submit_generation"
RUNTIME_TRANSPORT_KD_CLOSE_CALLBACK_GENERATION_SYMBOL = "runtime_transport_kd_close_callback_generation"
RUNTIME_TRANSPORT_KD_CLOSE_SUBMITTED_FD_SYMBOL = "runtime_transport_kd_close_submitted_fd"
RUNTIME_TRANSPORT_KD_FD_BEFORE_CLOSE_SYMBOL = "runtime_transport_kd_fd_before_close"
RUNTIME_TRANSPORT_KD_FD_AFTER_CLOSE_SYMBOL = "runtime_transport_kd_fd_after_close"
RUNTIME_TRANSPORT_IP_CLOSE_SUBMIT_COUNT_SYMBOL = "runtime_transport_ip_close_submit_count"
RUNTIME_TRANSPORT_SOCKET_CLOSE_SUBMIT_COUNT_SYMBOL = "runtime_transport_socket_close_submit_count"
RUNTIME_TRANSPORT_STARTUP_SUBMIT_COUNT_SYMBOL = "runtime_transport_startup_submit_count"
RUNTIME_TRANSPORT_STARTUP_CALLBACK_COUNT_SYMBOL = "runtime_transport_startup_callback_count"
RUNTIME_TRANSPORT_STARTUP_SUBMIT_RESULT_SYMBOL = "runtime_transport_startup_submit_result"
RUNTIME_TRANSPORT_STARTUP_CALLBACK_RESULT_SYMBOL = "runtime_transport_startup_callback_result"
RUNTIME_TRANSPORT_STARTUP_SUBMIT_GENERATION_SYMBOL = "runtime_transport_startup_submit_generation"
RUNTIME_TRANSPORT_STARTUP_CALLBACK_GENERATION_SYMBOL = "runtime_transport_startup_callback_generation"
RUNTIME_TRANSPORT_STARTUP_TARGET_ADDRESS_SYMBOL = "runtime_transport_startup_target_address"
RUNTIME_TRANSPORT_STARTUP_COMMAND_SYMBOL = "runtime_transport_startup_command"
RUNTIME_TRANSPORT_STARTUP_SUBMITTED_FD_SYMBOL = "runtime_transport_startup_submitted_fd"
RUNTIME_TRANSPORT_STARTUP_CALLBACK_POINTER_SYMBOL = "runtime_transport_startup_callback_pointer"
RUNTIME_TRANSPORT_STARTUP_CONTEXT_POINTER_SYMBOL = "runtime_transport_startup_context_pointer"
RUNTIME_TRANSPORT_STARTUP_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_transport_startup_callback_exit_count"
RUNTIME_TRANSPORT_STARTUP_STALE_CALLBACK_COUNT_SYMBOL = "runtime_transport_startup_stale_callback_count"
RUNTIME_TRANSPORT_STARTUP_DUPLICATE_CALLBACK_COUNT_SYMBOL = "runtime_transport_startup_duplicate_callback_count"
RUNTIME_TRANSPORT_STARTUP_SERVICE_STARTED_BEFORE_SUBMIT_SYMBOL = (
    "runtime_transport_startup_service_started_before_submit"
)
RUNTIME_TRANSPORT_STARTUP_SERVICE_STARTED_AFTER_COMPLETION_SYMBOL = (
    "runtime_transport_startup_service_started_after_completion"
)
RUNTIME_TRANSPORT_IP_FD_BEFORE_STARTUP_SYMBOL = "runtime_transport_ip_fd_before_startup"
RUNTIME_TRANSPORT_IP_FD_AFTER_STARTUP_SYMBOL = "runtime_transport_ip_fd_after_startup"
RUNTIME_TRANSPORT_STARTUP_PENDING_BEFORE_SUBMIT_SYMBOL = "runtime_transport_startup_pending_before_submit"
RUNTIME_TRANSPORT_STARTUP_PENDING_AFTER_COMPLETION_SYMBOL = "runtime_transport_startup_pending_after_completion"
RUNTIME_TRANSPORT_STARTUP_PHASE_BEFORE_SUBMIT_SYMBOL = "runtime_transport_startup_phase_before_submit"
RUNTIME_TRANSPORT_STARTUP_PHASE_AFTER_COMPLETION_SYMBOL = "runtime_transport_startup_phase_after_completion"
RUNTIME_TRANSPORT_STARTUP_PRE_CALL_ARGS_SYMBOL = "runtime_transport_startup_pre_call_args"
RUNTIME_TRANSPORT_GET_HOST_ID_SUBMIT_COUNT_SYMBOL = "runtime_transport_get_host_id_submit_count"
RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_COUNT_SYMBOL = "runtime_transport_get_host_id_callback_count"
RUNTIME_TRANSPORT_GET_HOST_ID_SUBMIT_RESULT_SYMBOL = "runtime_transport_get_host_id_submit_result"
RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_RESULT_SYMBOL = "runtime_transport_get_host_id_callback_result"
RUNTIME_TRANSPORT_GET_HOST_ID_SUBMIT_GENERATION_SYMBOL = "runtime_transport_get_host_id_submit_generation"
RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_GENERATION_SYMBOL = "runtime_transport_get_host_id_callback_generation"
RUNTIME_TRANSPORT_GET_HOST_ID_TARGET_ADDRESS_SYMBOL = "runtime_transport_get_host_id_target_address"
RUNTIME_TRANSPORT_GET_HOST_ID_COMMAND_SYMBOL = "runtime_transport_get_host_id_command"
RUNTIME_TRANSPORT_GET_HOST_ID_SUBMITTED_FD_SYMBOL = "runtime_transport_get_host_id_submitted_fd"
RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_POINTER_SYMBOL = "runtime_transport_get_host_id_callback_pointer"
RUNTIME_TRANSPORT_GET_HOST_ID_CONTEXT_POINTER_SYMBOL = "runtime_transport_get_host_id_context_pointer"
RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_transport_get_host_id_callback_exit_count"
RUNTIME_TRANSPORT_GET_HOST_ID_STALE_CALLBACK_COUNT_SYMBOL = "runtime_transport_get_host_id_stale_callback_count"
RUNTIME_TRANSPORT_GET_HOST_ID_DUPLICATE_CALLBACK_COUNT_SYMBOL = "runtime_transport_get_host_id_duplicate_callback_count"
RUNTIME_TRANSPORT_GET_HOST_ID_SERVICE_STARTED_BEFORE_SUBMIT_SYMBOL = (
    "runtime_transport_get_host_id_service_started_before_submit"
)
RUNTIME_TRANSPORT_GET_HOST_ID_SERVICE_STARTED_AFTER_COMPLETION_SYMBOL = (
    "runtime_transport_get_host_id_service_started_after_completion"
)
RUNTIME_TRANSPORT_IP_FD_BEFORE_GET_HOST_ID_SYMBOL = "runtime_transport_ip_fd_before_get_host_id"
RUNTIME_TRANSPORT_IP_FD_AFTER_GET_HOST_ID_SYMBOL = "runtime_transport_ip_fd_after_get_host_id"
RUNTIME_TRANSPORT_GET_HOST_ID_PENDING_BEFORE_SUBMIT_SYMBOL = "runtime_transport_get_host_id_pending_before_submit"
RUNTIME_TRANSPORT_GET_HOST_ID_PENDING_AFTER_COMPLETION_SYMBOL = "runtime_transport_get_host_id_pending_after_completion"
RUNTIME_TRANSPORT_GET_HOST_ID_PHASE_BEFORE_SUBMIT_SYMBOL = "runtime_transport_get_host_id_phase_before_submit"
RUNTIME_TRANSPORT_GET_HOST_ID_PHASE_AFTER_COMPLETION_SYMBOL = "runtime_transport_get_host_id_phase_after_completion"
RUNTIME_TRANSPORT_GET_HOST_ID_PRE_CALL_ARGS_SYMBOL = "runtime_transport_get_host_id_pre_call_args"
RUNTIME_TRANSPORT_SOCKET_SUBMIT_COUNT_SYMBOL = "runtime_transport_socket_submit_count"
RUNTIME_TRANSPORT_SOCKET_CALLBACK_COUNT_SYMBOL = "runtime_transport_socket_callback_count"
RUNTIME_TRANSPORT_SOCKET_SUBMIT_RESULT_SYMBOL = "runtime_transport_socket_submit_result"
RUNTIME_TRANSPORT_SOCKET_CALLBACK_RESULT_SYMBOL = "runtime_transport_socket_callback_result"
RUNTIME_TRANSPORT_SOCKET_SUBMIT_GENERATION_SYMBOL = "runtime_transport_socket_submit_generation"
RUNTIME_TRANSPORT_SOCKET_CALLBACK_GENERATION_SYMBOL = "runtime_transport_socket_callback_generation"
RUNTIME_TRANSPORT_SOCKET_TARGET_ADDRESS_SYMBOL = "runtime_transport_socket_target_address"
RUNTIME_TRANSPORT_SOCKET_COMMAND_SYMBOL = "runtime_transport_socket_command"
RUNTIME_TRANSPORT_SOCKET_SUBMITTED_FD_SYMBOL = "runtime_transport_socket_submitted_fd"
RUNTIME_TRANSPORT_SOCKET_CALLBACK_POINTER_SYMBOL = "runtime_transport_socket_callback_pointer"
RUNTIME_TRANSPORT_SOCKET_CONTEXT_POINTER_SYMBOL = "runtime_transport_socket_context_pointer"
RUNTIME_TRANSPORT_SOCKET_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_transport_socket_callback_exit_count"
RUNTIME_TRANSPORT_SOCKET_STALE_CALLBACK_COUNT_SYMBOL = "runtime_transport_socket_stale_callback_count"
RUNTIME_TRANSPORT_SOCKET_DUPLICATE_CALLBACK_COUNT_SYMBOL = "runtime_transport_socket_duplicate_callback_count"
RUNTIME_TRANSPORT_SOCKET_FD_BEFORE_SUBMIT_SYMBOL = "runtime_transport_socket_fd_before_submit"
RUNTIME_TRANSPORT_SOCKET_FD_AFTER_COMPLETION_SYMBOL = "runtime_transport_socket_fd_after_completion"
RUNTIME_TRANSPORT_SOCKET_REQUEST_ADDRESS_SYMBOL = "runtime_transport_socket_request_address"
RUNTIME_TRANSPORT_SOCKET_REQUEST_STORAGE_SIZE_SYMBOL = "runtime_transport_socket_request_storage_size"
RUNTIME_TRANSPORT_SOCKET_REQUEST_LOGICAL_SIZE_SYMBOL = "runtime_transport_socket_request_logical_size"
RUNTIME_TRANSPORT_SOCKET_REQUEST_ALIGNMENT_SYMBOL = "runtime_transport_socket_request_alignment"
RUNTIME_TRANSPORT_SOCKET_FAMILY_VALUE_SYMBOL = "runtime_transport_socket_family_value"
RUNTIME_TRANSPORT_SOCKET_TYPE_VALUE_SYMBOL = "runtime_transport_socket_type_value"
RUNTIME_TRANSPORT_SOCKET_PROTOCOL_VALUE_SYMBOL = "runtime_transport_socket_protocol_value"
RUNTIME_TRANSPORT_SOCKET_DESCRIPTOR_VALID_SYMBOL = "runtime_transport_socket_descriptor_valid"
RUNTIME_TRANSPORT_SOCKET_READY_SYMBOL = "runtime_transport_socket_ready"
RUNTIME_TRANSPORT_SOCKET_REQUEST_BYTES_SYMBOL = "runtime_transport_socket_request_bytes"
RUNTIME_TRANSPORT_SOCKET_PRE_CALL_ARGS_SYMBOL = "runtime_transport_socket_pre_call_args"
RUNTIME_TRANSPORT_BIND_SUBMIT_COUNT_SYMBOL = "runtime_transport_bind_submit_count"
RUNTIME_TRANSPORT_BIND_CALLBACK_COUNT_SYMBOL = "runtime_transport_bind_callback_count"
RUNTIME_TRANSPORT_BIND_SUBMIT_RESULT_SYMBOL = "runtime_transport_bind_submit_result"
RUNTIME_TRANSPORT_BIND_CALLBACK_RESULT_SYMBOL = "runtime_transport_bind_callback_result"
RUNTIME_TRANSPORT_BIND_SUBMIT_GENERATION_SYMBOL = "runtime_transport_bind_submit_generation"
RUNTIME_TRANSPORT_BIND_CALLBACK_GENERATION_SYMBOL = "runtime_transport_bind_callback_generation"
RUNTIME_TRANSPORT_BIND_TARGET_ADDRESS_SYMBOL = "runtime_transport_bind_target_address"
RUNTIME_TRANSPORT_BIND_COMMAND_SYMBOL = "runtime_transport_bind_command"
RUNTIME_TRANSPORT_BIND_SUBMITTED_FD_SYMBOL = "runtime_transport_bind_submitted_fd"
RUNTIME_TRANSPORT_BIND_CALLBACK_POINTER_SYMBOL = "runtime_transport_bind_callback_pointer"
RUNTIME_TRANSPORT_BIND_CONTEXT_POINTER_SYMBOL = "runtime_transport_bind_context_pointer"
RUNTIME_TRANSPORT_BIND_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_transport_bind_callback_exit_count"
RUNTIME_TRANSPORT_BIND_STALE_CALLBACK_COUNT_SYMBOL = "runtime_transport_bind_stale_callback_count"
RUNTIME_TRANSPORT_BIND_DUPLICATE_CALLBACK_COUNT_SYMBOL = "runtime_transport_bind_duplicate_callback_count"
RUNTIME_TRANSPORT_BIND_REQUEST_ADDRESS_SYMBOL = "runtime_transport_bind_request_address"
RUNTIME_TRANSPORT_BIND_REQUEST_STORAGE_SIZE_SYMBOL = "runtime_transport_bind_request_storage_size"
RUNTIME_TRANSPORT_BIND_REQUEST_LOGICAL_SIZE_SYMBOL = "runtime_transport_bind_request_logical_size"
RUNTIME_TRANSPORT_BIND_REQUEST_ALIGNMENT_SYMBOL = "runtime_transport_bind_request_alignment"
RUNTIME_TRANSPORT_BIND_SOCKADDR_LENGTH_SYMBOL = "runtime_transport_bind_sockaddr_length"
RUNTIME_TRANSPORT_BIND_FAMILY_VALUE_SYMBOL = "runtime_transport_bind_family_value"
RUNTIME_TRANSPORT_BIND_PORT_VALUE_SYMBOL = "runtime_transport_bind_port_value"
RUNTIME_TRANSPORT_BIND_ADDRESS_VALUE_SYMBOL = "runtime_transport_bind_address_value"
RUNTIME_TRANSPORT_BIND_REQUEST_BYTES_SYMBOL = "runtime_transport_bind_request_bytes"
RUNTIME_TRANSPORT_BIND_PRE_CALL_ARGS_SYMBOL = "runtime_transport_bind_pre_call_args"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_COUNT_SYMBOL = "runtime_transport_cleanup_close_callback_count"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_SUBMIT_RESULT_SYMBOL = "runtime_transport_cleanup_close_submit_result"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_RESULT_SYMBOL = "runtime_transport_cleanup_close_callback_result"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_SUBMIT_GENERATION_SYMBOL = "runtime_transport_cleanup_close_submit_generation"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_GENERATION_SYMBOL = "runtime_transport_cleanup_close_callback_generation"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_TARGET_ADDRESS_SYMBOL = "runtime_transport_cleanup_close_target_address"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_COMMAND_SYMBOL = "runtime_transport_cleanup_close_command"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_SUBMITTED_FD_SYMBOL = "runtime_transport_cleanup_close_submitted_fd"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_POINTER_SYMBOL = "runtime_transport_cleanup_close_callback_pointer"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_CONTEXT_POINTER_SYMBOL = "runtime_transport_cleanup_close_context_pointer"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_EXIT_COUNT_SYMBOL = "runtime_transport_cleanup_close_callback_exit_count"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_STALE_CALLBACK_COUNT_SYMBOL = "runtime_transport_cleanup_close_stale_callback_count"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_DUPLICATE_CALLBACK_COUNT_SYMBOL = (
    "runtime_transport_cleanup_close_duplicate_callback_count"
)
RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_ADDRESS_SYMBOL = "runtime_transport_cleanup_close_request_address"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_STORAGE_SIZE_SYMBOL = "runtime_transport_cleanup_close_request_storage_size"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_LOGICAL_SIZE_SYMBOL = "runtime_transport_cleanup_close_request_logical_size"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_ALIGNMENT_SYMBOL = "runtime_transport_cleanup_close_request_alignment"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_VALUE_SYMBOL = "runtime_transport_cleanup_close_request_value"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_BYTES_SYMBOL = "runtime_transport_cleanup_close_request_bytes"
RUNTIME_TRANSPORT_CLEANUP_CLOSE_PRE_CALL_ARGS_SYMBOL = "runtime_transport_cleanup_close_pre_call_args"
RUNTIME_TRANSPORT_BOUND_FLAG_SYMBOL = "runtime_transport_bound_flag"
RUNTIME_TRANSPORT_BOUND_ADDRESS_SYMBOL = "runtime_transport_bound_address"
RUNTIME_TRANSPORT_SOCKET_CLOSED_AFTER_BIND_FAILURE_SYMBOL = "runtime_transport_socket_closed_after_bind_failure"
RUNTIME_TRANSPORT_SOCKET_LEAK_DETECTED_SYMBOL = "runtime_transport_socket_leak_detected"
RUNTIME_TRANSPORT_KD_FD_SYMBOL = "runtime_transport_kd_fd"
RUNTIME_TRANSPORT_KD_CLOSED_SYMBOL = "runtime_transport_kd_closed"
RUNTIME_TRANSPORT_IP_FD_SYMBOL = "runtime_transport_ip_fd"
RUNTIME_TRANSPORT_SOCKET_FD_SYMBOL = "runtime_transport_socket_fd"
RUNTIME_TRANSPORT_HOST_ID_SYMBOL = "runtime_transport_host_id"
RUNTIME_TRANSPORT_HOST_ID_AVAILABLE_SYMBOL = "runtime_transport_host_id_available"
RUNTIME_TRANSPORT_HOST_ID_READY_SYMBOL = "runtime_transport_host_id_ready"
RUNTIME_TRANSPORT_SERVICE_STARTED_SYMBOL = "runtime_transport_service_started"
RUNTIME_TRANSPORT_BOUND_PORT_SYMBOL = "runtime_transport_bound_port"
RUNTIME_TRANSPORT_RECEIVE_SUBMIT_COUNT_SYMBOL = "runtime_transport_receive_submit_count"
RUNTIME_TRANSPORT_SEND_SUBMIT_COUNT_SYMBOL = "runtime_transport_send_submit_count"
RUNTIME_TRANSPORT_RECEIVE_COUNT_SYMBOL = "runtime_transport_receive_count"
RUNTIME_TRANSPORT_RECEIVE_BYTES_SYMBOL = "runtime_transport_receive_bytes"
RUNTIME_TRANSPORT_SEND_COUNT_SYMBOL = "runtime_transport_send_count"
RUNTIME_TRANSPORT_SEND_BYTES_SYMBOL = "runtime_transport_send_bytes"
RUNTIME_TRANSPORT_RECEIVE_ARM_COUNT_SYMBOL = "runtime_transport_receive_arm_count"
RUNTIME_TRANSPORT_RECEIVE_REARM_COUNT_SYMBOL = "runtime_transport_receive_rearm_count"
RUNTIME_TRANSPORT_CONFIGURED_EXCHANGE_LIMIT_SYMBOL = "runtime_transport_configured_exchange_limit"
RUNTIME_TRANSPORT_COMPLETED_EXCHANGE_COUNT_SYMBOL = "runtime_transport_completed_exchange_count"
RUNTIME_TRANSPORT_CURRENT_EXCHANGE_INDEX_SYMBOL = "runtime_transport_current_exchange_index"
RUNTIME_TRANSPORT_LAST_COMPLETED_EXCHANGE_INDEX_SYMBOL = "runtime_transport_last_completed_exchange_index"
RUNTIME_TRANSPORT_PREVIOUS_PEER_IPV4_SYMBOL = "runtime_transport_previous_peer_ipv4"
RUNTIME_TRANSPORT_PREVIOUS_PEER_PORT_SYMBOL = "runtime_transport_previous_peer_port"
RUNTIME_TRANSPORT_REARM_SUBMISSION_FAILURE_COUNT_SYMBOL = "runtime_transport_rearm_submission_failure_count"
RUNTIME_TRANSPORT_LOOP_COMPLETE_TRANSITION_COUNT_SYMBOL = "runtime_transport_loop_complete_transition_count"
RUNTIME_TRANSPORT_CLEANUP_DEFERRED_COUNT_SYMBOL = "runtime_transport_cleanup_deferred_count"
RUNTIME_TRANSPORT_LAST_RECEIVE_LENGTH_SYMBOL = "runtime_transport_last_receive_length"
RUNTIME_TRANSPORT_LAST_SEND_LENGTH_SYMBOL = "runtime_transport_last_send_length"
RUNTIME_TRANSPORT_LAST_PEER_IPV4_SYMBOL = "runtime_transport_last_peer_ipv4"
RUNTIME_TRANSPORT_LAST_PEER_PORT_SYMBOL = "runtime_transport_last_peer_port"
RUNTIME_TRANSPORT_LAST_PEER_FAMILY_SYMBOL = "runtime_transport_last_peer_family"
RUNTIME_TRANSPORT_LAST_POLL_ACTION_SYMBOL = "runtime_transport_last_poll_action"
RUNTIME_TRANSPORT_LAST_SUBMIT_RESULT_SYMBOL = "runtime_transport_last_submit_result"
RUNTIME_TRANSPORT_POLLS_WHILE_RECEIVE_PENDING_SYMBOL = "runtime_transport_polls_while_receive_pending"
RUNTIME_TRANSPORT_POLLS_AFTER_LOOP_COMPLETE_SYMBOL = "runtime_transport_polls_after_loop_complete"
RUNTIME_TRANSPORT_LAST_RECEIVE_PREVIEW_SYMBOL = "runtime_transport_last_receive_preview"
RUNTIME_TRANSPORT_LAST_SEND_PREVIEW_SYMBOL = "runtime_transport_last_send_preview"
RUNTIME_TRANSPORT_PREPARED_SEND_LENGTH_SYMBOL = "runtime_transport_prepared_send_length"
RUNTIME_TRANSPORT_CP3W_DATAGRAMS_PROCESSED_SYMBOL = "runtime_transport_cp3w_datagrams_processed"
RUNTIME_TRANSPORT_CP3W_FRAMES_VALID_SYMBOL = "runtime_transport_cp3w_frames_valid"
RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_SYMBOL = "runtime_transport_cp3w_frames_invalid"
RUNTIME_TRANSPORT_CP3W_FRAMES_TOO_SHORT_SYMBOL = "runtime_transport_cp3w_frames_too_short"
RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_MAGIC_SYMBOL = "runtime_transport_cp3w_frames_invalid_magic"
RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_VERSION_SYMBOL = "runtime_transport_cp3w_frames_invalid_version"
RUNTIME_TRANSPORT_CP3W_FRAMES_UNSUPPORTED_TYPE_SYMBOL = "runtime_transport_cp3w_frames_unsupported_type"
RUNTIME_TRANSPORT_CP3W_FRAMES_NONZERO_FLAGS_SYMBOL = "runtime_transport_cp3w_frames_nonzero_flags"
RUNTIME_TRANSPORT_CP3W_FRAMES_LENGTH_MISMATCH_SYMBOL = "runtime_transport_cp3w_frames_length_mismatch"
RUNTIME_TRANSPORT_CP3W_FRAMES_PAYLOAD_TOO_LARGE_SYMBOL = "runtime_transport_cp3w_frames_payload_too_large"
RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_PAYLOAD_SYMBOL = "runtime_transport_cp3w_frames_invalid_payload"
RUNTIME_TRANSPORT_CP3W_FRAMES_MALFORMED_SYMBOL = "runtime_transport_cp3w_frames_malformed"
RUNTIME_TRANSPORT_CP3W_FRAMED_RESPONSES_SUBMITTED_SYMBOL = "runtime_transport_cp3w_framed_responses_submitted"
RUNTIME_TRANSPORT_CP3W_FRAMED_RESPONSES_COMPLETED_SYMBOL = "runtime_transport_cp3w_framed_responses_completed"
RUNTIME_TRANSPORT_CP3W_LAST_REQUEST_ID_SYMBOL = "runtime_transport_cp3w_last_request_id"
RUNTIME_TRANSPORT_CP3W_LAST_RESPONSE_ID_SYMBOL = "runtime_transport_cp3w_last_response_id"
RUNTIME_TRANSPORT_CP3W_LAST_MESSAGE_TYPE_SYMBOL = "runtime_transport_cp3w_last_message_type"
RUNTIME_TRANSPORT_CP3W_LAST_DECLARED_PAYLOAD_LENGTH_SYMBOL = "runtime_transport_cp3w_last_declared_payload_length"
RUNTIME_TRANSPORT_CP3W_LAST_ACTUAL_PAYLOAD_LENGTH_SYMBOL = "runtime_transport_cp3w_last_actual_payload_length"
RUNTIME_TRANSPORT_CP3W_LAST_FRAME_RESULT_SYMBOL = "runtime_transport_cp3w_last_frame_result"
RUNTIME_TRANSPORT_CP3W_FINAL_DATAGRAM_INDEX_SYMBOL = "runtime_transport_cp3w_final_datagram_index"
RUNTIME_TRANSPORT_CP3W_REQUESTS_DISPATCHED_SYMBOL = "runtime_transport_cp3w_requests_dispatched"
RUNTIME_TRANSPORT_CP3W_HELLO_REQUESTS_RECEIVED_SYMBOL = "runtime_transport_cp3w_hello_requests_received"
RUNTIME_TRANSPORT_CP3W_HELLO_SUCCESSES_SYMBOL = "runtime_transport_cp3w_hello_successes"
RUNTIME_TRANSPORT_CP3W_HELLO_VERSION_REJECTIONS_SYMBOL = "runtime_transport_cp3w_hello_version_rejections"
RUNTIME_TRANSPORT_CP3W_HELLO_RESPONSES_SUBMITTED_SYMBOL = "runtime_transport_cp3w_hello_responses_submitted"
RUNTIME_TRANSPORT_CP3W_HELLO_RESPONSES_COMPLETED_SYMBOL = "runtime_transport_cp3w_hello_responses_completed"
RUNTIME_TRANSPORT_CP3W_HELLO_DUPLICATE_REQUESTS_SYMBOL = "runtime_transport_cp3w_hello_duplicate_requests"
RUNTIME_TRANSPORT_CP3W_HELLO_RENEGOTIATION_REJECTIONS_SYMBOL = "runtime_transport_cp3w_hello_renegotiation_rejections"
RUNTIME_TRANSPORT_CP3W_PRE_HELLO_GATED_COMMANDS_SYMBOL = "runtime_transport_cp3w_pre_hello_gated_commands"
RUNTIME_TRANSPORT_CP3W_NOT_NEGOTIATED_RESPONSES_SUBMITTED_SYMBOL = (
    "runtime_transport_cp3w_not_negotiated_responses_submitted"
)
RUNTIME_TRANSPORT_CP3W_NOT_NEGOTIATED_RESPONSES_COMPLETED_SYMBOL = (
    "runtime_transport_cp3w_not_negotiated_responses_completed"
)
RUNTIME_TRANSPORT_CP3W_PING_REQUESTS_RECEIVED_SYMBOL = "runtime_transport_cp3w_ping_requests_received"
RUNTIME_TRANSPORT_CP3W_PONG_RESPONSES_SUBMITTED_SYMBOL = "runtime_transport_cp3w_pong_responses_submitted"
RUNTIME_TRANSPORT_CP3W_PONG_RESPONSES_COMPLETED_SYMBOL = "runtime_transport_cp3w_pong_responses_completed"
RUNTIME_TRANSPORT_CP3W_UNSUPPORTED_COMMANDS_RECEIVED_SYMBOL = "runtime_transport_cp3w_unsupported_commands_received"
RUNTIME_TRANSPORT_CP3W_UNSUPPORTED_RESPONSES_SUBMITTED_SYMBOL = "runtime_transport_cp3w_unsupported_responses_submitted"
RUNTIME_TRANSPORT_CP3W_UNSUPPORTED_RESPONSES_COMPLETED_SYMBOL = "runtime_transport_cp3w_unsupported_responses_completed"
RUNTIME_TRANSPORT_CP3W_NEGOTIATED_FLAG_SYMBOL = "runtime_transport_cp3w_negotiated_flag"
RUNTIME_TRANSPORT_CP3W_SELECTED_PROTOCOL_VERSION_SYMBOL = "runtime_transport_cp3w_selected_protocol_version"
RUNTIME_TRANSPORT_CP3W_CLIENT_NONCE_SYMBOL = "runtime_transport_cp3w_client_nonce"
RUNTIME_TRANSPORT_CP3W_CLIENT_CAPABILITIES_SYMBOL = "runtime_transport_cp3w_client_capabilities"
RUNTIME_TRANSPORT_CP3W_RUNTIME_CAPABILITIES_SYMBOL = "runtime_transport_cp3w_runtime_capabilities"
RUNTIME_TRANSPORT_CP3W_ACCEPTED_CAPABILITIES_SYMBOL = "runtime_transport_cp3w_accepted_capabilities"
RUNTIME_TRANSPORT_CP3W_SESSION_ID_SYMBOL = "runtime_transport_cp3w_session_id"
RUNTIME_TRANSPORT_CP3W_RUNTIME_BUILD_ID_SYMBOL = "runtime_transport_cp3w_runtime_build_id"
RUNTIME_TRANSPORT_CP3W_LAST_COMMAND_SYMBOL = "runtime_transport_cp3w_last_command"
RUNTIME_TRANSPORT_CP3W_LAST_RESPONSE_STATUS_SYMBOL = "runtime_transport_cp3w_last_response_status"
RUNTIME_TRANSPORT_CP3W_LAST_PING_PAYLOAD_LENGTH_SYMBOL = "runtime_transport_cp3w_last_ping_payload_length"
RUNTIME_TRANSPORT_CP3W_LAST_DISPATCH_RESULT_SYMBOL = "runtime_transport_cp3w_last_dispatch_result"
RUNTIME_TRANSPORT_CP3W_GAME_IDENTITY_SYMBOLS = {
    name.removeprefix("runtime_transport_cp3w_game_identity_"): name
    for name in (
        "runtime_transport_cp3w_game_identity_requests",
        "runtime_transport_cp3w_game_identity_successes",
        "runtime_transport_cp3w_game_identity_pre_hello_rejections",
        "runtime_transport_cp3w_game_identity_capability_rejections",
        "runtime_transport_cp3w_game_identity_invalid_payload_rejections",
        "runtime_transport_cp3w_game_identity_executable_validations",
        "runtime_transport_cp3w_game_identity_executable_failures",
        "runtime_transport_cp3w_game_identity_game_state_valid",
        "runtime_transport_cp3w_game_identity_game_state_invalid",
        "runtime_transport_cp3w_game_identity_player_state_valid",
        "runtime_transport_cp3w_game_identity_player_state_invalid",
        "runtime_transport_cp3w_game_identity_inventory_root_available",
        "runtime_transport_cp3w_game_identity_responses_submitted",
        "runtime_transport_cp3w_game_identity_responses_completed",
        "runtime_transport_cp3w_game_identity_capability_errors_submitted",
        "runtime_transport_cp3w_game_identity_capability_errors_completed",
        "runtime_transport_cp3w_game_identity_invalid_payload_errors_submitted",
        "runtime_transport_cp3w_game_identity_invalid_payload_errors_completed",
        "runtime_transport_cp3w_game_identity_last_request_id",
        "runtime_transport_cp3w_game_identity_last_status",
        "runtime_transport_cp3w_game_identity_last_availability",
        "runtime_transport_cp3w_game_identity_last_profile_id",
        "runtime_transport_cp3w_game_identity_last_fingerprint",
        "runtime_transport_cp3w_game_identity_executable_recognized",
        "runtime_transport_cp3w_game_identity_game_state_pointer",
        "runtime_transport_cp3w_game_identity_player_state_pointer",
        "runtime_transport_cp3w_game_identity_inventory_root_pointer",
    )
}
RUNTIME_TRANSPORT_CP3W_INVENTORY_SYMBOLS = {
    name.removeprefix("runtime_transport_cp3w_inventory_"): name
    for name in (
        "runtime_transport_cp3w_inventory_requests",
        "runtime_transport_cp3w_inventory_available_snapshots",
        "runtime_transport_cp3w_inventory_unavailable_snapshots",
        "runtime_transport_cp3w_inventory_pre_hello_rejections",
        "runtime_transport_cp3w_inventory_capability_rejections",
        "runtime_transport_cp3w_inventory_invalid_payload_rejections",
        "runtime_transport_cp3w_inventory_executable_failures",
        "runtime_transport_cp3w_inventory_game_state_valid",
        "runtime_transport_cp3w_inventory_game_state_invalid",
        "runtime_transport_cp3w_inventory_root_valid",
        "runtime_transport_cp3w_inventory_root_invalid",
        "runtime_transport_cp3w_inventory_range_failures",
        "runtime_transport_cp3w_inventory_consistency_successes",
        "runtime_transport_cp3w_inventory_consistency_failures",
        "runtime_transport_cp3w_inventory_responses_submitted",
        "runtime_transport_cp3w_inventory_responses_completed",
        "runtime_transport_cp3w_inventory_last_request_id",
        "runtime_transport_cp3w_inventory_last_status",
        "runtime_transport_cp3w_inventory_last_availability",
        "runtime_transport_cp3w_inventory_snapshot_sequence",
        "runtime_transport_cp3w_inventory_last_root",
    )
}
RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS = 0x800BB720


@dataclasses.dataclass(frozen=True)
class RelocatedRuntimeBuildResult:
    payload_bytes: bytes
    payload_sha256: str
    payload_size: int
    entry_address: int
    poll_entry_address: int
    poll_hook_wrapper_address: int
    code_start: int
    code_end: int
    state_start: int
    state_end: int
    cp3c_config_start_address: int
    cp3c_config_end_address: int
    cp3c_server_ipv4_address: int
    cp3c_server_port_address: int
    network_diagnostics_address: int
    native_beacon_ipv4_address: int | None
    canary_address: int
    canary_size: int
    canary_sha256: str
    copy_complete_marker_address: int
    runtime_executed_marker_address: int
    runtime_execution_counter_address: int
    runtime_status_address: int
    bootstrap_return_marker_address: int
    poll_counter_address: int
    poll_heartbeat_address: int
    poll_last_sequence_address: int
    diagnostic_hook_wrapper_entry_count_address: int | None
    diagnostic_hook_wrapper_before_poll_count_address: int | None
    diagnostic_poll_entry_count_address: int | None
    diagnostic_poll_exit_count_address: int | None
    diagnostic_state_machine_entry_count_address: int | None
    diagnostic_state_machine_exit_count_address: int | None
    diagnostic_c_before_veneer_call_count_address: int | None
    diagnostic_retail_veneer_entry_count_address: int | None
    diagnostic_retail_target_return_count_address: int | None
    diagnostic_retail_veneer_exit_count_address: int | None
    diagnostic_c_after_veneer_call_count_address: int | None
    diagnostic_ios_submit_attempt_count_address: int | None
    diagnostic_ios_submit_return_count_address: int | None
    diagnostic_ios_submit_return_value_address: int | None
    diagnostic_callback_entry_count_address: int | None
    diagnostic_callback_exit_count_address: int | None
    diagnostic_hook_wrapper_after_poll_count_address: int | None
    diagnostic_hook_wrapper_exit_count_address: int | None
    diagnostic_last_execution_marker_address: int | None
    diagnostic_last_phase_before_step_address: int | None
    diagnostic_last_phase_after_step_address: int | None
    diagnostic_callback_result_address: int | None
    verified_game_r2_address: int
    verified_game_r13_address: int
    abi_probe_supplied_args_address: int
    abi_probe_supplied_args_size: int
    abi_probe_pre_call_args_address: int
    abi_probe_pre_call_args_size: int
    abi_probe_target_args_address: int
    abi_probe_target_args_size: int
    abi_probe_return_value_address: int
    abi_probe_result_flags_address: int
    abi_probe_stack_pointer_before_address: int
    abi_probe_stack_pointer_after_address: int
    abi_probe_saved_lr_address: int
    abi_probe_restored_lr_address: int
    abi_probe_saved_r2_address: int
    abi_probe_restored_r2_address: int
    abi_probe_saved_r13_address: int
    abi_probe_restored_r13_address: int
    abi_probe_target_ctr_address: int
    abi_probe_after_call_flag_address: int
    abi_probe_expected_return_value_address: int
    transport_phase_address: int
    transport_last_error_address: int
    transport_last_socket_error_address: int
    transport_last_ios_result_address: int
    transport_pending_operation_address: int
    transport_pending_generation_address: int
    transport_callback_generation_address: int
    transport_callback_count_address: int
    transport_rejected_callback_count_address: int
    transport_callback_pending_address: int
    transport_open_kd_submit_count_address: int
    transport_open_kd_callback_count_address: int
    transport_nwc24_submit_count_address: int
    transport_nwc24_callback_count_address: int
    transport_nwc24_synchronous_result_address: int
    transport_nwc24_callback_result_address: int
    transport_nwc24_output_buffer_address: int
    transport_nwc24_output_digest_address: int
    transport_open_ip_submit_count_address: int
    transport_open_ip_callback_count_address: int
    transport_kd_close_submit_count_address: int
    transport_kd_close_callback_count_address: int
    transport_ip_close_submit_count_address: int
    transport_socket_close_submit_count_address: int
    transport_startup_submit_count_address: int
    transport_startup_callback_count_address: int
    transport_get_host_id_submit_count_address: int
    transport_get_host_id_callback_count_address: int
    transport_socket_submit_count_address: int
    transport_socket_callback_count_address: int
    transport_bind_submit_count_address: int
    transport_bind_callback_count_address: int
    transport_kd_fd_address: int
    transport_kd_closed_address: int
    transport_ip_fd_address: int
    transport_socket_fd_address: int
    transport_host_id_address: int
    transport_host_id_available_address: int
    transport_host_id_ready_address: int
    transport_service_started_address: int
    transport_bound_port_address: int
    transport_receive_submit_count_address: int
    transport_send_submit_count_address: int
    transport_receive_count_address: int
    transport_receive_bytes_address: int
    transport_send_count_address: int
    transport_send_bytes_address: int
    transport_receive_arm_count_address: int
    transport_receive_rearm_count_address: int
    transport_configured_exchange_limit_address: int
    transport_completed_exchange_count_address: int
    transport_current_exchange_index_address: int
    transport_last_completed_exchange_index_address: int
    transport_previous_peer_ipv4_address: int
    transport_previous_peer_port_address: int
    transport_rearm_submission_failure_count_address: int
    transport_loop_complete_transition_count_address: int
    transport_cleanup_deferred_count_address: int
    transport_last_receive_length_address: int
    transport_last_send_length_address: int
    transport_last_peer_ipv4_address: int
    transport_last_peer_port_address: int
    transport_last_peer_family_address: int
    transport_last_poll_action_address: int
    transport_last_submit_result_address: int
    transport_polls_while_receive_pending_address: int
    transport_polls_after_loop_complete_address: int
    transport_last_receive_preview_address: int
    transport_last_receive_preview_size: int
    transport_last_send_preview_address: int
    transport_last_send_preview_size: int
    transport_prepared_send_length_address: int
    transport_cp3w_datagrams_processed_address: int
    transport_cp3w_frames_valid_address: int
    transport_cp3w_frames_invalid_address: int
    transport_cp3w_frames_too_short_address: int
    transport_cp3w_frames_invalid_magic_address: int
    transport_cp3w_frames_invalid_version_address: int
    transport_cp3w_frames_unsupported_type_address: int
    transport_cp3w_frames_nonzero_flags_address: int
    transport_cp3w_frames_length_mismatch_address: int
    transport_cp3w_frames_payload_too_large_address: int
    transport_cp3w_frames_invalid_payload_address: int
    transport_cp3w_frames_malformed_address: int
    transport_cp3w_framed_responses_submitted_address: int
    transport_cp3w_framed_responses_completed_address: int
    transport_cp3w_last_request_id_address: int
    transport_cp3w_last_response_id_address: int
    transport_cp3w_last_message_type_address: int
    transport_cp3w_last_declared_payload_length_address: int
    transport_cp3w_last_actual_payload_length_address: int
    transport_cp3w_last_frame_result_address: int
    transport_cp3w_final_datagram_index_address: int
    transport_cp3w_requests_dispatched_address: int
    transport_cp3w_hello_requests_received_address: int
    transport_cp3w_hello_successes_address: int
    transport_cp3w_hello_version_rejections_address: int
    transport_cp3w_hello_responses_submitted_address: int
    transport_cp3w_hello_responses_completed_address: int
    transport_cp3w_hello_duplicate_requests_address: int
    transport_cp3w_hello_renegotiation_rejections_address: int
    transport_cp3w_pre_hello_gated_commands_address: int
    transport_cp3w_not_negotiated_responses_submitted_address: int
    transport_cp3w_not_negotiated_responses_completed_address: int
    transport_cp3w_ping_requests_received_address: int
    transport_cp3w_pong_responses_submitted_address: int
    transport_cp3w_pong_responses_completed_address: int
    transport_cp3w_unsupported_commands_received_address: int
    transport_cp3w_unsupported_responses_submitted_address: int
    transport_cp3w_unsupported_responses_completed_address: int
    transport_cp3w_negotiated_flag_address: int
    transport_cp3w_selected_protocol_version_address: int
    transport_cp3w_client_nonce_address: int
    transport_cp3w_client_capabilities_address: int
    transport_cp3w_runtime_capabilities_address: int
    transport_cp3w_accepted_capabilities_address: int
    transport_cp3w_session_id_address: int
    transport_cp3w_runtime_build_id_address: int
    transport_cp3w_last_command_address: int
    transport_cp3w_last_response_status_address: int
    transport_cp3w_last_ping_payload_length_address: int
    transport_cp3w_last_dispatch_result_address: int
    transport_cp3w_game_identity_state_addresses: dict[str, int]
    transport_cp3w_inventory_state_addresses: dict[str, int]
    transport_open_kd_submit_result_address: int
    transport_open_kd_callback_result_address: int
    transport_open_kd_submit_generation_address: int
    transport_open_kd_callback_generation_address: int
    transport_nwc24_submit_generation_address: int
    transport_nwc24_callback_generation_address: int
    transport_open_ip_submit_result_address: int
    transport_open_ip_callback_result_address: int
    transport_open_ip_submit_generation_address: int
    transport_open_ip_callback_generation_address: int
    transport_open_ip_path_pointer_address: int
    transport_open_ip_path_length_address: int
    transport_open_ip_mode_value_address: int
    transport_open_ip_callback_pointer_address: int
    transport_open_ip_context_pointer_address: int
    transport_open_ip_callback_exit_count_address: int
    transport_open_ip_stale_callback_count_address: int
    transport_open_ip_duplicate_callback_count_address: int
    transport_ip_fd_before_open_ip_address: int
    transport_kd_close_submit_result_address: int
    transport_kd_close_callback_result_address: int
    transport_kd_close_submit_generation_address: int
    transport_kd_close_callback_generation_address: int
    transport_kd_close_submitted_fd_address: int
    transport_kd_fd_before_close_address: int
    transport_kd_fd_after_close_address: int
    transport_startup_submit_result_address: int
    transport_startup_callback_result_address: int
    transport_startup_submit_generation_address: int
    transport_startup_callback_generation_address: int
    transport_startup_target_address: int
    transport_startup_command_address: int
    transport_startup_submitted_fd_address: int
    transport_startup_callback_pointer_address: int
    transport_startup_context_pointer_address: int
    transport_startup_callback_exit_count_address: int
    transport_startup_stale_callback_count_address: int
    transport_startup_duplicate_callback_count_address: int
    transport_startup_service_started_before_submit_address: int
    transport_startup_service_started_after_completion_address: int
    transport_ip_fd_before_startup_address: int
    transport_ip_fd_after_startup_address: int
    transport_startup_pending_before_submit_address: int
    transport_startup_pending_after_completion_address: int
    transport_startup_phase_before_submit_address: int
    transport_startup_phase_after_completion_address: int
    transport_startup_pre_call_args_address: int
    transport_startup_pre_call_args_size: int
    transport_get_host_id_submit_result_address: int
    transport_get_host_id_callback_result_address: int
    transport_get_host_id_submit_generation_address: int
    transport_get_host_id_callback_generation_address: int
    transport_get_host_id_target_address: int
    transport_get_host_id_command_address: int
    transport_get_host_id_submitted_fd_address: int
    transport_get_host_id_callback_pointer_address: int
    transport_get_host_id_context_pointer_address: int
    transport_get_host_id_callback_exit_count_address: int
    transport_get_host_id_stale_callback_count_address: int
    transport_get_host_id_duplicate_callback_count_address: int
    transport_get_host_id_service_started_before_submit_address: int
    transport_get_host_id_service_started_after_completion_address: int
    transport_ip_fd_before_get_host_id_address: int
    transport_ip_fd_after_get_host_id_address: int
    transport_get_host_id_pending_before_submit_address: int
    transport_get_host_id_pending_after_completion_address: int
    transport_get_host_id_phase_before_submit_address: int
    transport_get_host_id_phase_after_completion_address: int
    transport_get_host_id_pre_call_args_address: int
    transport_get_host_id_pre_call_args_size: int
    transport_socket_submit_result_address: int
    transport_socket_callback_result_address: int
    transport_socket_submit_generation_address: int
    transport_socket_callback_generation_address: int
    transport_socket_target_address: int
    transport_socket_command_address: int
    transport_socket_submitted_fd_address: int
    transport_socket_callback_pointer_address: int
    transport_socket_context_pointer_address: int
    transport_socket_callback_exit_count_address: int
    transport_socket_stale_callback_count_address: int
    transport_socket_duplicate_callback_count_address: int
    transport_socket_fd_before_submit_address: int
    transport_socket_fd_after_completion_address: int
    transport_socket_request_address_address: int
    transport_socket_request_storage_size_address: int
    transport_socket_request_logical_size_address: int
    transport_socket_request_alignment_address: int
    transport_socket_family_value_address: int
    transport_socket_type_value_address: int
    transport_socket_protocol_value_address: int
    transport_socket_descriptor_valid_address: int
    transport_socket_ready_address: int
    transport_socket_request_bytes_address: int
    transport_socket_request_bytes_size: int
    transport_socket_pre_call_args_address: int
    transport_socket_pre_call_args_size: int
    transport_bind_submit_result_address: int
    transport_bind_callback_result_address: int
    transport_bind_submit_generation_address: int
    transport_bind_callback_generation_address: int
    transport_bind_target_address: int
    transport_bind_command_address: int
    transport_bind_submitted_fd_address: int
    transport_bind_callback_pointer_address: int
    transport_bind_context_pointer_address: int
    transport_bind_callback_exit_count_address: int
    transport_bind_stale_callback_count_address: int
    transport_bind_duplicate_callback_count_address: int
    transport_bind_request_address_address: int
    transport_bind_request_storage_size_address: int
    transport_bind_request_logical_size_address: int
    transport_bind_request_alignment_address: int
    transport_bind_sockaddr_length_address: int
    transport_bind_family_value_address: int
    transport_bind_port_value_address: int
    transport_bind_address_value_address: int
    transport_bind_request_bytes_address: int
    transport_bind_request_bytes_size: int
    transport_bind_pre_call_args_address: int
    transport_bind_pre_call_args_size: int
    transport_cleanup_close_callback_count_address: int
    transport_cleanup_close_submit_result_address: int
    transport_cleanup_close_callback_result_address: int
    transport_cleanup_close_submit_generation_address: int
    transport_cleanup_close_callback_generation_address: int
    transport_cleanup_close_target_address: int
    transport_cleanup_close_command_address: int
    transport_cleanup_close_submitted_fd_address: int
    transport_cleanup_close_callback_pointer_address: int
    transport_cleanup_close_context_pointer_address: int
    transport_cleanup_close_callback_exit_count_address: int
    transport_cleanup_close_stale_callback_count_address: int
    transport_cleanup_close_duplicate_callback_count_address: int
    transport_cleanup_close_request_address_address: int
    transport_cleanup_close_request_storage_size_address: int
    transport_cleanup_close_request_logical_size_address: int
    transport_cleanup_close_request_alignment_address: int
    transport_cleanup_close_request_value_address: int
    transport_cleanup_close_request_bytes_address: int
    transport_cleanup_close_request_bytes_size: int
    transport_cleanup_close_pre_call_args_address: int
    transport_cleanup_close_pre_call_args_size: int
    transport_bound_flag_address: int
    transport_bound_address_address: int
    transport_socket_closed_after_bind_failure_address: int
    transport_socket_leak_detected_address: int
    cache_range_start: int
    cache_range_size: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--probe", action="store_true")
    parser.add_argument("--bootstrap-halt", action="store_true")
    parser.add_argument("--bootstrap-continue", action="store_true")
    parser.add_argument("--relocated-copy-halt", action="store_true")
    parser.add_argument("--relocated-return-halt", action="store_true")
    parser.add_argument("--relocated-continue", action="store_true")
    parser.add_argument("--enable-recurring-hook-diagnostics", action="store_true")
    parser.add_argument("--enable-ios-udp-diagnostic", action="store_true")
    parser.add_argument("--enable-ios-udp-diagnostic-init", action="store_true")
    parser.add_argument("--ios-udp-dry-run", action="store_true")
    parser.add_argument("--ios-open-via-retail-wrapper-once", action="store_true")
    parser.add_argument("--ios-nwc24-once", action="store_true")
    parser.add_argument("--ios-nwc24-via-retail-ioctl-once", action="store_true")
    parser.add_argument("--ios-close-kd-once", action="store_true")
    parser.add_argument("--ios-open-ip-once", action="store_true")
    parser.add_argument("--ios-so-startup-once", action="store_true")
    parser.add_argument("--ios-startup-once", action="store_true")
    parser.add_argument("--ios-get-host-id-once", action="store_true")
    parser.add_argument("--ios-create-socket-once", action="store_true")
    parser.add_argument("--ios-bind-once", action="store_true")
    parser.add_argument("--ios-recvfrom-once", action="store_true")
    parser.add_argument("--ios-recv-send-once", action="store_true")
    parser.add_argument("--ios-recv-send-loop", action="store_true")
    parser.add_argument("--ios-recv-send-loop-count", type=int, default=3)
    parser.add_argument("--ios-cp3w-frame-validation", action="store_true")
    parser.add_argument("--ios-cp3w-frame-validation-count", type=int, default=6)
    parser.add_argument("--ios-cp3w-ping-pong", action="store_true")
    parser.add_argument("--ios-cp3w-ping-pong-count", type=int, default=8)
    parser.add_argument("--ios-cp3w-hello-session", action="store_true")
    parser.add_argument("--ios-cp3w-hello-session-count", type=int, default=10)
    parser.add_argument("--ios-cp3w-game-identity", action="store_true")
    parser.add_argument("--ios-cp3w-game-identity-count", type=int, default=12)
    parser.add_argument("--ios-cp3w-inventory", action="store_true")
    parser.add_argument("--ios-cp3w-inventory-count", type=int, default=14)
    parser.add_argument("--ios-ioctl-async-abi-probe", action="store_true")
    parser.add_argument("--ios-open-kd-once", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--reserved-high")
    parser.add_argument("--diagnostic-address")
    parser.add_argument("--runtime-destination")
    return parser.parse_args()


def _argument_was_supplied(option: str) -> bool:
    return any(arg == option or arg.startswith(f"{option}=") for arg in sys.argv[1:])


def _prime3_ntsc_retail_ios_wrapper_metadata() -> Prime3RetailIosWrapperMetadata:
    return Prime3RetailIosWrapperMetadata(
        supported_dol_sha256=PRIME3_NTSC_RETAIL_DOL_SHA256,
        open_async_address=PRIME3_NTSC_IOS_OPEN_ASYNC_ADDRESS,
        open_address=PRIME3_NTSC_IOS_OPEN_ADDRESS,
        close_async_address=PRIME3_NTSC_IOS_CLOSE_ASYNC_ADDRESS,
        close_address=PRIME3_NTSC_IOS_CLOSE_ADDRESS,
        async_close_address=PRIME3_NTSC_IOS_CLOSE_ASYNC_ADDRESS,
        async_close_extent="0x805048A0..0x80504960",
        async_close_argument_count=3,
        async_close_stack_argument_count=0,
        async_close_operation=2,
        async_close_fingerprint_sha256="cad7a4b8950241515a9399d51c69d5680bba41fe060c37f5b6953effcdcb1288",
        async_close_prototype="s32 close_async(s32 fd, completion_fn completion, void *userdata)",
        async_close_register_arguments=("r3=fd", "r4=completion", "r5=userdata"),
        async_close_confidence="verified",
        read_async_address=PRIME3_NTSC_IOS_READ_ASYNC_ADDRESS,
        read_sync_address=PRIME3_NTSC_IOS_READ_SYNC_ADDRESS,
        write_async_address=PRIME3_NTSC_IOS_WRITE_ASYNC_ADDRESS,
        write_sync_address=PRIME3_NTSC_IOS_WRITE_SYNC_ADDRESS,
        seek_async_address=PRIME3_NTSC_IOS_SEEK_ASYNC_ADDRESS,
        seek_sync_address=PRIME3_NTSC_IOS_SEEK_SYNC_ADDRESS,
        confirmed_ioctl_async_address=PRIME3_NTSC_CONFIRMED_IOS_IOCTL_ASYNC_ADDRESS,
        confirmed_ioctl_sync_address=PRIME3_NTSC_CONFIRMED_IOS_IOCTL_SYNC_ADDRESS,
        confirmed_ioctlv_async_address=PRIME3_NTSC_CONFIRMED_IOS_IOCTLV_ASYNC_ADDRESS,
        confirmed_ioctlv_sync_address=PRIME3_NTSC_CONFIRMED_IOS_IOCTLV_SYNC_ADDRESS,
        async_ioctl_address=PRIME3_NTSC_CONFIRMED_IOS_IOCTL_ASYNC_ADDRESS,
        async_ioctl_extent="0x80504FE0..0x80505118",
        async_ioctl_argument_count=8,
        async_ioctl_stack_argument_count=0,
        async_ioctl_operation=6,
        async_ioctl_confidence="verified",
        confirmed_ioctl_async_fingerprint_sha256=("031342395575c5542428b9edfcd4fd3bf9633bfb54bd39726d3766b3e6f3b17b"),
        confirmed_ioctl_async_prototype=(
            "s32 ioctl_async(s32 fd, u32 command, const void *input, u32 input_length, "
            "void *output, u32 output_length, completion_fn completion, void *userdata)"
        ),
        confirmed_ioctl_async_register_arguments=(
            "r3=fd",
            "r4=command",
            "r5=input",
            "r6=input_length",
            "r7=output",
            "r8=output_length",
            "r9=completion",
            "r10=userdata",
        ),
        confirmed_ioctl_async_stack_arguments=(),
        request_field_offsets=(
            "operation=0x00",
            "result=0x04",
            "fd=0x08",
            "argument_0=0x0c",
            "argument_1=0x10",
            "argument_2=0x14",
            "argument_3=0x18",
            "argument_4=0x1c",
            "completion=0x20",
            "completion_userdata=0x24",
            "special_vector_flag=0x28",
        ),
        open_async_guard_words=PRIME3_NTSC_IOS_OPEN_ASYNC_GUARD_WORDS,
        callback_signature="s32 callback(s32 result, void *userdata)",
        preserved_registers=("r2", "r13"),
        submit_helper_address=PRIME3_NTSC_IOS_SUBMIT_HELPER_ADDRESS,
        request_allocator_address=PRIME3_NTSC_IOS_REQUEST_ALLOCATOR_ADDRESS,
        evidence_source=(
            "prime3-ntsc retail DOL operation 3-7 request construction, cache handling, "
            "completion fields, and compatible callsite verification"
        ),
        confidence="verified",
    )


def build_prime3_runtime_payload(  # noqa: C901
    output_dir: Path,
    *,
    probe: bool = False,
    payload_mode: str = PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL,
    enable_recurring_hook_diagnostics: bool = False,
    enable_ios_udp_diagnostic: bool = False,
    enable_tcp_tracker: bool = True,
    enable_ios_network_lifecycle: bool = True,
    ios_udp_mode: str = "normal",
    ios_udp_loop_count: int = 3,
    production_guard_bypass: str = "none",
    production_lifecycle_trace: bool = False,
    production_skyward_parity_owned_ip_top: bool = False,
    production_preserve_ping_layout: bool | None = None,
    production_size_optimize: bool = False,
    production_force_isolated_layout: bool = False,
    production_skyward_socket_bind_graft: bool = False,
    production_owned_ip_top_no_restart: bool = False,
    early_sda_capture: bool = False,
    native_beacon_ipv4: int = DEFAULT_NATIVE_BEACON_IPV4,
    reserved_high: int | None = None,
    diagnostic_address: int | None = None,
    runtime_destination: int | None = None,
    devkitppc_path: Path | None = None,
) -> Prime3RuntimePayloadManifest:
    if probe:
        if payload_mode != PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL:
            raise RuntimeError("Use either probe=True or an explicit payload_mode, not both.")
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_PROBE
    if payload_mode in PRIME3_RUNTIME_RELOCATED_MODES and (reserved_high is None or diagnostic_address is None):
        raise RuntimeError("Relocated runtime modes require reserved_high and diagnostic_address.")
    if payload_mode in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES and (reserved_high is None or diagnostic_address is None):
        raise RuntimeError("Entry bootstrap payload mode requires reserved_high and diagnostic_address.")

    if devkitppc_path is None:
        toolchain = resolve_prime3_runtime_toolchain()
    else:
        toolchain_env = dict(os.environ)
        toolchain_env["DEVKITPPC"] = os.fspath(devkitppc_path)
        toolchain_env["DEVKITPRO"] = os.fspath(devkitppc_path.parent)
        toolchain = resolve_prime3_runtime_toolchain(toolchain_env)
    output_dir.mkdir(parents=True, exist_ok=True)
    object_path = output_dir.joinpath("payload.o")
    elf_path = output_dir.joinpath("payload.elf")
    binary_path = output_dir.joinpath("payload.bin")
    map_path = output_dir.joinpath("payload.map")
    manifest_path = output_dir.joinpath("payload.json")

    relocated_runtime = None
    extra_link_objects: list[str] = []
    compiler_defines: list[str] = []
    linker_defines: list[str] = []

    if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_PROBE:
        compiler_defines.append("-DPRIME3_RUNTIME_PROBE_MODE=1")
    elif payload_mode in PRIME3_RUNTIME_RELOCATED_MODES:
        assert reserved_high is not None
        assert diagnostic_address is not None
        runtime_destination = RELOCATED_RUNTIME_DESTINATION if runtime_destination is None else runtime_destination
        relocated_runtime = _build_relocated_runtime(
            toolchain=toolchain,
            output_dir=output_dir.joinpath("relocated_runtime"),
            runtime_destination=runtime_destination,
            enable_recurring_hook_diagnostics=enable_recurring_hook_diagnostics,
            enable_ios_udp_diagnostic=enable_ios_udp_diagnostic,
            enable_tcp_tracker=enable_tcp_tracker,
            enable_ios_network_lifecycle=enable_ios_network_lifecycle,
            ios_udp_mode=ios_udp_mode,
            ios_udp_loop_count=ios_udp_loop_count,
            production_guard_bypass=production_guard_bypass,
            production_lifecycle_trace=production_lifecycle_trace,
            production_skyward_parity_owned_ip_top=production_skyward_parity_owned_ip_top,
            production_preserve_ping_layout=production_preserve_ping_layout,
            production_size_optimize=production_size_optimize,
            production_force_isolated_layout=production_force_isolated_layout,
            production_skyward_socket_bind_graft=production_skyward_socket_bind_graft,
            production_owned_ip_top_no_restart=production_owned_ip_top_no_restart,
            early_sda_capture=early_sda_capture,
            native_beacon_ipv4=native_beacon_ipv4,
        )
        _write_runtime_blob_object(
            toolchain=toolchain,
            output_dir=output_dir.joinpath("relocated_runtime"),
        )
        extra_link_objects.append(os.fspath(output_dir.joinpath("relocated_runtime", "runtime_blob.o")))
        compiler_defines.extend(
            [
                "-DPRIME3_RUNTIME_RELOCATED_MODE=1",
                f"-DPRIME3_BOOTSTRAP_STAGING_ADDRESS=0x{BOOTSTRAP_STAGING_ADDRESS:08X}",
                f"-DPRIME3_BOOTSTRAP_RESERVED_HIGH=0x{reserved_high:08X}",
                f"-DPRIME3_BOOTSTRAP_DIAGNOSTIC_ADDRESS=0x{diagnostic_address:08X}",
                f"-DPRIME3_RELOCATED_RUNTIME_DESTINATION_ADDRESS=0x{runtime_destination:08X}",
                f"-DPRIME3_RELOCATED_RUNTIME_ENTRY_ADDRESS=0x{relocated_runtime.entry_address:08X}",
                f"-DPRIME3_RELOCATED_CACHE_RANGE_START=0x{relocated_runtime.cache_range_start:08X}",
                (
                    f"-DPRIME3_RELOCATED_CACHE_RANGE_END="
                    f"0x{relocated_runtime.cache_range_start + relocated_runtime.cache_range_size:08X}"
                ),
                f"-DPRIME3_RUNTIME_CACHE_LINE_SIZE={RELOCATED_RUNTIME_CACHE_LINE_SIZE}",
                f"-DPRIME3_RUNTIME_COPY_COMPLETE_MARKER_ADDRESS=0x{relocated_runtime.copy_complete_marker_address:08X}",
                f"-DPRIME3_RUNTIME_COPY_COMPLETE_MARKER_VALUE=0x{RELOCATED_COPY_COMPLETE_MARKER_VALUE:08X}",
                f"-DPRIME3_RUNTIME_BOOTSTRAP_RETURN_MARKER_ADDRESS=0x{relocated_runtime.bootstrap_return_marker_address:08X}",
                f"-DPRIME3_RUNTIME_BOOTSTRAP_RETURN_MARKER_VALUE=0x{RELOCATED_BOOTSTRAP_RETURN_MARKER_VALUE:08X}",
            ]
        )
        compiler_defines.append(f"-DPRIME3_BOOTSTRAP_STATUS_VALUE=0x{_bootstrap_status_value(payload_mode):08X}")
        linker_defines.append(f"--defsym=__payload_link_address=0x{BOOTSTRAP_STAGING_ADDRESS:08X}")
        if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT:
            compiler_defines.append("-DPRIME3_RUNTIME_RELOCATED_COPY_HALT=1")
        elif payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT:
            compiler_defines.append("-DPRIME3_RUNTIME_RELOCATED_RETURN_HALT=1")
        else:
            compiler_defines.append("-DPRIME3_RUNTIME_RELOCATED_CONTINUE=1")
    elif payload_mode in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES:
        assert reserved_high is not None
        assert diagnostic_address is not None
        compiler_defines.extend(
            [
                "-DPRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODE=1",
                f"-DPRIME3_BOOTSTRAP_STAGING_ADDRESS=0x{BOOTSTRAP_STAGING_ADDRESS:08X}",
                f"-DPRIME3_BOOTSTRAP_RESERVED_HIGH=0x{reserved_high:08X}",
                f"-DPRIME3_BOOTSTRAP_DIAGNOSTIC_ADDRESS=0x{diagnostic_address:08X}",
                f"-DPRIME3_BOOTSTRAP_STATUS_VALUE=0x{_bootstrap_status_value(payload_mode):08X}",
            ]
        )
        linker_defines.append(f"--defsym=__payload_link_address=0x{BOOTSTRAP_STAGING_ADDRESS:08X}")
        if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT:
            compiler_defines.append("-DPRIME3_RUNTIME_ENTRY_BOOTSTRAP_HALT=1")
        else:
            compiler_defines.append("-DPRIME3_RUNTIME_ENTRY_BOOTSTRAP_CONTINUE=1")

    _run(
        [
            os.fspath(toolchain.compiler_path),
            *toolchain.required_machine_flags,
            *compiler_defines,
            "-x",
            "assembler-with-cpp",
            "-c",
            os.fspath(SCRIPT_ROOT.joinpath("payload.S")),
            "-o",
            os.fspath(object_path),
        ]
    )
    _run(
        [
            os.fspath(toolchain.linker_path),
            "-EB",
            "--build-id=none",
            "--gc-sections",
            *linker_defines,
            "-T",
            os.fspath(SCRIPT_ROOT.joinpath("payload.ld")),
            "-Map",
            os.fspath(map_path),
            "-o",
            os.fspath(elf_path),
            os.fspath(object_path),
            *extra_link_objects,
        ]
    )
    _run(
        [
            os.fspath(toolchain.objcopy_path),
            "-O",
            "binary",
            os.fspath(elf_path),
            os.fspath(binary_path),
        ]
    )

    payload_bytes = binary_path.read_bytes()
    payload_sha256 = hashlib.sha256(payload_bytes).hexdigest()
    readelf_header = _run([os.fspath(toolchain.readelf_path), "-h", os.fspath(elf_path)])
    readelf_symbols = _run([os.fspath(toolchain.readelf_path), "-s", "--wide", os.fspath(elf_path)])
    readelf_relocations = _run([os.fspath(toolchain.readelf_path), "-r", os.fspath(elf_path)])
    readelf_dynamic = _run([os.fspath(toolchain.readelf_path), "-d", os.fspath(elf_path)], allow_failure=True)
    _validate_readelf_header(readelf_header)

    symbol_base = BOOTSTRAP_STAGING_ADDRESS if payload_mode in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES else 0
    entry_offset = _extract_entry_offset(readelf_symbols, PRIME3_RUNTIME_ENTRY_SYMBOL, symbol_base=symbol_base)
    canary_start_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        PROBE_CANARY_START_SYMBOL,
        symbol_base=symbol_base,
    )
    canary_end_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        PROBE_CANARY_END_SYMBOL,
        symbol_base=symbol_base,
    )
    counter_offset = _extract_optional_symbol_offset(readelf_symbols, PROBE_COUNTER_SYMBOL, symbol_base=symbol_base)
    save_area_start_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        BOOTSTRAP_SAVE_AREA_START_SYMBOL,
        symbol_base=symbol_base,
    )
    save_area_end_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        BOOTSTRAP_SAVE_AREA_END_SYMBOL,
        symbol_base=symbol_base,
    )
    halt_loop_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        BOOTSTRAP_HALT_LOOP_SYMBOL,
        symbol_base=symbol_base,
    )
    embedded_runtime_start_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        EMBEDDED_RUNTIME_START_SYMBOL,
        symbol_base=symbol_base,
    )
    embedded_runtime_end_offset = _extract_optional_symbol_offset(
        readelf_symbols,
        EMBEDDED_RUNTIME_END_SYMBOL,
        symbol_base=symbol_base,
    )
    unresolved_relocation_count = _count_relocations(readelf_relocations)
    dynamic_section_count = _count_dynamic_sections(readelf_dynamic)

    canary_size = None
    if canary_start_offset is not None or canary_end_offset is not None:
        if canary_start_offset is None or canary_end_offset is None or canary_end_offset <= canary_start_offset:
            raise RuntimeError("Probe payload canary symbols are malformed.")
        canary_size = canary_end_offset - canary_start_offset

    entry_bootstrap = None
    relocated_runtime_metadata = None
    if payload_mode in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES:
        if (
            save_area_start_offset is None
            or save_area_end_offset is None
            or save_area_end_offset <= save_area_start_offset
        ):
            raise RuntimeError("Entry bootstrap payload save-area symbols are malformed.")
        if payload_mode in PRIME3_RUNTIME_HALT_MODES and halt_loop_offset is None:
            raise RuntimeError("Halt bootstrap payload is missing the halt-loop symbol.")
        if payload_mode in PRIME3_RUNTIME_CONTINUE_MODES and halt_loop_offset is not None:
            raise RuntimeError("Continue bootstrap payload should not export a halt-loop symbol.")
        assert reserved_high is not None
        assert diagnostic_address is not None
        entry_bootstrap = Prime3EntryBootstrapMetadata(
            mode=payload_mode,
            staging_address=BOOTSTRAP_STAGING_ADDRESS,
            staging_save_area_offset=save_area_start_offset,
            staging_save_area_size=save_area_end_offset - save_area_start_offset,
            halt_loop_address=None if halt_loop_offset is None else BOOTSTRAP_STAGING_ADDRESS + halt_loop_offset,
            reserved_boundary=reserved_high,
            reserved_range_start=reserved_high,
            reserved_range_end=0x817FE3A0,
            diagnostic_address=diagnostic_address,
            diagnostic_block_size=BOOTSTRAP_DIAGNOSTIC_BLOCK_SIZE,
            canary_address=diagnostic_address + BOOTSTRAP_CANARY_OFFSET,
            canary_size=len(BOOTSTRAP_CANARY_BYTES),
            canary_sha256=hashlib.sha256(BOOTSTRAP_CANARY_BYTES).hexdigest(),
            marker_address=diagnostic_address + BOOTSTRAP_MARKER_OFFSET,
            marker_value=BOOTSTRAP_MARKER_VALUE,
            counter_address=diagnostic_address + BOOTSTRAP_COUNTER_OFFSET,
            counter_size=4,
            original_80000034_address=diagnostic_address + BOOTSTRAP_ORIGINAL_80000034_OFFSET,
            original_80003110_address=diagnostic_address + BOOTSTRAP_ORIGINAL_80003110_OFFSET,
            replacement_value_address=diagnostic_address + BOOTSTRAP_REPLACEMENT_VALUE_OFFSET,
            replacement_value=reserved_high,
            status_address=diagnostic_address + BOOTSTRAP_STATUS_OFFSET,
            status_value=_bootstrap_status_value(payload_mode),
            original_entry_instruction=BOOTSTRAP_ORIGINAL_ENTRY_INSTRUCTION,
            original_branch_target=BOOTSTRAP_ORIGINAL_BRANCH_TARGET,
            original_continuation_address=BOOTSTRAP_ORIGINAL_CONTINUATION_ADDRESS,
        )

    if payload_mode in PRIME3_RUNTIME_RELOCATED_MODES:
        if embedded_runtime_start_offset is None or embedded_runtime_end_offset is None:
            raise RuntimeError("Relocated compound payload is missing the embedded runtime blob symbols.")
        if embedded_runtime_end_offset <= embedded_runtime_start_offset:
            raise RuntimeError("Relocated embedded runtime blob symbols are malformed.")
        assert relocated_runtime is not None
        low_bootstrap_bytes = payload_bytes[:embedded_runtime_start_offset]
        embedded_runtime_bytes = payload_bytes[embedded_runtime_start_offset:embedded_runtime_end_offset]
        if hashlib.sha256(embedded_runtime_bytes).hexdigest() != relocated_runtime.payload_sha256:
            raise RuntimeError("Embedded runtime blob hash does not match the separately linked runtime payload.")
        runtime_destination = RELOCATED_RUNTIME_DESTINATION if runtime_destination is None else runtime_destination
        diagnostic_metadata = None
        abi_probe_metadata = Prime3RuntimeAbiProbeMetadata(
            mode="retail_wrapper_ioctl_async_abi_probe",
            supplied_args_address=relocated_runtime.abi_probe_supplied_args_address,
            supplied_args_size=relocated_runtime.abi_probe_supplied_args_size,
            pre_call_args_address=relocated_runtime.abi_probe_pre_call_args_address,
            pre_call_args_size=relocated_runtime.abi_probe_pre_call_args_size,
            target_args_address=relocated_runtime.abi_probe_target_args_address,
            target_args_size=relocated_runtime.abi_probe_target_args_size,
            return_value_address=relocated_runtime.abi_probe_return_value_address,
            return_value_size=4,
            expected_return_value=0x13579BDF,
            result_flags_address=relocated_runtime.abi_probe_result_flags_address,
            result_flags_size=4,
            stack_pointer_before_address=relocated_runtime.abi_probe_stack_pointer_before_address,
            stack_pointer_before_size=4,
            stack_pointer_after_address=relocated_runtime.abi_probe_stack_pointer_after_address,
            stack_pointer_after_size=4,
            saved_lr_address=relocated_runtime.abi_probe_saved_lr_address,
            saved_lr_size=4,
            restored_lr_address=relocated_runtime.abi_probe_restored_lr_address,
            restored_lr_size=4,
            saved_r2_address=relocated_runtime.abi_probe_saved_r2_address,
            saved_r2_size=4,
            restored_r2_address=relocated_runtime.abi_probe_restored_r2_address,
            restored_r2_size=4,
            saved_r13_address=relocated_runtime.abi_probe_saved_r13_address,
            saved_r13_size=4,
            restored_r13_address=relocated_runtime.abi_probe_restored_r13_address,
            restored_r13_size=4,
            target_ctr_address=relocated_runtime.abi_probe_target_ctr_address,
            target_ctr_size=4,
            after_call_flag_address=relocated_runtime.abi_probe_after_call_flag_address,
            after_call_flag_size=4,
        )
        if enable_recurring_hook_diagnostics:
            diagnostic_fields = (
                relocated_runtime.diagnostic_hook_wrapper_entry_count_address,
                relocated_runtime.diagnostic_hook_wrapper_before_poll_count_address,
                relocated_runtime.diagnostic_poll_entry_count_address,
                relocated_runtime.diagnostic_poll_exit_count_address,
                relocated_runtime.diagnostic_state_machine_entry_count_address,
                relocated_runtime.diagnostic_state_machine_exit_count_address,
                relocated_runtime.diagnostic_c_before_veneer_call_count_address,
                relocated_runtime.diagnostic_retail_veneer_entry_count_address,
                relocated_runtime.diagnostic_retail_target_return_count_address,
                relocated_runtime.diagnostic_retail_veneer_exit_count_address,
                relocated_runtime.diagnostic_c_after_veneer_call_count_address,
                relocated_runtime.diagnostic_ios_submit_attempt_count_address,
                relocated_runtime.diagnostic_ios_submit_return_count_address,
                relocated_runtime.diagnostic_ios_submit_return_value_address,
                relocated_runtime.diagnostic_callback_entry_count_address,
                relocated_runtime.diagnostic_callback_exit_count_address,
                relocated_runtime.diagnostic_hook_wrapper_after_poll_count_address,
                relocated_runtime.diagnostic_hook_wrapper_exit_count_address,
                relocated_runtime.diagnostic_last_execution_marker_address,
                relocated_runtime.diagnostic_last_phase_before_step_address,
                relocated_runtime.diagnostic_last_phase_after_step_address,
                relocated_runtime.diagnostic_callback_result_address,
            )
            if any(value is None for value in diagnostic_fields):
                raise RuntimeError("Relocated runtime diagnostics are missing required symbols.")
            assert relocated_runtime.diagnostic_hook_wrapper_entry_count_address is not None
            assert relocated_runtime.diagnostic_hook_wrapper_before_poll_count_address is not None
            assert relocated_runtime.diagnostic_poll_entry_count_address is not None
            assert relocated_runtime.diagnostic_poll_exit_count_address is not None
            assert relocated_runtime.diagnostic_state_machine_entry_count_address is not None
            assert relocated_runtime.diagnostic_state_machine_exit_count_address is not None
            assert relocated_runtime.diagnostic_c_before_veneer_call_count_address is not None
            assert relocated_runtime.diagnostic_retail_veneer_entry_count_address is not None
            assert relocated_runtime.diagnostic_retail_target_return_count_address is not None
            assert relocated_runtime.diagnostic_retail_veneer_exit_count_address is not None
            assert relocated_runtime.diagnostic_c_after_veneer_call_count_address is not None
            assert relocated_runtime.diagnostic_ios_submit_attempt_count_address is not None
            assert relocated_runtime.diagnostic_ios_submit_return_count_address is not None
            assert relocated_runtime.diagnostic_ios_submit_return_value_address is not None
            assert relocated_runtime.diagnostic_callback_entry_count_address is not None
            assert relocated_runtime.diagnostic_callback_exit_count_address is not None
            assert relocated_runtime.diagnostic_hook_wrapper_after_poll_count_address is not None
            assert relocated_runtime.diagnostic_hook_wrapper_exit_count_address is not None
            assert relocated_runtime.diagnostic_last_execution_marker_address is not None
            assert relocated_runtime.diagnostic_last_phase_before_step_address is not None
            assert relocated_runtime.diagnostic_last_phase_after_step_address is not None
            assert relocated_runtime.diagnostic_callback_result_address is not None
            diagnostic_metadata = Prime3RuntimeDiagnosticMetadata(
                mode=ios_udp_mode if enable_ios_udp_diagnostic else "transport_disabled",
                hook_wrapper_entry_count_address=relocated_runtime.diagnostic_hook_wrapper_entry_count_address,
                hook_wrapper_entry_count_size=4,
                hook_wrapper_before_poll_count_address=relocated_runtime.diagnostic_hook_wrapper_before_poll_count_address,
                hook_wrapper_before_poll_count_size=4,
                runtime_poll_entry_count_address=relocated_runtime.diagnostic_poll_entry_count_address,
                runtime_poll_entry_count_size=4,
                runtime_poll_exit_count_address=relocated_runtime.diagnostic_poll_exit_count_address,
                runtime_poll_exit_count_size=4,
                state_machine_entry_count_address=relocated_runtime.diagnostic_state_machine_entry_count_address,
                state_machine_entry_count_size=4,
                state_machine_exit_count_address=relocated_runtime.diagnostic_state_machine_exit_count_address,
                state_machine_exit_count_size=4,
                c_before_veneer_call_count_address=relocated_runtime.diagnostic_c_before_veneer_call_count_address,
                c_before_veneer_call_count_size=4,
                retail_veneer_entry_count_address=relocated_runtime.diagnostic_retail_veneer_entry_count_address,
                retail_veneer_entry_count_size=4,
                retail_target_return_count_address=relocated_runtime.diagnostic_retail_target_return_count_address,
                retail_target_return_count_size=4,
                retail_veneer_exit_count_address=relocated_runtime.diagnostic_retail_veneer_exit_count_address,
                retail_veneer_exit_count_size=4,
                c_after_veneer_call_count_address=relocated_runtime.diagnostic_c_after_veneer_call_count_address,
                c_after_veneer_call_count_size=4,
                ios_submit_attempt_count_address=relocated_runtime.diagnostic_ios_submit_attempt_count_address,
                ios_submit_attempt_count_size=4,
                ios_submit_return_count_address=relocated_runtime.diagnostic_ios_submit_return_count_address,
                ios_submit_return_count_size=4,
                ios_submit_return_value_address=relocated_runtime.diagnostic_ios_submit_return_value_address,
                ios_submit_return_value_size=4,
                callback_entry_count_address=relocated_runtime.diagnostic_callback_entry_count_address,
                callback_entry_count_size=4,
                callback_exit_count_address=relocated_runtime.diagnostic_callback_exit_count_address,
                callback_exit_count_size=4,
                hook_wrapper_after_poll_count_address=relocated_runtime.diagnostic_hook_wrapper_after_poll_count_address,
                hook_wrapper_after_poll_count_size=4,
                hook_wrapper_exit_count_address=relocated_runtime.diagnostic_hook_wrapper_exit_count_address,
                hook_wrapper_exit_count_size=4,
                last_execution_marker_address=relocated_runtime.diagnostic_last_execution_marker_address,
                last_execution_marker_size=4,
                last_transport_phase_before_step_address=relocated_runtime.diagnostic_last_phase_before_step_address,
                last_transport_phase_before_step_size=4,
                last_transport_phase_after_step_address=relocated_runtime.diagnostic_last_phase_after_step_address,
                last_transport_phase_after_step_size=4,
                callback_result_address=relocated_runtime.diagnostic_callback_result_address,
                callback_result_size=4,
            )
        # The legacy UDP metadata is retained below only while old assets remain
        # readable. It is not part of the TCP production manifest.
        transport_metadata = None
        if False:
            nwc24_ioctl_once = ios_udp_mode == "retail_wrapper_nwc24_startup_once"
            nwc24_close_once = ios_udp_mode == "retail_wrapper_nwc24_close_kd_once"
            open_ip_once = ios_udp_mode == "retail_wrapper_nwc24_close_open_ip_once"
            so_startup_once = ios_udp_mode == "retail_wrapper_nwc24_close_open_ip_startup_once"
            startup_once = ios_udp_mode == "retail_wrapper_startup_once"
            get_host_id_once = ios_udp_mode == "retail_wrapper_get_host_id_once"
            create_socket_once = ios_udp_mode == "retail_wrapper_create_socket_once"
            recvfrom_once = ios_udp_mode == "retail_wrapper_recvfrom_once"
            recv_send_once = ios_udp_mode == "retail_wrapper_recv_send_once"
            recv_send_loop = ios_udp_mode == "retail_wrapper_recv_send_loop"
            cp3w_frame_validation = ios_udp_mode == "cp3w_frame_validation"
            cp3w_ping_pong = ios_udp_mode == "cp3w_ping_pong"
            cp3w_hello_session = ios_udp_mode == "cp3w_hello_session"
            cp3w_game_identity = ios_udp_mode == "cp3w_game_identity"
            cp3w_inventory_service = ios_udp_mode == "cp3w_inventory_service"
            cp3w_inventory = ios_udp_mode in {"cp3w_inventory", "cp3w_inventory_service"}
            native_wc24_bootstrap = ios_udp_mode == "native_wc24_bootstrap_beacon_once"
            transport_metadata = LegacyPrime3RuntimeTransportMetadata(
                mode=ios_udp_mode,
                udp_port=43674,
                initialization_enabled=True,
                receive_enabled=(
                    recvfrom_once
                    or recv_send_once
                    or recv_send_loop
                    or cp3w_frame_validation
                    or cp3w_ping_pong
                    or cp3w_hello_session
                    or cp3w_game_identity
                    or cp3w_inventory
                ),
                send_enabled=(
                    recv_send_once
                    or recv_send_loop
                    or cp3w_frame_validation
                    or cp3w_ping_pong
                    or cp3w_hello_session
                    or cp3w_game_identity
                    or cp3w_inventory
                    or native_wc24_bootstrap
                ),
                nwc24_startup_enabled=True,
                kd_close_enabled=not (nwc24_ioctl_once or native_wc24_bootstrap),
                ip_close_on_success=False,
                socket_close_on_success=False,
                network_diagnostics_address=relocated_runtime.network_diagnostics_address,
                network_diagnostics_size=0x100,
                network_diagnostics_version=1,
                terminal_phase_value=(
                    26
                    if cp3w_inventory_service
                    else 115
                    if native_wc24_bootstrap
                    else 0xFE
                    if nwc24_ioctl_once or nwc24_close_once or open_ip_once or startup_once
                    else 18
                    if so_startup_once
                    else 19
                    if get_host_id_once
                    else 20
                    if create_socket_once
                    else 27
                    if recvfrom_once
                    else 61
                    if cp3w_ping_pong
                    else 69
                    if cp3w_hello_session
                    else 79
                    if cp3w_game_identity
                    else 93
                    if cp3w_inventory
                    else 55
                    if cp3w_frame_validation
                    else 45
                    if recv_send_loop
                    else 37
                    if recv_send_once
                    else 0x11
                ),
                terminal_phase_name=(
                    "WAIT_RECEIVE"
                    if cp3w_inventory_service
                    else "NATIVE_BEACON_COMPLETE"
                    if native_wc24_bootstrap
                    else "DIAGNOSTIC_COMPLETE"
                    if startup_once
                    else "NWC24_COMPLETE"
                    if nwc24_ioctl_once
                    else "KD_CLOSED"
                    if nwc24_close_once
                    else "IP_OPEN"
                    if open_ip_once
                    else "SO_STARTED"
                    if so_startup_once
                    else "HOST_ID_READY"
                    if get_host_id_once
                    else "SOCKET_READY"
                    if create_socket_once
                    else "RECEIVED_DATAGRAM"
                    if recvfrom_once
                    else "CP3W_PING_PONG_LOOP_COMPLETE"
                    if cp3w_ping_pong
                    else "CP3W_HELLO_SESSION_LOOP_COMPLETE"
                    if cp3w_hello_session
                    else "CP3W_GAME_IDENTITY_LOOP_COMPLETE"
                    if cp3w_game_identity
                    else "CP3W_INVENTORY_LOOP_COMPLETE"
                    if cp3w_inventory
                    else "CP3W_FRAME_LOOP_COMPLETE"
                    if cp3w_frame_validation
                    else "LOOP_COMPLETE"
                    if recv_send_loop
                    else "SENT_DATAGRAM"
                    if recv_send_once
                    else "BOUND_NO_RECV"
                ),
                phase_address=relocated_runtime.transport_phase_address,
                phase_size=4,
                last_error_address=relocated_runtime.transport_last_error_address,
                last_error_size=4,
                last_socket_error_address=relocated_runtime.transport_last_socket_error_address,
                last_socket_error_size=4,
                last_ios_result_address=relocated_runtime.transport_last_ios_result_address,
                last_ios_result_size=4,
                pending_operation_address=relocated_runtime.transport_pending_operation_address,
                pending_operation_size=4,
                pending_generation_address=relocated_runtime.transport_pending_generation_address,
                pending_generation_size=4,
                callback_generation_address=relocated_runtime.transport_callback_generation_address,
                callback_generation_size=4,
                callback_count_address=relocated_runtime.transport_callback_count_address,
                callback_count_size=4,
                rejected_callback_count_address=relocated_runtime.transport_rejected_callback_count_address,
                rejected_callback_count_size=4,
                callback_pending_address=relocated_runtime.transport_callback_pending_address,
                callback_pending_size=4,
                open_kd_submit_count_address=relocated_runtime.transport_open_kd_submit_count_address,
                open_kd_submit_count_size=4,
                open_kd_callback_count_address=relocated_runtime.transport_open_kd_callback_count_address,
                open_kd_callback_count_size=4,
                nwc24_output_buffer_address=relocated_runtime.transport_nwc24_output_buffer_address,
                nwc24_output_buffer_size=0x20,
                nwc24_output_buffer_alignment=0x20,
                nwc24_submit_count_address=relocated_runtime.transport_nwc24_submit_count_address,
                nwc24_submit_count_size=4,
                nwc24_callback_count_address=relocated_runtime.transport_nwc24_callback_count_address,
                nwc24_callback_count_size=4,
                nwc24_synchronous_result_address=relocated_runtime.transport_nwc24_synchronous_result_address,
                nwc24_synchronous_result_size=4,
                nwc24_callback_result_address=relocated_runtime.transport_nwc24_callback_result_address,
                nwc24_callback_result_size=4,
                nwc24_output_digest_address=relocated_runtime.transport_nwc24_output_digest_address,
                nwc24_output_digest_size=4,
                open_ip_submit_count_address=relocated_runtime.transport_open_ip_submit_count_address,
                open_ip_submit_count_size=4,
                open_ip_callback_count_address=relocated_runtime.transport_open_ip_callback_count_address,
                open_ip_callback_count_size=4,
                kd_close_submit_count_address=relocated_runtime.transport_kd_close_submit_count_address,
                kd_close_submit_count_size=4,
                kd_close_callback_count_address=relocated_runtime.transport_kd_close_callback_count_address,
                kd_close_callback_count_size=4,
                startup_submit_count_address=relocated_runtime.transport_startup_submit_count_address,
                startup_submit_count_size=4,
                startup_callback_count_address=relocated_runtime.transport_startup_callback_count_address,
                startup_callback_count_size=4,
                get_host_id_submit_count_address=relocated_runtime.transport_get_host_id_submit_count_address,
                get_host_id_submit_count_size=4,
                get_host_id_callback_count_address=relocated_runtime.transport_get_host_id_callback_count_address,
                get_host_id_callback_count_size=4,
                socket_submit_count_address=relocated_runtime.transport_socket_submit_count_address,
                socket_submit_count_size=4,
                socket_callback_count_address=relocated_runtime.transport_socket_callback_count_address,
                socket_callback_count_size=4,
                bind_submit_count_address=relocated_runtime.transport_bind_submit_count_address,
                bind_submit_count_size=4,
                bind_callback_count_address=relocated_runtime.transport_bind_callback_count_address,
                bind_callback_count_size=4,
                kd_fd_address=relocated_runtime.transport_kd_fd_address,
                kd_fd_size=4,
                kd_closed_address=relocated_runtime.transport_kd_closed_address,
                kd_closed_size=4,
                ip_fd_address=relocated_runtime.transport_ip_fd_address,
                ip_fd_size=4,
                socket_fd_address=relocated_runtime.transport_socket_fd_address,
                socket_fd_size=4,
                host_id_address=relocated_runtime.transport_host_id_address,
                host_id_size=4,
                host_id_available_address=relocated_runtime.transport_host_id_available_address,
                host_id_available_size=4,
                host_id_ready_address=relocated_runtime.transport_host_id_ready_address,
                host_id_ready_size=4,
                service_started_address=relocated_runtime.transport_service_started_address,
                service_started_size=4,
                bound_port_address=relocated_runtime.transport_bound_port_address,
                bound_port_size=4,
                receive_submit_count_address=relocated_runtime.transport_receive_submit_count_address,
                receive_submit_count_size=4,
                send_submit_count_address=relocated_runtime.transport_send_submit_count_address,
                send_submit_count_size=4,
                ip_close_submit_count_address=relocated_runtime.transport_ip_close_submit_count_address,
                ip_close_submit_count_size=4,
                socket_close_submit_count_address=relocated_runtime.transport_socket_close_submit_count_address,
                socket_close_submit_count_size=4,
                receive_count_address=relocated_runtime.transport_receive_count_address,
                receive_count_size=4,
                receive_bytes_address=relocated_runtime.transport_receive_bytes_address,
                receive_bytes_size=4,
                send_count_address=relocated_runtime.transport_send_count_address,
                send_count_size=4,
                send_bytes_address=relocated_runtime.transport_send_bytes_address,
                send_bytes_size=4,
                cp3w_magic_hex=PROTOCOL_MAGIC.hex(),
                cp3w_protocol_version=PROTOCOL_VERSION,
                cp3w_header_size=HEADER_SIZE,
                cp3w_crc_size=CRC_SIZE,
                cp3w_crc_initial_value=0xFFFFFFFF,
                cp3w_crc_final_xor_value=0xFFFFFFFF,
                cp3w_crc_polynomial=0xEDB88320,
                cp3w_crc_reflected=True,
                cp3w_packet_kind_request=1,
                cp3w_packet_kind_response=2,
                cp3w_response_status_error=1,
                cp3w_command_ping=3,
                cp3w_pong_command=3,
                cp3w_pong_uses_ping_command=True,
                cp3w_command_reserved_mailbox=127,
                cp3w_error_code_unknown_command=4,
                cp3w_packet_kind_offset=5,
                cp3w_command_offset=6,
                cp3w_response_status_offset=7,
                cp3w_request_id_offset=8,
                cp3w_payload_length_offset=12,
                cp3w_ping_max_payload_length=64 - HEADER_SIZE - CRC_SIZE,
                cp3w_request_payload_ascii="P3_FRAME_TEST_20260717",
                cp3w_response_payload_ascii="P3_FRAME_ACK_20260717",
                cp3w_unsupported_message_ascii="Command is unsupported",
                cp3w_request_payload_length=len("P3_FRAME_TEST_20260717"),
                cp3w_response_payload_length=len("P3_FRAME_ACK_20260717"),
                prepared_send_length_address=relocated_runtime.transport_prepared_send_length_address,
                prepared_send_length_size=4,
                cp3w_datagrams_processed_address=relocated_runtime.transport_cp3w_datagrams_processed_address,
                cp3w_datagrams_processed_size=4,
                cp3w_frames_valid_address=relocated_runtime.transport_cp3w_frames_valid_address,
                cp3w_frames_valid_size=4,
                cp3w_frames_invalid_address=relocated_runtime.transport_cp3w_frames_invalid_address,
                cp3w_frames_invalid_size=4,
                cp3w_frames_too_short_address=relocated_runtime.transport_cp3w_frames_too_short_address,
                cp3w_frames_too_short_size=4,
                cp3w_frames_invalid_magic_address=relocated_runtime.transport_cp3w_frames_invalid_magic_address,
                cp3w_frames_invalid_magic_size=4,
                cp3w_frames_invalid_version_address=relocated_runtime.transport_cp3w_frames_invalid_version_address,
                cp3w_frames_invalid_version_size=4,
                cp3w_frames_unsupported_type_address=relocated_runtime.transport_cp3w_frames_unsupported_type_address,
                cp3w_frames_unsupported_type_size=4,
                cp3w_frames_nonzero_flags_address=relocated_runtime.transport_cp3w_frames_nonzero_flags_address,
                cp3w_frames_nonzero_flags_size=4,
                cp3w_frames_length_mismatch_address=relocated_runtime.transport_cp3w_frames_length_mismatch_address,
                cp3w_frames_length_mismatch_size=4,
                cp3w_frames_payload_too_large_address=relocated_runtime.transport_cp3w_frames_payload_too_large_address,
                cp3w_frames_payload_too_large_size=4,
                cp3w_frames_invalid_payload_address=relocated_runtime.transport_cp3w_frames_invalid_payload_address,
                cp3w_frames_invalid_payload_size=4,
                cp3w_frames_malformed_address=relocated_runtime.transport_cp3w_frames_malformed_address,
                cp3w_frames_malformed_size=4,
                cp3w_framed_responses_submitted_address=relocated_runtime.transport_cp3w_framed_responses_submitted_address,
                cp3w_framed_responses_submitted_size=4,
                cp3w_framed_responses_completed_address=relocated_runtime.transport_cp3w_framed_responses_completed_address,
                cp3w_framed_responses_completed_size=4,
                cp3w_last_request_id_address=relocated_runtime.transport_cp3w_last_request_id_address,
                cp3w_last_request_id_size=4,
                cp3w_last_response_id_address=relocated_runtime.transport_cp3w_last_response_id_address,
                cp3w_last_response_id_size=4,
                cp3w_last_message_type_address=relocated_runtime.transport_cp3w_last_message_type_address,
                cp3w_last_message_type_size=4,
                cp3w_last_declared_payload_length_address=(
                    relocated_runtime.transport_cp3w_last_declared_payload_length_address
                ),
                cp3w_last_declared_payload_length_size=4,
                cp3w_last_actual_payload_length_address=(
                    relocated_runtime.transport_cp3w_last_actual_payload_length_address
                ),
                cp3w_last_actual_payload_length_size=4,
                cp3w_last_frame_result_address=relocated_runtime.transport_cp3w_last_frame_result_address,
                cp3w_last_frame_result_size=4,
                cp3w_final_datagram_index_address=relocated_runtime.transport_cp3w_final_datagram_index_address,
                cp3w_final_datagram_index_size=4,
                cp3w_requests_dispatched_address=relocated_runtime.transport_cp3w_requests_dispatched_address,
                cp3w_requests_dispatched_size=4,
                cp3w_hello_requests_received_address=relocated_runtime.transport_cp3w_hello_requests_received_address,
                cp3w_hello_requests_received_size=4,
                cp3w_hello_successes_address=relocated_runtime.transport_cp3w_hello_successes_address,
                cp3w_hello_successes_size=4,
                cp3w_hello_version_rejections_address=(
                    relocated_runtime.transport_cp3w_hello_version_rejections_address
                ),
                cp3w_hello_version_rejections_size=4,
                cp3w_hello_responses_submitted_address=(
                    relocated_runtime.transport_cp3w_hello_responses_submitted_address
                ),
                cp3w_hello_responses_submitted_size=4,
                cp3w_hello_responses_completed_address=(
                    relocated_runtime.transport_cp3w_hello_responses_completed_address
                ),
                cp3w_hello_responses_completed_size=4,
                cp3w_hello_duplicate_requests_address=(
                    relocated_runtime.transport_cp3w_hello_duplicate_requests_address
                ),
                cp3w_hello_duplicate_requests_size=4,
                cp3w_hello_renegotiation_rejections_address=(
                    relocated_runtime.transport_cp3w_hello_renegotiation_rejections_address
                ),
                cp3w_hello_renegotiation_rejections_size=4,
                cp3w_pre_hello_gated_commands_address=(
                    relocated_runtime.transport_cp3w_pre_hello_gated_commands_address
                ),
                cp3w_pre_hello_gated_commands_size=4,
                cp3w_not_negotiated_responses_submitted_address=(
                    relocated_runtime.transport_cp3w_not_negotiated_responses_submitted_address
                ),
                cp3w_not_negotiated_responses_submitted_size=4,
                cp3w_not_negotiated_responses_completed_address=(
                    relocated_runtime.transport_cp3w_not_negotiated_responses_completed_address
                ),
                cp3w_not_negotiated_responses_completed_size=4,
                cp3w_ping_requests_received_address=relocated_runtime.transport_cp3w_ping_requests_received_address,
                cp3w_ping_requests_received_size=4,
                cp3w_pong_responses_submitted_address=relocated_runtime.transport_cp3w_pong_responses_submitted_address,
                cp3w_pong_responses_submitted_size=4,
                cp3w_pong_responses_completed_address=relocated_runtime.transport_cp3w_pong_responses_completed_address,
                cp3w_pong_responses_completed_size=4,
                cp3w_unsupported_commands_received_address=(
                    relocated_runtime.transport_cp3w_unsupported_commands_received_address
                ),
                cp3w_unsupported_commands_received_size=4,
                cp3w_unsupported_responses_submitted_address=(
                    relocated_runtime.transport_cp3w_unsupported_responses_submitted_address
                ),
                cp3w_unsupported_responses_submitted_size=4,
                cp3w_unsupported_responses_completed_address=(
                    relocated_runtime.transport_cp3w_unsupported_responses_completed_address
                ),
                cp3w_unsupported_responses_completed_size=4,
                cp3w_negotiated_flag_address=relocated_runtime.transport_cp3w_negotiated_flag_address,
                cp3w_negotiated_flag_size=4,
                cp3w_selected_protocol_version_address=(
                    relocated_runtime.transport_cp3w_selected_protocol_version_address
                ),
                cp3w_selected_protocol_version_size=4,
                cp3w_client_nonce_address=relocated_runtime.transport_cp3w_client_nonce_address,
                cp3w_client_nonce_size=4,
                cp3w_client_capabilities_address=relocated_runtime.transport_cp3w_client_capabilities_address,
                cp3w_client_capabilities_size=4,
                cp3w_runtime_capabilities_address=relocated_runtime.transport_cp3w_runtime_capabilities_address,
                cp3w_runtime_capabilities_size=4,
                cp3w_accepted_capabilities_address=relocated_runtime.transport_cp3w_accepted_capabilities_address,
                cp3w_accepted_capabilities_size=4,
                cp3w_session_id_address=relocated_runtime.transport_cp3w_session_id_address,
                cp3w_session_id_size=4,
                cp3w_runtime_build_id_address=relocated_runtime.transport_cp3w_runtime_build_id_address,
                cp3w_runtime_build_id_size=4,
                cp3w_last_command_address=relocated_runtime.transport_cp3w_last_command_address,
                cp3w_last_command_size=4,
                cp3w_last_response_status_address=relocated_runtime.transport_cp3w_last_response_status_address,
                cp3w_last_response_status_size=4,
                cp3w_last_ping_payload_length_address=relocated_runtime.transport_cp3w_last_ping_payload_length_address,
                cp3w_last_ping_payload_length_size=4,
                cp3w_last_dispatch_result_address=relocated_runtime.transport_cp3w_last_dispatch_result_address,
                cp3w_last_dispatch_result_size=4,
                receive_arm_count_address=relocated_runtime.transport_receive_arm_count_address,
                receive_arm_count_size=4,
                receive_rearm_count_address=relocated_runtime.transport_receive_rearm_count_address,
                receive_rearm_count_size=4,
                configured_exchange_limit_address=relocated_runtime.transport_configured_exchange_limit_address,
                configured_exchange_limit_size=4,
                completed_exchange_count_address=relocated_runtime.transport_completed_exchange_count_address,
                completed_exchange_count_size=4,
                current_exchange_index_address=relocated_runtime.transport_current_exchange_index_address,
                current_exchange_index_size=4,
                last_completed_exchange_index_address=(
                    relocated_runtime.transport_last_completed_exchange_index_address
                ),
                last_completed_exchange_index_size=4,
                previous_peer_ipv4_address=relocated_runtime.transport_previous_peer_ipv4_address,
                previous_peer_ipv4_size=4,
                previous_peer_port_address=relocated_runtime.transport_previous_peer_port_address,
                previous_peer_port_size=4,
                rearm_submission_failure_count_address=(
                    relocated_runtime.transport_rearm_submission_failure_count_address
                ),
                rearm_submission_failure_count_size=4,
                loop_complete_transition_count_address=(
                    relocated_runtime.transport_loop_complete_transition_count_address
                ),
                loop_complete_transition_count_size=4,
                cleanup_deferred_count_address=relocated_runtime.transport_cleanup_deferred_count_address,
                cleanup_deferred_count_size=4,
                last_receive_length_address=relocated_runtime.transport_last_receive_length_address,
                last_receive_length_size=4,
                last_send_length_address=relocated_runtime.transport_last_send_length_address,
                last_send_length_size=4,
                last_peer_ipv4_address=relocated_runtime.transport_last_peer_ipv4_address,
                last_peer_ipv4_size=4,
                last_peer_port_address=relocated_runtime.transport_last_peer_port_address,
                last_peer_port_size=4,
                last_peer_family_address=relocated_runtime.transport_last_peer_family_address,
                last_peer_family_size=4,
                last_poll_action_address=relocated_runtime.transport_last_poll_action_address,
                last_poll_action_size=4,
                last_submit_result_address=relocated_runtime.transport_last_submit_result_address,
                last_submit_result_size=4,
                polls_while_receive_pending_address=relocated_runtime.transport_polls_while_receive_pending_address,
                polls_while_receive_pending_size=4,
                polls_after_loop_complete_address=relocated_runtime.transport_polls_after_loop_complete_address,
                polls_after_loop_complete_size=4,
                last_receive_preview_address=relocated_runtime.transport_last_receive_preview_address,
                last_receive_preview_size=relocated_runtime.transport_last_receive_preview_size,
                last_send_preview_address=relocated_runtime.transport_last_send_preview_address,
                last_send_preview_size=relocated_runtime.transport_last_send_preview_size,
                open_kd_submit_result_address=relocated_runtime.transport_open_kd_submit_result_address,
                open_kd_submit_result_size=4,
                open_kd_callback_result_address=relocated_runtime.transport_open_kd_callback_result_address,
                open_kd_callback_result_size=4,
                open_kd_submit_generation_address=relocated_runtime.transport_open_kd_submit_generation_address,
                open_kd_submit_generation_size=4,
                open_kd_callback_generation_address=relocated_runtime.transport_open_kd_callback_generation_address,
                open_kd_callback_generation_size=4,
                nwc24_submit_generation_address=relocated_runtime.transport_nwc24_submit_generation_address,
                nwc24_submit_generation_size=4,
                nwc24_callback_generation_address=relocated_runtime.transport_nwc24_callback_generation_address,
                nwc24_callback_generation_size=4,
                open_ip_submit_result_address=relocated_runtime.transport_open_ip_submit_result_address,
                open_ip_submit_result_size=4,
                open_ip_callback_result_address=relocated_runtime.transport_open_ip_callback_result_address,
                open_ip_callback_result_size=4,
                open_ip_submit_generation_address=relocated_runtime.transport_open_ip_submit_generation_address,
                open_ip_submit_generation_size=4,
                open_ip_callback_generation_address=relocated_runtime.transport_open_ip_callback_generation_address,
                open_ip_callback_generation_size=4,
                open_ip_path_pointer_address=relocated_runtime.transport_open_ip_path_pointer_address,
                open_ip_path_pointer_size=4,
                open_ip_path_length_address=relocated_runtime.transport_open_ip_path_length_address,
                open_ip_path_length_size=4,
                open_ip_mode_value_address=relocated_runtime.transport_open_ip_mode_value_address,
                open_ip_mode_value_size=4,
                open_ip_callback_pointer_address=relocated_runtime.transport_open_ip_callback_pointer_address,
                open_ip_callback_pointer_size=4,
                open_ip_context_pointer_address=relocated_runtime.transport_open_ip_context_pointer_address,
                open_ip_context_pointer_size=4,
                open_ip_callback_exit_count_address=relocated_runtime.transport_open_ip_callback_exit_count_address,
                open_ip_callback_exit_count_size=4,
                open_ip_stale_callback_count_address=relocated_runtime.transport_open_ip_stale_callback_count_address,
                open_ip_stale_callback_count_size=4,
                open_ip_duplicate_callback_count_address=(
                    relocated_runtime.transport_open_ip_duplicate_callback_count_address
                ),
                open_ip_duplicate_callback_count_size=4,
                ip_fd_before_open_ip_address=relocated_runtime.transport_ip_fd_before_open_ip_address,
                ip_fd_before_open_ip_size=4,
                kd_close_submit_result_address=relocated_runtime.transport_kd_close_submit_result_address,
                kd_close_submit_result_size=4,
                kd_close_callback_result_address=relocated_runtime.transport_kd_close_callback_result_address,
                kd_close_callback_result_size=4,
                kd_close_submit_generation_address=relocated_runtime.transport_kd_close_submit_generation_address,
                kd_close_submit_generation_size=4,
                kd_close_callback_generation_address=relocated_runtime.transport_kd_close_callback_generation_address,
                kd_close_callback_generation_size=4,
                kd_close_submitted_fd_address=relocated_runtime.transport_kd_close_submitted_fd_address,
                kd_close_submitted_fd_size=4,
                kd_fd_before_close_address=relocated_runtime.transport_kd_fd_before_close_address,
                kd_fd_before_close_size=4,
                kd_fd_after_close_address=relocated_runtime.transport_kd_fd_after_close_address,
                kd_fd_after_close_size=4,
                startup_submit_result_address=relocated_runtime.transport_startup_submit_result_address,
                startup_submit_result_size=4,
                startup_callback_result_address=relocated_runtime.transport_startup_callback_result_address,
                startup_callback_result_size=4,
                startup_submit_generation_address=relocated_runtime.transport_startup_submit_generation_address,
                startup_submit_generation_size=4,
                startup_callback_generation_address=relocated_runtime.transport_startup_callback_generation_address,
                startup_callback_generation_size=4,
                startup_target_address=relocated_runtime.transport_startup_target_address,
                startup_target_size=4,
                startup_command_address=relocated_runtime.transport_startup_command_address,
                startup_command_size=4,
                startup_submitted_fd_address=relocated_runtime.transport_startup_submitted_fd_address,
                startup_submitted_fd_size=4,
                startup_callback_pointer_address=relocated_runtime.transport_startup_callback_pointer_address,
                startup_callback_pointer_size=4,
                startup_context_pointer_address=relocated_runtime.transport_startup_context_pointer_address,
                startup_context_pointer_size=4,
                startup_callback_exit_count_address=relocated_runtime.transport_startup_callback_exit_count_address,
                startup_callback_exit_count_size=4,
                startup_stale_callback_count_address=relocated_runtime.transport_startup_stale_callback_count_address,
                startup_stale_callback_count_size=4,
                startup_duplicate_callback_count_address=(
                    relocated_runtime.transport_startup_duplicate_callback_count_address
                ),
                startup_duplicate_callback_count_size=4,
                startup_service_started_before_submit_address=(
                    relocated_runtime.transport_startup_service_started_before_submit_address
                ),
                startup_service_started_before_submit_size=4,
                startup_service_started_after_completion_address=(
                    relocated_runtime.transport_startup_service_started_after_completion_address
                ),
                startup_service_started_after_completion_size=4,
                ip_fd_before_startup_address=relocated_runtime.transport_ip_fd_before_startup_address,
                ip_fd_before_startup_size=4,
                ip_fd_after_startup_address=relocated_runtime.transport_ip_fd_after_startup_address,
                ip_fd_after_startup_size=4,
                startup_pending_before_submit_address=(
                    relocated_runtime.transport_startup_pending_before_submit_address
                ),
                startup_pending_before_submit_size=4,
                startup_pending_after_completion_address=(
                    relocated_runtime.transport_startup_pending_after_completion_address
                ),
                startup_pending_after_completion_size=4,
                startup_phase_before_submit_address=relocated_runtime.transport_startup_phase_before_submit_address,
                startup_phase_before_submit_size=4,
                startup_phase_after_completion_address=(
                    relocated_runtime.transport_startup_phase_after_completion_address
                ),
                startup_phase_after_completion_size=4,
                startup_pre_call_args_address=relocated_runtime.transport_startup_pre_call_args_address,
                startup_pre_call_args_size=relocated_runtime.transport_startup_pre_call_args_size,
                get_host_id_submit_result_address=relocated_runtime.transport_get_host_id_submit_result_address,
                get_host_id_submit_result_size=4,
                get_host_id_callback_result_address=relocated_runtime.transport_get_host_id_callback_result_address,
                get_host_id_callback_result_size=4,
                get_host_id_submit_generation_address=relocated_runtime.transport_get_host_id_submit_generation_address,
                get_host_id_submit_generation_size=4,
                get_host_id_callback_generation_address=(
                    relocated_runtime.transport_get_host_id_callback_generation_address
                ),
                get_host_id_callback_generation_size=4,
                get_host_id_target_address=relocated_runtime.transport_get_host_id_target_address,
                get_host_id_target_size=4,
                get_host_id_command_address=relocated_runtime.transport_get_host_id_command_address,
                get_host_id_command_size=4,
                get_host_id_submitted_fd_address=relocated_runtime.transport_get_host_id_submitted_fd_address,
                get_host_id_submitted_fd_size=4,
                get_host_id_callback_pointer_address=relocated_runtime.transport_get_host_id_callback_pointer_address,
                get_host_id_callback_pointer_size=4,
                get_host_id_context_pointer_address=relocated_runtime.transport_get_host_id_context_pointer_address,
                get_host_id_context_pointer_size=4,
                get_host_id_callback_exit_count_address=(
                    relocated_runtime.transport_get_host_id_callback_exit_count_address
                ),
                get_host_id_callback_exit_count_size=4,
                get_host_id_stale_callback_count_address=(
                    relocated_runtime.transport_get_host_id_stale_callback_count_address
                ),
                get_host_id_stale_callback_count_size=4,
                get_host_id_duplicate_callback_count_address=(
                    relocated_runtime.transport_get_host_id_duplicate_callback_count_address
                ),
                get_host_id_duplicate_callback_count_size=4,
                get_host_id_service_started_before_submit_address=(
                    relocated_runtime.transport_get_host_id_service_started_before_submit_address
                ),
                get_host_id_service_started_before_submit_size=4,
                get_host_id_service_started_after_completion_address=(
                    relocated_runtime.transport_get_host_id_service_started_after_completion_address
                ),
                get_host_id_service_started_after_completion_size=4,
                ip_fd_before_get_host_id_address=relocated_runtime.transport_ip_fd_before_get_host_id_address,
                ip_fd_before_get_host_id_size=4,
                ip_fd_after_get_host_id_address=relocated_runtime.transport_ip_fd_after_get_host_id_address,
                ip_fd_after_get_host_id_size=4,
                get_host_id_pending_before_submit_address=(
                    relocated_runtime.transport_get_host_id_pending_before_submit_address
                ),
                get_host_id_pending_before_submit_size=4,
                get_host_id_pending_after_completion_address=(
                    relocated_runtime.transport_get_host_id_pending_after_completion_address
                ),
                get_host_id_pending_after_completion_size=4,
                get_host_id_phase_before_submit_address=(
                    relocated_runtime.transport_get_host_id_phase_before_submit_address
                ),
                get_host_id_phase_before_submit_size=4,
                get_host_id_phase_after_completion_address=(
                    relocated_runtime.transport_get_host_id_phase_after_completion_address
                ),
                get_host_id_phase_after_completion_size=4,
                get_host_id_pre_call_args_address=relocated_runtime.transport_get_host_id_pre_call_args_address,
                get_host_id_pre_call_args_size=relocated_runtime.transport_get_host_id_pre_call_args_size,
                socket_submit_result_address=relocated_runtime.transport_socket_submit_result_address,
                socket_submit_result_size=4,
                socket_callback_result_address=relocated_runtime.transport_socket_callback_result_address,
                socket_callback_result_size=4,
                socket_submit_generation_address=relocated_runtime.transport_socket_submit_generation_address,
                socket_submit_generation_size=4,
                socket_callback_generation_address=relocated_runtime.transport_socket_callback_generation_address,
                socket_callback_generation_size=4,
                socket_target_address=relocated_runtime.transport_socket_target_address,
                socket_target_size=4,
                socket_command_address=relocated_runtime.transport_socket_command_address,
                socket_command_size=4,
                socket_submitted_fd_address=relocated_runtime.transport_socket_submitted_fd_address,
                socket_submitted_fd_size=4,
                socket_callback_pointer_address=relocated_runtime.transport_socket_callback_pointer_address,
                socket_callback_pointer_size=4,
                socket_context_pointer_address=relocated_runtime.transport_socket_context_pointer_address,
                socket_context_pointer_size=4,
                socket_callback_exit_count_address=relocated_runtime.transport_socket_callback_exit_count_address,
                socket_callback_exit_count_size=4,
                socket_stale_callback_count_address=relocated_runtime.transport_socket_stale_callback_count_address,
                socket_stale_callback_count_size=4,
                socket_duplicate_callback_count_address=(
                    relocated_runtime.transport_socket_duplicate_callback_count_address
                ),
                socket_duplicate_callback_count_size=4,
                socket_fd_before_submit_address=relocated_runtime.transport_socket_fd_before_submit_address,
                socket_fd_before_submit_size=4,
                socket_fd_after_completion_address=relocated_runtime.transport_socket_fd_after_completion_address,
                socket_fd_after_completion_size=4,
                socket_request_address_address=relocated_runtime.transport_socket_request_address_address,
                socket_request_address_size=4,
                socket_request_storage_size_address=relocated_runtime.transport_socket_request_storage_size_address,
                socket_request_storage_size_size=4,
                socket_request_logical_size_address=relocated_runtime.transport_socket_request_logical_size_address,
                socket_request_logical_size_size=4,
                socket_request_alignment_address=relocated_runtime.transport_socket_request_alignment_address,
                socket_request_alignment_size=4,
                socket_family_value_address=relocated_runtime.transport_socket_family_value_address,
                socket_family_value_size=4,
                socket_type_value_address=relocated_runtime.transport_socket_type_value_address,
                socket_type_value_size=4,
                socket_protocol_value_address=relocated_runtime.transport_socket_protocol_value_address,
                socket_protocol_value_size=4,
                socket_descriptor_valid_address=relocated_runtime.transport_socket_descriptor_valid_address,
                socket_descriptor_valid_size=4,
                socket_ready_address=relocated_runtime.transport_socket_ready_address,
                socket_ready_size=4,
                socket_request_bytes_address=relocated_runtime.transport_socket_request_bytes_address,
                socket_request_bytes_size=relocated_runtime.transport_socket_request_bytes_size,
                socket_pre_call_args_address=relocated_runtime.transport_socket_pre_call_args_address,
                socket_pre_call_args_size=relocated_runtime.transport_socket_pre_call_args_size,
                bind_submit_result_address=relocated_runtime.transport_bind_submit_result_address,
                bind_submit_result_size=4,
                bind_callback_result_address=relocated_runtime.transport_bind_callback_result_address,
                bind_callback_result_size=4,
                bind_submit_generation_address=relocated_runtime.transport_bind_submit_generation_address,
                bind_submit_generation_size=4,
                bind_callback_generation_address=relocated_runtime.transport_bind_callback_generation_address,
                bind_callback_generation_size=4,
                bind_target_address=relocated_runtime.transport_bind_target_address,
                bind_target_size=4,
                bind_command_address=relocated_runtime.transport_bind_command_address,
                bind_command_size=4,
                bind_submitted_fd_address=relocated_runtime.transport_bind_submitted_fd_address,
                bind_submitted_fd_size=4,
                bind_callback_pointer_address=relocated_runtime.transport_bind_callback_pointer_address,
                bind_callback_pointer_size=4,
                bind_context_pointer_address=relocated_runtime.transport_bind_context_pointer_address,
                bind_context_pointer_size=4,
                bind_callback_exit_count_address=relocated_runtime.transport_bind_callback_exit_count_address,
                bind_callback_exit_count_size=4,
                bind_stale_callback_count_address=relocated_runtime.transport_bind_stale_callback_count_address,
                bind_stale_callback_count_size=4,
                bind_duplicate_callback_count_address=relocated_runtime.transport_bind_duplicate_callback_count_address,
                bind_duplicate_callback_count_size=4,
                bind_request_address_address=relocated_runtime.transport_bind_request_address_address,
                bind_request_address_size=4,
                bind_request_storage_size_address=relocated_runtime.transport_bind_request_storage_size_address,
                bind_request_storage_size_size=4,
                bind_request_logical_size_address=relocated_runtime.transport_bind_request_logical_size_address,
                bind_request_logical_size_size=4,
                bind_request_alignment_address=relocated_runtime.transport_bind_request_alignment_address,
                bind_request_alignment_size=4,
                bind_sockaddr_length_address=relocated_runtime.transport_bind_sockaddr_length_address,
                bind_sockaddr_length_size=4,
                bind_family_value_address=relocated_runtime.transport_bind_family_value_address,
                bind_family_value_size=4,
                bind_port_value_address=relocated_runtime.transport_bind_port_value_address,
                bind_port_value_size=4,
                bind_address_value_address=relocated_runtime.transport_bind_address_value_address,
                bind_address_value_size=4,
                bind_request_bytes_address=relocated_runtime.transport_bind_request_bytes_address,
                bind_request_bytes_size=relocated_runtime.transport_bind_request_bytes_size,
                bind_pre_call_args_address=relocated_runtime.transport_bind_pre_call_args_address,
                bind_pre_call_args_size=relocated_runtime.transport_bind_pre_call_args_size,
                cleanup_close_callback_count_address=relocated_runtime.transport_cleanup_close_callback_count_address,
                cleanup_close_callback_count_size=4,
                cleanup_close_submit_result_address=relocated_runtime.transport_cleanup_close_submit_result_address,
                cleanup_close_submit_result_size=4,
                cleanup_close_callback_result_address=relocated_runtime.transport_cleanup_close_callback_result_address,
                cleanup_close_callback_result_size=4,
                cleanup_close_submit_generation_address=(
                    relocated_runtime.transport_cleanup_close_submit_generation_address
                ),
                cleanup_close_submit_generation_size=4,
                cleanup_close_callback_generation_address=(
                    relocated_runtime.transport_cleanup_close_callback_generation_address
                ),
                cleanup_close_callback_generation_size=4,
                cleanup_close_target_address=relocated_runtime.transport_cleanup_close_target_address,
                cleanup_close_target_size=4,
                cleanup_close_command_address=relocated_runtime.transport_cleanup_close_command_address,
                cleanup_close_command_size=4,
                cleanup_close_submitted_fd_address=relocated_runtime.transport_cleanup_close_submitted_fd_address,
                cleanup_close_submitted_fd_size=4,
                cleanup_close_callback_pointer_address=(
                    relocated_runtime.transport_cleanup_close_callback_pointer_address
                ),
                cleanup_close_callback_pointer_size=4,
                cleanup_close_context_pointer_address=(
                    relocated_runtime.transport_cleanup_close_context_pointer_address
                ),
                cleanup_close_context_pointer_size=4,
                cleanup_close_callback_exit_count_address=(
                    relocated_runtime.transport_cleanup_close_callback_exit_count_address
                ),
                cleanup_close_callback_exit_count_size=4,
                cleanup_close_stale_callback_count_address=(
                    relocated_runtime.transport_cleanup_close_stale_callback_count_address
                ),
                cleanup_close_stale_callback_count_size=4,
                cleanup_close_duplicate_callback_count_address=(
                    relocated_runtime.transport_cleanup_close_duplicate_callback_count_address
                ),
                cleanup_close_duplicate_callback_count_size=4,
                cleanup_close_request_address_address=(
                    relocated_runtime.transport_cleanup_close_request_address_address
                ),
                cleanup_close_request_address_size=4,
                cleanup_close_request_storage_size_address=(
                    relocated_runtime.transport_cleanup_close_request_storage_size_address
                ),
                cleanup_close_request_storage_size_size=4,
                cleanup_close_request_logical_size_address=(
                    relocated_runtime.transport_cleanup_close_request_logical_size_address
                ),
                cleanup_close_request_logical_size_size=4,
                cleanup_close_request_alignment_address=(
                    relocated_runtime.transport_cleanup_close_request_alignment_address
                ),
                cleanup_close_request_alignment_size=4,
                cleanup_close_request_value_address=relocated_runtime.transport_cleanup_close_request_value_address,
                cleanup_close_request_value_size=4,
                cleanup_close_request_bytes_address=relocated_runtime.transport_cleanup_close_request_bytes_address,
                cleanup_close_request_bytes_size=relocated_runtime.transport_cleanup_close_request_bytes_size,
                cleanup_close_pre_call_args_address=relocated_runtime.transport_cleanup_close_pre_call_args_address,
                cleanup_close_pre_call_args_size=relocated_runtime.transport_cleanup_close_pre_call_args_size,
                bound_flag_address=relocated_runtime.transport_bound_flag_address,
                bound_flag_size=4,
                bound_address_address=relocated_runtime.transport_bound_address_address,
                bound_address_size=4,
                socket_closed_after_bind_failure_address=(
                    relocated_runtime.transport_socket_closed_after_bind_failure_address
                ),
                socket_closed_after_bind_failure_size=4,
                socket_leak_detected_address=relocated_runtime.transport_socket_leak_detected_address,
                socket_leak_detected_size=4,
                cp3w_game_identity=(
                    Prime3RuntimeGameIdentityMetadata(
                        mode_value=20,
                        mode_name="cp3w_game_identity",
                        command_value=int(Prime3WiiCommand.GET_GAME_IDENTITY),
                        capability_value=int(Prime3WiiCapability.GAME_IDENTITY),
                        schema_version=GAME_IDENTITY_SCHEMA_VERSION,
                        payload_size=GAME_IDENTITY_PAYLOAD_SIZE,
                        field_offsets=GAME_IDENTITY_FIELD_OFFSETS,
                        game_id=int(Prime3WiiGameId.METROID_PRIME_3_CORRUPTION),
                        platform_id=int(Prime3WiiPlatformId.WII),
                        region_id=int(Prime3WiiRegionId.NTSC_U),
                        revision_id=int(Prime3WiiRevisionId.WII_NTSC_3_436),
                        profile_id=PRIME3_NTSC_RETAIL_PROFILE_ID,
                        profile_fingerprint=PRIME3_NTSC_RETAIL_PROFILE_FINGERPRINT,
                        fingerprint_derivation=(
                            "CRC32 over >BBBHIIIII: game, platform, region, revision, profile ID, "
                            "game-state root, CStateManager root, CPlayer vtable, DOL SHA-256 prefix"
                        ),
                        runtime_build_id=DEFAULT_RUNTIME_BUILD_ID,
                        availability_flags={
                            item.name: int(item) for item in Prime3WiiAvailability if item.name is not None
                        },
                        phase_names={
                            "VALIDATE_REQUEST": 70,
                            "VALIDATE_CAPABILITY": 71,
                            "VALIDATE_EXECUTABLE": 72,
                            "RESOLVE_GAME_STATE": 73,
                            "RESOLVE_PLAYER_STATE": 74,
                            "BUILD_RESPONSE": 75,
                            "SUBMIT_RESPONSE": 76,
                            "RESPONSE_COMPLETE": 77,
                            "HANDLE_ERROR": 78,
                            "LOOP_COMPLETE": 79,
                        },
                        configured_count=ios_udp_loop_count,
                        state_addresses=relocated_runtime.transport_cp3w_game_identity_state_addresses,
                    )
                    if cp3w_game_identity or cp3w_inventory
                    else None
                ),
                cp3w_inventory=(
                    Prime3RuntimeInventoryMetadata(
                        mode_value=22 if cp3w_inventory_service else 21,
                        mode_name=ios_udp_mode,
                        command_value=int(Prime3WiiCommand.GET_INVENTORY),
                        capability_value=int(Prime3WiiCapability.INVENTORY_STATE),
                        schema_version=INVENTORY_SCHEMA_VERSION,
                        item_ids=list(INVENTORY_ITEM_IDS),
                        header_size=INVENTORY_FIELD_OFFSETS["records"],
                        record_size=INVENTORY_RECORD_SIZE,
                        payload_size=INVENTORY_PAYLOAD_SIZE,
                        frame_size=INVENTORY_FRAME_SIZE,
                        field_offsets=INVENTORY_FIELD_OFFSETS,
                        availability_flags={
                            item.name: int(item) for item in Prime3WiiInventoryAvailability if item.name is not None
                        },
                        phase_names={
                            "VALIDATE_REQUEST": 80,
                            "VALIDATE_CAPABILITY": 81,
                            "VALIDATE_IDENTITY": 82,
                            "RESOLVE_GAME_STATE": 83,
                            "RESOLVE_ROOT": 84,
                            "VALIDATE_RANGE": 85,
                            "READ_RECORDS": 86,
                            "REVALIDATE_ROOT": 87,
                            "BUILD_RESPONSE": 88,
                            "SUBMIT_RESPONSE": 89,
                            "RESPONSE_COMPLETE": 90,
                            "HANDLE_UNAVAILABLE": 91,
                            "HANDLE_ERROR": 92,
                            "LOOP_COMPLETE": 93,
                        },
                        configured_count=ios_udp_loop_count,
                        send_buffer_size=512,
                        ping_payload_limit=44,
                        state_addresses=relocated_runtime.transport_cp3w_inventory_state_addresses,
                    )
                    if cp3w_inventory
                    else None
                ),
            )
        cp3c_config_offset = relocated_runtime.cp3c_config_start_address - runtime_destination
        cp3c_config_size = relocated_runtime.cp3c_config_end_address - relocated_runtime.cp3c_config_start_address
        server_ipv4_offset = relocated_runtime.cp3c_server_ipv4_address - runtime_destination
        server_port_offset = relocated_runtime.cp3c_server_port_address - runtime_destination
        transport_metadata = Prime3RuntimeTransportMetadata(
            transport_kind="tcp",
            protocol_magic_hex=PROTOCOL_MAGIC.hex(),
            protocol_version=PROTOCOL_VERSION,
            frame_size=64,
            diagnostics_enabled=False,
            inbound_queue_depth=4,
            outbound_queue_depth=4,
            cp3c_config_offset=cp3c_config_offset,
            cp3c_config_size=cp3c_config_size,
            server_ipv4_offset=server_ipv4_offset,
            server_ipv4_size=4,
            server_ipv4_byte_order="big",
            server_port_offset=server_port_offset,
            server_port_size=2,
            server_port_byte_order="big",
            inventory_tracker_capability=True,
            tracker_snapshot_capability=True,
            tracker_delta_capability=True,
            resync_capability=True,
            kd_startup_capability=enable_ios_network_lifecycle,
            ip_startup_capability=enable_ios_network_lifecycle,
            tcp_connect_capability=enable_tcp_tracker,
            tcp_send_capability=enable_tcp_tracker,
            tcp_receive_capability=enable_tcp_tracker,
            wait_connect_tcp_capability=enable_tcp_tracker and enable_ios_network_lifecycle,
        )
        transport_metadata.validate(runtime_blob_size=len(embedded_runtime_bytes))

        relocated_runtime_metadata = Prime3RelocatedRuntimeMetadata(
            mode=payload_mode,
            low_bootstrap_address=BOOTSTRAP_STAGING_ADDRESS,
            low_bootstrap_size=len(low_bootstrap_bytes),
            low_bootstrap_sha256=hashlib.sha256(low_bootstrap_bytes).hexdigest(),
            embedded_runtime_blob_offset=embedded_runtime_start_offset,
            embedded_runtime_blob_size=len(embedded_runtime_bytes),
            embedded_runtime_blob_sha256=relocated_runtime.payload_sha256,
            runtime_destination_address=runtime_destination,
            runtime_entry_address=relocated_runtime.entry_address,
            runtime_poll_entry_address=relocated_runtime.poll_entry_address,
            runtime_poll_hook_wrapper_address=relocated_runtime.poll_hook_wrapper_address,
            runtime_code_start=relocated_runtime.code_start,
            runtime_code_end=relocated_runtime.code_end,
            runtime_state_start=relocated_runtime.state_start,
            runtime_state_end=relocated_runtime.state_end,
            runtime_stack_start=None,
            runtime_stack_end=None,
            required_source_alignment=PRIME3_RUNTIME_REQUIRED_ALIGNMENT,
            required_destination_alignment=PRIME3_RUNTIME_REQUIRED_ALIGNMENT,
            cache_line_size=RELOCATED_RUNTIME_CACHE_LINE_SIZE,
            cache_range_start=relocated_runtime.cache_range_start,
            cache_range_size=relocated_runtime.cache_range_size,
            runtime_canary_address=relocated_runtime.canary_address,
            runtime_canary_size=relocated_runtime.canary_size,
            runtime_canary_sha256=relocated_runtime.canary_sha256,
            copy_complete_marker_address=relocated_runtime.copy_complete_marker_address,
            copy_complete_marker_value=RELOCATED_COPY_COMPLETE_MARKER_VALUE,
            runtime_executed_marker_address=relocated_runtime.runtime_executed_marker_address,
            runtime_executed_marker_value=RELOCATED_EXECUTED_MARKER_VALUE,
            runtime_execution_counter_address=relocated_runtime.runtime_execution_counter_address,
            runtime_execution_counter_size=4,
            runtime_status_address=relocated_runtime.runtime_status_address,
            runtime_success_status_value=RELOCATED_SUCCESS_STATUS_VALUE,
            bootstrap_return_marker_address=relocated_runtime.bootstrap_return_marker_address,
            bootstrap_return_marker_value=RELOCATED_BOOTSTRAP_RETURN_MARKER_VALUE,
            runtime_poll_counter_address=relocated_runtime.poll_counter_address,
            runtime_poll_counter_size=4,
            runtime_poll_heartbeat_address=relocated_runtime.poll_heartbeat_address,
            runtime_poll_heartbeat_size=4,
            runtime_poll_last_sequence_address=relocated_runtime.poll_last_sequence_address,
            runtime_poll_last_sequence_size=4,
            diagnostics=diagnostic_metadata,
            ios_udp_diagnostic_enabled=enable_ios_udp_diagnostic,
            transport=transport_metadata,
            abi_probe=abi_probe_metadata,
            retail_ios_wrapper=_prime3_ntsc_retail_ios_wrapper_metadata() if enable_ios_udp_diagnostic else None,
        )

    beacon_ipv4_patch = None
    if ios_udp_mode == "native_wc24_bootstrap_beacon_once":
        assert relocated_runtime is not None
        assert relocated_runtime.native_beacon_ipv4_address is not None
        assert runtime_destination is not None
        assert embedded_runtime_start_offset is not None
        beacon_ipv4_offset = (
            embedded_runtime_start_offset + relocated_runtime.native_beacon_ipv4_address - runtime_destination
        )
        expected_beacon_bytes = native_beacon_ipv4.to_bytes(4, "big")
        if payload_bytes[beacon_ipv4_offset : beacon_ipv4_offset + 4] != expected_beacon_bytes:
            raise RuntimeError("Linked native beacon IPv4 field does not contain the configured original bytes.")
        beacon_ipv4_patch = Prime3RuntimePayloadPatchField(
            payload_offset=beacon_ipv4_offset,
            expected_original_bytes=expected_beacon_bytes.hex(),
            field_size=4,
            byte_order="big",
        )

    manifest = Prime3RuntimePayloadManifest(
        schema_version=PRIME3_RUNTIME_PAYLOAD_SCHEMA_VERSION,
        target_architecture=PRIME3_RUNTIME_TARGET_ARCHITECTURE,
        target_endianness=PRIME3_RUNTIME_TARGET_ENDIANNESS,
        target_abi=PRIME3_RUNTIME_TARGET_ABI,
        compiler_identity=f"powerpc-eabi-gcc (devkitPPC release {toolchain.devkitppc_release})",
        compiler_version=toolchain.compiler_version,
        linker_identity="GNU ld",
        linker_version=toolchain.binutils_version,
        payload_sha256=payload_sha256,
        payload_size=len(payload_bytes),
        required_alignment=PRIME3_RUNTIME_REQUIRED_ALIGNMENT,
        entry_symbol_name=PRIME3_RUNTIME_ENTRY_SYMBOL,
        entry_symbol_offset=entry_offset,
        source_digest=compute_source_digest(SCRIPT_ROOT, SOURCE_FILES),
        protocol_artifact_version=PROTOCOL_VERSION,
        unresolved_relocation_count=unresolved_relocation_count,
        dynamic_section_count=dynamic_section_count,
        payload_mode=payload_mode,
        canary_start_offset=canary_start_offset,
        canary_size=canary_size,
        counter_offset=counter_offset,
        counter_size=4 if counter_offset is not None else None,
        entry_bootstrap=entry_bootstrap,
        relocated_runtime=relocated_runtime_metadata,
        beacon_ipv4_patch=beacon_ipv4_patch,
    )
    manifest.validate()
    manifest_path.write_text(manifest.to_json_text(), encoding="utf-8")
    return manifest


def _build_relocated_runtime(
    *,
    toolchain: Any,
    output_dir: Path,
    runtime_destination: int,
    enable_recurring_hook_diagnostics: bool,
    enable_ios_udp_diagnostic: bool,
    enable_tcp_tracker: bool,
    enable_ios_network_lifecycle: bool,
    ios_udp_mode: str,
    ios_udp_loop_count: int,
    production_guard_bypass: str,
    production_lifecycle_trace: bool,
    production_skyward_parity_owned_ip_top: bool,
    production_preserve_ping_layout: bool | None,
    production_size_optimize: bool,
    production_force_isolated_layout: bool,
    production_skyward_socket_bind_graft: bool,
    production_owned_ip_top_no_restart: bool,
    early_sda_capture: bool,
    native_beacon_ipv4: int,
) -> RelocatedRuntimeBuildResult:
    output_dir.mkdir(parents=True, exist_ok=True)
    asm_object_path = output_dir.joinpath("relocated_runtime_asm.o")
    c_object_path = output_dir.joinpath("relocated_runtime_c.o")
    elf_path = output_dir.joinpath("relocated_runtime.elf")
    binary_path = output_dir.joinpath("runtime_blob.bin")
    map_path = output_dir.joinpath("relocated_runtime.map")
    production_guard_bypass_value = {"none": 0, "socket": 1, "socket_bind": 2}[production_guard_bypass]
    preserve_ping_layout = (
        ios_udp_mode == "cp3w_inventory_service" and not production_skyward_parity_owned_ip_top
        if production_preserve_ping_layout is None
        else production_preserve_ping_layout
    )
    common_compiler_defines = [
        f"-DPRIME3_RUNTIME_EXECUTED_MARKER_VALUE=0x{RELOCATED_EXECUTED_MARKER_VALUE:08X}",
        f"-DPRIME3_CP3W_GAME_IDENTITY_COMMAND={int(Prime3WiiCommand.GET_GAME_IDENTITY)}",
        f"-DPRIME3_CP3W_GAME_IDENTITY_CAPABILITY={int(Prime3WiiCapability.GAME_IDENTITY)}",
        f"-DPRIME3_CP3W_GAME_IDENTITY_SCHEMA_VERSION={GAME_IDENTITY_SCHEMA_VERSION}",
        f"-DPRIME3_CP3W_INVENTORY_COMMAND={int(Prime3WiiCommand.GET_INVENTORY)}",
        f"-DPRIME3_CP3W_INVENTORY_CAPABILITY={int(Prime3WiiCapability.INVENTORY_STATE)}",
        f"-DPRIME3_CP3W_INVENTORY_SCHEMA_VERSION={INVENTORY_SCHEMA_VERSION}",
        f"-DPRIME3_CP3W_INVENTORY_RECORD_COUNT={INVENTORY_RECORD_COUNT}",
        f"-DPRIME3_CP3W_INVENTORY_RECORD_SIZE={INVENTORY_RECORD_SIZE}",
        f"-DPRIME3_CP3W_INVENTORY_PAYLOAD_SIZE={INVENTORY_PAYLOAD_SIZE}",
        f"-DPRIME3_CP3W_GAME_IDENTITY_PROFILE_ID=0x{PRIME3_NTSC_RETAIL_PROFILE_ID:08X}",
        f"-DPRIME3_CP3W_GAME_IDENTITY_PROFILE_FINGERPRINT=0x{PRIME3_NTSC_RETAIL_PROFILE_FINGERPRINT:08X}",
        f"-DPRIME3_CP3W_RUNTIME_BUILD_ID=0x{DEFAULT_RUNTIME_BUILD_ID:08X}",
        f"-DPRIME3_RUNTIME_SUCCESS_STATUS_VALUE=0x{RELOCATED_SUCCESS_STATUS_VALUE:08X}",
        f"-DPRIME3_RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS=0x{RUNTIME_POLL_HOOK_CONTINUATION_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_IOS_OPEN_ASYNC_ADDRESS=0x{PRIME3_NTSC_IOS_OPEN_ASYNC_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_IOS_CLOSE_ASYNC_ADDRESS=0x{PRIME3_NTSC_IOS_CLOSE_ASYNC_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_IOS_READ_ASYNC_ADDRESS=0x{PRIME3_NTSC_IOS_READ_ASYNC_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_IOS_WRITE_ASYNC_ADDRESS=0x{PRIME3_NTSC_IOS_WRITE_ASYNC_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_IOS_IOCTL_ASYNC_ADDRESS=0x{PRIME3_NTSC_CONFIRMED_IOS_IOCTL_ASYNC_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_IOS_IOCTLV_ASYNC_ADDRESS=0x{PRIME3_NTSC_CONFIRMED_IOS_IOCTLV_ASYNC_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_NWC24_OPEN_LIB_ADDRESS=0x{PRIME3_NTSC_NWC24_OPEN_LIB_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_NETWORK_BOOTSTRAP_ADDRESS=0x{PRIME3_NTSC_NETWORK_BOOTSTRAP_ADDRESS:08X}",
        f"-DPRIME3_RETAIL_SO_FD_SDA_OFFSET={PRIME3_NTSC_SO_FD_SDA_OFFSET}",
        f"-DPRIME3_NATIVE_BEACON_IPV4=0x{native_beacon_ipv4:08X}",
        f"-DPRIME3_NATIVE_BEACON_PORT={DEFAULT_NATIVE_BEACON_PORT}",
        f"-DPRIME3_ENABLE_RECURRING_HOOK_DIAGNOSTICS={1 if enable_recurring_hook_diagnostics else 0}",
        f"-DPRIME3_ENABLE_IOS_UDP_DIAGNOSTIC={1 if enable_ios_udp_diagnostic else 0}",
        f"-DPRIME3_ENABLE_TCP_TRACKER={1 if enable_tcp_tracker else 0}",
        f"-DPRIME3_ENABLE_IOS_NETWORK_LIFECYCLE={1 if enable_ios_network_lifecycle else 0}",
        f"-DPRIME3_PRODUCTION_GUARD_BYPASS={production_guard_bypass_value}",
        f"-DPRIME3_PRODUCTION_LIFECYCLE_TRACE={1 if production_lifecycle_trace else 0}",
        (f"-DPRIME3_PRODUCTION_SKYWARD_PARITY_OWNED_IP_TOP={1 if production_skyward_parity_owned_ip_top else 0}"),
        f"-DPRIME3_PRODUCTION_SKYWARD_SOCKET_BIND_GRAFT={1 if production_skyward_socket_bind_graft else 0}",
        f"-DPRIME3_PRODUCTION_OWNED_IP_TOP_NO_RESTART={1 if production_owned_ip_top_no_restart else 0}",
        f"-DPRIME3_EARLY_SDA_CAPTURE={1 if early_sda_capture else 0}",
        (
            "-DPRIME3_IOS_UDP_DIAGNOSTIC_MODE="
            + {
                "normal": "0",
                "dry_run": "1",
                "retail_wrapper_open_kd_once": "2",
                "retail_wrapper_nwc24_startup_once": "3",
                "retail_wrapper_nwc24_close_kd_once": "11",
                "retail_wrapper_nwc24_close_open_ip_once": "12",
                "retail_wrapper_nwc24_close_open_ip_startup_once": "13",
                "retail_wrapper_close_kd_once": "4",
                "retail_wrapper_open_ip_once": "5",
                "retail_wrapper_startup_once": "6",
                "retail_wrapper_get_host_id_once": "7",
                "retail_wrapper_create_socket_once": "8",
                "retail_wrapper_bind_once": "9",
                "retail_wrapper_ioctl_async_abi_probe": "10",
                "retail_wrapper_recvfrom_once": "14",
                "retail_wrapper_recv_send_once": "15",
                "retail_wrapper_recv_send_loop": "16",
                "cp3w_frame_validation": "17",
                "cp3w_ping_pong": "18",
                "cp3w_hello_session": "19",
                "cp3w_game_identity": "20",
                "cp3w_inventory": "21",
                "cp3w_inventory_service": "22",
                "native_wc24_bootstrap_beacon_once": "23",
            }[ios_udp_mode]
        ),
        f"-DPRIME3_IOS_UDP_DIAGNOSTIC_LOOP_COUNT={ios_udp_loop_count}",
    ]
    _run(
        [
            os.fspath(toolchain.compiler_path),
            *toolchain.required_machine_flags,
            *common_compiler_defines,
            "-x",
            "assembler-with-cpp",
            "-c",
            os.fspath(SCRIPT_ROOT.parent.joinpath("prime3_tcp_runtime_clean", "runtime.S")),
            "-o",
            os.fspath(asm_object_path),
        ]
    )
    _run(
        [
            os.fspath(toolchain.compiler_path),
            *toolchain.required_machine_flags,
            *common_compiler_defines,
            "-Os" if production_size_optimize else "-O2",
            "-ffreestanding",
            "-fno-builtin",
            "-fno-common",
            "-fno-exceptions",
            "-fno-unwind-tables",
            "-fno-asynchronous-unwind-tables",
            "-fno-stack-protector",
            "-ffunction-sections",
            "-fdata-sections",
            "-fno-pic",
            "-msdata=none",
            "-c",
            os.fspath(SCRIPT_ROOT.parent.joinpath("prime3_tcp_runtime_clean", "runtime.c")),
            "-o",
            os.fspath(c_object_path),
        ]
    )
    _run(
        [
            os.fspath(toolchain.linker_path),
            "-EB",
            "--build-id=none",
            "--gc-sections",
            f"--defsym=__runtime_link_address=0x{runtime_destination:08X}",
            (f"--defsym=__runtime_preserve_ping_layout={int(preserve_ping_layout)}"),
            f"--defsym=__runtime_force_isolated_layout={int(production_force_isolated_layout)}",
            "-T",
            os.fspath(SCRIPT_ROOT.parent.joinpath("prime3_tcp_runtime_clean", "runtime.ld")),
            "-Map",
            os.fspath(map_path),
            "-o",
            os.fspath(elf_path),
            os.fspath(asm_object_path),
            os.fspath(c_object_path),
        ]
    )
    _run(
        [
            os.fspath(toolchain.objcopy_path),
            "-O",
            "binary",
            os.fspath(elf_path),
            os.fspath(binary_path),
        ]
    )
    payload_bytes = binary_path.read_bytes()
    payload_sha256 = hashlib.sha256(payload_bytes).hexdigest()
    readelf_header = _run([os.fspath(toolchain.readelf_path), "-h", os.fspath(elf_path)])
    readelf_symbols = _run([os.fspath(toolchain.readelf_path), "-s", "--wide", os.fspath(elf_path)])
    readelf_relocations = _run([os.fspath(toolchain.readelf_path), "-r", os.fspath(elf_path)])
    readelf_dynamic = _run([os.fspath(toolchain.readelf_path), "-d", os.fspath(elf_path)], allow_failure=True)
    objdump_disassembly = _run([os.fspath(toolchain.objdump_path), "-d", os.fspath(elf_path)])
    _validate_readelf_header(readelf_header)
    if _count_relocations(readelf_relocations) != 0:
        raise RuntimeError("Relocated runtime ELF has unresolved relocations.")
    if _count_dynamic_sections(readelf_dynamic) != 0:
        raise RuntimeError("Relocated runtime ELF has dynamic sections.")
    _validate_forbidden_renderer_references(readelf_symbols, readelf_relocations)
    _validate_retail_call_veneer_disassembly(
        objdump_output=objdump_disassembly,
        symbol_output=readelf_symbols,
        wrapper_metadata=_prime3_ntsc_retail_ios_wrapper_metadata(),
    )

    entry_address = _extract_symbol_address(readelf_symbols, RUNTIME_ENTRY_SYMBOL)
    poll_entry_address = _extract_symbol_address(readelf_symbols, RUNTIME_POLL_ENTRY_SYMBOL)
    poll_hook_wrapper_address = _extract_symbol_address(readelf_symbols, RUNTIME_POLL_HOOK_WRAPPER_SYMBOL)
    code_start = _extract_symbol_address(readelf_symbols, RUNTIME_CODE_START_SYMBOL)
    code_end = _extract_symbol_address(readelf_symbols, RUNTIME_CODE_END_SYMBOL)
    state_start = _extract_symbol_address(readelf_symbols, RUNTIME_STATE_START_SYMBOL)
    state_end = _extract_symbol_address(readelf_symbols, RUNTIME_STATE_END_SYMBOL)
    network_diagnostics_address = _extract_symbol_address(readelf_symbols, RUNTIME_NETWORK_DIAGNOSTICS_SYMBOL)
    canary_start = _extract_symbol_address(readelf_symbols, RUNTIME_CANARY_START_SYMBOL)
    canary_end = _extract_symbol_address(readelf_symbols, RUNTIME_CANARY_END_SYMBOL)
    copy_complete_marker_address = _extract_symbol_address(readelf_symbols, RUNTIME_COPY_COMPLETE_MARKER_SYMBOL)
    runtime_executed_marker_address = _extract_symbol_address(readelf_symbols, RUNTIME_EXECUTED_MARKER_SYMBOL)
    runtime_execution_counter_address = _extract_symbol_address(readelf_symbols, RUNTIME_EXECUTION_COUNTER_SYMBOL)
    runtime_status_address = _extract_symbol_address(readelf_symbols, RUNTIME_STATUS_SYMBOL)
    bootstrap_return_marker_address = _extract_symbol_address(readelf_symbols, RUNTIME_BOOTSTRAP_RETURN_MARKER_SYMBOL)
    poll_counter_address = _extract_symbol_address(readelf_symbols, RUNTIME_POLL_COUNTER_SYMBOL)
    poll_heartbeat_address = _extract_symbol_address(readelf_symbols, RUNTIME_POLL_HEARTBEAT_SYMBOL)
    poll_last_sequence_address = _extract_symbol_address(readelf_symbols, RUNTIME_POLL_LAST_SEQUENCE_SYMBOL)
    diagnostic_hook_wrapper_entry_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_ENTRY_COUNT_SYMBOL
    )
    diagnostic_hook_wrapper_before_poll_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_BEFORE_POLL_COUNT_SYMBOL
    )
    diagnostic_poll_entry_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_POLL_ENTRY_COUNT_SYMBOL
    )
    diagnostic_poll_exit_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_POLL_EXIT_COUNT_SYMBOL
    )
    diagnostic_state_machine_entry_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_STATE_MACHINE_ENTRY_COUNT_SYMBOL
    )
    diagnostic_state_machine_exit_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_STATE_MACHINE_EXIT_COUNT_SYMBOL
    )
    diagnostic_c_before_veneer_call_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_C_BEFORE_VENEER_CALL_COUNT_SYMBOL
    )
    diagnostic_retail_veneer_entry_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_RETAIL_VENEER_ENTRY_COUNT_SYMBOL
    )
    diagnostic_retail_target_return_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_RETAIL_TARGET_RETURN_COUNT_SYMBOL
    )
    diagnostic_retail_veneer_exit_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_RETAIL_VENEER_EXIT_COUNT_SYMBOL
    )
    diagnostic_c_after_veneer_call_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_C_AFTER_VENEER_CALL_COUNT_SYMBOL
    )
    diagnostic_ios_submit_attempt_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_IOS_SUBMIT_ATTEMPT_COUNT_SYMBOL
    )
    diagnostic_ios_submit_return_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_IOS_SUBMIT_RETURN_COUNT_SYMBOL
    )
    diagnostic_ios_submit_return_value_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_IOS_SUBMIT_RETURN_VALUE_SYMBOL
    )
    diagnostic_callback_entry_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_CALLBACK_ENTRY_COUNT_SYMBOL
    )
    diagnostic_callback_exit_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_CALLBACK_EXIT_COUNT_SYMBOL
    )
    diagnostic_hook_wrapper_after_poll_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_AFTER_POLL_COUNT_SYMBOL
    )
    diagnostic_hook_wrapper_exit_count_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_HOOK_WRAPPER_EXIT_COUNT_SYMBOL
    )
    diagnostic_last_execution_marker_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_LAST_EXECUTION_MARKER_SYMBOL
    )
    diagnostic_last_phase_before_step_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_LAST_PHASE_BEFORE_STEP_SYMBOL
    )
    diagnostic_last_phase_after_step_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_LAST_PHASE_AFTER_STEP_SYMBOL
    )
    diagnostic_callback_result_address = _extract_optional_symbol_address(
        readelf_symbols, RUNTIME_DIAGNOSTIC_CALLBACK_RESULT_SYMBOL
    )
    verified_game_r2_address = _extract_symbol_address(readelf_symbols, RUNTIME_VERIFIED_GAME_R2_SYMBOL)
    verified_game_r13_address = _extract_symbol_address(readelf_symbols, RUNTIME_VERIFIED_GAME_R13_SYMBOL)
    abi_probe_supplied_args_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_SUPPLIED_ARGS_SYMBOL)
    abi_probe_supplied_args_size = _extract_symbol_size(readelf_symbols, RUNTIME_ABI_PROBE_SUPPLIED_ARGS_SYMBOL)
    abi_probe_pre_call_args_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_PRE_CALL_ARGS_SYMBOL)
    abi_probe_pre_call_args_size = _extract_symbol_size(readelf_symbols, RUNTIME_ABI_PROBE_PRE_CALL_ARGS_SYMBOL)
    abi_probe_target_args_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_TARGET_ARGS_SYMBOL)
    abi_probe_target_args_size = _extract_symbol_size(readelf_symbols, RUNTIME_ABI_PROBE_TARGET_ARGS_SYMBOL)
    abi_probe_return_value_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_RETURN_VALUE_SYMBOL)
    abi_probe_result_flags_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_RESULT_FLAGS_SYMBOL)
    abi_probe_stack_pointer_before_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_ABI_PROBE_STACK_POINTER_BEFORE_SYMBOL
    )
    abi_probe_stack_pointer_after_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_ABI_PROBE_STACK_POINTER_AFTER_SYMBOL
    )
    abi_probe_saved_lr_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_SAVED_LR_SYMBOL)
    abi_probe_restored_lr_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_RESTORED_LR_SYMBOL)
    abi_probe_saved_r2_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_SAVED_R2_SYMBOL)
    abi_probe_restored_r2_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_RESTORED_R2_SYMBOL)
    abi_probe_saved_r13_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_SAVED_R13_SYMBOL)
    abi_probe_restored_r13_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_RESTORED_R13_SYMBOL)
    abi_probe_target_ctr_address = _extract_symbol_address(readelf_symbols, RUNTIME_ABI_PROBE_TARGET_CTR_SYMBOL)
    abi_probe_after_call_flag_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_ABI_PROBE_AFTER_CALL_FLAG_SYMBOL
    )
    abi_probe_expected_return_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_ABI_PROBE_EXPECTED_RETURN_VALUE_SYMBOL
    )
    transport_phase_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_PHASE_SYMBOL)
    native_beacon_ipv4_address = (
        _extract_symbol_address(readelf_symbols, RUNTIME_NATIVE_BEACON_IPV4_SYMBOL)
        if ios_udp_mode == "native_wc24_bootstrap_beacon_once"
        else None
    )
    transport_last_error_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_LAST_ERROR_SYMBOL)
    transport_last_socket_error_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_SOCKET_ERROR_SYMBOL
    )
    transport_last_ios_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_IOS_RESULT_SYMBOL
    )
    transport_pending_operation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_PENDING_OPERATION_SYMBOL
    )
    transport_pending_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_PENDING_GENERATION_SYMBOL
    )
    transport_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CALLBACK_GENERATION_SYMBOL
    )
    transport_callback_count_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_CALLBACK_COUNT_SYMBOL)
    transport_rejected_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_REJECTED_CALLBACK_COUNT_SYMBOL
    )
    transport_callback_pending_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CALLBACK_PENDING_SYMBOL
    )
    transport_open_kd_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_KD_SUBMIT_COUNT_SYMBOL
    )
    transport_open_kd_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_KD_CALLBACK_COUNT_SYMBOL
    )
    transport_open_kd_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_KD_SUBMIT_RESULT_SYMBOL
    )
    transport_open_kd_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_KD_CALLBACK_RESULT_SYMBOL
    )
    transport_open_kd_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_KD_SUBMIT_GENERATION_SYMBOL
    )
    transport_open_kd_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_KD_CALLBACK_GENERATION_SYMBOL
    )
    transport_nwc24_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_SUBMIT_COUNT_SYMBOL
    )
    transport_nwc24_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_CALLBACK_COUNT_SYMBOL
    )
    transport_nwc24_synchronous_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_SYNCHRONOUS_RESULT_SYMBOL
    )
    transport_nwc24_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_CALLBACK_RESULT_SYMBOL
    )
    transport_nwc24_output_buffer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_OUTPUT_BUFFER_SYMBOL
    )
    transport_nwc24_output_digest_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_OUTPUT_DIGEST_SYMBOL
    )
    transport_nwc24_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_SUBMIT_GENERATION_SYMBOL
    )
    transport_nwc24_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_NWC24_CALLBACK_GENERATION_SYMBOL
    )
    transport_open_ip_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_SUBMIT_COUNT_SYMBOL
    )
    transport_open_ip_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_COUNT_SYMBOL
    )
    transport_open_ip_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_SUBMIT_RESULT_SYMBOL
    )
    transport_open_ip_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_RESULT_SYMBOL
    )
    transport_open_ip_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_SUBMIT_GENERATION_SYMBOL
    )
    transport_open_ip_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_GENERATION_SYMBOL
    )
    transport_open_ip_path_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_PATH_POINTER_SYMBOL
    )
    transport_open_ip_path_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_PATH_LENGTH_SYMBOL
    )
    transport_open_ip_mode_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_MODE_VALUE_SYMBOL
    )
    transport_open_ip_callback_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_POINTER_SYMBOL
    )
    transport_open_ip_context_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_CONTEXT_POINTER_SYMBOL
    )
    transport_open_ip_callback_exit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_CALLBACK_EXIT_COUNT_SYMBOL
    )
    transport_open_ip_stale_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_STALE_CALLBACK_COUNT_SYMBOL
    )
    transport_open_ip_duplicate_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_OPEN_IP_DUPLICATE_CALLBACK_COUNT_SYMBOL
    )
    transport_ip_fd_before_open_ip_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_IP_FD_BEFORE_OPEN_IP_SYMBOL
    )
    transport_kd_close_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_SUBMIT_COUNT_SYMBOL
    )
    transport_kd_close_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_CALLBACK_COUNT_SYMBOL
    )
    transport_kd_close_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_SUBMIT_RESULT_SYMBOL
    )
    transport_kd_close_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_CALLBACK_RESULT_SYMBOL
    )
    transport_kd_close_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_SUBMIT_GENERATION_SYMBOL
    )
    transport_kd_close_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_CALLBACK_GENERATION_SYMBOL
    )
    transport_kd_close_submitted_fd_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSE_SUBMITTED_FD_SYMBOL
    )
    transport_kd_fd_before_close_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_FD_BEFORE_CLOSE_SYMBOL
    )
    transport_kd_fd_after_close_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_KD_FD_AFTER_CLOSE_SYMBOL
    )
    transport_ip_close_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_IP_CLOSE_SUBMIT_COUNT_SYMBOL
    )
    transport_socket_close_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CLOSE_SUBMIT_COUNT_SYMBOL
    )
    transport_startup_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_SUBMIT_COUNT_SYMBOL
    )
    transport_startup_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_CALLBACK_COUNT_SYMBOL
    )
    transport_startup_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_SUBMIT_RESULT_SYMBOL
    )
    transport_startup_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_CALLBACK_RESULT_SYMBOL
    )
    transport_startup_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_SUBMIT_GENERATION_SYMBOL
    )
    transport_startup_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_CALLBACK_GENERATION_SYMBOL
    )
    transport_startup_target_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_TARGET_ADDRESS_SYMBOL
    )
    transport_startup_command_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_COMMAND_SYMBOL
    )
    transport_startup_submitted_fd_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_SUBMITTED_FD_SYMBOL
    )
    transport_startup_callback_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_CALLBACK_POINTER_SYMBOL
    )
    transport_startup_context_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_CONTEXT_POINTER_SYMBOL
    )
    transport_startup_callback_exit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_CALLBACK_EXIT_COUNT_SYMBOL
    )
    transport_startup_stale_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_STALE_CALLBACK_COUNT_SYMBOL
    )
    transport_startup_duplicate_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_DUPLICATE_CALLBACK_COUNT_SYMBOL
    )
    transport_startup_service_started_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_SERVICE_STARTED_BEFORE_SUBMIT_SYMBOL
    )
    transport_startup_service_started_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_SERVICE_STARTED_AFTER_COMPLETION_SYMBOL
    )
    transport_ip_fd_before_startup_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_IP_FD_BEFORE_STARTUP_SYMBOL
    )
    transport_ip_fd_after_startup_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_IP_FD_AFTER_STARTUP_SYMBOL
    )
    transport_startup_pending_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_PENDING_BEFORE_SUBMIT_SYMBOL
    )
    transport_startup_pending_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_PENDING_AFTER_COMPLETION_SYMBOL
    )
    transport_startup_phase_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_PHASE_BEFORE_SUBMIT_SYMBOL
    )
    transport_startup_phase_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_PHASE_AFTER_COMPLETION_SYMBOL
    )
    transport_startup_pre_call_args_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_PRE_CALL_ARGS_SYMBOL
    )
    transport_startup_pre_call_args_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_STARTUP_PRE_CALL_ARGS_SYMBOL
    )
    transport_get_host_id_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_SUBMIT_COUNT_SYMBOL
    )
    transport_get_host_id_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_COUNT_SYMBOL
    )
    transport_get_host_id_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_SUBMIT_RESULT_SYMBOL
    )
    transport_get_host_id_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_RESULT_SYMBOL
    )
    transport_get_host_id_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_SUBMIT_GENERATION_SYMBOL
    )
    transport_get_host_id_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_GENERATION_SYMBOL
    )
    transport_get_host_id_target_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_TARGET_ADDRESS_SYMBOL
    )
    transport_get_host_id_command_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_COMMAND_SYMBOL
    )
    transport_get_host_id_submitted_fd_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_SUBMITTED_FD_SYMBOL
    )
    transport_get_host_id_callback_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_POINTER_SYMBOL
    )
    transport_get_host_id_context_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_CONTEXT_POINTER_SYMBOL
    )
    transport_get_host_id_callback_exit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_CALLBACK_EXIT_COUNT_SYMBOL
    )
    transport_get_host_id_stale_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_STALE_CALLBACK_COUNT_SYMBOL
    )
    transport_get_host_id_duplicate_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_DUPLICATE_CALLBACK_COUNT_SYMBOL
    )
    transport_get_host_id_service_started_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_SERVICE_STARTED_BEFORE_SUBMIT_SYMBOL
    )
    transport_get_host_id_service_started_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_SERVICE_STARTED_AFTER_COMPLETION_SYMBOL
    )
    transport_ip_fd_before_get_host_id_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_IP_FD_BEFORE_GET_HOST_ID_SYMBOL
    )
    transport_ip_fd_after_get_host_id_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_IP_FD_AFTER_GET_HOST_ID_SYMBOL
    )
    transport_get_host_id_pending_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_PENDING_BEFORE_SUBMIT_SYMBOL
    )
    transport_get_host_id_pending_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_PENDING_AFTER_COMPLETION_SYMBOL
    )
    transport_get_host_id_phase_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_PHASE_BEFORE_SUBMIT_SYMBOL
    )
    transport_get_host_id_phase_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_PHASE_AFTER_COMPLETION_SYMBOL
    )
    transport_get_host_id_pre_call_args_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_PRE_CALL_ARGS_SYMBOL
    )
    transport_get_host_id_pre_call_args_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_GET_HOST_ID_PRE_CALL_ARGS_SYMBOL
    )
    transport_socket_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_SUBMIT_COUNT_SYMBOL
    )
    transport_socket_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CALLBACK_COUNT_SYMBOL
    )
    transport_socket_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_SUBMIT_RESULT_SYMBOL
    )
    transport_socket_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CALLBACK_RESULT_SYMBOL
    )
    transport_socket_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_SUBMIT_GENERATION_SYMBOL
    )
    transport_socket_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CALLBACK_GENERATION_SYMBOL
    )
    transport_socket_target_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_TARGET_ADDRESS_SYMBOL
    )
    transport_socket_command_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_SOCKET_COMMAND_SYMBOL)
    transport_socket_submitted_fd_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_SUBMITTED_FD_SYMBOL
    )
    transport_socket_callback_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CALLBACK_POINTER_SYMBOL
    )
    transport_socket_context_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CONTEXT_POINTER_SYMBOL
    )
    transport_socket_callback_exit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CALLBACK_EXIT_COUNT_SYMBOL
    )
    transport_socket_stale_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_STALE_CALLBACK_COUNT_SYMBOL
    )
    transport_socket_duplicate_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_DUPLICATE_CALLBACK_COUNT_SYMBOL
    )
    transport_socket_fd_before_submit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_FD_BEFORE_SUBMIT_SYMBOL
    )
    transport_socket_fd_after_completion_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_FD_AFTER_COMPLETION_SYMBOL
    )
    transport_socket_request_address_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_REQUEST_ADDRESS_SYMBOL
    )
    transport_socket_request_storage_size_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_REQUEST_STORAGE_SIZE_SYMBOL
    )
    transport_socket_request_logical_size_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_REQUEST_LOGICAL_SIZE_SYMBOL
    )
    transport_socket_request_alignment_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_REQUEST_ALIGNMENT_SYMBOL
    )
    transport_socket_family_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_FAMILY_VALUE_SYMBOL
    )
    transport_socket_type_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_TYPE_VALUE_SYMBOL
    )
    transport_socket_protocol_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_PROTOCOL_VALUE_SYMBOL
    )
    transport_socket_descriptor_valid_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_DESCRIPTOR_VALID_SYMBOL
    )
    transport_socket_ready_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_SOCKET_READY_SYMBOL)
    transport_socket_request_bytes_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_REQUEST_BYTES_SYMBOL
    )
    transport_socket_request_bytes_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_REQUEST_BYTES_SYMBOL
    )
    transport_socket_pre_call_args_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_PRE_CALL_ARGS_SYMBOL
    )
    transport_socket_pre_call_args_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_PRE_CALL_ARGS_SYMBOL
    )
    transport_bind_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_SUBMIT_COUNT_SYMBOL
    )
    transport_bind_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_CALLBACK_COUNT_SYMBOL
    )
    transport_bind_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_SUBMIT_RESULT_SYMBOL
    )
    transport_bind_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_CALLBACK_RESULT_SYMBOL
    )
    transport_bind_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_SUBMIT_GENERATION_SYMBOL
    )
    transport_bind_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_CALLBACK_GENERATION_SYMBOL
    )
    transport_bind_target_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_TARGET_ADDRESS_SYMBOL
    )
    transport_bind_command_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_BIND_COMMAND_SYMBOL)
    transport_bind_submitted_fd_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_SUBMITTED_FD_SYMBOL
    )
    transport_bind_callback_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_CALLBACK_POINTER_SYMBOL
    )
    transport_bind_context_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_CONTEXT_POINTER_SYMBOL
    )
    transport_bind_callback_exit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_CALLBACK_EXIT_COUNT_SYMBOL
    )
    transport_bind_stale_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_STALE_CALLBACK_COUNT_SYMBOL
    )
    transport_bind_duplicate_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_DUPLICATE_CALLBACK_COUNT_SYMBOL
    )
    transport_bind_request_address_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_REQUEST_ADDRESS_SYMBOL
    )
    transport_bind_request_storage_size_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_REQUEST_STORAGE_SIZE_SYMBOL
    )
    transport_bind_request_logical_size_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_REQUEST_LOGICAL_SIZE_SYMBOL
    )
    transport_bind_request_alignment_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_REQUEST_ALIGNMENT_SYMBOL
    )
    transport_bind_sockaddr_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_SOCKADDR_LENGTH_SYMBOL
    )
    transport_bind_family_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_FAMILY_VALUE_SYMBOL
    )
    transport_bind_port_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_PORT_VALUE_SYMBOL
    )
    transport_bind_address_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_ADDRESS_VALUE_SYMBOL
    )
    transport_bind_request_bytes_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_REQUEST_BYTES_SYMBOL
    )
    transport_bind_request_bytes_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_REQUEST_BYTES_SYMBOL
    )
    transport_bind_pre_call_args_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_PRE_CALL_ARGS_SYMBOL
    )
    transport_bind_pre_call_args_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_BIND_PRE_CALL_ARGS_SYMBOL
    )
    transport_cleanup_close_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_COUNT_SYMBOL
    )
    transport_cleanup_close_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_SUBMIT_RESULT_SYMBOL
    )
    transport_cleanup_close_callback_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_RESULT_SYMBOL
    )
    transport_cleanup_close_submit_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_SUBMIT_GENERATION_SYMBOL
    )
    transport_cleanup_close_callback_generation_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_GENERATION_SYMBOL
    )
    transport_cleanup_close_target_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_TARGET_ADDRESS_SYMBOL
    )
    transport_cleanup_close_command_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_COMMAND_SYMBOL
    )
    transport_cleanup_close_submitted_fd_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_SUBMITTED_FD_SYMBOL
    )
    transport_cleanup_close_callback_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_POINTER_SYMBOL
    )
    transport_cleanup_close_context_pointer_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_CONTEXT_POINTER_SYMBOL
    )
    transport_cleanup_close_callback_exit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_CALLBACK_EXIT_COUNT_SYMBOL
    )
    transport_cleanup_close_stale_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_STALE_CALLBACK_COUNT_SYMBOL
    )
    transport_cleanup_close_duplicate_callback_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_DUPLICATE_CALLBACK_COUNT_SYMBOL
    )
    transport_cleanup_close_request_address_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_ADDRESS_SYMBOL
    )
    transport_cleanup_close_request_storage_size_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_STORAGE_SIZE_SYMBOL
    )
    transport_cleanup_close_request_logical_size_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_LOGICAL_SIZE_SYMBOL
    )
    transport_cleanup_close_request_alignment_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_ALIGNMENT_SYMBOL
    )
    transport_cleanup_close_request_value_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_VALUE_SYMBOL
    )
    transport_cleanup_close_request_bytes_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_BYTES_SYMBOL
    )
    transport_cleanup_close_request_bytes_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_REQUEST_BYTES_SYMBOL
    )
    transport_cleanup_close_pre_call_args_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_PRE_CALL_ARGS_SYMBOL
    )
    transport_cleanup_close_pre_call_args_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_CLOSE_PRE_CALL_ARGS_SYMBOL
    )
    transport_bound_flag_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_BOUND_FLAG_SYMBOL)
    transport_bound_address_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_BOUND_ADDRESS_SYMBOL)
    transport_socket_closed_after_bind_failure_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_CLOSED_AFTER_BIND_FAILURE_SYMBOL
    )
    transport_socket_leak_detected_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SOCKET_LEAK_DETECTED_SYMBOL
    )
    transport_kd_fd_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_KD_FD_SYMBOL)
    transport_kd_closed_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_KD_CLOSED_SYMBOL)
    transport_ip_fd_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_IP_FD_SYMBOL)
    transport_socket_fd_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_SOCKET_FD_SYMBOL)
    transport_host_id_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_HOST_ID_SYMBOL)
    transport_host_id_available_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_HOST_ID_AVAILABLE_SYMBOL
    )
    transport_host_id_ready_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_HOST_ID_READY_SYMBOL)
    transport_service_started_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SERVICE_STARTED_SYMBOL
    )
    transport_bound_port_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_BOUND_PORT_SYMBOL)
    transport_receive_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_RECEIVE_SUBMIT_COUNT_SYMBOL
    )
    transport_send_submit_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_SEND_SUBMIT_COUNT_SYMBOL
    )
    transport_receive_count_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_RECEIVE_COUNT_SYMBOL)
    transport_receive_bytes_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_RECEIVE_BYTES_SYMBOL)
    transport_send_count_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_SEND_COUNT_SYMBOL)
    transport_send_bytes_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_SEND_BYTES_SYMBOL)
    transport_receive_arm_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_RECEIVE_ARM_COUNT_SYMBOL
    )
    transport_receive_rearm_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_RECEIVE_REARM_COUNT_SYMBOL
    )
    transport_configured_exchange_limit_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CONFIGURED_EXCHANGE_LIMIT_SYMBOL
    )
    transport_completed_exchange_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_COMPLETED_EXCHANGE_COUNT_SYMBOL
    )
    transport_current_exchange_index_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CURRENT_EXCHANGE_INDEX_SYMBOL
    )
    transport_last_completed_exchange_index_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_COMPLETED_EXCHANGE_INDEX_SYMBOL
    )
    transport_previous_peer_ipv4_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_PREVIOUS_PEER_IPV4_SYMBOL
    )
    transport_previous_peer_port_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_PREVIOUS_PEER_PORT_SYMBOL
    )
    transport_rearm_submission_failure_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_REARM_SUBMISSION_FAILURE_COUNT_SYMBOL
    )
    transport_loop_complete_transition_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LOOP_COMPLETE_TRANSITION_COUNT_SYMBOL
    )
    transport_cleanup_deferred_count_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CLEANUP_DEFERRED_COUNT_SYMBOL
    )
    transport_last_receive_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_RECEIVE_LENGTH_SYMBOL
    )
    transport_last_send_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_SEND_LENGTH_SYMBOL
    )
    transport_last_peer_ipv4_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_LAST_PEER_IPV4_SYMBOL)
    transport_last_peer_port_address = _extract_symbol_address(readelf_symbols, RUNTIME_TRANSPORT_LAST_PEER_PORT_SYMBOL)
    transport_last_peer_family_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_PEER_FAMILY_SYMBOL
    )
    transport_last_poll_action_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_POLL_ACTION_SYMBOL
    )
    transport_last_submit_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_SUBMIT_RESULT_SYMBOL
    )
    transport_polls_while_receive_pending_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_POLLS_WHILE_RECEIVE_PENDING_SYMBOL
    )
    transport_polls_after_loop_complete_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_POLLS_AFTER_LOOP_COMPLETE_SYMBOL
    )
    transport_last_receive_preview_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_RECEIVE_PREVIEW_SYMBOL
    )
    transport_last_receive_preview_size = _extract_symbol_size(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_RECEIVE_PREVIEW_SYMBOL
    )
    transport_last_send_preview_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_LAST_SEND_PREVIEW_SYMBOL
    )
    transport_last_send_preview_size = _extract_symbol_size(readelf_symbols, RUNTIME_TRANSPORT_LAST_SEND_PREVIEW_SYMBOL)
    transport_prepared_send_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_PREPARED_SEND_LENGTH_SYMBOL
    )
    transport_cp3w_datagrams_processed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_DATAGRAMS_PROCESSED_SYMBOL
    )
    transport_cp3w_frames_valid_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_VALID_SYMBOL
    )
    transport_cp3w_frames_invalid_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_SYMBOL
    )
    transport_cp3w_frames_too_short_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_TOO_SHORT_SYMBOL
    )
    transport_cp3w_frames_invalid_magic_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_MAGIC_SYMBOL
    )
    transport_cp3w_frames_invalid_version_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_VERSION_SYMBOL
    )
    transport_cp3w_frames_unsupported_type_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_UNSUPPORTED_TYPE_SYMBOL
    )
    transport_cp3w_frames_nonzero_flags_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_NONZERO_FLAGS_SYMBOL
    )
    transport_cp3w_frames_length_mismatch_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_LENGTH_MISMATCH_SYMBOL
    )
    transport_cp3w_frames_payload_too_large_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_PAYLOAD_TOO_LARGE_SYMBOL
    )
    transport_cp3w_frames_invalid_payload_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_INVALID_PAYLOAD_SYMBOL
    )
    transport_cp3w_frames_malformed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMES_MALFORMED_SYMBOL
    )
    transport_cp3w_framed_responses_submitted_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMED_RESPONSES_SUBMITTED_SYMBOL
    )
    transport_cp3w_framed_responses_completed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FRAMED_RESPONSES_COMPLETED_SYMBOL
    )
    transport_cp3w_last_request_id_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_REQUEST_ID_SYMBOL
    )
    transport_cp3w_last_response_id_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_RESPONSE_ID_SYMBOL
    )
    transport_cp3w_last_message_type_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_MESSAGE_TYPE_SYMBOL
    )
    transport_cp3w_last_declared_payload_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_DECLARED_PAYLOAD_LENGTH_SYMBOL
    )
    transport_cp3w_last_actual_payload_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_ACTUAL_PAYLOAD_LENGTH_SYMBOL
    )
    transport_cp3w_last_frame_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_FRAME_RESULT_SYMBOL
    )
    transport_cp3w_final_datagram_index_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_FINAL_DATAGRAM_INDEX_SYMBOL
    )
    transport_cp3w_requests_dispatched_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_REQUESTS_DISPATCHED_SYMBOL
    )
    transport_cp3w_hello_requests_received_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_REQUESTS_RECEIVED_SYMBOL
    )
    transport_cp3w_hello_successes_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_SUCCESSES_SYMBOL
    )
    transport_cp3w_hello_version_rejections_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_VERSION_REJECTIONS_SYMBOL
    )
    transport_cp3w_hello_responses_submitted_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_RESPONSES_SUBMITTED_SYMBOL
    )
    transport_cp3w_hello_responses_completed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_RESPONSES_COMPLETED_SYMBOL
    )
    transport_cp3w_hello_duplicate_requests_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_DUPLICATE_REQUESTS_SYMBOL
    )
    transport_cp3w_hello_renegotiation_rejections_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_HELLO_RENEGOTIATION_REJECTIONS_SYMBOL
    )
    transport_cp3w_pre_hello_gated_commands_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_PRE_HELLO_GATED_COMMANDS_SYMBOL
    )
    transport_cp3w_not_negotiated_responses_submitted_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_NOT_NEGOTIATED_RESPONSES_SUBMITTED_SYMBOL
    )
    transport_cp3w_not_negotiated_responses_completed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_NOT_NEGOTIATED_RESPONSES_COMPLETED_SYMBOL
    )
    transport_cp3w_ping_requests_received_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_PING_REQUESTS_RECEIVED_SYMBOL
    )
    transport_cp3w_pong_responses_submitted_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_PONG_RESPONSES_SUBMITTED_SYMBOL
    )
    transport_cp3w_pong_responses_completed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_PONG_RESPONSES_COMPLETED_SYMBOL
    )
    transport_cp3w_unsupported_commands_received_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_UNSUPPORTED_COMMANDS_RECEIVED_SYMBOL
    )
    transport_cp3w_unsupported_responses_submitted_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_UNSUPPORTED_RESPONSES_SUBMITTED_SYMBOL
    )
    transport_cp3w_unsupported_responses_completed_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_UNSUPPORTED_RESPONSES_COMPLETED_SYMBOL
    )
    transport_cp3w_negotiated_flag_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_NEGOTIATED_FLAG_SYMBOL
    )
    transport_cp3w_selected_protocol_version_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_SELECTED_PROTOCOL_VERSION_SYMBOL
    )
    transport_cp3w_client_nonce_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_CLIENT_NONCE_SYMBOL
    )
    transport_cp3w_client_capabilities_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_CLIENT_CAPABILITIES_SYMBOL
    )
    transport_cp3w_runtime_capabilities_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_RUNTIME_CAPABILITIES_SYMBOL
    )
    transport_cp3w_accepted_capabilities_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_ACCEPTED_CAPABILITIES_SYMBOL
    )
    transport_cp3w_session_id_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_SESSION_ID_SYMBOL
    )
    transport_cp3w_runtime_build_id_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_RUNTIME_BUILD_ID_SYMBOL
    )
    transport_cp3w_last_command_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_COMMAND_SYMBOL
    )
    transport_cp3w_last_response_status_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_RESPONSE_STATUS_SYMBOL
    )
    transport_cp3w_last_ping_payload_length_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_PING_PAYLOAD_LENGTH_SYMBOL
    )
    transport_cp3w_last_dispatch_result_address = _extract_symbol_address(
        readelf_symbols, RUNTIME_TRANSPORT_CP3W_LAST_DISPATCH_RESULT_SYMBOL
    )
    transport_cp3w_game_identity_state_addresses = {
        name: _extract_symbol_address(readelf_symbols, symbol)
        for name, symbol in RUNTIME_TRANSPORT_CP3W_GAME_IDENTITY_SYMBOLS.items()
    }
    transport_cp3w_inventory_state_addresses = {
        name: _extract_symbol_address(readelf_symbols, symbol)
        for name, symbol in RUNTIME_TRANSPORT_CP3W_INVENTORY_SYMBOLS.items()
    }
    cache_range_start, cache_range_size = compute_cache_range(
        address=runtime_destination,
        size=len(payload_bytes),
        cache_line_size=RELOCATED_RUNTIME_CACHE_LINE_SIZE,
    )
    cp3c_config_start_address = _extract_symbol_address(readelf_symbols, CP3C_CONFIG_START_SYMBOL)
    cp3c_config_end_address = _extract_symbol_address(readelf_symbols, CP3C_CONFIG_END_SYMBOL)
    cp3c_server_ipv4_address = _extract_symbol_address(readelf_symbols, CP3C_SERVER_IPV4_SYMBOL)
    cp3c_server_port_address = _extract_symbol_address(readelf_symbols, CP3C_SERVER_PORT_SYMBOL)
    if not (
        cp3c_config_start_address < cp3c_config_end_address
        and cp3c_config_start_address <= cp3c_server_ipv4_address < cp3c_config_end_address
        and cp3c_config_start_address <= cp3c_server_port_address < cp3c_config_end_address
        and cp3c_server_ipv4_address + 4 <= cp3c_config_end_address
        and cp3c_server_port_address + 2 <= cp3c_config_end_address
        and runtime_destination <= cp3c_config_start_address
        and cp3c_config_end_address <= runtime_destination + len(payload_bytes)
    ):
        raise RuntimeError("Invalid CP3C configuration symbol bounds.")
    return RelocatedRuntimeBuildResult(
        payload_bytes=payload_bytes,
        payload_sha256=payload_sha256,
        payload_size=len(payload_bytes),
        entry_address=entry_address,
        poll_entry_address=poll_entry_address,
        poll_hook_wrapper_address=poll_hook_wrapper_address,
        code_start=code_start,
        code_end=code_end,
        state_start=state_start,
        state_end=state_end,
        cp3c_config_start_address=cp3c_config_start_address,
        cp3c_config_end_address=cp3c_config_end_address,
        cp3c_server_ipv4_address=cp3c_server_ipv4_address,
        cp3c_server_port_address=cp3c_server_port_address,
        network_diagnostics_address=network_diagnostics_address,
        native_beacon_ipv4_address=native_beacon_ipv4_address,
        canary_address=canary_start,
        canary_size=canary_end - canary_start,
        canary_sha256=hashlib.sha256(RELOCATED_RUNTIME_CANARY_BYTES).hexdigest(),
        copy_complete_marker_address=copy_complete_marker_address,
        runtime_executed_marker_address=runtime_executed_marker_address,
        runtime_execution_counter_address=runtime_execution_counter_address,
        runtime_status_address=runtime_status_address,
        bootstrap_return_marker_address=bootstrap_return_marker_address,
        poll_counter_address=poll_counter_address,
        poll_heartbeat_address=poll_heartbeat_address,
        poll_last_sequence_address=poll_last_sequence_address,
        diagnostic_hook_wrapper_entry_count_address=diagnostic_hook_wrapper_entry_count_address,
        diagnostic_hook_wrapper_before_poll_count_address=diagnostic_hook_wrapper_before_poll_count_address,
        diagnostic_poll_entry_count_address=diagnostic_poll_entry_count_address,
        diagnostic_poll_exit_count_address=diagnostic_poll_exit_count_address,
        diagnostic_state_machine_entry_count_address=diagnostic_state_machine_entry_count_address,
        diagnostic_state_machine_exit_count_address=diagnostic_state_machine_exit_count_address,
        diagnostic_c_before_veneer_call_count_address=diagnostic_c_before_veneer_call_count_address,
        diagnostic_retail_veneer_entry_count_address=diagnostic_retail_veneer_entry_count_address,
        diagnostic_retail_target_return_count_address=diagnostic_retail_target_return_count_address,
        diagnostic_retail_veneer_exit_count_address=diagnostic_retail_veneer_exit_count_address,
        diagnostic_c_after_veneer_call_count_address=diagnostic_c_after_veneer_call_count_address,
        diagnostic_ios_submit_attempt_count_address=diagnostic_ios_submit_attempt_count_address,
        diagnostic_ios_submit_return_count_address=diagnostic_ios_submit_return_count_address,
        diagnostic_ios_submit_return_value_address=diagnostic_ios_submit_return_value_address,
        diagnostic_callback_entry_count_address=diagnostic_callback_entry_count_address,
        diagnostic_callback_exit_count_address=diagnostic_callback_exit_count_address,
        diagnostic_hook_wrapper_after_poll_count_address=diagnostic_hook_wrapper_after_poll_count_address,
        diagnostic_hook_wrapper_exit_count_address=diagnostic_hook_wrapper_exit_count_address,
        diagnostic_last_execution_marker_address=diagnostic_last_execution_marker_address,
        diagnostic_last_phase_before_step_address=diagnostic_last_phase_before_step_address,
        diagnostic_last_phase_after_step_address=diagnostic_last_phase_after_step_address,
        diagnostic_callback_result_address=diagnostic_callback_result_address,
        verified_game_r2_address=verified_game_r2_address,
        verified_game_r13_address=verified_game_r13_address,
        abi_probe_supplied_args_address=abi_probe_supplied_args_address,
        abi_probe_supplied_args_size=abi_probe_supplied_args_size,
        abi_probe_pre_call_args_address=abi_probe_pre_call_args_address,
        abi_probe_pre_call_args_size=abi_probe_pre_call_args_size,
        abi_probe_target_args_address=abi_probe_target_args_address,
        abi_probe_target_args_size=abi_probe_target_args_size,
        abi_probe_return_value_address=abi_probe_return_value_address,
        abi_probe_result_flags_address=abi_probe_result_flags_address,
        abi_probe_stack_pointer_before_address=abi_probe_stack_pointer_before_address,
        abi_probe_stack_pointer_after_address=abi_probe_stack_pointer_after_address,
        abi_probe_saved_lr_address=abi_probe_saved_lr_address,
        abi_probe_restored_lr_address=abi_probe_restored_lr_address,
        abi_probe_saved_r2_address=abi_probe_saved_r2_address,
        abi_probe_restored_r2_address=abi_probe_restored_r2_address,
        abi_probe_saved_r13_address=abi_probe_saved_r13_address,
        abi_probe_restored_r13_address=abi_probe_restored_r13_address,
        abi_probe_target_ctr_address=abi_probe_target_ctr_address,
        abi_probe_after_call_flag_address=abi_probe_after_call_flag_address,
        abi_probe_expected_return_value_address=abi_probe_expected_return_value_address,
        transport_phase_address=transport_phase_address,
        transport_last_error_address=transport_last_error_address,
        transport_last_socket_error_address=transport_last_socket_error_address,
        transport_last_ios_result_address=transport_last_ios_result_address,
        transport_pending_operation_address=transport_pending_operation_address,
        transport_pending_generation_address=transport_pending_generation_address,
        transport_callback_generation_address=transport_callback_generation_address,
        transport_callback_count_address=transport_callback_count_address,
        transport_rejected_callback_count_address=transport_rejected_callback_count_address,
        transport_callback_pending_address=transport_callback_pending_address,
        transport_open_kd_submit_count_address=transport_open_kd_submit_count_address,
        transport_open_kd_callback_count_address=transport_open_kd_callback_count_address,
        transport_nwc24_submit_count_address=transport_nwc24_submit_count_address,
        transport_nwc24_callback_count_address=transport_nwc24_callback_count_address,
        transport_nwc24_synchronous_result_address=transport_nwc24_synchronous_result_address,
        transport_nwc24_callback_result_address=transport_nwc24_callback_result_address,
        transport_nwc24_output_buffer_address=transport_nwc24_output_buffer_address,
        transport_nwc24_output_digest_address=transport_nwc24_output_digest_address,
        transport_open_ip_submit_count_address=transport_open_ip_submit_count_address,
        transport_open_ip_callback_count_address=transport_open_ip_callback_count_address,
        transport_kd_close_submit_count_address=transport_kd_close_submit_count_address,
        transport_kd_close_callback_count_address=transport_kd_close_callback_count_address,
        transport_ip_close_submit_count_address=transport_ip_close_submit_count_address,
        transport_socket_close_submit_count_address=transport_socket_close_submit_count_address,
        transport_startup_submit_count_address=transport_startup_submit_count_address,
        transport_startup_callback_count_address=transport_startup_callback_count_address,
        transport_get_host_id_submit_count_address=transport_get_host_id_submit_count_address,
        transport_get_host_id_callback_count_address=transport_get_host_id_callback_count_address,
        transport_socket_submit_count_address=transport_socket_submit_count_address,
        transport_socket_callback_count_address=transport_socket_callback_count_address,
        transport_bind_submit_count_address=transport_bind_submit_count_address,
        transport_bind_callback_count_address=transport_bind_callback_count_address,
        transport_kd_fd_address=transport_kd_fd_address,
        transport_kd_closed_address=transport_kd_closed_address,
        transport_ip_fd_address=transport_ip_fd_address,
        transport_socket_fd_address=transport_socket_fd_address,
        transport_host_id_address=transport_host_id_address,
        transport_host_id_available_address=transport_host_id_available_address,
        transport_host_id_ready_address=transport_host_id_ready_address,
        transport_service_started_address=transport_service_started_address,
        transport_bound_port_address=transport_bound_port_address,
        transport_receive_submit_count_address=transport_receive_submit_count_address,
        transport_send_submit_count_address=transport_send_submit_count_address,
        transport_receive_count_address=transport_receive_count_address,
        transport_receive_bytes_address=transport_receive_bytes_address,
        transport_send_count_address=transport_send_count_address,
        transport_send_bytes_address=transport_send_bytes_address,
        transport_receive_arm_count_address=transport_receive_arm_count_address,
        transport_receive_rearm_count_address=transport_receive_rearm_count_address,
        transport_configured_exchange_limit_address=transport_configured_exchange_limit_address,
        transport_completed_exchange_count_address=transport_completed_exchange_count_address,
        transport_current_exchange_index_address=transport_current_exchange_index_address,
        transport_last_completed_exchange_index_address=transport_last_completed_exchange_index_address,
        transport_previous_peer_ipv4_address=transport_previous_peer_ipv4_address,
        transport_previous_peer_port_address=transport_previous_peer_port_address,
        transport_rearm_submission_failure_count_address=transport_rearm_submission_failure_count_address,
        transport_loop_complete_transition_count_address=transport_loop_complete_transition_count_address,
        transport_cleanup_deferred_count_address=transport_cleanup_deferred_count_address,
        transport_last_receive_length_address=transport_last_receive_length_address,
        transport_last_send_length_address=transport_last_send_length_address,
        transport_last_peer_ipv4_address=transport_last_peer_ipv4_address,
        transport_last_peer_port_address=transport_last_peer_port_address,
        transport_last_peer_family_address=transport_last_peer_family_address,
        transport_last_poll_action_address=transport_last_poll_action_address,
        transport_last_submit_result_address=transport_last_submit_result_address,
        transport_polls_while_receive_pending_address=transport_polls_while_receive_pending_address,
        transport_polls_after_loop_complete_address=transport_polls_after_loop_complete_address,
        transport_last_receive_preview_address=transport_last_receive_preview_address,
        transport_last_receive_preview_size=transport_last_receive_preview_size,
        transport_last_send_preview_address=transport_last_send_preview_address,
        transport_last_send_preview_size=transport_last_send_preview_size,
        transport_prepared_send_length_address=transport_prepared_send_length_address,
        transport_cp3w_datagrams_processed_address=transport_cp3w_datagrams_processed_address,
        transport_cp3w_frames_valid_address=transport_cp3w_frames_valid_address,
        transport_cp3w_frames_invalid_address=transport_cp3w_frames_invalid_address,
        transport_cp3w_frames_too_short_address=transport_cp3w_frames_too_short_address,
        transport_cp3w_frames_invalid_magic_address=transport_cp3w_frames_invalid_magic_address,
        transport_cp3w_frames_invalid_version_address=transport_cp3w_frames_invalid_version_address,
        transport_cp3w_frames_unsupported_type_address=transport_cp3w_frames_unsupported_type_address,
        transport_cp3w_frames_nonzero_flags_address=transport_cp3w_frames_nonzero_flags_address,
        transport_cp3w_frames_length_mismatch_address=transport_cp3w_frames_length_mismatch_address,
        transport_cp3w_frames_payload_too_large_address=transport_cp3w_frames_payload_too_large_address,
        transport_cp3w_frames_invalid_payload_address=transport_cp3w_frames_invalid_payload_address,
        transport_cp3w_frames_malformed_address=transport_cp3w_frames_malformed_address,
        transport_cp3w_framed_responses_submitted_address=transport_cp3w_framed_responses_submitted_address,
        transport_cp3w_framed_responses_completed_address=transport_cp3w_framed_responses_completed_address,
        transport_cp3w_last_request_id_address=transport_cp3w_last_request_id_address,
        transport_cp3w_last_response_id_address=transport_cp3w_last_response_id_address,
        transport_cp3w_last_message_type_address=transport_cp3w_last_message_type_address,
        transport_cp3w_last_declared_payload_length_address=transport_cp3w_last_declared_payload_length_address,
        transport_cp3w_last_actual_payload_length_address=transport_cp3w_last_actual_payload_length_address,
        transport_cp3w_last_frame_result_address=transport_cp3w_last_frame_result_address,
        transport_cp3w_final_datagram_index_address=transport_cp3w_final_datagram_index_address,
        transport_cp3w_requests_dispatched_address=transport_cp3w_requests_dispatched_address,
        transport_cp3w_hello_requests_received_address=transport_cp3w_hello_requests_received_address,
        transport_cp3w_hello_successes_address=transport_cp3w_hello_successes_address,
        transport_cp3w_hello_version_rejections_address=transport_cp3w_hello_version_rejections_address,
        transport_cp3w_hello_responses_submitted_address=transport_cp3w_hello_responses_submitted_address,
        transport_cp3w_hello_responses_completed_address=transport_cp3w_hello_responses_completed_address,
        transport_cp3w_hello_duplicate_requests_address=transport_cp3w_hello_duplicate_requests_address,
        transport_cp3w_hello_renegotiation_rejections_address=(transport_cp3w_hello_renegotiation_rejections_address),
        transport_cp3w_pre_hello_gated_commands_address=transport_cp3w_pre_hello_gated_commands_address,
        transport_cp3w_not_negotiated_responses_submitted_address=(
            transport_cp3w_not_negotiated_responses_submitted_address
        ),
        transport_cp3w_not_negotiated_responses_completed_address=(
            transport_cp3w_not_negotiated_responses_completed_address
        ),
        transport_cp3w_ping_requests_received_address=transport_cp3w_ping_requests_received_address,
        transport_cp3w_pong_responses_submitted_address=transport_cp3w_pong_responses_submitted_address,
        transport_cp3w_pong_responses_completed_address=transport_cp3w_pong_responses_completed_address,
        transport_cp3w_unsupported_commands_received_address=transport_cp3w_unsupported_commands_received_address,
        transport_cp3w_unsupported_responses_submitted_address=transport_cp3w_unsupported_responses_submitted_address,
        transport_cp3w_unsupported_responses_completed_address=transport_cp3w_unsupported_responses_completed_address,
        transport_cp3w_negotiated_flag_address=transport_cp3w_negotiated_flag_address,
        transport_cp3w_selected_protocol_version_address=transport_cp3w_selected_protocol_version_address,
        transport_cp3w_client_nonce_address=transport_cp3w_client_nonce_address,
        transport_cp3w_client_capabilities_address=transport_cp3w_client_capabilities_address,
        transport_cp3w_runtime_capabilities_address=transport_cp3w_runtime_capabilities_address,
        transport_cp3w_accepted_capabilities_address=transport_cp3w_accepted_capabilities_address,
        transport_cp3w_session_id_address=transport_cp3w_session_id_address,
        transport_cp3w_runtime_build_id_address=transport_cp3w_runtime_build_id_address,
        transport_cp3w_last_command_address=transport_cp3w_last_command_address,
        transport_cp3w_last_response_status_address=transport_cp3w_last_response_status_address,
        transport_cp3w_last_ping_payload_length_address=transport_cp3w_last_ping_payload_length_address,
        transport_cp3w_last_dispatch_result_address=transport_cp3w_last_dispatch_result_address,
        transport_cp3w_game_identity_state_addresses=transport_cp3w_game_identity_state_addresses,
        transport_cp3w_inventory_state_addresses=transport_cp3w_inventory_state_addresses,
        transport_open_kd_submit_result_address=transport_open_kd_submit_result_address,
        transport_open_kd_callback_result_address=transport_open_kd_callback_result_address,
        transport_open_kd_submit_generation_address=transport_open_kd_submit_generation_address,
        transport_open_kd_callback_generation_address=transport_open_kd_callback_generation_address,
        transport_nwc24_submit_generation_address=transport_nwc24_submit_generation_address,
        transport_nwc24_callback_generation_address=transport_nwc24_callback_generation_address,
        transport_open_ip_submit_result_address=transport_open_ip_submit_result_address,
        transport_open_ip_callback_result_address=transport_open_ip_callback_result_address,
        transport_open_ip_submit_generation_address=transport_open_ip_submit_generation_address,
        transport_open_ip_callback_generation_address=transport_open_ip_callback_generation_address,
        transport_open_ip_path_pointer_address=transport_open_ip_path_pointer_address,
        transport_open_ip_path_length_address=transport_open_ip_path_length_address,
        transport_open_ip_mode_value_address=transport_open_ip_mode_value_address,
        transport_open_ip_callback_pointer_address=transport_open_ip_callback_pointer_address,
        transport_open_ip_context_pointer_address=transport_open_ip_context_pointer_address,
        transport_open_ip_callback_exit_count_address=transport_open_ip_callback_exit_count_address,
        transport_open_ip_stale_callback_count_address=transport_open_ip_stale_callback_count_address,
        transport_open_ip_duplicate_callback_count_address=transport_open_ip_duplicate_callback_count_address,
        transport_ip_fd_before_open_ip_address=transport_ip_fd_before_open_ip_address,
        transport_kd_close_submit_result_address=transport_kd_close_submit_result_address,
        transport_kd_close_callback_result_address=transport_kd_close_callback_result_address,
        transport_kd_close_submit_generation_address=transport_kd_close_submit_generation_address,
        transport_kd_close_callback_generation_address=transport_kd_close_callback_generation_address,
        transport_kd_close_submitted_fd_address=transport_kd_close_submitted_fd_address,
        transport_kd_fd_before_close_address=transport_kd_fd_before_close_address,
        transport_kd_fd_after_close_address=transport_kd_fd_after_close_address,
        transport_startup_submit_result_address=transport_startup_submit_result_address,
        transport_startup_callback_result_address=transport_startup_callback_result_address,
        transport_startup_submit_generation_address=transport_startup_submit_generation_address,
        transport_startup_callback_generation_address=transport_startup_callback_generation_address,
        transport_startup_target_address=transport_startup_target_address,
        transport_startup_command_address=transport_startup_command_address,
        transport_startup_submitted_fd_address=transport_startup_submitted_fd_address,
        transport_startup_callback_pointer_address=transport_startup_callback_pointer_address,
        transport_startup_context_pointer_address=transport_startup_context_pointer_address,
        transport_startup_callback_exit_count_address=transport_startup_callback_exit_count_address,
        transport_startup_stale_callback_count_address=transport_startup_stale_callback_count_address,
        transport_startup_duplicate_callback_count_address=transport_startup_duplicate_callback_count_address,
        transport_startup_service_started_before_submit_address=transport_startup_service_started_before_submit_address,
        transport_startup_service_started_after_completion_address=(
            transport_startup_service_started_after_completion_address
        ),
        transport_ip_fd_before_startup_address=transport_ip_fd_before_startup_address,
        transport_ip_fd_after_startup_address=transport_ip_fd_after_startup_address,
        transport_startup_pending_before_submit_address=transport_startup_pending_before_submit_address,
        transport_startup_pending_after_completion_address=transport_startup_pending_after_completion_address,
        transport_startup_phase_before_submit_address=transport_startup_phase_before_submit_address,
        transport_startup_phase_after_completion_address=transport_startup_phase_after_completion_address,
        transport_startup_pre_call_args_address=transport_startup_pre_call_args_address,
        transport_startup_pre_call_args_size=transport_startup_pre_call_args_size,
        transport_get_host_id_submit_result_address=transport_get_host_id_submit_result_address,
        transport_get_host_id_callback_result_address=transport_get_host_id_callback_result_address,
        transport_get_host_id_submit_generation_address=transport_get_host_id_submit_generation_address,
        transport_get_host_id_callback_generation_address=transport_get_host_id_callback_generation_address,
        transport_get_host_id_target_address=transport_get_host_id_target_address,
        transport_get_host_id_command_address=transport_get_host_id_command_address,
        transport_get_host_id_submitted_fd_address=transport_get_host_id_submitted_fd_address,
        transport_get_host_id_callback_pointer_address=transport_get_host_id_callback_pointer_address,
        transport_get_host_id_context_pointer_address=transport_get_host_id_context_pointer_address,
        transport_get_host_id_callback_exit_count_address=transport_get_host_id_callback_exit_count_address,
        transport_get_host_id_stale_callback_count_address=transport_get_host_id_stale_callback_count_address,
        transport_get_host_id_duplicate_callback_count_address=transport_get_host_id_duplicate_callback_count_address,
        transport_get_host_id_service_started_before_submit_address=(
            transport_get_host_id_service_started_before_submit_address
        ),
        transport_get_host_id_service_started_after_completion_address=(
            transport_get_host_id_service_started_after_completion_address
        ),
        transport_ip_fd_before_get_host_id_address=transport_ip_fd_before_get_host_id_address,
        transport_ip_fd_after_get_host_id_address=transport_ip_fd_after_get_host_id_address,
        transport_get_host_id_pending_before_submit_address=transport_get_host_id_pending_before_submit_address,
        transport_get_host_id_pending_after_completion_address=(transport_get_host_id_pending_after_completion_address),
        transport_get_host_id_phase_before_submit_address=transport_get_host_id_phase_before_submit_address,
        transport_get_host_id_phase_after_completion_address=transport_get_host_id_phase_after_completion_address,
        transport_get_host_id_pre_call_args_address=transport_get_host_id_pre_call_args_address,
        transport_get_host_id_pre_call_args_size=transport_get_host_id_pre_call_args_size,
        transport_socket_submit_result_address=transport_socket_submit_result_address,
        transport_socket_callback_result_address=transport_socket_callback_result_address,
        transport_socket_submit_generation_address=transport_socket_submit_generation_address,
        transport_socket_callback_generation_address=transport_socket_callback_generation_address,
        transport_socket_target_address=transport_socket_target_address,
        transport_socket_command_address=transport_socket_command_address,
        transport_socket_submitted_fd_address=transport_socket_submitted_fd_address,
        transport_socket_callback_pointer_address=transport_socket_callback_pointer_address,
        transport_socket_context_pointer_address=transport_socket_context_pointer_address,
        transport_socket_callback_exit_count_address=transport_socket_callback_exit_count_address,
        transport_socket_stale_callback_count_address=transport_socket_stale_callback_count_address,
        transport_socket_duplicate_callback_count_address=transport_socket_duplicate_callback_count_address,
        transport_socket_fd_before_submit_address=transport_socket_fd_before_submit_address,
        transport_socket_fd_after_completion_address=transport_socket_fd_after_completion_address,
        transport_socket_request_address_address=transport_socket_request_address_address,
        transport_socket_request_storage_size_address=transport_socket_request_storage_size_address,
        transport_socket_request_logical_size_address=transport_socket_request_logical_size_address,
        transport_socket_request_alignment_address=transport_socket_request_alignment_address,
        transport_socket_family_value_address=transport_socket_family_value_address,
        transport_socket_type_value_address=transport_socket_type_value_address,
        transport_socket_protocol_value_address=transport_socket_protocol_value_address,
        transport_socket_descriptor_valid_address=transport_socket_descriptor_valid_address,
        transport_socket_ready_address=transport_socket_ready_address,
        transport_socket_request_bytes_address=transport_socket_request_bytes_address,
        transport_socket_request_bytes_size=transport_socket_request_bytes_size,
        transport_socket_pre_call_args_address=transport_socket_pre_call_args_address,
        transport_socket_pre_call_args_size=transport_socket_pre_call_args_size,
        transport_bind_submit_result_address=transport_bind_submit_result_address,
        transport_bind_callback_result_address=transport_bind_callback_result_address,
        transport_bind_submit_generation_address=transport_bind_submit_generation_address,
        transport_bind_callback_generation_address=transport_bind_callback_generation_address,
        transport_bind_target_address=transport_bind_target_address,
        transport_bind_command_address=transport_bind_command_address,
        transport_bind_submitted_fd_address=transport_bind_submitted_fd_address,
        transport_bind_callback_pointer_address=transport_bind_callback_pointer_address,
        transport_bind_context_pointer_address=transport_bind_context_pointer_address,
        transport_bind_callback_exit_count_address=transport_bind_callback_exit_count_address,
        transport_bind_stale_callback_count_address=transport_bind_stale_callback_count_address,
        transport_bind_duplicate_callback_count_address=transport_bind_duplicate_callback_count_address,
        transport_bind_request_address_address=transport_bind_request_address_address,
        transport_bind_request_storage_size_address=transport_bind_request_storage_size_address,
        transport_bind_request_logical_size_address=transport_bind_request_logical_size_address,
        transport_bind_request_alignment_address=transport_bind_request_alignment_address,
        transport_bind_sockaddr_length_address=transport_bind_sockaddr_length_address,
        transport_bind_family_value_address=transport_bind_family_value_address,
        transport_bind_port_value_address=transport_bind_port_value_address,
        transport_bind_address_value_address=transport_bind_address_value_address,
        transport_bind_request_bytes_address=transport_bind_request_bytes_address,
        transport_bind_request_bytes_size=transport_bind_request_bytes_size,
        transport_bind_pre_call_args_address=transport_bind_pre_call_args_address,
        transport_bind_pre_call_args_size=transport_bind_pre_call_args_size,
        transport_cleanup_close_callback_count_address=transport_cleanup_close_callback_count_address,
        transport_cleanup_close_submit_result_address=transport_cleanup_close_submit_result_address,
        transport_cleanup_close_callback_result_address=transport_cleanup_close_callback_result_address,
        transport_cleanup_close_submit_generation_address=transport_cleanup_close_submit_generation_address,
        transport_cleanup_close_callback_generation_address=transport_cleanup_close_callback_generation_address,
        transport_cleanup_close_target_address=transport_cleanup_close_target_address,
        transport_cleanup_close_command_address=transport_cleanup_close_command_address,
        transport_cleanup_close_submitted_fd_address=transport_cleanup_close_submitted_fd_address,
        transport_cleanup_close_callback_pointer_address=transport_cleanup_close_callback_pointer_address,
        transport_cleanup_close_context_pointer_address=transport_cleanup_close_context_pointer_address,
        transport_cleanup_close_callback_exit_count_address=transport_cleanup_close_callback_exit_count_address,
        transport_cleanup_close_stale_callback_count_address=transport_cleanup_close_stale_callback_count_address,
        transport_cleanup_close_duplicate_callback_count_address=transport_cleanup_close_duplicate_callback_count_address,
        transport_cleanup_close_request_address_address=transport_cleanup_close_request_address_address,
        transport_cleanup_close_request_storage_size_address=transport_cleanup_close_request_storage_size_address,
        transport_cleanup_close_request_logical_size_address=transport_cleanup_close_request_logical_size_address,
        transport_cleanup_close_request_alignment_address=transport_cleanup_close_request_alignment_address,
        transport_cleanup_close_request_value_address=transport_cleanup_close_request_value_address,
        transport_cleanup_close_request_bytes_address=transport_cleanup_close_request_bytes_address,
        transport_cleanup_close_request_bytes_size=transport_cleanup_close_request_bytes_size,
        transport_cleanup_close_pre_call_args_address=transport_cleanup_close_pre_call_args_address,
        transport_cleanup_close_pre_call_args_size=transport_cleanup_close_pre_call_args_size,
        transport_bound_flag_address=transport_bound_flag_address,
        transport_bound_address_address=transport_bound_address_address,
        transport_socket_closed_after_bind_failure_address=transport_socket_closed_after_bind_failure_address,
        transport_socket_leak_detected_address=transport_socket_leak_detected_address,
        cache_range_start=cache_range_start,
        cache_range_size=cache_range_size,
    )


def _write_runtime_blob_object(*, toolchain: Any, output_dir: Path) -> None:
    _run(
        [
            os.fspath(toolchain.objcopy_path),
            "-I",
            "binary",
            "-O",
            "elf32-powerpc",
            "-B",
            "powerpc",
            "runtime_blob.bin",
            "runtime_blob.o",
        ],
        cwd=output_dir,
    )


def _bootstrap_status_value(payload_mode: str) -> int:
    if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT:
        return BOOTSTRAP_HALT_STATUS_VALUE
    if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_CONTINUE:
        return BOOTSTRAP_CONTINUE_STATUS_VALUE
    if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT:
        return RELOCATED_COPY_HALT_STATUS_VALUE
    if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT:
        return RELOCATED_RETURN_HALT_STATUS_VALUE
    if payload_mode == PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE:
        return RELOCATED_CONTINUE_STATUS_VALUE
    raise RuntimeError(f"Unsupported bootstrap payload mode {payload_mode!r}.")


def _run(command: list[str], *, allow_failure: bool = False, cwd: Path | None = None) -> str:
    result = subprocess.run(command, capture_output=True, text=True, check=False, cwd=cwd)
    if result.returncode != 0 and not allow_failure:
        raise RuntimeError(
            f"Command failed with exit code {result.returncode}: {' '.join(command)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return (result.stdout or result.stderr).strip()


def _validate_readelf_header(output: str) -> None:
    required_lines = (
        "Class:                             ELF32",
        "Data:                              2's complement, big endian",
        "Type:                              EXEC (Executable file)",
        "Machine:                           PowerPC",
    )
    for line in required_lines:
        if line not in output:
            raise RuntimeError(f"Built payload ELF is missing expected header line: {line!r}")


def _extract_entry_offset(symbol_output: str, entry_symbol: str, *, symbol_base: int = 0) -> int:
    return _normalize_symbol_value(_extract_symbol_address(symbol_output, entry_symbol), symbol_base=symbol_base)


def _extract_symbol_address(symbol_output: str, symbol_name: str) -> int:
    for line in symbol_output.splitlines():
        if line.strip().endswith(f" {symbol_name}"):
            return int(line.split()[1], 16)
    raise RuntimeError(f"Unable to locate symbol {symbol_name!r} in readelf symbol output.")


def _extract_optional_symbol_address(symbol_output: str, symbol_name: str) -> int | None:
    for line in symbol_output.splitlines():
        if line.strip().endswith(f" {symbol_name}"):
            return int(line.split()[1], 16)
    return None


def _extract_symbol_size(symbol_output: str, symbol_name: str) -> int:
    for line in symbol_output.splitlines():
        if line.strip().endswith(f" {symbol_name}"):
            columns = line.split()
            if len(columns) < 3:
                break
            return int(columns[2], 10)
    raise RuntimeError(f"Unable to locate size for symbol {symbol_name!r} in readelf symbol output.")


def _extract_optional_symbol_offset(symbol_output: str, symbol_name: str, *, symbol_base: int = 0) -> int | None:
    for line in symbol_output.splitlines():
        if line.strip().endswith(f" {symbol_name}"):
            return _normalize_symbol_value(int(line.split()[1], 16), symbol_base=symbol_base)
    return None


def _normalize_symbol_value(value: int, *, symbol_base: int) -> int:
    if value < symbol_base:
        raise RuntimeError(f"Symbol value 0x{value:08x} is below the expected base 0x{symbol_base:08x}.")
    return value - symbol_base


def _count_relocations(relocation_output: str) -> int:
    count = 0
    for line in relocation_output.splitlines():
        stripped = line.strip()
        if stripped.startswith(("Offset", "There are no relocations")):
            continue
        if stripped and stripped[0] in "0123456789abcdefABCDEF":
            count += 1
    return count


def _validate_forbidden_renderer_references(symbol_output: str, relocation_output: str) -> None:
    combined_output = f"{symbol_output}\n{relocation_output}".lower()
    present = tuple(fragment for fragment in FORBIDDEN_RENDERER_SYMBOL_FRAGMENTS if fragment in combined_output)
    if present:
        raise RuntimeError(f"Relocated runtime contains forbidden renderer references: {', '.join(present)}.")


def _count_dynamic_sections(dynamic_output: str) -> int:
    if not dynamic_output or "There is no dynamic section in this file." in dynamic_output:
        return 0
    count = 0
    for line in dynamic_output.splitlines():
        stripped = line.strip()
        if stripped.startswith(("Tag", "Dynamic section at offset")):
            continue
        if stripped.startswith("0x"):
            count += 1
    return count


def _parse_objdump_functions(disassembly_output: str) -> dict[str, list[tuple[int, str, str]]]:
    functions: dict[str, list[tuple[int, str, str]]] = {}
    current_name: str | None = None
    for line in disassembly_output.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.endswith(">:") and "<" in stripped:
            name = stripped.split("<", 1)[1].split(">", 1)[0]
            current_name = name
            functions[current_name] = []
            continue
        if current_name is None or ":" not in stripped:
            continue
        address_text, rest = stripped.split(":", 1)
        try:
            address = int(address_text, 16)
        except ValueError:
            continue
        columns = rest.strip().split("\t")
        if len(columns) < 2:
            continue
        mnemonic_text = columns[-1].strip()
        if not mnemonic_text:
            continue
        mnemonic_parts = mnemonic_text.split(None, 1)
        mnemonic = mnemonic_parts[0]
        operands = mnemonic_parts[1] if len(mnemonic_parts) > 1 else ""
        functions[current_name].append((address, mnemonic, operands))
    return functions


def _find_instruction_index(
    instructions: list[tuple[int, str, str]],
    mnemonic: str,
    *,
    start: int = 0,
) -> int:
    for index in range(start, len(instructions)):
        if instructions[index][1] == mnemonic:
            return index
    raise RuntimeError(f"Unable to locate {mnemonic!r} in generated disassembly.")


def _validate_retail_call_veneer_instructions(  # noqa: C901
    *,
    veneer_name: str,
    instructions: list[tuple[int, str, str]],
    expected_target: int,
) -> None:
    argument_registers = {f"r{index}" for index in range(3, 11)}

    def _normalized_operands(operands: str) -> list[str]:
        return [item.strip().lower() for item in operands.split(",") if item.strip()]

    def _written_register(mnemonic: str, operands: str) -> str | None:
        normalized = _normalized_operands(operands)
        if not normalized:
            return None
        if mnemonic in {"mr", "addi", "addis", "ori", "oris", "lwz", "li", "lis", "lbz", "lha", "lhz", "slwi"}:
            return normalized[0]
        return None

    if not instructions:
        raise RuntimeError(f"Generated disassembly for {veneer_name} is empty.")
    frame_mnemonic = instructions[0][1]
    frame_operands = instructions[0][2]
    if frame_mnemonic != "stwu" or not frame_operands.replace(" ", "").startswith("r1,-"):
        raise RuntimeError(f"{veneer_name} must begin with an ABI stack frame save before calling the retail target.")
    try:
        frame_size = abs(int(frame_operands.split(",", 1)[1].split("(", 1)[0], 0))
    except (IndexError, ValueError) as exc:
        raise RuntimeError(f"{veneer_name} stack frame could not be decoded from {frame_operands!r}.") from exc
    if frame_size < 0x20 or frame_size % 0x10 != 0:
        raise RuntimeError(f"{veneer_name} must allocate an ABI-aligned frame of at least 0x20 bytes.")
    mflr_index = _find_instruction_index(instructions, "mflr")
    lr_store_index = _find_instruction_index(instructions, "stw", start=mflr_index + 1)
    mtctr_index = _find_instruction_index(instructions, "mtctr")
    bctrl_index = _find_instruction_index(instructions, "bctrl", start=mtctr_index + 1)
    if not (mflr_index < lr_store_index < mtctr_index < bctrl_index):
        raise RuntimeError(f"{veneer_name} must save LR before its CTR call sequence.")
    lis_index = -1
    ori_index = -1
    for index in range(mtctr_index - 1, -1, -1):
        if instructions[index][1] == "ori":
            ori_index = index
            break
    for index in range(ori_index - 1, -1, -1):
        if instructions[index][1] == "lis":
            lis_index = index
            break
    if lis_index < 0 or ori_index < 0:
        raise RuntimeError(f"{veneer_name} is missing the expected lis/ori target load sequence.")
    lis_operands = [item.strip() for item in instructions[lis_index][2].split(",")]
    ori_operands = [item.strip() for item in instructions[ori_index][2].split(",")]
    if len(lis_operands) < 2 or len(ori_operands) < 3:
        raise RuntimeError(f"{veneer_name} is missing the expected lis/ori target load sequence.")
    lis_target = lis_operands[0].lower()
    ori_target = ori_operands[0].lower()
    ori_source = ori_operands[1].lower()
    if lis_target != ori_target or lis_target != ori_source:
        raise RuntimeError(f"{veneer_name} must keep the retail target load in one scratch register.")
    if lis_target in argument_registers:
        raise RuntimeError(f"{veneer_name} must not use argument register {lis_target} for the retail target address.")
    mtctr_operands = _normalized_operands(instructions[mtctr_index][2])
    if not mtctr_operands or mtctr_operands[0] != lis_target:
        raise RuntimeError(f"{veneer_name} must transfer CTR from the loaded retail target register.")
    loaded_hi = int(lis_operands[1], 0) & 0xFFFF
    loaded_lo = int(ori_operands[2], 0) & 0xFFFF
    loaded_target = (loaded_hi << 16) | loaded_lo
    if loaded_target != expected_target:
        raise RuntimeError(f"{veneer_name} loads 0x{loaded_target:08X}, expected 0x{expected_target:08X}.")
    for _, mnemonic, operands in instructions[:bctrl_index]:
        written_register = _written_register(mnemonic, operands)
        if written_register in argument_registers:
            raise RuntimeError(
                f"{veneer_name} clobbers {written_register} before bctrl; "
                "retail argument registers must reach the target unchanged."
            )
    target_return_index = _find_instruction_index(instructions, "lwz", start=bctrl_index + 1)
    mtlr_index = _find_instruction_index(instructions, "mtlr", start=bctrl_index + 1)
    blr_index = _find_instruction_index(instructions, "blr", start=mtlr_index + 1)
    stack_restore_index = -1
    for index in range(blr_index - 1, mtlr_index, -1):
        mnemonic, operands = instructions[index][1], instructions[index][2].replace(" ", "").lower()
        if mnemonic == "addi" and operands.startswith("r1,r1,"):
            stack_restore_index = index
            break
    if stack_restore_index < 0:
        raise RuntimeError(f"{veneer_name} must restore the full veneer frame before blr.")
    if not (bctrl_index < target_return_index < mtlr_index < stack_restore_index < blr_index):
        raise RuntimeError(f"{veneer_name} must restore LR and stack after the retail target returns.")
    restore_r2 = any(
        mnemonic == "lwz" and operands.replace(" ", "").startswith("r2,")
        for _, mnemonic, operands in instructions[bctrl_index + 1 : blr_index]
    )
    restore_r13 = any(
        mnemonic == "lwz" and operands.replace(" ", "").startswith("r13,")
        for _, mnemonic, operands in instructions[bctrl_index + 1 : blr_index]
    )
    if not restore_r2 or not restore_r13:
        raise RuntimeError(f"{veneer_name} must restore both r2 and r13 after the retail target returns.")


def _validate_retail_call_veneer_disassembly(
    *,
    objdump_output: str,
    symbol_output: str,
    wrapper_metadata: Prime3RetailIosWrapperMetadata,
) -> None:
    functions = _parse_objdump_functions(objdump_output)
    selftest_target_address = _extract_symbol_address(symbol_output, RUNTIME_RETAIL_VENEER_SELFTEST_TARGET_SYMBOL)
    veneer_targets = {
        RUNTIME_RETAIL_IOS_OPEN_VENEER_SYMBOL: wrapper_metadata.open_async_address,
        RUNTIME_RETAIL_IOS_CLOSE_VENEER_SYMBOL: wrapper_metadata.close_async_address,
        RUNTIME_RETAIL_READ_ASYNC_VENEER_SYMBOL: wrapper_metadata.read_async_address,
        RUNTIME_RETAIL_WRITE_ASYNC_VENEER_SYMBOL: wrapper_metadata.write_async_address,
        RUNTIME_RETAIL_IOS_IOCTL_ASYNC_VENEER_SYMBOL: wrapper_metadata.confirmed_ioctl_async_address,
        RUNTIME_RETAIL_IOS_IOCTLV_ASYNC_VENEER_SYMBOL: wrapper_metadata.confirmed_ioctlv_async_address,
        RUNTIME_RETAIL_NWC24_OPEN_LIB_VENEER_SYMBOL: PRIME3_NTSC_NWC24_OPEN_LIB_ADDRESS,
        RUNTIME_RETAIL_NETWORK_BOOTSTRAP_VENEER_SYMBOL: PRIME3_NTSC_NETWORK_BOOTSTRAP_ADDRESS,
        RUNTIME_RETAIL_VENEER_SELFTEST_SYMBOL: selftest_target_address,
    }
    for veneer_name, expected_target in veneer_targets.items():
        instructions = functions.get(veneer_name)
        if instructions is None:
            raise RuntimeError(f"Generated disassembly is missing veneer symbol {veneer_name}.")
        _validate_retail_call_veneer_instructions(
            veneer_name=veneer_name,
            instructions=instructions,
            expected_target=expected_target,
        )
    selftest_caller = functions.get(RUNTIME_RETAIL_VENEER_SELFTEST_CALLER_SYMBOL)
    if selftest_caller is None:
        raise RuntimeError("Generated disassembly is missing the retained veneer self-test caller.")
    bl_index = _find_instruction_index(selftest_caller, "bl")
    blr_index = _find_instruction_index(selftest_caller, "blr", start=bl_index + 1)
    if blr_index <= bl_index + 1:
        raise RuntimeError("Retained veneer self-test caller does not execute a visible post-call continuation.")


def main() -> None:  # noqa: C901
    args = parse_args()
    selected_modes = [
        args.probe,
        args.bootstrap_halt,
        args.bootstrap_continue,
        args.relocated_copy_halt,
        args.relocated_return_halt,
        args.relocated_continue,
    ]
    if sum(1 for selected in selected_modes if selected) > 1:
        raise RuntimeError("Use only one payload mode flag at a time.")
    if args.probe:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_PROBE
    elif args.bootstrap_halt:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT
    elif args.bootstrap_continue:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_CONTINUE
    elif args.relocated_copy_halt:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT
    elif args.relocated_return_halt:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT
    elif args.relocated_continue:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE
    else:
        payload_mode = PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL

    if args.ios_open_kd_once:
        raise RuntimeError(
            "--ios-open-kd-once is the failed direct-submit experiment and is no longer selectable; "
            "use --ios-open-via-retail-wrapper-once."
        )
    if (
        sum(
            1
            for selected in (
                args.ios_udp_dry_run,
                args.ios_open_via_retail_wrapper_once,
                args.ios_nwc24_once,
                args.ios_nwc24_via_retail_ioctl_once,
                args.ios_close_kd_once,
                args.ios_open_ip_once,
                args.ios_so_startup_once,
                args.ios_startup_once,
                args.ios_get_host_id_once,
                args.ios_create_socket_once,
                args.ios_bind_once,
                args.ios_recvfrom_once,
                args.ios_recv_send_once,
                args.ios_recv_send_loop,
                args.ios_cp3w_frame_validation,
                args.ios_cp3w_ping_pong,
                args.ios_cp3w_hello_session,
                args.ios_cp3w_game_identity,
                args.ios_cp3w_inventory,
                args.ios_ioctl_async_abi_probe,
                args.enable_ios_udp_diagnostic_init,
            )
            if selected
        )
        > 1
    ):
        raise RuntimeError("Use at most one IOS UDP diagnostic sub-mode flag at a time.")
    if args.ios_recv_send_loop_count < 1 or args.ios_recv_send_loop_count > 100:
        raise RuntimeError("--ios-recv-send-loop-count must be between 1 and 100.")
    if _argument_was_supplied("--ios-recv-send-loop-count") and not args.ios_recv_send_loop:
        raise RuntimeError("--ios-recv-send-loop-count requires --ios-recv-send-loop.")
    if args.ios_cp3w_frame_validation_count < 1 or args.ios_cp3w_frame_validation_count > 100:
        raise RuntimeError("--ios-cp3w-frame-validation-count must be between 1 and 100.")
    if _argument_was_supplied("--ios-cp3w-frame-validation-count") and not args.ios_cp3w_frame_validation:
        raise RuntimeError("--ios-cp3w-frame-validation-count requires --ios-cp3w-frame-validation.")
    if args.ios_cp3w_ping_pong_count < 1 or args.ios_cp3w_ping_pong_count > 100:
        raise RuntimeError("--ios-cp3w-ping-pong-count must be between 1 and 100.")
    if _argument_was_supplied("--ios-cp3w-ping-pong-count") and not args.ios_cp3w_ping_pong:
        raise RuntimeError("--ios-cp3w-ping-pong-count requires --ios-cp3w-ping-pong.")
    if args.ios_cp3w_hello_session_count < 1 or args.ios_cp3w_hello_session_count > 100:
        raise RuntimeError("--ios-cp3w-hello-session-count must be between 1 and 100.")
    if _argument_was_supplied("--ios-cp3w-hello-session-count") and not args.ios_cp3w_hello_session:
        raise RuntimeError("--ios-cp3w-hello-session-count requires --ios-cp3w-hello-session.")
    if args.ios_cp3w_game_identity_count < 1 or args.ios_cp3w_game_identity_count > 100:
        raise RuntimeError("--ios-cp3w-game-identity-count must be between 1 and 100.")
    if _argument_was_supplied("--ios-cp3w-game-identity-count") and not args.ios_cp3w_game_identity:
        raise RuntimeError("--ios-cp3w-game-identity-count requires --ios-cp3w-game-identity.")
    if args.ios_cp3w_inventory_count < 1 or args.ios_cp3w_inventory_count > 100:
        raise RuntimeError("--ios-cp3w-inventory-count must be between 1 and 100.")
    if _argument_was_supplied("--ios-cp3w-inventory-count") and not args.ios_cp3w_inventory:
        raise RuntimeError("--ios-cp3w-inventory-count requires --ios-cp3w-inventory.")
    ios_udp_mode = "normal"
    if args.ios_udp_dry_run:
        ios_udp_mode = "dry_run"
    elif args.ios_open_via_retail_wrapper_once:
        ios_udp_mode = "retail_wrapper_open_kd_once"
    elif args.ios_nwc24_once or args.ios_nwc24_via_retail_ioctl_once:
        ios_udp_mode = "retail_wrapper_nwc24_startup_once"
    elif args.ios_close_kd_once:
        ios_udp_mode = "retail_wrapper_nwc24_close_kd_once"
    elif args.ios_open_ip_once:
        ios_udp_mode = "retail_wrapper_nwc24_close_open_ip_once"
    elif args.ios_so_startup_once:
        ios_udp_mode = "retail_wrapper_nwc24_close_open_ip_startup_once"
    elif args.ios_startup_once:
        ios_udp_mode = "retail_wrapper_startup_once"
    elif args.ios_get_host_id_once:
        ios_udp_mode = "retail_wrapper_get_host_id_once"
    elif args.ios_create_socket_once:
        ios_udp_mode = "retail_wrapper_create_socket_once"
    elif args.ios_recvfrom_once:
        ios_udp_mode = "retail_wrapper_recvfrom_once"
    elif args.ios_recv_send_once:
        ios_udp_mode = "retail_wrapper_recv_send_once"
    elif args.ios_recv_send_loop:
        ios_udp_mode = "retail_wrapper_recv_send_loop"
    elif args.ios_cp3w_frame_validation:
        ios_udp_mode = "cp3w_frame_validation"
    elif args.ios_cp3w_ping_pong:
        ios_udp_mode = "cp3w_ping_pong"
    elif args.ios_cp3w_hello_session:
        ios_udp_mode = "cp3w_hello_session"
    elif args.ios_cp3w_game_identity:
        ios_udp_mode = "cp3w_game_identity"
    elif args.ios_cp3w_inventory:
        ios_udp_mode = "cp3w_inventory"
    elif args.ios_ioctl_async_abi_probe:
        ios_udp_mode = "retail_wrapper_ioctl_async_abi_probe"
    elif args.ios_bind_once or args.enable_ios_udp_diagnostic_init:
        ios_udp_mode = "retail_wrapper_bind_once" if args.ios_bind_once else "normal"

    reserved_high = None if args.reserved_high is None else int(args.reserved_high, 0)
    diagnostic_address = None if args.diagnostic_address is None else int(args.diagnostic_address, 0)
    runtime_destination = None if args.runtime_destination is None else int(args.runtime_destination, 0)
    enable_ios_udp_diagnostic = (
        args.enable_ios_udp_diagnostic or args.enable_ios_udp_diagnostic_init or ios_udp_mode != "normal"
    )
    if enable_ios_udp_diagnostic and payload_mode != PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE:
        raise RuntimeError("--enable-ios-udp-diagnostic requires --relocated-continue.")
    if payload_mode in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES:
        if reserved_high is None or diagnostic_address is None:
            raise RuntimeError("Bootstrap payload modes require --reserved-high and --diagnostic-address.")
    build_prime3_runtime_payload(
        Path(args.output_dir),
        payload_mode=payload_mode,
        enable_recurring_hook_diagnostics=args.enable_recurring_hook_diagnostics,
        enable_ios_udp_diagnostic=enable_ios_udp_diagnostic,
        ios_udp_mode=ios_udp_mode,
        ios_udp_loop_count=(
            args.ios_cp3w_frame_validation_count
            if args.ios_cp3w_frame_validation
            else args.ios_cp3w_ping_pong_count
            if args.ios_cp3w_ping_pong
            else args.ios_cp3w_hello_session_count
            if args.ios_cp3w_hello_session
            else args.ios_cp3w_game_identity_count
            if args.ios_cp3w_game_identity
            else args.ios_cp3w_inventory_count
            if args.ios_cp3w_inventory
            else args.ios_recv_send_loop_count
        ),
        reserved_high=reserved_high,
        diagnostic_address=diagnostic_address,
        runtime_destination=runtime_destination,
    )


if __name__ == "__main__":
    main()
