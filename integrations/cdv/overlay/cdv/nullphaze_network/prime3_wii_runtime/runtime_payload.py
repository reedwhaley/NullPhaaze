# Payload construction binds addresses, code sections, cache ranges and transport metadata
# to the supported executable. A parsed metadata record cannot substitute for the guarded
# retail preimage checks. Boundary names here: compute_cache_range,
# Prime3EntryBootstrapMetadata, Prime3RuntimeGameIdentityMetadata,
# Prime3RuntimeInventoryMetadata, LegacyPrime3RuntimeTransportMetadata.
from __future__ import annotations

import dataclasses
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING

from randovania.games.prime3.exporter.dol_patcher import Prime3DolPatchError, Prime3PayloadArtifact

if TYPE_CHECKING:
    from collections.abc import Iterable

PRIME3_RUNTIME_PAYLOAD_SCHEMA_VERSION = 3
PROTOCOL_VERSION = 1
PRIME3_RUNTIME_TARGET_ARCHITECTURE = "powerpc"
PRIME3_RUNTIME_TARGET_ENDIANNESS = "big"
PRIME3_RUNTIME_TARGET_ABI = "eabi"
PRIME3_RUNTIME_REQUIRED_ALIGNMENT = 0x20
PRIME3_RUNTIME_ENTRY_SYMBOL = "payload_entry"
PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL = "normal"
PRIME3_RUNTIME_PAYLOAD_MODE_PROBE = "probe"
PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT = "entry_bootstrap_halt"
PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_CONTINUE = "entry_bootstrap_continue"
PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT = "relocated_copy_halt"
PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT = "relocated_return_halt"
PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE = "relocated_continue"
PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES = (
    PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_CONTINUE,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE,
)
PRIME3_RUNTIME_RELOCATED_MODES = (
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE,
)
PRIME3_RUNTIME_HALT_MODES = (
    PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_COPY_HALT,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_RETURN_HALT,
)
PRIME3_RUNTIME_CONTINUE_MODES = (
    PRIME3_RUNTIME_PAYLOAD_MODE_ENTRY_BOOTSTRAP_CONTINUE,
    PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE,
)


def compute_cache_range(*, address: int, size: int, cache_line_size: int) -> tuple[int, int]:
    if cache_line_size <= 0 or cache_line_size & (cache_line_size - 1) != 0:
        raise Prime3DolPatchError(f"Cache line size must be a positive power of two, got {cache_line_size}.")
    if address < 0:
        raise Prime3DolPatchError(f"Cache range address must be non-negative, got {address}.")
    if size <= 0:
        raise Prime3DolPatchError(f"Cache range size must be positive, got {size}.")
    try:
        end = address + size
    except OverflowError as exc:
        raise Prime3DolPatchError("Cache range overflowed the integer address space.") from exc
    if end <= address:
        raise Prime3DolPatchError("Cache range end must be above the start address.")
    aligned_start = address & ~(cache_line_size - 1)
    aligned_end = (end + cache_line_size - 1) & ~(cache_line_size - 1)
    if aligned_end <= aligned_start:
        raise Prime3DolPatchError("Cache-aligned range must be non-empty.")
    return aligned_start, aligned_end - aligned_start


@dataclasses.dataclass(frozen=True)
class Prime3EntryBootstrapMetadata:
    mode: str
    staging_address: int
    staging_save_area_offset: int
    staging_save_area_size: int
    halt_loop_address: int | None
    reserved_boundary: int
    reserved_range_start: int
    reserved_range_end: int
    diagnostic_address: int
    diagnostic_block_size: int
    canary_address: int
    canary_size: int
    canary_sha256: str
    marker_address: int
    marker_value: int
    counter_address: int
    counter_size: int
    original_80000034_address: int
    original_80003110_address: int
    replacement_value_address: int
    replacement_value: int
    status_address: int
    status_value: int
    original_entry_instruction: int
    original_branch_target: int
    original_continuation_address: int

    def validate(self, *, payload_size: int) -> None:
        if self.mode not in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES:
            raise Prime3DolPatchError(f"Unsupported Prime 3 entry bootstrap mode {self.mode!r}.")
        _validate_optional_range(
            payload_size=payload_size,
            field_name="staging_save_area_offset",
            start=self.staging_save_area_offset,
            size=self.staging_save_area_size,
        )
        if self.halt_loop_address is not None and not (
            self.staging_address <= self.halt_loop_address < self.staging_address + payload_size
        ):
            raise Prime3DolPatchError("Entry bootstrap halt loop address is outside the staged payload range.")
        if self.mode in PRIME3_RUNTIME_HALT_MODES and self.halt_loop_address is None:
            raise Prime3DolPatchError("Entry bootstrap halt modes require a halt loop address.")
        if self.mode in PRIME3_RUNTIME_CONTINUE_MODES and self.halt_loop_address is not None:
            raise Prime3DolPatchError("Entry bootstrap continue modes must not define a halt loop address.")
        if self.reserved_range_start != self.reserved_boundary:
            raise Prime3DolPatchError("Entry bootstrap reserved range must start at the reserved boundary.")
        if self.reserved_range_end <= self.reserved_range_start:
            raise Prime3DolPatchError("Entry bootstrap reserved range end must be above the reserved range start.")
        if not (self.reserved_range_start <= self.diagnostic_address < self.reserved_range_end):
            raise Prime3DolPatchError("Entry bootstrap diagnostic block address is outside the reserved range.")
        if self.diagnostic_address + self.diagnostic_block_size > self.reserved_range_end:
            raise Prime3DolPatchError("Entry bootstrap diagnostic block exceeds the reserved range.")

        occupied_ranges = (
            ("canary", self.canary_address, self.canary_size),
            ("marker", self.marker_address, 4),
            ("counter", self.counter_address, self.counter_size),
            ("original_80000034", self.original_80000034_address, 4),
            ("original_80003110", self.original_80003110_address, 4),
            ("replacement_value", self.replacement_value_address, 4),
            ("status", self.status_address, 4),
        )
        for name, start, size in occupied_ranges:
            if not (self.reserved_range_start <= start < self.reserved_range_end):
                raise Prime3DolPatchError(f"Entry bootstrap field {name} is outside the reserved range.")
            if start + size > self.reserved_range_end:
                raise Prime3DolPatchError(f"Entry bootstrap field {name} exceeds the reserved range.")
        _validate_non_overlapping_ranges(tuple((name, start, size) for name, start, size in occupied_ranges))

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object], *, payload_size: int) -> Prime3EntryBootstrapMetadata:
        metadata = cls(
            mode=_json_string(data, "mode"),
            staging_address=_json_int(data, "staging_address"),
            staging_save_area_offset=_json_int(data, "staging_save_area_offset"),
            staging_save_area_size=_json_int(data, "staging_save_area_size"),
            halt_loop_address=_json_optional_int(data, "halt_loop_address"),
            reserved_boundary=_json_int(data, "reserved_boundary"),
            reserved_range_start=_json_int(data, "reserved_range_start"),
            reserved_range_end=_json_int(data, "reserved_range_end"),
            diagnostic_address=_json_int(data, "diagnostic_address"),
            diagnostic_block_size=_json_int(data, "diagnostic_block_size"),
            canary_address=_json_int(data, "canary_address"),
            canary_size=_json_int(data, "canary_size"),
            canary_sha256=_json_string(data, "canary_sha256"),
            marker_address=_json_int(data, "marker_address"),
            marker_value=_json_int(data, "marker_value"),
            counter_address=_json_int(data, "counter_address"),
            counter_size=_json_int(data, "counter_size"),
            original_80000034_address=_json_int(data, "original_80000034_address"),
            original_80003110_address=_json_int(data, "original_80003110_address"),
            replacement_value_address=_json_int(data, "replacement_value_address"),
            replacement_value=_json_int(data, "replacement_value"),
            status_address=_json_int(data, "status_address"),
            status_value=_json_int(data, "status_value"),
            original_entry_instruction=_json_int(data, "original_entry_instruction"),
            original_branch_target=_json_int(data, "original_branch_target"),
            original_continuation_address=_json_int(data, "original_continuation_address"),
        )
        metadata.validate(payload_size=payload_size)
        return metadata


@dataclasses.dataclass(frozen=True)
class Prime3RuntimeGameIdentityMetadata:
    mode_value: int
    mode_name: str
    command_value: int
    capability_value: int
    schema_version: int
    payload_size: int
    field_offsets: dict[str, int]
    game_id: int
    platform_id: int
    region_id: int
    revision_id: int
    profile_id: int
    profile_fingerprint: int
    fingerprint_derivation: str
    runtime_build_id: int
    availability_flags: dict[str, int]
    phase_names: dict[str, int]
    configured_count: int
    state_addresses: dict[str, int]

    def validate(self, *, runtime_state_start: int, runtime_state_end: int) -> tuple[tuple[str, int, int], ...]:
        if self.mode_value != 20 or self.mode_name != "cp3w_game_identity":
            raise Prime3DolPatchError("CP3W game identity metadata must use diagnostic mode 20.")
        if self.command_value != 5 or self.capability_value != 1 << 11:
            raise Prime3DolPatchError("CP3W game identity command or capability metadata is invalid.")
        if self.schema_version != 1 or self.payload_size != 28:
            raise Prime3DolPatchError("CP3W game identity schema metadata is invalid.")
        if self.configured_count < 0 or self.configured_count > 100:
            raise Prime3DolPatchError("CP3W game identity configured count must be between 0 and 100.")
        if self.field_offsets.get("reserved") != 24 or self.phase_names.get("LOOP_COMPLETE") != 79:
            raise Prime3DolPatchError("CP3W game identity layout or terminal phase metadata is invalid.")
        ranges = tuple((name, address, 4) for name, address in self.state_addresses.items())
        for name, address, size in ranges:
            if not (runtime_state_start <= address < runtime_state_end) or address + size > runtime_state_end:
                raise Prime3DolPatchError(f"CP3W game identity state field {name} is outside runtime state.")
        _validate_non_overlapping_ranges(ranges)
        return ranges

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RuntimeGameIdentityMetadata:
        metadata = cls(
            mode_value=_json_int(data, "mode_value"),
            mode_name=_json_string(data, "mode_name"),
            command_value=_json_int(data, "command_value"),
            capability_value=_json_int(data, "capability_value"),
            schema_version=_json_int(data, "schema_version"),
            payload_size=_json_int(data, "payload_size"),
            field_offsets=_json_int_dict(data, "field_offsets"),
            game_id=_json_int(data, "game_id"),
            platform_id=_json_int(data, "platform_id"),
            region_id=_json_int(data, "region_id"),
            revision_id=_json_int(data, "revision_id"),
            profile_id=_json_int(data, "profile_id"),
            profile_fingerprint=_json_int(data, "profile_fingerprint"),
            fingerprint_derivation=_json_string(data, "fingerprint_derivation"),
            runtime_build_id=_json_int(data, "runtime_build_id"),
            availability_flags=_json_int_dict(data, "availability_flags"),
            phase_names=_json_int_dict(data, "phase_names"),
            configured_count=_json_int(data, "configured_count"),
            state_addresses=_json_int_dict(data, "state_addresses"),
        )
        return metadata


@dataclasses.dataclass(frozen=True)
class Prime3RuntimeInventoryMetadata:
    mode_value: int
    mode_name: str
    command_value: int
    capability_value: int
    schema_version: int
    item_ids: list[int]
    header_size: int
    record_size: int
    payload_size: int
    frame_size: int
    field_offsets: dict[str, int]
    availability_flags: dict[str, int]
    phase_names: dict[str, int]
    configured_count: int
    send_buffer_size: int
    ping_payload_limit: int
    state_addresses: dict[str, int]

    def validate(self, *, runtime_state_start: int, runtime_state_end: int) -> tuple[tuple[str, int, int], ...]:
        valid_modes = {(21, "cp3w_inventory"), (22, "cp3w_inventory_service")}
        if (self.mode_value, self.mode_name) not in valid_modes:
            raise Prime3DolPatchError("CP3W inventory metadata must use mode 21 or production service mode 22.")
        if self.command_value != 6 or self.capability_value != 1 << 12:
            raise Prime3DolPatchError("CP3W inventory command or capability metadata is invalid.")
        if self.schema_version != 1 or len(self.item_ids) != 59 or len(set(self.item_ids)) != 59:
            raise Prime3DolPatchError("CP3W inventory schema or item ordering metadata is invalid.")
        if self.header_size != 12 or self.record_size != 8 or self.payload_size != 484 or self.frame_size != 504:
            raise Prime3DolPatchError("CP3W inventory payload sizing metadata is invalid.")
        if self.send_buffer_size < self.frame_size or self.ping_payload_limit != 44:
            raise Prime3DolPatchError("CP3W inventory send capacity or retained PING limit is invalid.")
        if self.mode_value == 22 and self.configured_count != 0:
            raise Prime3DolPatchError("CP3W inventory service metadata must use an unbounded count of zero.")
        if self.mode_value == 21 and not 1 <= self.configured_count <= 100:
            raise Prime3DolPatchError("CP3W inventory diagnostic count must be between 1 and 100.")
        if self.field_offsets.get("records") != 12 or self.phase_names.get("LOOP_COMPLETE") != 93:
            raise Prime3DolPatchError("CP3W inventory layout or terminal phase metadata is invalid.")
        ranges = tuple((name, address, 4) for name, address in self.state_addresses.items())
        for name, address, size in ranges:
            if not (runtime_state_start <= address < runtime_state_end) or address + size > runtime_state_end:
                raise Prime3DolPatchError(f"CP3W inventory state field {name} is outside runtime state.")
        _validate_non_overlapping_ranges(ranges)
        return ranges

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RuntimeInventoryMetadata:
        return cls(
            mode_value=_json_int(data, "mode_value"),
            mode_name=_json_string(data, "mode_name"),
            command_value=_json_int(data, "command_value"),
            capability_value=_json_int(data, "capability_value"),
            schema_version=_json_int(data, "schema_version"),
            item_ids=_json_int_list(data, "item_ids"),
            header_size=_json_int(data, "header_size"),
            record_size=_json_int(data, "record_size"),
            payload_size=_json_int(data, "payload_size"),
            frame_size=_json_int(data, "frame_size"),
            field_offsets=_json_int_dict(data, "field_offsets"),
            availability_flags=_json_int_dict(data, "availability_flags"),
            phase_names=_json_int_dict(data, "phase_names"),
            configured_count=_json_int(data, "configured_count"),
            send_buffer_size=_json_int(data, "send_buffer_size"),
            ping_payload_limit=_json_int(data, "ping_payload_limit"),
            state_addresses=_json_int_dict(data, "state_addresses"),
        )


@dataclasses.dataclass(frozen=True)
class LegacyPrime3RuntimeTransportMetadata:
    mode: str
    udp_port: int
    initialization_enabled: bool
    receive_enabled: bool
    send_enabled: bool
    nwc24_startup_enabled: bool
    kd_close_enabled: bool
    ip_close_on_success: bool
    socket_close_on_success: bool
    terminal_phase_value: int
    terminal_phase_name: str
    phase_address: int
    phase_size: int
    last_error_address: int
    last_error_size: int
    last_socket_error_address: int
    last_socket_error_size: int
    last_ios_result_address: int
    last_ios_result_size: int
    pending_operation_address: int
    pending_operation_size: int
    pending_generation_address: int
    pending_generation_size: int
    callback_generation_address: int
    callback_generation_size: int
    callback_count_address: int
    callback_count_size: int
    rejected_callback_count_address: int
    rejected_callback_count_size: int
    callback_pending_address: int
    callback_pending_size: int
    open_kd_submit_count_address: int
    open_kd_submit_count_size: int
    open_kd_callback_count_address: int
    open_kd_callback_count_size: int
    nwc24_output_buffer_address: int
    nwc24_output_buffer_size: int
    nwc24_output_buffer_alignment: int
    nwc24_submit_count_address: int
    nwc24_submit_count_size: int
    nwc24_callback_count_address: int
    nwc24_callback_count_size: int
    nwc24_synchronous_result_address: int
    nwc24_synchronous_result_size: int
    nwc24_callback_result_address: int
    nwc24_callback_result_size: int
    nwc24_output_digest_address: int
    nwc24_output_digest_size: int
    open_ip_submit_count_address: int
    open_ip_submit_count_size: int
    open_ip_callback_count_address: int
    open_ip_callback_count_size: int
    kd_close_submit_count_address: int
    kd_close_submit_count_size: int
    kd_close_callback_count_address: int
    kd_close_callback_count_size: int
    startup_submit_count_address: int
    startup_submit_count_size: int
    startup_callback_count_address: int
    startup_callback_count_size: int
    get_host_id_submit_count_address: int
    get_host_id_submit_count_size: int
    get_host_id_callback_count_address: int
    get_host_id_callback_count_size: int
    socket_submit_count_address: int
    socket_submit_count_size: int
    socket_callback_count_address: int
    socket_callback_count_size: int
    bind_submit_count_address: int
    bind_submit_count_size: int
    bind_callback_count_address: int
    bind_callback_count_size: int
    kd_fd_address: int
    kd_fd_size: int
    kd_closed_address: int
    kd_closed_size: int
    ip_fd_address: int
    ip_fd_size: int
    socket_fd_address: int
    socket_fd_size: int
    host_id_address: int
    host_id_size: int
    service_started_address: int | None
    service_started_size: int | None
    bound_port_address: int
    bound_port_size: int
    receive_submit_count_address: int
    receive_submit_count_size: int
    send_submit_count_address: int
    send_submit_count_size: int
    ip_close_submit_count_address: int
    ip_close_submit_count_size: int
    socket_close_submit_count_address: int
    socket_close_submit_count_size: int
    receive_count_address: int
    receive_count_size: int
    receive_bytes_address: int
    receive_bytes_size: int
    send_count_address: int
    send_count_size: int
    send_bytes_address: int
    send_bytes_size: int
    last_receive_length_address: int
    last_receive_length_size: int
    last_send_length_address: int
    last_send_length_size: int
    last_peer_ipv4_address: int
    last_peer_ipv4_size: int
    last_peer_port_address: int
    last_peer_port_size: int
    last_peer_family_address: int
    last_peer_family_size: int
    last_poll_action_address: int
    last_poll_action_size: int
    last_submit_result_address: int
    last_submit_result_size: int
    last_receive_preview_address: int
    last_receive_preview_size: int
    last_send_preview_address: int
    last_send_preview_size: int
    cp3w_magic_hex: str | None = None
    cp3w_protocol_version: int | None = None
    cp3w_header_size: int | None = None
    cp3w_crc_size: int | None = None
    cp3w_crc_initial_value: int | None = None
    cp3w_crc_final_xor_value: int | None = None
    cp3w_crc_polynomial: int | None = None
    cp3w_crc_reflected: bool | None = None
    cp3w_packet_kind_request: int | None = None
    cp3w_packet_kind_response: int | None = None
    cp3w_response_status_error: int | None = None
    cp3w_command_ping: int | None = None
    cp3w_pong_command: int | None = None
    cp3w_pong_uses_ping_command: bool | None = None
    cp3w_command_reserved_mailbox: int | None = None
    cp3w_error_code_unknown_command: int | None = None
    cp3w_packet_kind_offset: int | None = None
    cp3w_command_offset: int | None = None
    cp3w_response_status_offset: int | None = None
    cp3w_request_id_offset: int | None = None
    cp3w_payload_length_offset: int | None = None
    cp3w_ping_max_payload_length: int | None = None
    cp3w_request_payload_ascii: str | None = None
    cp3w_response_payload_ascii: str | None = None
    cp3w_unsupported_message_ascii: str | None = None
    cp3w_request_payload_length: int | None = None
    cp3w_response_payload_length: int | None = None
    prepared_send_length_address: int | None = None
    prepared_send_length_size: int | None = None
    cp3w_datagrams_processed_address: int | None = None
    cp3w_datagrams_processed_size: int | None = None
    cp3w_frames_valid_address: int | None = None
    cp3w_frames_valid_size: int | None = None
    cp3w_frames_invalid_address: int | None = None
    cp3w_frames_invalid_size: int | None = None
    cp3w_frames_too_short_address: int | None = None
    cp3w_frames_too_short_size: int | None = None
    cp3w_frames_invalid_magic_address: int | None = None
    cp3w_frames_invalid_magic_size: int | None = None
    cp3w_frames_invalid_version_address: int | None = None
    cp3w_frames_invalid_version_size: int | None = None
    cp3w_frames_unsupported_type_address: int | None = None
    cp3w_frames_unsupported_type_size: int | None = None
    cp3w_frames_nonzero_flags_address: int | None = None
    cp3w_frames_nonzero_flags_size: int | None = None
    cp3w_frames_length_mismatch_address: int | None = None
    cp3w_frames_length_mismatch_size: int | None = None
    cp3w_frames_payload_too_large_address: int | None = None
    cp3w_frames_payload_too_large_size: int | None = None
    cp3w_frames_invalid_payload_address: int | None = None
    cp3w_frames_invalid_payload_size: int | None = None
    cp3w_frames_malformed_address: int | None = None
    cp3w_frames_malformed_size: int | None = None
    cp3w_framed_responses_submitted_address: int | None = None
    cp3w_framed_responses_submitted_size: int | None = None
    cp3w_framed_responses_completed_address: int | None = None
    cp3w_framed_responses_completed_size: int | None = None
    cp3w_last_request_id_address: int | None = None
    cp3w_last_request_id_size: int | None = None
    cp3w_last_response_id_address: int | None = None
    cp3w_last_response_id_size: int | None = None
    cp3w_last_message_type_address: int | None = None
    cp3w_last_message_type_size: int | None = None
    cp3w_last_declared_payload_length_address: int | None = None
    cp3w_last_declared_payload_length_size: int | None = None
    cp3w_last_actual_payload_length_address: int | None = None
    cp3w_last_actual_payload_length_size: int | None = None
    cp3w_last_frame_result_address: int | None = None
    cp3w_last_frame_result_size: int | None = None
    cp3w_final_datagram_index_address: int | None = None
    cp3w_final_datagram_index_size: int | None = None
    cp3w_requests_dispatched_address: int | None = None
    cp3w_requests_dispatched_size: int | None = None
    cp3w_hello_requests_received_address: int | None = None
    cp3w_hello_requests_received_size: int | None = None
    cp3w_hello_successes_address: int | None = None
    cp3w_hello_successes_size: int | None = None
    cp3w_hello_version_rejections_address: int | None = None
    cp3w_hello_version_rejections_size: int | None = None
    cp3w_hello_responses_submitted_address: int | None = None
    cp3w_hello_responses_submitted_size: int | None = None
    cp3w_hello_responses_completed_address: int | None = None
    cp3w_hello_responses_completed_size: int | None = None
    cp3w_hello_duplicate_requests_address: int | None = None
    cp3w_hello_duplicate_requests_size: int | None = None
    cp3w_hello_renegotiation_rejections_address: int | None = None
    cp3w_hello_renegotiation_rejections_size: int | None = None
    cp3w_pre_hello_gated_commands_address: int | None = None
    cp3w_pre_hello_gated_commands_size: int | None = None
    cp3w_not_negotiated_responses_submitted_address: int | None = None
    cp3w_not_negotiated_responses_submitted_size: int | None = None
    cp3w_not_negotiated_responses_completed_address: int | None = None
    cp3w_not_negotiated_responses_completed_size: int | None = None
    cp3w_ping_requests_received_address: int | None = None
    cp3w_ping_requests_received_size: int | None = None
    cp3w_pong_responses_submitted_address: int | None = None
    cp3w_pong_responses_submitted_size: int | None = None
    cp3w_pong_responses_completed_address: int | None = None
    cp3w_pong_responses_completed_size: int | None = None
    cp3w_unsupported_commands_received_address: int | None = None
    cp3w_unsupported_commands_received_size: int | None = None
    cp3w_unsupported_responses_submitted_address: int | None = None
    cp3w_unsupported_responses_submitted_size: int | None = None
    cp3w_unsupported_responses_completed_address: int | None = None
    cp3w_unsupported_responses_completed_size: int | None = None
    cp3w_negotiated_flag_address: int | None = None
    cp3w_negotiated_flag_size: int | None = None
    cp3w_selected_protocol_version_address: int | None = None
    cp3w_selected_protocol_version_size: int | None = None
    cp3w_client_nonce_address: int | None = None
    cp3w_client_nonce_size: int | None = None
    cp3w_client_capabilities_address: int | None = None
    cp3w_client_capabilities_size: int | None = None
    cp3w_runtime_capabilities_address: int | None = None
    cp3w_runtime_capabilities_size: int | None = None
    cp3w_accepted_capabilities_address: int | None = None
    cp3w_accepted_capabilities_size: int | None = None
    cp3w_session_id_address: int | None = None
    cp3w_session_id_size: int | None = None
    cp3w_runtime_build_id_address: int | None = None
    cp3w_runtime_build_id_size: int | None = None
    cp3w_last_command_address: int | None = None
    cp3w_last_command_size: int | None = None
    cp3w_last_response_status_address: int | None = None
    cp3w_last_response_status_size: int | None = None
    cp3w_last_ping_payload_length_address: int | None = None
    cp3w_last_ping_payload_length_size: int | None = None
    cp3w_last_dispatch_result_address: int | None = None
    cp3w_last_dispatch_result_size: int | None = None
    receive_arm_count_address: int | None = None
    receive_arm_count_size: int | None = None
    receive_rearm_count_address: int | None = None
    receive_rearm_count_size: int | None = None
    configured_exchange_limit_address: int | None = None
    configured_exchange_limit_size: int | None = None
    completed_exchange_count_address: int | None = None
    completed_exchange_count_size: int | None = None
    current_exchange_index_address: int | None = None
    current_exchange_index_size: int | None = None
    last_completed_exchange_index_address: int | None = None
    last_completed_exchange_index_size: int | None = None
    previous_peer_ipv4_address: int | None = None
    previous_peer_ipv4_size: int | None = None
    previous_peer_port_address: int | None = None
    previous_peer_port_size: int | None = None
    rearm_submission_failure_count_address: int | None = None
    rearm_submission_failure_count_size: int | None = None
    loop_complete_transition_count_address: int | None = None
    loop_complete_transition_count_size: int | None = None
    cleanup_deferred_count_address: int | None = None
    cleanup_deferred_count_size: int | None = None
    polls_while_receive_pending_address: int | None = None
    polls_while_receive_pending_size: int | None = None
    polls_after_loop_complete_address: int | None = None
    polls_after_loop_complete_size: int | None = None
    host_id_available_address: int | None = None
    host_id_available_size: int | None = None
    host_id_ready_address: int | None = None
    host_id_ready_size: int | None = None
    open_kd_submit_result_address: int | None = None
    open_kd_submit_result_size: int | None = None
    open_kd_callback_result_address: int | None = None
    open_kd_callback_result_size: int | None = None
    open_kd_submit_generation_address: int | None = None
    open_kd_submit_generation_size: int | None = None
    open_kd_callback_generation_address: int | None = None
    open_kd_callback_generation_size: int | None = None
    nwc24_submit_generation_address: int | None = None
    nwc24_submit_generation_size: int | None = None
    nwc24_callback_generation_address: int | None = None
    nwc24_callback_generation_size: int | None = None
    open_ip_submit_result_address: int | None = None
    open_ip_submit_result_size: int | None = None
    open_ip_callback_result_address: int | None = None
    open_ip_callback_result_size: int | None = None
    open_ip_submit_generation_address: int | None = None
    open_ip_submit_generation_size: int | None = None
    open_ip_callback_generation_address: int | None = None
    open_ip_callback_generation_size: int | None = None
    open_ip_path_pointer_address: int | None = None
    open_ip_path_pointer_size: int | None = None
    open_ip_path_length_address: int | None = None
    open_ip_path_length_size: int | None = None
    open_ip_mode_value_address: int | None = None
    open_ip_mode_value_size: int | None = None
    open_ip_callback_pointer_address: int | None = None
    open_ip_callback_pointer_size: int | None = None
    open_ip_context_pointer_address: int | None = None
    open_ip_context_pointer_size: int | None = None
    open_ip_callback_exit_count_address: int | None = None
    open_ip_callback_exit_count_size: int | None = None
    open_ip_stale_callback_count_address: int | None = None
    open_ip_stale_callback_count_size: int | None = None
    open_ip_duplicate_callback_count_address: int | None = None
    open_ip_duplicate_callback_count_size: int | None = None
    ip_fd_before_open_ip_address: int | None = None
    ip_fd_before_open_ip_size: int | None = None
    kd_close_submit_result_address: int | None = None
    kd_close_submit_result_size: int | None = None
    kd_close_callback_result_address: int | None = None
    kd_close_callback_result_size: int | None = None
    kd_close_submit_generation_address: int | None = None
    kd_close_submit_generation_size: int | None = None
    kd_close_callback_generation_address: int | None = None
    kd_close_callback_generation_size: int | None = None
    kd_close_submitted_fd_address: int | None = None
    kd_close_submitted_fd_size: int | None = None
    kd_fd_before_close_address: int | None = None
    kd_fd_before_close_size: int | None = None
    kd_fd_after_close_address: int | None = None
    kd_fd_after_close_size: int | None = None
    startup_submit_result_address: int | None = None
    startup_submit_result_size: int | None = None
    startup_callback_result_address: int | None = None
    startup_callback_result_size: int | None = None
    startup_submit_generation_address: int | None = None
    startup_submit_generation_size: int | None = None
    startup_callback_generation_address: int | None = None
    startup_callback_generation_size: int | None = None
    startup_target_address: int | None = None
    startup_target_size: int | None = None
    startup_command_address: int | None = None
    startup_command_size: int | None = None
    startup_submitted_fd_address: int | None = None
    startup_submitted_fd_size: int | None = None
    startup_callback_pointer_address: int | None = None
    startup_callback_pointer_size: int | None = None
    startup_context_pointer_address: int | None = None
    startup_context_pointer_size: int | None = None
    startup_callback_exit_count_address: int | None = None
    startup_callback_exit_count_size: int | None = None
    startup_stale_callback_count_address: int | None = None
    startup_stale_callback_count_size: int | None = None
    startup_duplicate_callback_count_address: int | None = None
    startup_duplicate_callback_count_size: int | None = None
    startup_service_started_before_submit_address: int | None = None
    startup_service_started_before_submit_size: int | None = None
    startup_service_started_after_completion_address: int | None = None
    startup_service_started_after_completion_size: int | None = None
    ip_fd_before_startup_address: int | None = None
    ip_fd_before_startup_size: int | None = None
    ip_fd_after_startup_address: int | None = None
    ip_fd_after_startup_size: int | None = None
    startup_pending_before_submit_address: int | None = None
    startup_pending_before_submit_size: int | None = None
    startup_pending_after_completion_address: int | None = None
    startup_pending_after_completion_size: int | None = None
    startup_phase_before_submit_address: int | None = None
    startup_phase_before_submit_size: int | None = None
    startup_phase_after_completion_address: int | None = None
    startup_phase_after_completion_size: int | None = None
    startup_pre_call_args_address: int | None = None
    startup_pre_call_args_size: int | None = None
    get_host_id_submit_result_address: int | None = None
    get_host_id_submit_result_size: int | None = None
    get_host_id_callback_result_address: int | None = None
    get_host_id_callback_result_size: int | None = None
    get_host_id_submit_generation_address: int | None = None
    get_host_id_submit_generation_size: int | None = None
    get_host_id_callback_generation_address: int | None = None
    get_host_id_callback_generation_size: int | None = None
    get_host_id_target_address: int | None = None
    get_host_id_target_size: int | None = None
    get_host_id_command_address: int | None = None
    get_host_id_command_size: int | None = None
    get_host_id_submitted_fd_address: int | None = None
    get_host_id_submitted_fd_size: int | None = None
    get_host_id_callback_pointer_address: int | None = None
    get_host_id_callback_pointer_size: int | None = None
    get_host_id_context_pointer_address: int | None = None
    get_host_id_context_pointer_size: int | None = None
    get_host_id_callback_exit_count_address: int | None = None
    get_host_id_callback_exit_count_size: int | None = None
    get_host_id_stale_callback_count_address: int | None = None
    get_host_id_stale_callback_count_size: int | None = None
    get_host_id_duplicate_callback_count_address: int | None = None
    get_host_id_duplicate_callback_count_size: int | None = None
    get_host_id_service_started_before_submit_address: int | None = None
    get_host_id_service_started_before_submit_size: int | None = None
    get_host_id_service_started_after_completion_address: int | None = None
    get_host_id_service_started_after_completion_size: int | None = None
    ip_fd_before_get_host_id_address: int | None = None
    ip_fd_before_get_host_id_size: int | None = None
    ip_fd_after_get_host_id_address: int | None = None
    ip_fd_after_get_host_id_size: int | None = None
    get_host_id_pending_before_submit_address: int | None = None
    get_host_id_pending_before_submit_size: int | None = None
    get_host_id_pending_after_completion_address: int | None = None
    get_host_id_pending_after_completion_size: int | None = None
    get_host_id_phase_before_submit_address: int | None = None
    get_host_id_phase_before_submit_size: int | None = None
    get_host_id_phase_after_completion_address: int | None = None
    get_host_id_phase_after_completion_size: int | None = None
    get_host_id_pre_call_args_address: int | None = None
    get_host_id_pre_call_args_size: int | None = None
    socket_submit_result_address: int | None = None
    socket_submit_result_size: int | None = None
    socket_callback_result_address: int | None = None
    socket_callback_result_size: int | None = None
    socket_submit_generation_address: int | None = None
    socket_submit_generation_size: int | None = None
    socket_callback_generation_address: int | None = None
    socket_callback_generation_size: int | None = None
    socket_target_address: int | None = None
    socket_target_size: int | None = None
    socket_command_address: int | None = None
    socket_command_size: int | None = None
    socket_submitted_fd_address: int | None = None
    socket_submitted_fd_size: int | None = None
    socket_callback_pointer_address: int | None = None
    socket_callback_pointer_size: int | None = None
    socket_context_pointer_address: int | None = None
    socket_context_pointer_size: int | None = None
    socket_callback_exit_count_address: int | None = None
    socket_callback_exit_count_size: int | None = None
    socket_stale_callback_count_address: int | None = None
    socket_stale_callback_count_size: int | None = None
    socket_duplicate_callback_count_address: int | None = None
    socket_duplicate_callback_count_size: int | None = None
    socket_fd_before_submit_address: int | None = None
    socket_fd_before_submit_size: int | None = None
    socket_fd_after_completion_address: int | None = None
    socket_fd_after_completion_size: int | None = None
    socket_request_address_address: int | None = None
    socket_request_address_size: int | None = None
    socket_request_storage_size_address: int | None = None
    socket_request_storage_size_size: int | None = None
    socket_request_logical_size_address: int | None = None
    socket_request_logical_size_size: int | None = None
    socket_request_alignment_address: int | None = None
    socket_request_alignment_size: int | None = None
    socket_family_value_address: int | None = None
    socket_family_value_size: int | None = None
    socket_type_value_address: int | None = None
    socket_type_value_size: int | None = None
    socket_protocol_value_address: int | None = None
    socket_protocol_value_size: int | None = None
    socket_descriptor_valid_address: int | None = None
    socket_descriptor_valid_size: int | None = None
    socket_ready_address: int | None = None
    socket_ready_size: int | None = None
    socket_request_bytes_address: int | None = None
    socket_request_bytes_size: int | None = None
    socket_pre_call_args_address: int | None = None
    socket_pre_call_args_size: int | None = None
    bind_submit_result_address: int | None = None
    bind_submit_result_size: int | None = None
    bind_callback_result_address: int | None = None
    bind_callback_result_size: int | None = None
    bind_submit_generation_address: int | None = None
    bind_submit_generation_size: int | None = None
    bind_callback_generation_address: int | None = None
    bind_callback_generation_size: int | None = None
    bind_target_address: int | None = None
    bind_target_size: int | None = None
    bind_command_address: int | None = None
    bind_command_size: int | None = None
    bind_submitted_fd_address: int | None = None
    bind_submitted_fd_size: int | None = None
    bind_callback_pointer_address: int | None = None
    bind_callback_pointer_size: int | None = None
    bind_context_pointer_address: int | None = None
    bind_context_pointer_size: int | None = None
    bind_callback_exit_count_address: int | None = None
    bind_callback_exit_count_size: int | None = None
    bind_stale_callback_count_address: int | None = None
    bind_stale_callback_count_size: int | None = None
    bind_duplicate_callback_count_address: int | None = None
    bind_duplicate_callback_count_size: int | None = None
    bind_request_address_address: int | None = None
    bind_request_address_size: int | None = None
    bind_request_storage_size_address: int | None = None
    bind_request_storage_size_size: int | None = None
    bind_request_logical_size_address: int | None = None
    bind_request_logical_size_size: int | None = None
    bind_request_alignment_address: int | None = None
    bind_request_alignment_size: int | None = None
    bind_sockaddr_length_address: int | None = None
    bind_sockaddr_length_size: int | None = None
    bind_family_value_address: int | None = None
    bind_family_value_size: int | None = None
    bind_port_value_address: int | None = None
    bind_port_value_size: int | None = None
    bind_address_value_address: int | None = None
    bind_address_value_size: int | None = None
    bind_request_bytes_address: int | None = None
    bind_request_bytes_size: int | None = None
    bind_pre_call_args_address: int | None = None
    bind_pre_call_args_size: int | None = None
    cleanup_close_callback_count_address: int | None = None
    cleanup_close_callback_count_size: int | None = None
    cleanup_close_submit_result_address: int | None = None
    cleanup_close_submit_result_size: int | None = None
    cleanup_close_callback_result_address: int | None = None
    cleanup_close_callback_result_size: int | None = None
    cleanup_close_submit_generation_address: int | None = None
    cleanup_close_submit_generation_size: int | None = None
    cleanup_close_callback_generation_address: int | None = None
    cleanup_close_callback_generation_size: int | None = None
    cleanup_close_target_address: int | None = None
    cleanup_close_target_size: int | None = None
    cleanup_close_command_address: int | None = None
    cleanup_close_command_size: int | None = None
    cleanup_close_submitted_fd_address: int | None = None
    cleanup_close_submitted_fd_size: int | None = None
    cleanup_close_callback_pointer_address: int | None = None
    cleanup_close_callback_pointer_size: int | None = None
    cleanup_close_context_pointer_address: int | None = None
    cleanup_close_context_pointer_size: int | None = None
    cleanup_close_callback_exit_count_address: int | None = None
    cleanup_close_callback_exit_count_size: int | None = None
    cleanup_close_stale_callback_count_address: int | None = None
    cleanup_close_stale_callback_count_size: int | None = None
    cleanup_close_duplicate_callback_count_address: int | None = None
    cleanup_close_duplicate_callback_count_size: int | None = None
    cleanup_close_request_address_address: int | None = None
    cleanup_close_request_address_size: int | None = None
    cleanup_close_request_storage_size_address: int | None = None
    cleanup_close_request_storage_size_size: int | None = None
    cleanup_close_request_logical_size_address: int | None = None
    cleanup_close_request_logical_size_size: int | None = None
    cleanup_close_request_alignment_address: int | None = None
    cleanup_close_request_alignment_size: int | None = None
    cleanup_close_request_value_address: int | None = None
    cleanup_close_request_value_size: int | None = None
    cleanup_close_request_bytes_address: int | None = None
    cleanup_close_request_bytes_size: int | None = None
    cleanup_close_pre_call_args_address: int | None = None
    cleanup_close_pre_call_args_size: int | None = None
    bound_flag_address: int | None = None
    bound_flag_size: int | None = None
    bound_address_address: int | None = None
    bound_address_size: int | None = None
    socket_closed_after_bind_failure_address: int | None = None
    socket_closed_after_bind_failure_size: int | None = None
    socket_leak_detected_address: int | None = None
    socket_leak_detected_size: int | None = None
    cp3w_game_identity: Prime3RuntimeGameIdentityMetadata | None = None
    cp3w_inventory: Prime3RuntimeInventoryMetadata | None = None
    network_diagnostics_address: int | None = None
    network_diagnostics_size: int | None = None
    network_diagnostics_version: int | None = None

    def validate(  # noqa: C901
        self, *, runtime_state_start: int, runtime_state_end: int
    ) -> tuple[tuple[str, int, int], ...]:
        if not self.mode:
            raise Prime3DolPatchError("Relocated runtime transport metadata requires a mode.")
        if self.udp_port != 43674:
            raise Prime3DolPatchError("Prime 3 CP3W transport must use UDP port 43674.")
        diagnostics_fields = (
            self.network_diagnostics_address,
            self.network_diagnostics_size,
            self.network_diagnostics_version,
        )
        if any(value is not None for value in diagnostics_fields):
            if self.network_diagnostics_address is None or self.network_diagnostics_size != 0x100:
                raise Prime3DolPatchError("Prime 3 network diagnostics must define a 0x100-byte state block.")
            if self.network_diagnostics_version != 1:
                raise Prime3DolPatchError("Prime 3 network diagnostics must use ABI version 1.")
        if not self.initialization_enabled:
            raise Prime3DolPatchError("Relocated runtime transport metadata must mark initialization_enabled.")
        is_recvfrom_once = self.mode == "retail_wrapper_recvfrom_once"
        is_recv_send_once = self.mode == "retail_wrapper_recv_send_once"
        is_recv_send_loop = self.mode == "retail_wrapper_recv_send_loop"
        is_cp3w_frame_validation = self.mode == "cp3w_frame_validation"
        is_cp3w_ping_pong = self.mode == "cp3w_ping_pong"
        is_cp3w_hello_session = self.mode == "cp3w_hello_session"
        is_cp3w_game_identity = self.mode == "cp3w_game_identity"
        is_cp3w_inventory_service = self.mode == "cp3w_inventory_service"
        is_cp3w_inventory = self.mode in {"cp3w_inventory", "cp3w_inventory_service"}
        is_native_wc24_bootstrap = self.mode == "native_wc24_bootstrap_beacon_once"
        if self.receive_enabled and not is_recvfrom_once:
            if (
                not is_recv_send_once
                and not is_recv_send_loop
                and not is_cp3w_frame_validation
                and not is_cp3w_ping_pong
                and not is_cp3w_hello_session
                and not is_cp3w_game_identity
                and not is_cp3w_inventory
            ):
                raise Prime3DolPatchError("Initialization-only transport metadata must not enable receive.")
        if (
            is_recvfrom_once
            or is_recv_send_once
            or is_recv_send_loop
            or is_cp3w_frame_validation
            or is_cp3w_ping_pong
            or is_cp3w_hello_session
            or is_cp3w_game_identity
            or is_cp3w_inventory
        ) and not self.receive_enabled:
            raise Prime3DolPatchError("Recvfrom-once metadata must enable receive.")
        if (
            self.send_enabled
            and not is_recv_send_once
            and not is_recv_send_loop
            and not is_cp3w_frame_validation
            and not is_cp3w_ping_pong
            and not is_cp3w_hello_session
            and not is_cp3w_game_identity
            and not is_cp3w_inventory
            and not is_native_wc24_bootstrap
        ):
            raise Prime3DolPatchError("Initialization-only transport metadata must not enable send.")
        if (
            is_recv_send_once
            or is_recv_send_loop
            or is_cp3w_frame_validation
            or is_cp3w_ping_pong
            or is_cp3w_hello_session
            or is_cp3w_game_identity
            or is_cp3w_inventory
            or is_native_wc24_bootstrap
        ) and not self.send_enabled:
            raise Prime3DolPatchError("Recv-send metadata must enable send.")
        if is_cp3w_inventory_service:
            if not self.nwc24_startup_enabled or not self.kd_close_enabled:
                raise Prime3DolPatchError(
                    "CP3W inventory service metadata must include passive NWC24 startup and owned KD cleanup."
                )
        elif not self.nwc24_startup_enabled:
            raise Prime3DolPatchError("Initialization-only transport metadata must enable NWC24 startup.")
        is_nwc24_ioctl_once = self.mode == "retail_wrapper_nwc24_startup_once"
        is_nwc24_close_once = self.mode == "retail_wrapper_nwc24_close_kd_once"
        is_nwc24_close_open_ip_once = self.mode == "retail_wrapper_nwc24_close_open_ip_once"
        is_nwc24_close_open_ip_startup_once = self.mode == "retail_wrapper_nwc24_close_open_ip_startup_once"
        is_startup_once = self.mode == "retail_wrapper_startup_once"
        is_get_host_id_once = self.mode == "retail_wrapper_get_host_id_once"
        if is_nwc24_ioctl_once or is_native_wc24_bootstrap:
            if self.kd_close_enabled:
                raise Prime3DolPatchError("Retained NWC24 metadata must not enable kd close.")
            expected_phase_value = 115 if is_native_wc24_bootstrap else 0xFE
            expected_phase_name = "NATIVE_BEACON_COMPLETE" if is_native_wc24_bootstrap else "NWC24_COMPLETE"
            if self.terminal_phase_value != expected_phase_value or self.terminal_phase_name != expected_phase_name:
                raise Prime3DolPatchError("NWC24 ioctl-once metadata must use the terminal diagnostic phase.")
        elif not self.kd_close_enabled:
            raise Prime3DolPatchError("Initialization-only transport metadata must enable kd close.")
        if is_nwc24_close_once and (self.terminal_phase_value != 0xFE or self.terminal_phase_name != "KD_CLOSED"):
            raise Prime3DolPatchError("NWC24 close-once metadata must use the KD_CLOSED terminal phase.")
        if is_nwc24_close_open_ip_once and (self.terminal_phase_value != 0xFE or self.terminal_phase_name != "IP_OPEN"):
            raise Prime3DolPatchError("NWC24 close-open-ip metadata must use the IP_OPEN terminal phase.")
        if is_nwc24_close_open_ip_startup_once and (
            self.terminal_phase_value != 18 or self.terminal_phase_name != "SO_STARTED"
        ):
            raise Prime3DolPatchError("NWC24 close-open-ip-startup metadata must use the SO_STARTED terminal phase.")
        if is_startup_once and (self.terminal_phase_value != 0xFE or self.terminal_phase_name != "DIAGNOSTIC_COMPLETE"):
            raise Prime3DolPatchError("Startup-once metadata must use the terminal diagnostic phase.")
        if is_get_host_id_once and (self.terminal_phase_value != 19 or self.terminal_phase_name != "HOST_ID_READY"):
            raise Prime3DolPatchError("GET_HOST_ID metadata must use the HOST_ID_READY terminal phase.")
        if is_recvfrom_once and (self.terminal_phase_value != 27 or self.terminal_phase_name != "RECEIVED_DATAGRAM"):
            raise Prime3DolPatchError("Recvfrom-once metadata must use the RECEIVED_DATAGRAM terminal phase.")
        if is_recv_send_once and (self.terminal_phase_value != 37 or self.terminal_phase_name != "SENT_DATAGRAM"):
            raise Prime3DolPatchError("Recv-send metadata must use the SENT_DATAGRAM terminal phase.")
        if is_recv_send_loop and (self.terminal_phase_value != 45 or self.terminal_phase_name != "LOOP_COMPLETE"):
            raise Prime3DolPatchError("Recv-send-loop metadata must use the LOOP_COMPLETE terminal phase.")
        if is_cp3w_frame_validation and (
            self.terminal_phase_value != 55 or self.terminal_phase_name != "CP3W_FRAME_LOOP_COMPLETE"
        ):
            raise Prime3DolPatchError(
                "CP3W frame validation metadata must use the CP3W_FRAME_LOOP_COMPLETE terminal phase."
            )
        if is_cp3w_ping_pong and (
            self.terminal_phase_value != 61 or self.terminal_phase_name != "CP3W_PING_PONG_LOOP_COMPLETE"
        ):
            raise Prime3DolPatchError(
                "CP3W ping/pong metadata must use the CP3W_PING_PONG_LOOP_COMPLETE terminal phase."
            )
        if is_cp3w_hello_session and (
            self.terminal_phase_value != 69 or self.terminal_phase_name != "CP3W_HELLO_SESSION_LOOP_COMPLETE"
        ):
            raise Prime3DolPatchError(
                "CP3W hello/session metadata must use the CP3W_HELLO_SESSION_LOOP_COMPLETE terminal phase."
            )
        if is_cp3w_game_identity and (
            self.terminal_phase_value != 79 or self.terminal_phase_name != "CP3W_GAME_IDENTITY_LOOP_COMPLETE"
        ):
            raise Prime3DolPatchError(
                "CP3W game identity metadata must use the CP3W_GAME_IDENTITY_LOOP_COMPLETE terminal phase."
            )
        if is_cp3w_game_identity or is_cp3w_inventory:
            if self.cp3w_game_identity is None:
                raise Prime3DolPatchError("Structured CP3W metadata is missing game identity details.")
        elif self.cp3w_game_identity is not None:
            raise Prime3DolPatchError("CP3W game identity details require game identity or inventory mode.")
        if (
            is_cp3w_inventory
            and not is_cp3w_inventory_service
            and (self.terminal_phase_value != 93 or self.terminal_phase_name != "CP3W_INVENTORY_LOOP_COMPLETE")
        ):
            raise Prime3DolPatchError("CP3W inventory metadata must use the CP3W_INVENTORY_LOOP_COMPLETE phase.")
        if is_cp3w_inventory_service and (
            self.terminal_phase_value != 26 or self.terminal_phase_name != "WAIT_RECEIVE"
        ):
            raise Prime3DolPatchError("CP3W inventory service metadata must identify WAIT_RECEIVE as steady state.")
        if is_cp3w_inventory:
            if self.cp3w_inventory is None:
                raise Prime3DolPatchError("CP3W inventory metadata is missing inventory details.")
        elif self.cp3w_inventory is not None:
            raise Prime3DolPatchError("CP3W inventory details require inventory mode.")
        if self.ip_close_on_success:
            raise Prime3DolPatchError(
                "Initialization-only transport metadata must not close ip descriptors on success."
            )
        if self.socket_close_on_success:
            raise Prime3DolPatchError(
                "Initialization-only transport metadata must not close socket descriptors on success."
            )
        if self.terminal_phase_value <= 0:
            raise Prime3DolPatchError("Relocated runtime transport terminal phase must be positive.")
        if not self.terminal_phase_name:
            raise Prime3DolPatchError("Relocated runtime transport metadata requires a terminal phase name.")
        if self.nwc24_output_buffer_size != 0x20:
            raise Prime3DolPatchError("NWC24 output buffer must be exactly 0x20 bytes.")
        if (
            self.nwc24_output_buffer_alignment < 0x20
            or (self.nwc24_output_buffer_alignment & (self.nwc24_output_buffer_alignment - 1)) != 0
        ):
            raise Prime3DolPatchError("NWC24 output buffer alignment must be a power of two at least 0x20.")
        if self.nwc24_output_buffer_address % self.nwc24_output_buffer_alignment != 0:
            raise Prime3DolPatchError("NWC24 output buffer address must satisfy its declared alignment.")
        ranges: tuple[tuple[str, int, int], ...] = (
            ("transport_phase", self.phase_address, self.phase_size),
            ("transport_last_error", self.last_error_address, self.last_error_size),
            ("transport_last_socket_error", self.last_socket_error_address, self.last_socket_error_size),
            ("transport_last_ios_result", self.last_ios_result_address, self.last_ios_result_size),
            ("transport_pending_operation", self.pending_operation_address, self.pending_operation_size),
            ("transport_pending_generation", self.pending_generation_address, self.pending_generation_size),
            ("transport_callback_generation", self.callback_generation_address, self.callback_generation_size),
            ("transport_callback_count", self.callback_count_address, self.callback_count_size),
            (
                "transport_rejected_callback_count",
                self.rejected_callback_count_address,
                self.rejected_callback_count_size,
            ),
            ("transport_callback_pending", self.callback_pending_address, self.callback_pending_size),
            ("transport_open_kd_submit_count", self.open_kd_submit_count_address, self.open_kd_submit_count_size),
            (
                "transport_open_kd_callback_count",
                self.open_kd_callback_count_address,
                self.open_kd_callback_count_size,
            ),
            ("transport_nwc24_output_buffer", self.nwc24_output_buffer_address, self.nwc24_output_buffer_size),
            ("transport_nwc24_submit_count", self.nwc24_submit_count_address, self.nwc24_submit_count_size),
            (
                "transport_nwc24_callback_count",
                self.nwc24_callback_count_address,
                self.nwc24_callback_count_size,
            ),
            (
                "transport_nwc24_synchronous_result",
                self.nwc24_synchronous_result_address,
                self.nwc24_synchronous_result_size,
            ),
            (
                "transport_nwc24_callback_result",
                self.nwc24_callback_result_address,
                self.nwc24_callback_result_size,
            ),
            ("transport_nwc24_output_digest", self.nwc24_output_digest_address, self.nwc24_output_digest_size),
            ("transport_open_ip_submit_count", self.open_ip_submit_count_address, self.open_ip_submit_count_size),
            (
                "transport_open_ip_callback_count",
                self.open_ip_callback_count_address,
                self.open_ip_callback_count_size,
            ),
            ("transport_kd_close_submit_count", self.kd_close_submit_count_address, self.kd_close_submit_count_size),
            (
                "transport_kd_close_callback_count",
                self.kd_close_callback_count_address,
                self.kd_close_callback_count_size,
            ),
            ("transport_startup_submit_count", self.startup_submit_count_address, self.startup_submit_count_size),
            (
                "transport_startup_callback_count",
                self.startup_callback_count_address,
                self.startup_callback_count_size,
            ),
            (
                "transport_get_host_id_submit_count",
                self.get_host_id_submit_count_address,
                self.get_host_id_submit_count_size,
            ),
            (
                "transport_get_host_id_callback_count",
                self.get_host_id_callback_count_address,
                self.get_host_id_callback_count_size,
            ),
            ("transport_socket_submit_count", self.socket_submit_count_address, self.socket_submit_count_size),
            ("transport_socket_callback_count", self.socket_callback_count_address, self.socket_callback_count_size),
            ("transport_bind_submit_count", self.bind_submit_count_address, self.bind_submit_count_size),
            ("transport_bind_callback_count", self.bind_callback_count_address, self.bind_callback_count_size),
            ("transport_kd_fd", self.kd_fd_address, self.kd_fd_size),
            ("transport_kd_closed", self.kd_closed_address, self.kd_closed_size),
            ("transport_ip_fd", self.ip_fd_address, self.ip_fd_size),
            ("transport_socket_fd", self.socket_fd_address, self.socket_fd_size),
            ("transport_host_id", self.host_id_address, self.host_id_size),
            ("transport_bound_port", self.bound_port_address, self.bound_port_size),
            (
                "transport_receive_submit_count",
                self.receive_submit_count_address,
                self.receive_submit_count_size,
            ),
            ("transport_send_submit_count", self.send_submit_count_address, self.send_submit_count_size),
            ("transport_ip_close_submit_count", self.ip_close_submit_count_address, self.ip_close_submit_count_size),
            (
                "transport_socket_close_submit_count",
                self.socket_close_submit_count_address,
                self.socket_close_submit_count_size,
            ),
            ("transport_receive_count", self.receive_count_address, self.receive_count_size),
            ("transport_receive_bytes", self.receive_bytes_address, self.receive_bytes_size),
            ("transport_send_count", self.send_count_address, self.send_count_size),
            ("transport_send_bytes", self.send_bytes_address, self.send_bytes_size),
            ("transport_last_receive_length", self.last_receive_length_address, self.last_receive_length_size),
            ("transport_last_send_length", self.last_send_length_address, self.last_send_length_size),
            ("transport_last_peer_ipv4", self.last_peer_ipv4_address, self.last_peer_ipv4_size),
            ("transport_last_peer_port", self.last_peer_port_address, self.last_peer_port_size),
            ("transport_last_peer_family", self.last_peer_family_address, self.last_peer_family_size),
            ("transport_last_poll_action", self.last_poll_action_address, self.last_poll_action_size),
            ("transport_last_submit_result", self.last_submit_result_address, self.last_submit_result_size),
            ("transport_last_receive_preview", self.last_receive_preview_address, self.last_receive_preview_size),
            ("transport_last_send_preview", self.last_send_preview_address, self.last_send_preview_size),
        )
        for name, start, size in ranges:
            if size <= 0:
                raise Prime3DolPatchError(f"Relocated runtime transport field {name} size must be positive.")
            if not (runtime_state_start <= start < runtime_state_end):
                raise Prime3DolPatchError(
                    f"Relocated runtime transport field {name} is outside the runtime state range."
                )
            if start + size > runtime_state_end:
                raise Prime3DolPatchError(f"Relocated runtime transport field {name} exceeds the runtime state range.")
        optional_ranges: tuple[tuple[str, int | None, int | None], ...] = (
            ("transport_prepared_send_length", self.prepared_send_length_address, self.prepared_send_length_size),
            (
                "transport_cp3w_datagrams_processed",
                self.cp3w_datagrams_processed_address,
                self.cp3w_datagrams_processed_size,
            ),
            ("transport_cp3w_frames_valid", self.cp3w_frames_valid_address, self.cp3w_frames_valid_size),
            ("transport_cp3w_frames_invalid", self.cp3w_frames_invalid_address, self.cp3w_frames_invalid_size),
            ("transport_cp3w_frames_too_short", self.cp3w_frames_too_short_address, self.cp3w_frames_too_short_size),
            (
                "transport_cp3w_frames_invalid_magic",
                self.cp3w_frames_invalid_magic_address,
                self.cp3w_frames_invalid_magic_size,
            ),
            (
                "transport_cp3w_frames_invalid_version",
                self.cp3w_frames_invalid_version_address,
                self.cp3w_frames_invalid_version_size,
            ),
            (
                "transport_cp3w_frames_unsupported_type",
                self.cp3w_frames_unsupported_type_address,
                self.cp3w_frames_unsupported_type_size,
            ),
            (
                "transport_cp3w_frames_nonzero_flags",
                self.cp3w_frames_nonzero_flags_address,
                self.cp3w_frames_nonzero_flags_size,
            ),
            (
                "transport_cp3w_frames_length_mismatch",
                self.cp3w_frames_length_mismatch_address,
                self.cp3w_frames_length_mismatch_size,
            ),
            (
                "transport_cp3w_frames_payload_too_large",
                self.cp3w_frames_payload_too_large_address,
                self.cp3w_frames_payload_too_large_size,
            ),
            (
                "transport_cp3w_frames_invalid_payload",
                self.cp3w_frames_invalid_payload_address,
                self.cp3w_frames_invalid_payload_size,
            ),
            ("transport_cp3w_frames_malformed", self.cp3w_frames_malformed_address, self.cp3w_frames_malformed_size),
            (
                "transport_cp3w_framed_responses_submitted",
                self.cp3w_framed_responses_submitted_address,
                self.cp3w_framed_responses_submitted_size,
            ),
            (
                "transport_cp3w_framed_responses_completed",
                self.cp3w_framed_responses_completed_address,
                self.cp3w_framed_responses_completed_size,
            ),
            ("transport_cp3w_last_request_id", self.cp3w_last_request_id_address, self.cp3w_last_request_id_size),
            ("transport_cp3w_last_response_id", self.cp3w_last_response_id_address, self.cp3w_last_response_id_size),
            ("transport_cp3w_last_message_type", self.cp3w_last_message_type_address, self.cp3w_last_message_type_size),
            (
                "transport_cp3w_last_declared_payload_length",
                self.cp3w_last_declared_payload_length_address,
                self.cp3w_last_declared_payload_length_size,
            ),
            (
                "transport_cp3w_last_actual_payload_length",
                self.cp3w_last_actual_payload_length_address,
                self.cp3w_last_actual_payload_length_size,
            ),
            ("transport_cp3w_last_frame_result", self.cp3w_last_frame_result_address, self.cp3w_last_frame_result_size),
            (
                "transport_cp3w_final_datagram_index",
                self.cp3w_final_datagram_index_address,
                self.cp3w_final_datagram_index_size,
            ),
            (
                "transport_cp3w_requests_dispatched",
                self.cp3w_requests_dispatched_address,
                self.cp3w_requests_dispatched_size,
            ),
            (
                "transport_cp3w_ping_requests_received",
                self.cp3w_ping_requests_received_address,
                self.cp3w_ping_requests_received_size,
            ),
            (
                "transport_cp3w_pong_responses_submitted",
                self.cp3w_pong_responses_submitted_address,
                self.cp3w_pong_responses_submitted_size,
            ),
            (
                "transport_cp3w_pong_responses_completed",
                self.cp3w_pong_responses_completed_address,
                self.cp3w_pong_responses_completed_size,
            ),
            (
                "transport_cp3w_unsupported_commands_received",
                self.cp3w_unsupported_commands_received_address,
                self.cp3w_unsupported_commands_received_size,
            ),
            (
                "transport_cp3w_unsupported_responses_submitted",
                self.cp3w_unsupported_responses_submitted_address,
                self.cp3w_unsupported_responses_submitted_size,
            ),
            (
                "transport_cp3w_unsupported_responses_completed",
                self.cp3w_unsupported_responses_completed_address,
                self.cp3w_unsupported_responses_completed_size,
            ),
            ("transport_cp3w_last_command", self.cp3w_last_command_address, self.cp3w_last_command_size),
            (
                "transport_cp3w_last_response_status",
                self.cp3w_last_response_status_address,
                self.cp3w_last_response_status_size,
            ),
            (
                "transport_cp3w_last_ping_payload_length",
                self.cp3w_last_ping_payload_length_address,
                self.cp3w_last_ping_payload_length_size,
            ),
            (
                "transport_cp3w_last_dispatch_result",
                self.cp3w_last_dispatch_result_address,
                self.cp3w_last_dispatch_result_size,
            ),
            ("transport_receive_arm_count", self.receive_arm_count_address, self.receive_arm_count_size),
            ("transport_receive_rearm_count", self.receive_rearm_count_address, self.receive_rearm_count_size),
            (
                "transport_configured_exchange_limit",
                self.configured_exchange_limit_address,
                self.configured_exchange_limit_size,
            ),
            (
                "transport_completed_exchange_count",
                self.completed_exchange_count_address,
                self.completed_exchange_count_size,
            ),
            (
                "transport_current_exchange_index",
                self.current_exchange_index_address,
                self.current_exchange_index_size,
            ),
            (
                "transport_last_completed_exchange_index",
                self.last_completed_exchange_index_address,
                self.last_completed_exchange_index_size,
            ),
            ("transport_previous_peer_ipv4", self.previous_peer_ipv4_address, self.previous_peer_ipv4_size),
            ("transport_previous_peer_port", self.previous_peer_port_address, self.previous_peer_port_size),
            (
                "transport_rearm_submission_failure_count",
                self.rearm_submission_failure_count_address,
                self.rearm_submission_failure_count_size,
            ),
            (
                "transport_loop_complete_transition_count",
                self.loop_complete_transition_count_address,
                self.loop_complete_transition_count_size,
            ),
            (
                "transport_cleanup_deferred_count",
                self.cleanup_deferred_count_address,
                self.cleanup_deferred_count_size,
            ),
            (
                "transport_polls_while_receive_pending",
                self.polls_while_receive_pending_address,
                self.polls_while_receive_pending_size,
            ),
            (
                "transport_polls_after_loop_complete",
                self.polls_after_loop_complete_address,
                self.polls_after_loop_complete_size,
            ),
            ("transport_open_kd_submit_result", self.open_kd_submit_result_address, self.open_kd_submit_result_size),
            (
                "transport_open_kd_callback_result",
                self.open_kd_callback_result_address,
                self.open_kd_callback_result_size,
            ),
            (
                "transport_open_kd_submit_generation",
                self.open_kd_submit_generation_address,
                self.open_kd_submit_generation_size,
            ),
            (
                "transport_open_kd_callback_generation",
                self.open_kd_callback_generation_address,
                self.open_kd_callback_generation_size,
            ),
            (
                "transport_nwc24_submit_generation",
                self.nwc24_submit_generation_address,
                self.nwc24_submit_generation_size,
            ),
            (
                "transport_nwc24_callback_generation",
                self.nwc24_callback_generation_address,
                self.nwc24_callback_generation_size,
            ),
            ("transport_open_ip_submit_result", self.open_ip_submit_result_address, self.open_ip_submit_result_size),
            (
                "transport_open_ip_callback_result",
                self.open_ip_callback_result_address,
                self.open_ip_callback_result_size,
            ),
            (
                "transport_open_ip_submit_generation",
                self.open_ip_submit_generation_address,
                self.open_ip_submit_generation_size,
            ),
            (
                "transport_open_ip_callback_generation",
                self.open_ip_callback_generation_address,
                self.open_ip_callback_generation_size,
            ),
            (
                "transport_open_ip_path_pointer",
                self.open_ip_path_pointer_address,
                self.open_ip_path_pointer_size,
            ),
            (
                "transport_open_ip_path_length",
                self.open_ip_path_length_address,
                self.open_ip_path_length_size,
            ),
            (
                "transport_open_ip_mode_value",
                self.open_ip_mode_value_address,
                self.open_ip_mode_value_size,
            ),
            (
                "transport_open_ip_callback_pointer",
                self.open_ip_callback_pointer_address,
                self.open_ip_callback_pointer_size,
            ),
            (
                "transport_open_ip_context_pointer",
                self.open_ip_context_pointer_address,
                self.open_ip_context_pointer_size,
            ),
            (
                "transport_open_ip_callback_exit_count",
                self.open_ip_callback_exit_count_address,
                self.open_ip_callback_exit_count_size,
            ),
            (
                "transport_open_ip_stale_callback_count",
                self.open_ip_stale_callback_count_address,
                self.open_ip_stale_callback_count_size,
            ),
            (
                "transport_open_ip_duplicate_callback_count",
                self.open_ip_duplicate_callback_count_address,
                self.open_ip_duplicate_callback_count_size,
            ),
            (
                "transport_ip_fd_before_open_ip",
                self.ip_fd_before_open_ip_address,
                self.ip_fd_before_open_ip_size,
            ),
            (
                "transport_kd_close_submit_result",
                self.kd_close_submit_result_address,
                self.kd_close_submit_result_size,
            ),
            (
                "transport_kd_close_callback_result",
                self.kd_close_callback_result_address,
                self.kd_close_callback_result_size,
            ),
            (
                "transport_kd_close_submit_generation",
                self.kd_close_submit_generation_address,
                self.kd_close_submit_generation_size,
            ),
            (
                "transport_kd_close_callback_generation",
                self.kd_close_callback_generation_address,
                self.kd_close_callback_generation_size,
            ),
            (
                "transport_kd_close_submitted_fd",
                self.kd_close_submitted_fd_address,
                self.kd_close_submitted_fd_size,
            ),
            (
                "transport_kd_fd_before_close",
                self.kd_fd_before_close_address,
                self.kd_fd_before_close_size,
            ),
            (
                "transport_kd_fd_after_close",
                self.kd_fd_after_close_address,
                self.kd_fd_after_close_size,
            ),
            ("transport_startup_submit_result", self.startup_submit_result_address, self.startup_submit_result_size),
            (
                "transport_startup_callback_result",
                self.startup_callback_result_address,
                self.startup_callback_result_size,
            ),
            (
                "transport_startup_submit_generation",
                self.startup_submit_generation_address,
                self.startup_submit_generation_size,
            ),
            (
                "transport_startup_callback_generation",
                self.startup_callback_generation_address,
                self.startup_callback_generation_size,
            ),
            ("transport_service_started", self.service_started_address, self.service_started_size),
            ("transport_startup_target", self.startup_target_address, self.startup_target_size),
            ("transport_startup_command", self.startup_command_address, self.startup_command_size),
            ("transport_startup_submitted_fd", self.startup_submitted_fd_address, self.startup_submitted_fd_size),
            (
                "transport_startup_callback_pointer",
                self.startup_callback_pointer_address,
                self.startup_callback_pointer_size,
            ),
            (
                "transport_startup_context_pointer",
                self.startup_context_pointer_address,
                self.startup_context_pointer_size,
            ),
            (
                "transport_startup_callback_exit_count",
                self.startup_callback_exit_count_address,
                self.startup_callback_exit_count_size,
            ),
            (
                "transport_startup_stale_callback_count",
                self.startup_stale_callback_count_address,
                self.startup_stale_callback_count_size,
            ),
            (
                "transport_startup_duplicate_callback_count",
                self.startup_duplicate_callback_count_address,
                self.startup_duplicate_callback_count_size,
            ),
            (
                "transport_startup_service_started_before_submit",
                self.startup_service_started_before_submit_address,
                self.startup_service_started_before_submit_size,
            ),
            (
                "transport_startup_service_started_after_completion",
                self.startup_service_started_after_completion_address,
                self.startup_service_started_after_completion_size,
            ),
            ("transport_ip_fd_before_startup", self.ip_fd_before_startup_address, self.ip_fd_before_startup_size),
            ("transport_ip_fd_after_startup", self.ip_fd_after_startup_address, self.ip_fd_after_startup_size),
            (
                "transport_startup_pending_before_submit",
                self.startup_pending_before_submit_address,
                self.startup_pending_before_submit_size,
            ),
            (
                "transport_startup_pending_after_completion",
                self.startup_pending_after_completion_address,
                self.startup_pending_after_completion_size,
            ),
            (
                "transport_startup_phase_before_submit",
                self.startup_phase_before_submit_address,
                self.startup_phase_before_submit_size,
            ),
            (
                "transport_startup_phase_after_completion",
                self.startup_phase_after_completion_address,
                self.startup_phase_after_completion_size,
            ),
            ("transport_startup_pre_call_args", self.startup_pre_call_args_address, self.startup_pre_call_args_size),
            ("transport_host_id_available", self.host_id_available_address, self.host_id_available_size),
            ("transport_host_id_ready", self.host_id_ready_address, self.host_id_ready_size),
            (
                "transport_get_host_id_submit_result",
                self.get_host_id_submit_result_address,
                self.get_host_id_submit_result_size,
            ),
            (
                "transport_get_host_id_callback_result",
                self.get_host_id_callback_result_address,
                self.get_host_id_callback_result_size,
            ),
            (
                "transport_get_host_id_submit_generation",
                self.get_host_id_submit_generation_address,
                self.get_host_id_submit_generation_size,
            ),
            (
                "transport_get_host_id_callback_generation",
                self.get_host_id_callback_generation_address,
                self.get_host_id_callback_generation_size,
            ),
            ("transport_get_host_id_target", self.get_host_id_target_address, self.get_host_id_target_size),
            ("transport_get_host_id_command", self.get_host_id_command_address, self.get_host_id_command_size),
            (
                "transport_get_host_id_submitted_fd",
                self.get_host_id_submitted_fd_address,
                self.get_host_id_submitted_fd_size,
            ),
            (
                "transport_get_host_id_callback_pointer",
                self.get_host_id_callback_pointer_address,
                self.get_host_id_callback_pointer_size,
            ),
            (
                "transport_get_host_id_context_pointer",
                self.get_host_id_context_pointer_address,
                self.get_host_id_context_pointer_size,
            ),
            (
                "transport_get_host_id_callback_exit_count",
                self.get_host_id_callback_exit_count_address,
                self.get_host_id_callback_exit_count_size,
            ),
            (
                "transport_get_host_id_stale_callback_count",
                self.get_host_id_stale_callback_count_address,
                self.get_host_id_stale_callback_count_size,
            ),
            (
                "transport_get_host_id_duplicate_callback_count",
                self.get_host_id_duplicate_callback_count_address,
                self.get_host_id_duplicate_callback_count_size,
            ),
            (
                "transport_get_host_id_service_started_before_submit",
                self.get_host_id_service_started_before_submit_address,
                self.get_host_id_service_started_before_submit_size,
            ),
            (
                "transport_get_host_id_service_started_after_completion",
                self.get_host_id_service_started_after_completion_address,
                self.get_host_id_service_started_after_completion_size,
            ),
            (
                "transport_ip_fd_before_get_host_id",
                self.ip_fd_before_get_host_id_address,
                self.ip_fd_before_get_host_id_size,
            ),
            (
                "transport_ip_fd_after_get_host_id",
                self.ip_fd_after_get_host_id_address,
                self.ip_fd_after_get_host_id_size,
            ),
            (
                "transport_get_host_id_pending_before_submit",
                self.get_host_id_pending_before_submit_address,
                self.get_host_id_pending_before_submit_size,
            ),
            (
                "transport_get_host_id_pending_after_completion",
                self.get_host_id_pending_after_completion_address,
                self.get_host_id_pending_after_completion_size,
            ),
            (
                "transport_get_host_id_phase_before_submit",
                self.get_host_id_phase_before_submit_address,
                self.get_host_id_phase_before_submit_size,
            ),
            (
                "transport_get_host_id_phase_after_completion",
                self.get_host_id_phase_after_completion_address,
                self.get_host_id_phase_after_completion_size,
            ),
            (
                "transport_get_host_id_pre_call_args",
                self.get_host_id_pre_call_args_address,
                self.get_host_id_pre_call_args_size,
            ),
            ("transport_socket_submit_result", self.socket_submit_result_address, self.socket_submit_result_size),
            (
                "transport_socket_callback_result",
                self.socket_callback_result_address,
                self.socket_callback_result_size,
            ),
            (
                "transport_socket_submit_generation",
                self.socket_submit_generation_address,
                self.socket_submit_generation_size,
            ),
            (
                "transport_socket_callback_generation",
                self.socket_callback_generation_address,
                self.socket_callback_generation_size,
            ),
            ("transport_socket_target", self.socket_target_address, self.socket_target_size),
            ("transport_socket_command", self.socket_command_address, self.socket_command_size),
            ("transport_socket_submitted_fd", self.socket_submitted_fd_address, self.socket_submitted_fd_size),
            (
                "transport_socket_callback_pointer",
                self.socket_callback_pointer_address,
                self.socket_callback_pointer_size,
            ),
            (
                "transport_socket_context_pointer",
                self.socket_context_pointer_address,
                self.socket_context_pointer_size,
            ),
            (
                "transport_socket_callback_exit_count",
                self.socket_callback_exit_count_address,
                self.socket_callback_exit_count_size,
            ),
            (
                "transport_socket_stale_callback_count",
                self.socket_stale_callback_count_address,
                self.socket_stale_callback_count_size,
            ),
            (
                "transport_socket_duplicate_callback_count",
                self.socket_duplicate_callback_count_address,
                self.socket_duplicate_callback_count_size,
            ),
            (
                "transport_socket_fd_before_submit",
                self.socket_fd_before_submit_address,
                self.socket_fd_before_submit_size,
            ),
            (
                "transport_socket_fd_after_completion",
                self.socket_fd_after_completion_address,
                self.socket_fd_after_completion_size,
            ),
            (
                "transport_socket_request_address",
                self.socket_request_address_address,
                self.socket_request_address_size,
            ),
            (
                "transport_socket_request_storage_size",
                self.socket_request_storage_size_address,
                self.socket_request_storage_size_size,
            ),
            (
                "transport_socket_request_logical_size",
                self.socket_request_logical_size_address,
                self.socket_request_logical_size_size,
            ),
            (
                "transport_socket_request_alignment",
                self.socket_request_alignment_address,
                self.socket_request_alignment_size,
            ),
            ("transport_socket_family_value", self.socket_family_value_address, self.socket_family_value_size),
            ("transport_socket_type_value", self.socket_type_value_address, self.socket_type_value_size),
            (
                "transport_socket_protocol_value",
                self.socket_protocol_value_address,
                self.socket_protocol_value_size,
            ),
            (
                "transport_socket_descriptor_valid",
                self.socket_descriptor_valid_address,
                self.socket_descriptor_valid_size,
            ),
            ("transport_socket_ready", self.socket_ready_address, self.socket_ready_size),
            ("transport_socket_request_bytes", self.socket_request_bytes_address, self.socket_request_bytes_size),
            ("transport_socket_pre_call_args", self.socket_pre_call_args_address, self.socket_pre_call_args_size),
            ("transport_bind_submit_result", self.bind_submit_result_address, self.bind_submit_result_size),
            (
                "transport_bind_callback_result",
                self.bind_callback_result_address,
                self.bind_callback_result_size,
            ),
            (
                "transport_bind_submit_generation",
                self.bind_submit_generation_address,
                self.bind_submit_generation_size,
            ),
            (
                "transport_bind_callback_generation",
                self.bind_callback_generation_address,
                self.bind_callback_generation_size,
            ),
            ("transport_bind_target", self.bind_target_address, self.bind_target_size),
            ("transport_bind_command", self.bind_command_address, self.bind_command_size),
            ("transport_bind_submitted_fd", self.bind_submitted_fd_address, self.bind_submitted_fd_size),
            (
                "transport_bind_callback_pointer",
                self.bind_callback_pointer_address,
                self.bind_callback_pointer_size,
            ),
            ("transport_bind_context_pointer", self.bind_context_pointer_address, self.bind_context_pointer_size),
            (
                "transport_bind_callback_exit_count",
                self.bind_callback_exit_count_address,
                self.bind_callback_exit_count_size,
            ),
            (
                "transport_bind_stale_callback_count",
                self.bind_stale_callback_count_address,
                self.bind_stale_callback_count_size,
            ),
            (
                "transport_bind_duplicate_callback_count",
                self.bind_duplicate_callback_count_address,
                self.bind_duplicate_callback_count_size,
            ),
            ("transport_bind_request_address", self.bind_request_address_address, self.bind_request_address_size),
            (
                "transport_bind_request_storage_size",
                self.bind_request_storage_size_address,
                self.bind_request_storage_size_size,
            ),
            (
                "transport_bind_request_logical_size",
                self.bind_request_logical_size_address,
                self.bind_request_logical_size_size,
            ),
            (
                "transport_bind_request_alignment",
                self.bind_request_alignment_address,
                self.bind_request_alignment_size,
            ),
            (
                "transport_bind_sockaddr_length",
                self.bind_sockaddr_length_address,
                self.bind_sockaddr_length_size,
            ),
            ("transport_bind_family_value", self.bind_family_value_address, self.bind_family_value_size),
            ("transport_bind_port_value", self.bind_port_value_address, self.bind_port_value_size),
            ("transport_bind_address_value", self.bind_address_value_address, self.bind_address_value_size),
            ("transport_bind_request_bytes", self.bind_request_bytes_address, self.bind_request_bytes_size),
            ("transport_bind_pre_call_args", self.bind_pre_call_args_address, self.bind_pre_call_args_size),
            (
                "transport_cleanup_close_callback_count",
                self.cleanup_close_callback_count_address,
                self.cleanup_close_callback_count_size,
            ),
            (
                "transport_cleanup_close_submit_result",
                self.cleanup_close_submit_result_address,
                self.cleanup_close_submit_result_size,
            ),
            (
                "transport_cleanup_close_callback_result",
                self.cleanup_close_callback_result_address,
                self.cleanup_close_callback_result_size,
            ),
            (
                "transport_cleanup_close_submit_generation",
                self.cleanup_close_submit_generation_address,
                self.cleanup_close_submit_generation_size,
            ),
            (
                "transport_cleanup_close_callback_generation",
                self.cleanup_close_callback_generation_address,
                self.cleanup_close_callback_generation_size,
            ),
            ("transport_cleanup_close_target", self.cleanup_close_target_address, self.cleanup_close_target_size),
            ("transport_cleanup_close_command", self.cleanup_close_command_address, self.cleanup_close_command_size),
            (
                "transport_cleanup_close_submitted_fd",
                self.cleanup_close_submitted_fd_address,
                self.cleanup_close_submitted_fd_size,
            ),
            (
                "transport_cleanup_close_callback_pointer",
                self.cleanup_close_callback_pointer_address,
                self.cleanup_close_callback_pointer_size,
            ),
            (
                "transport_cleanup_close_context_pointer",
                self.cleanup_close_context_pointer_address,
                self.cleanup_close_context_pointer_size,
            ),
            (
                "transport_cleanup_close_callback_exit_count",
                self.cleanup_close_callback_exit_count_address,
                self.cleanup_close_callback_exit_count_size,
            ),
            (
                "transport_cleanup_close_stale_callback_count",
                self.cleanup_close_stale_callback_count_address,
                self.cleanup_close_stale_callback_count_size,
            ),
            (
                "transport_cleanup_close_duplicate_callback_count",
                self.cleanup_close_duplicate_callback_count_address,
                self.cleanup_close_duplicate_callback_count_size,
            ),
            (
                "transport_cleanup_close_request_address",
                self.cleanup_close_request_address_address,
                self.cleanup_close_request_address_size,
            ),
            (
                "transport_cleanup_close_request_storage_size",
                self.cleanup_close_request_storage_size_address,
                self.cleanup_close_request_storage_size_size,
            ),
            (
                "transport_cleanup_close_request_logical_size",
                self.cleanup_close_request_logical_size_address,
                self.cleanup_close_request_logical_size_size,
            ),
            (
                "transport_cleanup_close_request_alignment",
                self.cleanup_close_request_alignment_address,
                self.cleanup_close_request_alignment_size,
            ),
            (
                "transport_cleanup_close_request_value",
                self.cleanup_close_request_value_address,
                self.cleanup_close_request_value_size,
            ),
            (
                "transport_cleanup_close_request_bytes",
                self.cleanup_close_request_bytes_address,
                self.cleanup_close_request_bytes_size,
            ),
            (
                "transport_cleanup_close_pre_call_args",
                self.cleanup_close_pre_call_args_address,
                self.cleanup_close_pre_call_args_size,
            ),
            ("transport_bound_flag", self.bound_flag_address, self.bound_flag_size),
            ("transport_bound_address", self.bound_address_address, self.bound_address_size),
            (
                "transport_socket_closed_after_bind_failure",
                self.socket_closed_after_bind_failure_address,
                self.socket_closed_after_bind_failure_size,
            ),
            (
                "transport_socket_leak_detected",
                self.socket_leak_detected_address,
                self.socket_leak_detected_size,
            ),
            (
                "transport_network_diagnostics",
                self.network_diagnostics_address,
                self.network_diagnostics_size,
            ),
        )
        for name, optional_start, optional_size in optional_ranges:
            if optional_start is None and optional_size is None:
                continue
            if optional_start is None or optional_size is None:
                raise Prime3DolPatchError(
                    f"Relocated runtime transport field {name} must define both address and size."
                )
            if optional_size <= 0:
                raise Prime3DolPatchError(f"Relocated runtime transport field {name} size must be positive.")
            if not (runtime_state_start <= optional_start < runtime_state_end):
                raise Prime3DolPatchError(
                    f"Relocated runtime transport field {name} is outside the runtime state range."
                )
            if optional_start + optional_size > runtime_state_end:
                raise Prime3DolPatchError(f"Relocated runtime transport field {name} exceeds the runtime state range.")
        validated_optional_ranges: tuple[tuple[str, int, int], ...] = tuple(
            (name, start, size) for name, start, size in optional_ranges if start is not None and size is not None
        )
        ranges = ranges + validated_optional_ranges
        if self.cp3w_game_identity is not None:
            ranges += self.cp3w_game_identity.validate(
                runtime_state_start=runtime_state_start,
                runtime_state_end=runtime_state_end,
            )
        if self.cp3w_inventory is not None:
            ranges += self.cp3w_inventory.validate(
                runtime_state_start=runtime_state_start,
                runtime_state_end=runtime_state_end,
            )
        _validate_non_overlapping_ranges(ranges)
        return ranges

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> LegacyPrime3RuntimeTransportMetadata:
        return cls(
            mode=_json_string(data, "mode"),
            udp_port=_json_int(data, "udp_port") if "udp_port" in data else 43674,
            initialization_enabled=_json_bool(data, "initialization_enabled"),
            receive_enabled=_json_bool(data, "receive_enabled"),
            send_enabled=_json_bool(data, "send_enabled"),
            nwc24_startup_enabled=_json_bool(data, "nwc24_startup_enabled"),
            kd_close_enabled=_json_bool(data, "kd_close_enabled"),
            ip_close_on_success=_json_bool(data, "ip_close_on_success"),
            socket_close_on_success=_json_bool(data, "socket_close_on_success"),
            terminal_phase_value=_json_int(data, "terminal_phase_value"),
            terminal_phase_name=_json_string(data, "terminal_phase_name"),
            phase_address=_json_int(data, "phase_address"),
            phase_size=_json_int(data, "phase_size"),
            last_error_address=_json_int(data, "last_error_address"),
            last_error_size=_json_int(data, "last_error_size"),
            last_socket_error_address=_json_int(data, "last_socket_error_address"),
            last_socket_error_size=_json_int(data, "last_socket_error_size"),
            last_ios_result_address=_json_int(data, "last_ios_result_address"),
            last_ios_result_size=_json_int(data, "last_ios_result_size"),
            pending_operation_address=_json_int(data, "pending_operation_address"),
            pending_operation_size=_json_int(data, "pending_operation_size"),
            pending_generation_address=_json_int(data, "pending_generation_address"),
            pending_generation_size=_json_int(data, "pending_generation_size"),
            callback_generation_address=_json_int(data, "callback_generation_address"),
            callback_generation_size=_json_int(data, "callback_generation_size"),
            callback_count_address=_json_int(data, "callback_count_address"),
            callback_count_size=_json_int(data, "callback_count_size"),
            rejected_callback_count_address=_json_int(data, "rejected_callback_count_address"),
            rejected_callback_count_size=_json_int(data, "rejected_callback_count_size"),
            callback_pending_address=_json_int(data, "callback_pending_address"),
            callback_pending_size=_json_int(data, "callback_pending_size"),
            open_kd_submit_count_address=_json_int(data, "open_kd_submit_count_address"),
            open_kd_submit_count_size=_json_int(data, "open_kd_submit_count_size"),
            open_kd_callback_count_address=_json_int(data, "open_kd_callback_count_address"),
            open_kd_callback_count_size=_json_int(data, "open_kd_callback_count_size"),
            nwc24_output_buffer_address=_json_int(data, "nwc24_output_buffer_address"),
            nwc24_output_buffer_size=_json_int(data, "nwc24_output_buffer_size"),
            nwc24_output_buffer_alignment=_json_int(data, "nwc24_output_buffer_alignment"),
            nwc24_submit_count_address=_json_int(data, "nwc24_submit_count_address"),
            nwc24_submit_count_size=_json_int(data, "nwc24_submit_count_size"),
            nwc24_callback_count_address=_json_int(data, "nwc24_callback_count_address"),
            nwc24_callback_count_size=_json_int(data, "nwc24_callback_count_size"),
            nwc24_synchronous_result_address=_json_int(data, "nwc24_synchronous_result_address"),
            nwc24_synchronous_result_size=_json_int(data, "nwc24_synchronous_result_size"),
            nwc24_callback_result_address=_json_int(data, "nwc24_callback_result_address"),
            nwc24_callback_result_size=_json_int(data, "nwc24_callback_result_size"),
            nwc24_output_digest_address=_json_int(data, "nwc24_output_digest_address"),
            nwc24_output_digest_size=_json_int(data, "nwc24_output_digest_size"),
            open_ip_submit_count_address=_json_int(data, "open_ip_submit_count_address"),
            open_ip_submit_count_size=_json_int(data, "open_ip_submit_count_size"),
            open_ip_callback_count_address=_json_int(data, "open_ip_callback_count_address"),
            open_ip_callback_count_size=_json_int(data, "open_ip_callback_count_size"),
            kd_close_submit_count_address=_json_int(data, "kd_close_submit_count_address"),
            kd_close_submit_count_size=_json_int(data, "kd_close_submit_count_size"),
            kd_close_callback_count_address=_json_int(data, "kd_close_callback_count_address"),
            kd_close_callback_count_size=_json_int(data, "kd_close_callback_count_size"),
            startup_submit_count_address=_json_int(data, "startup_submit_count_address"),
            startup_submit_count_size=_json_int(data, "startup_submit_count_size"),
            startup_callback_count_address=_json_int(data, "startup_callback_count_address"),
            startup_callback_count_size=_json_int(data, "startup_callback_count_size"),
            get_host_id_submit_count_address=_json_int(data, "get_host_id_submit_count_address"),
            get_host_id_submit_count_size=_json_int(data, "get_host_id_submit_count_size"),
            get_host_id_callback_count_address=_json_int(data, "get_host_id_callback_count_address"),
            get_host_id_callback_count_size=_json_int(data, "get_host_id_callback_count_size"),
            socket_submit_count_address=_json_int(data, "socket_submit_count_address"),
            socket_submit_count_size=_json_int(data, "socket_submit_count_size"),
            socket_callback_count_address=_json_int(data, "socket_callback_count_address"),
            socket_callback_count_size=_json_int(data, "socket_callback_count_size"),
            bind_submit_count_address=_json_int(data, "bind_submit_count_address"),
            bind_submit_count_size=_json_int(data, "bind_submit_count_size"),
            bind_callback_count_address=_json_int(data, "bind_callback_count_address"),
            bind_callback_count_size=_json_int(data, "bind_callback_count_size"),
            kd_fd_address=_json_int(data, "kd_fd_address"),
            kd_fd_size=_json_int(data, "kd_fd_size"),
            kd_closed_address=_json_int(data, "kd_closed_address"),
            kd_closed_size=_json_int(data, "kd_closed_size"),
            ip_fd_address=_json_int(data, "ip_fd_address"),
            ip_fd_size=_json_int(data, "ip_fd_size"),
            socket_fd_address=_json_int(data, "socket_fd_address"),
            socket_fd_size=_json_int(data, "socket_fd_size"),
            host_id_address=_json_int(data, "host_id_address"),
            host_id_size=_json_int(data, "host_id_size"),
            host_id_available_address=_json_optional_int(data, "host_id_available_address"),
            host_id_available_size=_json_optional_int(data, "host_id_available_size"),
            host_id_ready_address=_json_optional_int(data, "host_id_ready_address"),
            host_id_ready_size=_json_optional_int(data, "host_id_ready_size"),
            service_started_address=_json_optional_int(data, "service_started_address"),
            service_started_size=_json_optional_int(data, "service_started_size"),
            bound_port_address=_json_int(data, "bound_port_address"),
            bound_port_size=_json_int(data, "bound_port_size"),
            receive_submit_count_address=_json_int(data, "receive_submit_count_address"),
            receive_submit_count_size=_json_int(data, "receive_submit_count_size"),
            send_submit_count_address=_json_int(data, "send_submit_count_address"),
            send_submit_count_size=_json_int(data, "send_submit_count_size"),
            ip_close_submit_count_address=_json_int(data, "ip_close_submit_count_address"),
            ip_close_submit_count_size=_json_int(data, "ip_close_submit_count_size"),
            socket_close_submit_count_address=_json_int(data, "socket_close_submit_count_address"),
            socket_close_submit_count_size=_json_int(data, "socket_close_submit_count_size"),
            receive_count_address=_json_int(data, "receive_count_address"),
            receive_count_size=_json_int(data, "receive_count_size"),
            receive_bytes_address=_json_int(data, "receive_bytes_address"),
            receive_bytes_size=_json_int(data, "receive_bytes_size"),
            send_count_address=_json_int(data, "send_count_address"),
            send_count_size=_json_int(data, "send_count_size"),
            send_bytes_address=_json_int(data, "send_bytes_address"),
            send_bytes_size=_json_int(data, "send_bytes_size"),
            cp3w_magic_hex=_json_optional_string(data, "cp3w_magic_hex"),
            cp3w_protocol_version=_json_optional_int(data, "cp3w_protocol_version"),
            cp3w_header_size=_json_optional_int(data, "cp3w_header_size"),
            cp3w_crc_size=_json_optional_int(data, "cp3w_crc_size"),
            cp3w_crc_initial_value=_json_optional_int(data, "cp3w_crc_initial_value"),
            cp3w_crc_final_xor_value=_json_optional_int(data, "cp3w_crc_final_xor_value"),
            cp3w_crc_polynomial=_json_optional_int(data, "cp3w_crc_polynomial"),
            cp3w_crc_reflected=_json_optional_bool(data, "cp3w_crc_reflected"),
            cp3w_packet_kind_request=_json_optional_int(data, "cp3w_packet_kind_request"),
            cp3w_packet_kind_response=_json_optional_int(data, "cp3w_packet_kind_response"),
            cp3w_response_status_error=_json_optional_int(data, "cp3w_response_status_error"),
            cp3w_command_ping=_json_optional_int(data, "cp3w_command_ping"),
            cp3w_pong_command=_json_optional_int(data, "cp3w_pong_command"),
            cp3w_pong_uses_ping_command=_json_optional_bool(data, "cp3w_pong_uses_ping_command"),
            cp3w_command_reserved_mailbox=_json_optional_int(data, "cp3w_command_reserved_mailbox"),
            cp3w_error_code_unknown_command=_json_optional_int(data, "cp3w_error_code_unknown_command"),
            cp3w_packet_kind_offset=_json_optional_int(data, "cp3w_packet_kind_offset"),
            cp3w_command_offset=_json_optional_int(data, "cp3w_command_offset"),
            cp3w_response_status_offset=_json_optional_int(data, "cp3w_response_status_offset"),
            cp3w_request_id_offset=_json_optional_int(data, "cp3w_request_id_offset"),
            cp3w_payload_length_offset=_json_optional_int(data, "cp3w_payload_length_offset"),
            cp3w_ping_max_payload_length=_json_optional_int(data, "cp3w_ping_max_payload_length"),
            cp3w_request_payload_ascii=_json_optional_string(data, "cp3w_request_payload_ascii"),
            cp3w_response_payload_ascii=_json_optional_string(data, "cp3w_response_payload_ascii"),
            cp3w_unsupported_message_ascii=_json_optional_string(data, "cp3w_unsupported_message_ascii"),
            cp3w_request_payload_length=_json_optional_int(data, "cp3w_request_payload_length"),
            cp3w_response_payload_length=_json_optional_int(data, "cp3w_response_payload_length"),
            prepared_send_length_address=_json_optional_int(data, "prepared_send_length_address"),
            prepared_send_length_size=_json_optional_int(data, "prepared_send_length_size"),
            cp3w_datagrams_processed_address=_json_optional_int(data, "cp3w_datagrams_processed_address"),
            cp3w_datagrams_processed_size=_json_optional_int(data, "cp3w_datagrams_processed_size"),
            cp3w_frames_valid_address=_json_optional_int(data, "cp3w_frames_valid_address"),
            cp3w_frames_valid_size=_json_optional_int(data, "cp3w_frames_valid_size"),
            cp3w_frames_invalid_address=_json_optional_int(data, "cp3w_frames_invalid_address"),
            cp3w_frames_invalid_size=_json_optional_int(data, "cp3w_frames_invalid_size"),
            cp3w_frames_too_short_address=_json_optional_int(data, "cp3w_frames_too_short_address"),
            cp3w_frames_too_short_size=_json_optional_int(data, "cp3w_frames_too_short_size"),
            cp3w_frames_invalid_magic_address=_json_optional_int(data, "cp3w_frames_invalid_magic_address"),
            cp3w_frames_invalid_magic_size=_json_optional_int(data, "cp3w_frames_invalid_magic_size"),
            cp3w_frames_invalid_version_address=_json_optional_int(data, "cp3w_frames_invalid_version_address"),
            cp3w_frames_invalid_version_size=_json_optional_int(data, "cp3w_frames_invalid_version_size"),
            cp3w_frames_unsupported_type_address=_json_optional_int(data, "cp3w_frames_unsupported_type_address"),
            cp3w_frames_unsupported_type_size=_json_optional_int(data, "cp3w_frames_unsupported_type_size"),
            cp3w_frames_nonzero_flags_address=_json_optional_int(data, "cp3w_frames_nonzero_flags_address"),
            cp3w_frames_nonzero_flags_size=_json_optional_int(data, "cp3w_frames_nonzero_flags_size"),
            cp3w_frames_length_mismatch_address=_json_optional_int(data, "cp3w_frames_length_mismatch_address"),
            cp3w_frames_length_mismatch_size=_json_optional_int(data, "cp3w_frames_length_mismatch_size"),
            cp3w_frames_payload_too_large_address=_json_optional_int(data, "cp3w_frames_payload_too_large_address"),
            cp3w_frames_payload_too_large_size=_json_optional_int(data, "cp3w_frames_payload_too_large_size"),
            cp3w_frames_invalid_payload_address=_json_optional_int(data, "cp3w_frames_invalid_payload_address"),
            cp3w_frames_invalid_payload_size=_json_optional_int(data, "cp3w_frames_invalid_payload_size"),
            cp3w_frames_malformed_address=_json_optional_int(data, "cp3w_frames_malformed_address"),
            cp3w_frames_malformed_size=_json_optional_int(data, "cp3w_frames_malformed_size"),
            cp3w_framed_responses_submitted_address=_json_optional_int(data, "cp3w_framed_responses_submitted_address"),
            cp3w_framed_responses_submitted_size=_json_optional_int(data, "cp3w_framed_responses_submitted_size"),
            cp3w_framed_responses_completed_address=_json_optional_int(data, "cp3w_framed_responses_completed_address"),
            cp3w_framed_responses_completed_size=_json_optional_int(data, "cp3w_framed_responses_completed_size"),
            cp3w_last_request_id_address=_json_optional_int(data, "cp3w_last_request_id_address"),
            cp3w_last_request_id_size=_json_optional_int(data, "cp3w_last_request_id_size"),
            cp3w_last_response_id_address=_json_optional_int(data, "cp3w_last_response_id_address"),
            cp3w_last_response_id_size=_json_optional_int(data, "cp3w_last_response_id_size"),
            cp3w_last_message_type_address=_json_optional_int(data, "cp3w_last_message_type_address"),
            cp3w_last_message_type_size=_json_optional_int(data, "cp3w_last_message_type_size"),
            cp3w_last_declared_payload_length_address=_json_optional_int(
                data, "cp3w_last_declared_payload_length_address"
            ),
            cp3w_last_declared_payload_length_size=_json_optional_int(data, "cp3w_last_declared_payload_length_size"),
            cp3w_last_actual_payload_length_address=_json_optional_int(data, "cp3w_last_actual_payload_length_address"),
            cp3w_last_actual_payload_length_size=_json_optional_int(data, "cp3w_last_actual_payload_length_size"),
            cp3w_last_frame_result_address=_json_optional_int(data, "cp3w_last_frame_result_address"),
            cp3w_last_frame_result_size=_json_optional_int(data, "cp3w_last_frame_result_size"),
            cp3w_final_datagram_index_address=_json_optional_int(data, "cp3w_final_datagram_index_address"),
            cp3w_final_datagram_index_size=_json_optional_int(data, "cp3w_final_datagram_index_size"),
            cp3w_requests_dispatched_address=_json_optional_int(data, "cp3w_requests_dispatched_address"),
            cp3w_requests_dispatched_size=_json_optional_int(data, "cp3w_requests_dispatched_size"),
            cp3w_hello_requests_received_address=_json_optional_int(data, "cp3w_hello_requests_received_address"),
            cp3w_hello_requests_received_size=_json_optional_int(data, "cp3w_hello_requests_received_size"),
            cp3w_hello_successes_address=_json_optional_int(data, "cp3w_hello_successes_address"),
            cp3w_hello_successes_size=_json_optional_int(data, "cp3w_hello_successes_size"),
            cp3w_hello_version_rejections_address=_json_optional_int(data, "cp3w_hello_version_rejections_address"),
            cp3w_hello_version_rejections_size=_json_optional_int(data, "cp3w_hello_version_rejections_size"),
            cp3w_hello_responses_submitted_address=_json_optional_int(data, "cp3w_hello_responses_submitted_address"),
            cp3w_hello_responses_submitted_size=_json_optional_int(data, "cp3w_hello_responses_submitted_size"),
            cp3w_hello_responses_completed_address=_json_optional_int(data, "cp3w_hello_responses_completed_address"),
            cp3w_hello_responses_completed_size=_json_optional_int(data, "cp3w_hello_responses_completed_size"),
            cp3w_hello_duplicate_requests_address=_json_optional_int(data, "cp3w_hello_duplicate_requests_address"),
            cp3w_hello_duplicate_requests_size=_json_optional_int(data, "cp3w_hello_duplicate_requests_size"),
            cp3w_hello_renegotiation_rejections_address=_json_optional_int(
                data, "cp3w_hello_renegotiation_rejections_address"
            ),
            cp3w_hello_renegotiation_rejections_size=_json_optional_int(
                data, "cp3w_hello_renegotiation_rejections_size"
            ),
            cp3w_pre_hello_gated_commands_address=_json_optional_int(data, "cp3w_pre_hello_gated_commands_address"),
            cp3w_pre_hello_gated_commands_size=_json_optional_int(data, "cp3w_pre_hello_gated_commands_size"),
            cp3w_not_negotiated_responses_submitted_address=_json_optional_int(
                data, "cp3w_not_negotiated_responses_submitted_address"
            ),
            cp3w_not_negotiated_responses_submitted_size=_json_optional_int(
                data, "cp3w_not_negotiated_responses_submitted_size"
            ),
            cp3w_not_negotiated_responses_completed_address=_json_optional_int(
                data, "cp3w_not_negotiated_responses_completed_address"
            ),
            cp3w_not_negotiated_responses_completed_size=_json_optional_int(
                data, "cp3w_not_negotiated_responses_completed_size"
            ),
            cp3w_ping_requests_received_address=_json_optional_int(data, "cp3w_ping_requests_received_address"),
            cp3w_ping_requests_received_size=_json_optional_int(data, "cp3w_ping_requests_received_size"),
            cp3w_pong_responses_submitted_address=_json_optional_int(data, "cp3w_pong_responses_submitted_address"),
            cp3w_pong_responses_submitted_size=_json_optional_int(data, "cp3w_pong_responses_submitted_size"),
            cp3w_pong_responses_completed_address=_json_optional_int(data, "cp3w_pong_responses_completed_address"),
            cp3w_pong_responses_completed_size=_json_optional_int(data, "cp3w_pong_responses_completed_size"),
            cp3w_unsupported_commands_received_address=_json_optional_int(
                data, "cp3w_unsupported_commands_received_address"
            ),
            cp3w_unsupported_commands_received_size=_json_optional_int(data, "cp3w_unsupported_commands_received_size"),
            cp3w_unsupported_responses_submitted_address=_json_optional_int(
                data, "cp3w_unsupported_responses_submitted_address"
            ),
            cp3w_unsupported_responses_submitted_size=_json_optional_int(
                data, "cp3w_unsupported_responses_submitted_size"
            ),
            cp3w_unsupported_responses_completed_address=_json_optional_int(
                data, "cp3w_unsupported_responses_completed_address"
            ),
            cp3w_unsupported_responses_completed_size=_json_optional_int(
                data, "cp3w_unsupported_responses_completed_size"
            ),
            cp3w_negotiated_flag_address=_json_optional_int(data, "cp3w_negotiated_flag_address"),
            cp3w_negotiated_flag_size=_json_optional_int(data, "cp3w_negotiated_flag_size"),
            cp3w_selected_protocol_version_address=_json_optional_int(data, "cp3w_selected_protocol_version_address"),
            cp3w_selected_protocol_version_size=_json_optional_int(data, "cp3w_selected_protocol_version_size"),
            cp3w_client_nonce_address=_json_optional_int(data, "cp3w_client_nonce_address"),
            cp3w_client_nonce_size=_json_optional_int(data, "cp3w_client_nonce_size"),
            cp3w_client_capabilities_address=_json_optional_int(data, "cp3w_client_capabilities_address"),
            cp3w_client_capabilities_size=_json_optional_int(data, "cp3w_client_capabilities_size"),
            cp3w_runtime_capabilities_address=_json_optional_int(data, "cp3w_runtime_capabilities_address"),
            cp3w_runtime_capabilities_size=_json_optional_int(data, "cp3w_runtime_capabilities_size"),
            cp3w_accepted_capabilities_address=_json_optional_int(data, "cp3w_accepted_capabilities_address"),
            cp3w_accepted_capabilities_size=_json_optional_int(data, "cp3w_accepted_capabilities_size"),
            cp3w_session_id_address=_json_optional_int(data, "cp3w_session_id_address"),
            cp3w_session_id_size=_json_optional_int(data, "cp3w_session_id_size"),
            cp3w_runtime_build_id_address=_json_optional_int(data, "cp3w_runtime_build_id_address"),
            cp3w_runtime_build_id_size=_json_optional_int(data, "cp3w_runtime_build_id_size"),
            cp3w_last_command_address=_json_optional_int(data, "cp3w_last_command_address"),
            cp3w_last_command_size=_json_optional_int(data, "cp3w_last_command_size"),
            cp3w_last_response_status_address=_json_optional_int(data, "cp3w_last_response_status_address"),
            cp3w_last_response_status_size=_json_optional_int(data, "cp3w_last_response_status_size"),
            cp3w_last_ping_payload_length_address=_json_optional_int(data, "cp3w_last_ping_payload_length_address"),
            cp3w_last_ping_payload_length_size=_json_optional_int(data, "cp3w_last_ping_payload_length_size"),
            cp3w_last_dispatch_result_address=_json_optional_int(data, "cp3w_last_dispatch_result_address"),
            cp3w_last_dispatch_result_size=_json_optional_int(data, "cp3w_last_dispatch_result_size"),
            receive_arm_count_address=_json_optional_int(data, "receive_arm_count_address"),
            receive_arm_count_size=_json_optional_int(data, "receive_arm_count_size"),
            receive_rearm_count_address=_json_optional_int(data, "receive_rearm_count_address"),
            receive_rearm_count_size=_json_optional_int(data, "receive_rearm_count_size"),
            configured_exchange_limit_address=_json_optional_int(data, "configured_exchange_limit_address"),
            configured_exchange_limit_size=_json_optional_int(data, "configured_exchange_limit_size"),
            completed_exchange_count_address=_json_optional_int(data, "completed_exchange_count_address"),
            completed_exchange_count_size=_json_optional_int(data, "completed_exchange_count_size"),
            current_exchange_index_address=_json_optional_int(data, "current_exchange_index_address"),
            current_exchange_index_size=_json_optional_int(data, "current_exchange_index_size"),
            last_completed_exchange_index_address=_json_optional_int(data, "last_completed_exchange_index_address"),
            last_completed_exchange_index_size=_json_optional_int(data, "last_completed_exchange_index_size"),
            previous_peer_ipv4_address=_json_optional_int(data, "previous_peer_ipv4_address"),
            previous_peer_ipv4_size=_json_optional_int(data, "previous_peer_ipv4_size"),
            previous_peer_port_address=_json_optional_int(data, "previous_peer_port_address"),
            previous_peer_port_size=_json_optional_int(data, "previous_peer_port_size"),
            rearm_submission_failure_count_address=_json_optional_int(data, "rearm_submission_failure_count_address"),
            rearm_submission_failure_count_size=_json_optional_int(data, "rearm_submission_failure_count_size"),
            loop_complete_transition_count_address=_json_optional_int(data, "loop_complete_transition_count_address"),
            loop_complete_transition_count_size=_json_optional_int(data, "loop_complete_transition_count_size"),
            cleanup_deferred_count_address=_json_optional_int(data, "cleanup_deferred_count_address"),
            cleanup_deferred_count_size=_json_optional_int(data, "cleanup_deferred_count_size"),
            last_receive_length_address=_json_int(data, "last_receive_length_address"),
            last_receive_length_size=_json_int(data, "last_receive_length_size"),
            last_send_length_address=_json_int(data, "last_send_length_address"),
            last_send_length_size=_json_int(data, "last_send_length_size"),
            last_peer_ipv4_address=_json_int(data, "last_peer_ipv4_address"),
            last_peer_ipv4_size=_json_int(data, "last_peer_ipv4_size"),
            last_peer_port_address=_json_int(data, "last_peer_port_address"),
            last_peer_port_size=_json_int(data, "last_peer_port_size"),
            last_peer_family_address=_json_int(data, "last_peer_family_address"),
            last_peer_family_size=_json_int(data, "last_peer_family_size"),
            last_poll_action_address=_json_int(data, "last_poll_action_address"),
            last_poll_action_size=_json_int(data, "last_poll_action_size"),
            last_submit_result_address=_json_int(data, "last_submit_result_address"),
            last_submit_result_size=_json_int(data, "last_submit_result_size"),
            polls_while_receive_pending_address=_json_optional_int(data, "polls_while_receive_pending_address"),
            polls_while_receive_pending_size=_json_optional_int(data, "polls_while_receive_pending_size"),
            polls_after_loop_complete_address=_json_optional_int(data, "polls_after_loop_complete_address"),
            polls_after_loop_complete_size=_json_optional_int(data, "polls_after_loop_complete_size"),
            last_receive_preview_address=_json_int(data, "last_receive_preview_address"),
            last_receive_preview_size=_json_int(data, "last_receive_preview_size"),
            last_send_preview_address=_json_int(data, "last_send_preview_address"),
            last_send_preview_size=_json_int(data, "last_send_preview_size"),
            open_kd_submit_result_address=_json_optional_int(data, "open_kd_submit_result_address"),
            open_kd_submit_result_size=_json_optional_int(data, "open_kd_submit_result_size"),
            open_kd_callback_result_address=_json_optional_int(data, "open_kd_callback_result_address"),
            open_kd_callback_result_size=_json_optional_int(data, "open_kd_callback_result_size"),
            open_kd_submit_generation_address=_json_optional_int(data, "open_kd_submit_generation_address"),
            open_kd_submit_generation_size=_json_optional_int(data, "open_kd_submit_generation_size"),
            open_kd_callback_generation_address=_json_optional_int(data, "open_kd_callback_generation_address"),
            open_kd_callback_generation_size=_json_optional_int(data, "open_kd_callback_generation_size"),
            nwc24_submit_generation_address=_json_optional_int(data, "nwc24_submit_generation_address"),
            nwc24_submit_generation_size=_json_optional_int(data, "nwc24_submit_generation_size"),
            nwc24_callback_generation_address=_json_optional_int(data, "nwc24_callback_generation_address"),
            nwc24_callback_generation_size=_json_optional_int(data, "nwc24_callback_generation_size"),
            open_ip_submit_result_address=_json_optional_int(data, "open_ip_submit_result_address"),
            open_ip_submit_result_size=_json_optional_int(data, "open_ip_submit_result_size"),
            open_ip_callback_result_address=_json_optional_int(data, "open_ip_callback_result_address"),
            open_ip_callback_result_size=_json_optional_int(data, "open_ip_callback_result_size"),
            open_ip_submit_generation_address=_json_optional_int(data, "open_ip_submit_generation_address"),
            open_ip_submit_generation_size=_json_optional_int(data, "open_ip_submit_generation_size"),
            open_ip_callback_generation_address=_json_optional_int(data, "open_ip_callback_generation_address"),
            open_ip_callback_generation_size=_json_optional_int(data, "open_ip_callback_generation_size"),
            open_ip_path_pointer_address=_json_optional_int(data, "open_ip_path_pointer_address"),
            open_ip_path_pointer_size=_json_optional_int(data, "open_ip_path_pointer_size"),
            open_ip_path_length_address=_json_optional_int(data, "open_ip_path_length_address"),
            open_ip_path_length_size=_json_optional_int(data, "open_ip_path_length_size"),
            open_ip_mode_value_address=_json_optional_int(data, "open_ip_mode_value_address"),
            open_ip_mode_value_size=_json_optional_int(data, "open_ip_mode_value_size"),
            open_ip_callback_pointer_address=_json_optional_int(data, "open_ip_callback_pointer_address"),
            open_ip_callback_pointer_size=_json_optional_int(data, "open_ip_callback_pointer_size"),
            open_ip_context_pointer_address=_json_optional_int(data, "open_ip_context_pointer_address"),
            open_ip_context_pointer_size=_json_optional_int(data, "open_ip_context_pointer_size"),
            open_ip_callback_exit_count_address=_json_optional_int(data, "open_ip_callback_exit_count_address"),
            open_ip_callback_exit_count_size=_json_optional_int(data, "open_ip_callback_exit_count_size"),
            open_ip_stale_callback_count_address=_json_optional_int(data, "open_ip_stale_callback_count_address"),
            open_ip_stale_callback_count_size=_json_optional_int(data, "open_ip_stale_callback_count_size"),
            open_ip_duplicate_callback_count_address=_json_optional_int(
                data, "open_ip_duplicate_callback_count_address"
            ),
            open_ip_duplicate_callback_count_size=_json_optional_int(data, "open_ip_duplicate_callback_count_size"),
            ip_fd_before_open_ip_address=_json_optional_int(data, "ip_fd_before_open_ip_address"),
            ip_fd_before_open_ip_size=_json_optional_int(data, "ip_fd_before_open_ip_size"),
            kd_close_submit_result_address=_json_optional_int(data, "kd_close_submit_result_address"),
            kd_close_submit_result_size=_json_optional_int(data, "kd_close_submit_result_size"),
            kd_close_callback_result_address=_json_optional_int(data, "kd_close_callback_result_address"),
            kd_close_callback_result_size=_json_optional_int(data, "kd_close_callback_result_size"),
            kd_close_submit_generation_address=_json_optional_int(data, "kd_close_submit_generation_address"),
            kd_close_submit_generation_size=_json_optional_int(data, "kd_close_submit_generation_size"),
            kd_close_callback_generation_address=_json_optional_int(data, "kd_close_callback_generation_address"),
            kd_close_callback_generation_size=_json_optional_int(data, "kd_close_callback_generation_size"),
            kd_close_submitted_fd_address=_json_optional_int(data, "kd_close_submitted_fd_address"),
            kd_close_submitted_fd_size=_json_optional_int(data, "kd_close_submitted_fd_size"),
            kd_fd_before_close_address=_json_optional_int(data, "kd_fd_before_close_address"),
            kd_fd_before_close_size=_json_optional_int(data, "kd_fd_before_close_size"),
            kd_fd_after_close_address=_json_optional_int(data, "kd_fd_after_close_address"),
            kd_fd_after_close_size=_json_optional_int(data, "kd_fd_after_close_size"),
            startup_submit_result_address=_json_optional_int(data, "startup_submit_result_address"),
            startup_submit_result_size=_json_optional_int(data, "startup_submit_result_size"),
            startup_callback_result_address=_json_optional_int(data, "startup_callback_result_address"),
            startup_callback_result_size=_json_optional_int(data, "startup_callback_result_size"),
            startup_submit_generation_address=_json_optional_int(data, "startup_submit_generation_address"),
            startup_submit_generation_size=_json_optional_int(data, "startup_submit_generation_size"),
            startup_callback_generation_address=_json_optional_int(data, "startup_callback_generation_address"),
            startup_callback_generation_size=_json_optional_int(data, "startup_callback_generation_size"),
            startup_target_address=_json_optional_int(data, "startup_target_address"),
            startup_target_size=_json_optional_int(data, "startup_target_size"),
            startup_command_address=_json_optional_int(data, "startup_command_address"),
            startup_command_size=_json_optional_int(data, "startup_command_size"),
            startup_submitted_fd_address=_json_optional_int(data, "startup_submitted_fd_address"),
            startup_submitted_fd_size=_json_optional_int(data, "startup_submitted_fd_size"),
            startup_callback_pointer_address=_json_optional_int(data, "startup_callback_pointer_address"),
            startup_callback_pointer_size=_json_optional_int(data, "startup_callback_pointer_size"),
            startup_context_pointer_address=_json_optional_int(data, "startup_context_pointer_address"),
            startup_context_pointer_size=_json_optional_int(data, "startup_context_pointer_size"),
            startup_callback_exit_count_address=_json_optional_int(data, "startup_callback_exit_count_address"),
            startup_callback_exit_count_size=_json_optional_int(data, "startup_callback_exit_count_size"),
            startup_stale_callback_count_address=_json_optional_int(data, "startup_stale_callback_count_address"),
            startup_stale_callback_count_size=_json_optional_int(data, "startup_stale_callback_count_size"),
            startup_duplicate_callback_count_address=_json_optional_int(
                data, "startup_duplicate_callback_count_address"
            ),
            startup_duplicate_callback_count_size=_json_optional_int(data, "startup_duplicate_callback_count_size"),
            startup_service_started_before_submit_address=_json_optional_int(
                data, "startup_service_started_before_submit_address"
            ),
            startup_service_started_before_submit_size=_json_optional_int(
                data, "startup_service_started_before_submit_size"
            ),
            startup_service_started_after_completion_address=_json_optional_int(
                data, "startup_service_started_after_completion_address"
            ),
            startup_service_started_after_completion_size=_json_optional_int(
                data, "startup_service_started_after_completion_size"
            ),
            ip_fd_before_startup_address=_json_optional_int(data, "ip_fd_before_startup_address"),
            ip_fd_before_startup_size=_json_optional_int(data, "ip_fd_before_startup_size"),
            ip_fd_after_startup_address=_json_optional_int(data, "ip_fd_after_startup_address"),
            ip_fd_after_startup_size=_json_optional_int(data, "ip_fd_after_startup_size"),
            startup_pending_before_submit_address=_json_optional_int(data, "startup_pending_before_submit_address"),
            startup_pending_before_submit_size=_json_optional_int(data, "startup_pending_before_submit_size"),
            startup_pending_after_completion_address=_json_optional_int(
                data, "startup_pending_after_completion_address"
            ),
            startup_pending_after_completion_size=_json_optional_int(data, "startup_pending_after_completion_size"),
            startup_phase_before_submit_address=_json_optional_int(data, "startup_phase_before_submit_address"),
            startup_phase_before_submit_size=_json_optional_int(data, "startup_phase_before_submit_size"),
            startup_phase_after_completion_address=_json_optional_int(data, "startup_phase_after_completion_address"),
            startup_phase_after_completion_size=_json_optional_int(data, "startup_phase_after_completion_size"),
            startup_pre_call_args_address=_json_optional_int(data, "startup_pre_call_args_address"),
            startup_pre_call_args_size=_json_optional_int(data, "startup_pre_call_args_size"),
            get_host_id_submit_result_address=_json_optional_int(data, "get_host_id_submit_result_address"),
            get_host_id_submit_result_size=_json_optional_int(data, "get_host_id_submit_result_size"),
            get_host_id_callback_result_address=_json_optional_int(data, "get_host_id_callback_result_address"),
            get_host_id_callback_result_size=_json_optional_int(data, "get_host_id_callback_result_size"),
            get_host_id_submit_generation_address=_json_optional_int(data, "get_host_id_submit_generation_address"),
            get_host_id_submit_generation_size=_json_optional_int(data, "get_host_id_submit_generation_size"),
            get_host_id_callback_generation_address=_json_optional_int(data, "get_host_id_callback_generation_address"),
            get_host_id_callback_generation_size=_json_optional_int(data, "get_host_id_callback_generation_size"),
            get_host_id_target_address=_json_optional_int(data, "get_host_id_target_address"),
            get_host_id_target_size=_json_optional_int(data, "get_host_id_target_size"),
            get_host_id_command_address=_json_optional_int(data, "get_host_id_command_address"),
            get_host_id_command_size=_json_optional_int(data, "get_host_id_command_size"),
            get_host_id_submitted_fd_address=_json_optional_int(data, "get_host_id_submitted_fd_address"),
            get_host_id_submitted_fd_size=_json_optional_int(data, "get_host_id_submitted_fd_size"),
            get_host_id_callback_pointer_address=_json_optional_int(data, "get_host_id_callback_pointer_address"),
            get_host_id_callback_pointer_size=_json_optional_int(data, "get_host_id_callback_pointer_size"),
            get_host_id_context_pointer_address=_json_optional_int(data, "get_host_id_context_pointer_address"),
            get_host_id_context_pointer_size=_json_optional_int(data, "get_host_id_context_pointer_size"),
            get_host_id_callback_exit_count_address=_json_optional_int(data, "get_host_id_callback_exit_count_address"),
            get_host_id_callback_exit_count_size=_json_optional_int(data, "get_host_id_callback_exit_count_size"),
            get_host_id_stale_callback_count_address=_json_optional_int(
                data, "get_host_id_stale_callback_count_address"
            ),
            get_host_id_stale_callback_count_size=_json_optional_int(data, "get_host_id_stale_callback_count_size"),
            get_host_id_duplicate_callback_count_address=_json_optional_int(
                data, "get_host_id_duplicate_callback_count_address"
            ),
            get_host_id_duplicate_callback_count_size=_json_optional_int(
                data, "get_host_id_duplicate_callback_count_size"
            ),
            get_host_id_service_started_before_submit_address=_json_optional_int(
                data, "get_host_id_service_started_before_submit_address"
            ),
            get_host_id_service_started_before_submit_size=_json_optional_int(
                data, "get_host_id_service_started_before_submit_size"
            ),
            get_host_id_service_started_after_completion_address=_json_optional_int(
                data, "get_host_id_service_started_after_completion_address"
            ),
            get_host_id_service_started_after_completion_size=_json_optional_int(
                data, "get_host_id_service_started_after_completion_size"
            ),
            ip_fd_before_get_host_id_address=_json_optional_int(data, "ip_fd_before_get_host_id_address"),
            ip_fd_before_get_host_id_size=_json_optional_int(data, "ip_fd_before_get_host_id_size"),
            ip_fd_after_get_host_id_address=_json_optional_int(data, "ip_fd_after_get_host_id_address"),
            ip_fd_after_get_host_id_size=_json_optional_int(data, "ip_fd_after_get_host_id_size"),
            get_host_id_pending_before_submit_address=_json_optional_int(
                data, "get_host_id_pending_before_submit_address"
            ),
            get_host_id_pending_before_submit_size=_json_optional_int(data, "get_host_id_pending_before_submit_size"),
            get_host_id_pending_after_completion_address=_json_optional_int(
                data, "get_host_id_pending_after_completion_address"
            ),
            get_host_id_pending_after_completion_size=_json_optional_int(
                data, "get_host_id_pending_after_completion_size"
            ),
            get_host_id_phase_before_submit_address=_json_optional_int(data, "get_host_id_phase_before_submit_address"),
            get_host_id_phase_before_submit_size=_json_optional_int(data, "get_host_id_phase_before_submit_size"),
            get_host_id_phase_after_completion_address=_json_optional_int(
                data, "get_host_id_phase_after_completion_address"
            ),
            get_host_id_phase_after_completion_size=_json_optional_int(data, "get_host_id_phase_after_completion_size"),
            get_host_id_pre_call_args_address=_json_optional_int(data, "get_host_id_pre_call_args_address"),
            get_host_id_pre_call_args_size=_json_optional_int(data, "get_host_id_pre_call_args_size"),
            socket_submit_result_address=_json_optional_int(data, "socket_submit_result_address"),
            socket_submit_result_size=_json_optional_int(data, "socket_submit_result_size"),
            socket_callback_result_address=_json_optional_int(data, "socket_callback_result_address"),
            socket_callback_result_size=_json_optional_int(data, "socket_callback_result_size"),
            socket_submit_generation_address=_json_optional_int(data, "socket_submit_generation_address"),
            socket_submit_generation_size=_json_optional_int(data, "socket_submit_generation_size"),
            socket_callback_generation_address=_json_optional_int(data, "socket_callback_generation_address"),
            socket_callback_generation_size=_json_optional_int(data, "socket_callback_generation_size"),
            socket_target_address=_json_optional_int(data, "socket_target_address"),
            socket_target_size=_json_optional_int(data, "socket_target_size"),
            socket_command_address=_json_optional_int(data, "socket_command_address"),
            socket_command_size=_json_optional_int(data, "socket_command_size"),
            socket_submitted_fd_address=_json_optional_int(data, "socket_submitted_fd_address"),
            socket_submitted_fd_size=_json_optional_int(data, "socket_submitted_fd_size"),
            socket_callback_pointer_address=_json_optional_int(data, "socket_callback_pointer_address"),
            socket_callback_pointer_size=_json_optional_int(data, "socket_callback_pointer_size"),
            socket_context_pointer_address=_json_optional_int(data, "socket_context_pointer_address"),
            socket_context_pointer_size=_json_optional_int(data, "socket_context_pointer_size"),
            socket_callback_exit_count_address=_json_optional_int(data, "socket_callback_exit_count_address"),
            socket_callback_exit_count_size=_json_optional_int(data, "socket_callback_exit_count_size"),
            socket_stale_callback_count_address=_json_optional_int(data, "socket_stale_callback_count_address"),
            socket_stale_callback_count_size=_json_optional_int(data, "socket_stale_callback_count_size"),
            socket_duplicate_callback_count_address=_json_optional_int(data, "socket_duplicate_callback_count_address"),
            socket_duplicate_callback_count_size=_json_optional_int(data, "socket_duplicate_callback_count_size"),
            socket_fd_before_submit_address=_json_optional_int(data, "socket_fd_before_submit_address"),
            socket_fd_before_submit_size=_json_optional_int(data, "socket_fd_before_submit_size"),
            socket_fd_after_completion_address=_json_optional_int(data, "socket_fd_after_completion_address"),
            socket_fd_after_completion_size=_json_optional_int(data, "socket_fd_after_completion_size"),
            socket_request_address_address=_json_optional_int(data, "socket_request_address_address"),
            socket_request_address_size=_json_optional_int(data, "socket_request_address_size"),
            socket_request_storage_size_address=_json_optional_int(data, "socket_request_storage_size_address"),
            socket_request_storage_size_size=_json_optional_int(data, "socket_request_storage_size_size"),
            socket_request_logical_size_address=_json_optional_int(data, "socket_request_logical_size_address"),
            socket_request_logical_size_size=_json_optional_int(data, "socket_request_logical_size_size"),
            socket_request_alignment_address=_json_optional_int(data, "socket_request_alignment_address"),
            socket_request_alignment_size=_json_optional_int(data, "socket_request_alignment_size"),
            socket_family_value_address=_json_optional_int(data, "socket_family_value_address"),
            socket_family_value_size=_json_optional_int(data, "socket_family_value_size"),
            socket_type_value_address=_json_optional_int(data, "socket_type_value_address"),
            socket_type_value_size=_json_optional_int(data, "socket_type_value_size"),
            socket_protocol_value_address=_json_optional_int(data, "socket_protocol_value_address"),
            socket_protocol_value_size=_json_optional_int(data, "socket_protocol_value_size"),
            socket_descriptor_valid_address=_json_optional_int(data, "socket_descriptor_valid_address"),
            socket_descriptor_valid_size=_json_optional_int(data, "socket_descriptor_valid_size"),
            socket_ready_address=_json_optional_int(data, "socket_ready_address"),
            socket_ready_size=_json_optional_int(data, "socket_ready_size"),
            socket_request_bytes_address=_json_optional_int(data, "socket_request_bytes_address"),
            socket_request_bytes_size=_json_optional_int(data, "socket_request_bytes_size"),
            socket_pre_call_args_address=_json_optional_int(data, "socket_pre_call_args_address"),
            socket_pre_call_args_size=_json_optional_int(data, "socket_pre_call_args_size"),
            bind_submit_result_address=_json_optional_int(data, "bind_submit_result_address"),
            bind_submit_result_size=_json_optional_int(data, "bind_submit_result_size"),
            bind_callback_result_address=_json_optional_int(data, "bind_callback_result_address"),
            bind_callback_result_size=_json_optional_int(data, "bind_callback_result_size"),
            bind_submit_generation_address=_json_optional_int(data, "bind_submit_generation_address"),
            bind_submit_generation_size=_json_optional_int(data, "bind_submit_generation_size"),
            bind_callback_generation_address=_json_optional_int(data, "bind_callback_generation_address"),
            bind_callback_generation_size=_json_optional_int(data, "bind_callback_generation_size"),
            bind_target_address=_json_optional_int(data, "bind_target_address"),
            bind_target_size=_json_optional_int(data, "bind_target_size"),
            bind_command_address=_json_optional_int(data, "bind_command_address"),
            bind_command_size=_json_optional_int(data, "bind_command_size"),
            bind_submitted_fd_address=_json_optional_int(data, "bind_submitted_fd_address"),
            bind_submitted_fd_size=_json_optional_int(data, "bind_submitted_fd_size"),
            bind_callback_pointer_address=_json_optional_int(data, "bind_callback_pointer_address"),
            bind_callback_pointer_size=_json_optional_int(data, "bind_callback_pointer_size"),
            bind_context_pointer_address=_json_optional_int(data, "bind_context_pointer_address"),
            bind_context_pointer_size=_json_optional_int(data, "bind_context_pointer_size"),
            bind_callback_exit_count_address=_json_optional_int(data, "bind_callback_exit_count_address"),
            bind_callback_exit_count_size=_json_optional_int(data, "bind_callback_exit_count_size"),
            bind_stale_callback_count_address=_json_optional_int(data, "bind_stale_callback_count_address"),
            bind_stale_callback_count_size=_json_optional_int(data, "bind_stale_callback_count_size"),
            bind_duplicate_callback_count_address=_json_optional_int(data, "bind_duplicate_callback_count_address"),
            bind_duplicate_callback_count_size=_json_optional_int(data, "bind_duplicate_callback_count_size"),
            bind_request_address_address=_json_optional_int(data, "bind_request_address_address"),
            bind_request_address_size=_json_optional_int(data, "bind_request_address_size"),
            bind_request_storage_size_address=_json_optional_int(data, "bind_request_storage_size_address"),
            bind_request_storage_size_size=_json_optional_int(data, "bind_request_storage_size_size"),
            bind_request_logical_size_address=_json_optional_int(data, "bind_request_logical_size_address"),
            bind_request_logical_size_size=_json_optional_int(data, "bind_request_logical_size_size"),
            bind_request_alignment_address=_json_optional_int(data, "bind_request_alignment_address"),
            bind_request_alignment_size=_json_optional_int(data, "bind_request_alignment_size"),
            bind_sockaddr_length_address=_json_optional_int(data, "bind_sockaddr_length_address"),
            bind_sockaddr_length_size=_json_optional_int(data, "bind_sockaddr_length_size"),
            bind_family_value_address=_json_optional_int(data, "bind_family_value_address"),
            bind_family_value_size=_json_optional_int(data, "bind_family_value_size"),
            bind_port_value_address=_json_optional_int(data, "bind_port_value_address"),
            bind_port_value_size=_json_optional_int(data, "bind_port_value_size"),
            bind_address_value_address=_json_optional_int(data, "bind_address_value_address"),
            bind_address_value_size=_json_optional_int(data, "bind_address_value_size"),
            bind_request_bytes_address=_json_optional_int(data, "bind_request_bytes_address"),
            bind_request_bytes_size=_json_optional_int(data, "bind_request_bytes_size"),
            bind_pre_call_args_address=_json_optional_int(data, "bind_pre_call_args_address"),
            bind_pre_call_args_size=_json_optional_int(data, "bind_pre_call_args_size"),
            cleanup_close_callback_count_address=_json_optional_int(data, "cleanup_close_callback_count_address"),
            cleanup_close_callback_count_size=_json_optional_int(data, "cleanup_close_callback_count_size"),
            cleanup_close_submit_result_address=_json_optional_int(data, "cleanup_close_submit_result_address"),
            cleanup_close_submit_result_size=_json_optional_int(data, "cleanup_close_submit_result_size"),
            cleanup_close_callback_result_address=_json_optional_int(data, "cleanup_close_callback_result_address"),
            cleanup_close_callback_result_size=_json_optional_int(data, "cleanup_close_callback_result_size"),
            cleanup_close_submit_generation_address=_json_optional_int(data, "cleanup_close_submit_generation_address"),
            cleanup_close_submit_generation_size=_json_optional_int(data, "cleanup_close_submit_generation_size"),
            cleanup_close_callback_generation_address=_json_optional_int(
                data, "cleanup_close_callback_generation_address"
            ),
            cleanup_close_callback_generation_size=_json_optional_int(data, "cleanup_close_callback_generation_size"),
            cleanup_close_target_address=_json_optional_int(data, "cleanup_close_target_address"),
            cleanup_close_target_size=_json_optional_int(data, "cleanup_close_target_size"),
            cleanup_close_command_address=_json_optional_int(data, "cleanup_close_command_address"),
            cleanup_close_command_size=_json_optional_int(data, "cleanup_close_command_size"),
            cleanup_close_submitted_fd_address=_json_optional_int(data, "cleanup_close_submitted_fd_address"),
            cleanup_close_submitted_fd_size=_json_optional_int(data, "cleanup_close_submitted_fd_size"),
            cleanup_close_callback_pointer_address=_json_optional_int(data, "cleanup_close_callback_pointer_address"),
            cleanup_close_callback_pointer_size=_json_optional_int(data, "cleanup_close_callback_pointer_size"),
            cleanup_close_context_pointer_address=_json_optional_int(data, "cleanup_close_context_pointer_address"),
            cleanup_close_context_pointer_size=_json_optional_int(data, "cleanup_close_context_pointer_size"),
            cleanup_close_callback_exit_count_address=_json_optional_int(
                data, "cleanup_close_callback_exit_count_address"
            ),
            cleanup_close_callback_exit_count_size=_json_optional_int(data, "cleanup_close_callback_exit_count_size"),
            cleanup_close_stale_callback_count_address=_json_optional_int(
                data, "cleanup_close_stale_callback_count_address"
            ),
            cleanup_close_stale_callback_count_size=_json_optional_int(data, "cleanup_close_stale_callback_count_size"),
            cleanup_close_duplicate_callback_count_address=_json_optional_int(
                data, "cleanup_close_duplicate_callback_count_address"
            ),
            cleanup_close_duplicate_callback_count_size=_json_optional_int(
                data, "cleanup_close_duplicate_callback_count_size"
            ),
            cleanup_close_request_address_address=_json_optional_int(data, "cleanup_close_request_address_address"),
            cleanup_close_request_address_size=_json_optional_int(data, "cleanup_close_request_address_size"),
            cleanup_close_request_storage_size_address=_json_optional_int(
                data, "cleanup_close_request_storage_size_address"
            ),
            cleanup_close_request_storage_size_size=_json_optional_int(data, "cleanup_close_request_storage_size_size"),
            cleanup_close_request_logical_size_address=_json_optional_int(
                data, "cleanup_close_request_logical_size_address"
            ),
            cleanup_close_request_logical_size_size=_json_optional_int(data, "cleanup_close_request_logical_size_size"),
            cleanup_close_request_alignment_address=_json_optional_int(data, "cleanup_close_request_alignment_address"),
            cleanup_close_request_alignment_size=_json_optional_int(data, "cleanup_close_request_alignment_size"),
            cleanup_close_request_value_address=_json_optional_int(data, "cleanup_close_request_value_address"),
            cleanup_close_request_value_size=_json_optional_int(data, "cleanup_close_request_value_size"),
            cleanup_close_request_bytes_address=_json_optional_int(data, "cleanup_close_request_bytes_address"),
            cleanup_close_request_bytes_size=_json_optional_int(data, "cleanup_close_request_bytes_size"),
            cleanup_close_pre_call_args_address=_json_optional_int(data, "cleanup_close_pre_call_args_address"),
            cleanup_close_pre_call_args_size=_json_optional_int(data, "cleanup_close_pre_call_args_size"),
            bound_flag_address=_json_optional_int(data, "bound_flag_address"),
            bound_flag_size=_json_optional_int(data, "bound_flag_size"),
            bound_address_address=_json_optional_int(data, "bound_address_address"),
            bound_address_size=_json_optional_int(data, "bound_address_size"),
            socket_closed_after_bind_failure_address=_json_optional_int(
                data, "socket_closed_after_bind_failure_address"
            ),
            socket_closed_after_bind_failure_size=_json_optional_int(data, "socket_closed_after_bind_failure_size"),
            socket_leak_detected_address=_json_optional_int(data, "socket_leak_detected_address"),
            socket_leak_detected_size=_json_optional_int(data, "socket_leak_detected_size"),
            cp3w_game_identity=_json_optional_game_identity(data, "cp3w_game_identity"),
            cp3w_inventory=_json_optional_inventory(data, "cp3w_inventory"),
            network_diagnostics_address=_json_optional_int(data, "network_diagnostics_address"),
            network_diagnostics_size=_json_optional_int(data, "network_diagnostics_size"),
            network_diagnostics_version=_json_optional_int(data, "network_diagnostics_version"),
        )


@dataclasses.dataclass(frozen=True)
class Prime3RetailIosWrapperMetadata:
    supported_dol_sha256: str
    open_async_address: int
    open_address: int
    close_async_address: int
    close_address: int
    async_close_address: int
    async_close_extent: str
    async_close_argument_count: int
    async_close_stack_argument_count: int
    async_close_operation: int
    async_close_fingerprint_sha256: str
    async_close_prototype: str
    async_close_register_arguments: tuple[str, ...]
    async_close_confidence: str
    read_async_address: int
    read_sync_address: int
    write_async_address: int
    write_sync_address: int
    seek_async_address: int
    seek_sync_address: int
    confirmed_ioctl_async_address: int
    confirmed_ioctl_sync_address: int
    confirmed_ioctlv_async_address: int
    confirmed_ioctlv_sync_address: int
    async_ioctl_address: int
    async_ioctl_extent: str
    async_ioctl_argument_count: int
    async_ioctl_stack_argument_count: int
    async_ioctl_operation: int
    async_ioctl_confidence: str
    confirmed_ioctl_async_fingerprint_sha256: str
    confirmed_ioctl_async_prototype: str
    confirmed_ioctl_async_register_arguments: tuple[str, ...]
    confirmed_ioctl_async_stack_arguments: tuple[str, ...]
    request_field_offsets: tuple[str, ...]
    open_async_guard_words: tuple[int, ...]
    callback_signature: str
    preserved_registers: tuple[str, ...]
    submit_helper_address: int
    request_allocator_address: int
    evidence_source: str
    confidence: str

    def validate(self) -> None:  # noqa: C901
        if len(self.supported_dol_sha256) != 64:
            raise Prime3DolPatchError("Retail IOS wrapper metadata requires a SHA-256 DOL fingerprint.")
        addresses = (
            self.open_async_address,
            self.open_address,
            self.close_async_address,
            self.close_address,
            self.async_close_address,
            self.read_async_address,
            self.read_sync_address,
            self.write_async_address,
            self.write_sync_address,
            self.seek_async_address,
            self.seek_sync_address,
            self.confirmed_ioctl_async_address,
            self.confirmed_ioctl_sync_address,
            self.confirmed_ioctlv_async_address,
            self.confirmed_ioctlv_sync_address,
            self.async_ioctl_address,
            self.submit_helper_address,
            self.request_allocator_address,
        )
        for address in addresses:
            if address <= 0 or address > 0xFFFFFFFF:
                raise Prime3DolPatchError(f"Retail IOS wrapper address is outside the 32-bit range: {address!r}")
        if len(self.open_async_guard_words) < 2:
            raise Prime3DolPatchError("Retail IOS wrapper metadata requires at least two guarded entry words.")
        if self.callback_signature != "s32 callback(s32 result, void *userdata)":
            raise Prime3DolPatchError("Retail IOS wrapper callback signature metadata is unexpected.")
        if tuple(self.preserved_registers) != ("r2", "r13"):
            raise Prime3DolPatchError("Retail IOS wrapper metadata must document preserved game SDA registers.")
        if self.async_close_address != 0x805048A0 or self.async_close_address != self.close_async_address:
            raise Prime3DolPatchError("Retail IOS metadata must identify the verified async close wrapper.")
        if self.async_close_extent != "0x805048A0..0x80504960":
            raise Prime3DolPatchError("Retail IOS async close metadata has an unexpected extent.")
        if self.async_close_argument_count != 3 or self.async_close_stack_argument_count != 0:
            raise Prime3DolPatchError("Retail IOS async close metadata has an unexpected ABI arity.")
        if self.async_close_operation != 2 or self.async_close_confidence != "verified":
            raise Prime3DolPatchError("Retail IOS async close metadata is not verified for operation 2.")
        if self.async_close_fingerprint_sha256 != "cad7a4b8950241515a9399d51c69d5680bba41fe060c37f5b6953effcdcb1288":
            raise Prime3DolPatchError("Retail IOS async close metadata has an unexpected function fingerprint.")
        if self.async_close_prototype != "s32 close_async(s32 fd, completion_fn completion, void *userdata)":
            raise Prime3DolPatchError("Retail IOS async close metadata has an unexpected prototype.")
        if self.async_close_register_arguments != ("r3=fd", "r4=completion", "r5=userdata"):
            raise Prime3DolPatchError("Retail IOS async close metadata has unexpected register argument placement.")
        expected_ioctl_async_fingerprint = "031342395575c5542428b9edfcd4fd3bf9633bfb54bd39726d3766b3e6f3b17b"
        if self.confirmed_ioctl_async_fingerprint_sha256 != expected_ioctl_async_fingerprint:
            raise Prime3DolPatchError("Retail IOS ioctl metadata has an unexpected function fingerprint.")
        if self.async_ioctl_address != 0x80504FE0 or self.async_ioctl_address == self.read_async_address:
            raise Prime3DolPatchError("Retail IOS metadata must identify the verified async ioctl wrapper.")
        if self.async_ioctl_extent != "0x80504FE0..0x80505118":
            raise Prime3DolPatchError("Retail IOS async ioctl metadata has an unexpected extent.")
        if self.async_ioctl_argument_count != 8 or self.async_ioctl_stack_argument_count != 0:
            raise Prime3DolPatchError("Retail IOS async ioctl metadata has an unexpected ABI arity.")
        if self.async_ioctl_operation != 6 or self.async_ioctl_confidence != "verified":
            raise Prime3DolPatchError("Retail IOS async ioctl metadata is not verified for operation 6.")
        if self.confirmed_ioctl_async_address != self.async_ioctl_address:
            raise Prime3DolPatchError("Retail IOS async ioctl metadata disagrees with the confirmed wrapper address.")
        expected_prototype = (
            "s32 ioctl_async(s32 fd, u32 command, const void *input, u32 input_length, "
            "void *output, u32 output_length, completion_fn completion, void *userdata)"
        )
        if self.confirmed_ioctl_async_prototype != expected_prototype:
            raise Prime3DolPatchError("Retail IOS ioctl metadata has an unexpected asynchronous prototype.")
        if self.confirmed_ioctl_async_register_arguments != (
            "r3=fd",
            "r4=command",
            "r5=input",
            "r6=input_length",
            "r7=output",
            "r8=output_length",
            "r9=completion",
            "r10=userdata",
        ):
            raise Prime3DolPatchError("Retail IOS ioctl metadata has unexpected register argument placement.")
        if self.confirmed_ioctl_async_stack_arguments:
            raise Prime3DolPatchError("Retail IOS ioctl metadata must not claim stack-passed arguments.")
        if self.request_field_offsets != (
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
        ):
            raise Prime3DolPatchError("Retail IOS wrapper metadata has an unexpected request-field map.")
        if not self.evidence_source:
            raise Prime3DolPatchError("Retail IOS wrapper metadata requires an evidence source.")
        if self.confidence not in {"candidate", "verified"}:
            raise Prime3DolPatchError(f"Unsupported retail IOS wrapper confidence {self.confidence!r}.")

    def to_json_dict(self) -> dict[str, object]:
        return {
            **dataclasses.asdict(self),
            "open_async_guard_words": list(self.open_async_guard_words),
            "preserved_registers": list(self.preserved_registers),
            "confirmed_ioctl_async_register_arguments": list(self.confirmed_ioctl_async_register_arguments),
            "confirmed_ioctl_async_stack_arguments": list(self.confirmed_ioctl_async_stack_arguments),
            "request_field_offsets": list(self.request_field_offsets),
        }

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RetailIosWrapperMetadata:
        legacy_keys = (
            "ioctl_async_address",
            "ioctl_address",
            "ioctlv_async_address",
            "ioctlv_address",
        )
        for legacy_key in legacy_keys:
            if legacy_key in data:
                raise Prime3DolPatchError(
                    f"Retail IOS wrapper metadata must not use legacy inferred label {legacy_key!r}."
                )
        metadata = cls(
            supported_dol_sha256=_json_string(data, "supported_dol_sha256"),
            open_async_address=_json_int(data, "open_async_address"),
            open_address=_json_int(data, "open_address"),
            close_async_address=_json_int(data, "close_async_address"),
            close_address=_json_int(data, "close_address"),
            async_close_address=_json_int(data, "async_close_address"),
            async_close_extent=_json_string(data, "async_close_extent"),
            async_close_argument_count=_json_int(data, "async_close_argument_count"),
            async_close_stack_argument_count=_json_int(data, "async_close_stack_argument_count"),
            async_close_operation=_json_int(data, "async_close_operation"),
            async_close_fingerprint_sha256=_json_string(data, "async_close_fingerprint_sha256"),
            async_close_prototype=_json_string(data, "async_close_prototype"),
            async_close_register_arguments=tuple(_json_string_list(data, "async_close_register_arguments")),
            async_close_confidence=_json_string(data, "async_close_confidence"),
            read_async_address=_json_int(data, "read_async_address"),
            read_sync_address=_json_int(data, "read_sync_address"),
            write_async_address=_json_int(data, "write_async_address"),
            write_sync_address=_json_int(data, "write_sync_address"),
            seek_async_address=_json_int(data, "seek_async_address"),
            seek_sync_address=_json_int(data, "seek_sync_address"),
            confirmed_ioctl_async_address=_json_int(data, "confirmed_ioctl_async_address"),
            confirmed_ioctl_sync_address=_json_int(data, "confirmed_ioctl_sync_address"),
            confirmed_ioctlv_async_address=_json_int(data, "confirmed_ioctlv_async_address"),
            confirmed_ioctlv_sync_address=_json_int(data, "confirmed_ioctlv_sync_address"),
            async_ioctl_address=_json_int(data, "async_ioctl_address"),
            async_ioctl_extent=_json_string(data, "async_ioctl_extent"),
            async_ioctl_argument_count=_json_int(data, "async_ioctl_argument_count"),
            async_ioctl_stack_argument_count=_json_int(data, "async_ioctl_stack_argument_count"),
            async_ioctl_operation=_json_int(data, "async_ioctl_operation"),
            async_ioctl_confidence=_json_string(data, "async_ioctl_confidence"),
            confirmed_ioctl_async_fingerprint_sha256=_json_string(data, "confirmed_ioctl_async_fingerprint_sha256"),
            confirmed_ioctl_async_prototype=_json_string(data, "confirmed_ioctl_async_prototype"),
            confirmed_ioctl_async_register_arguments=tuple(
                _json_string_list(data, "confirmed_ioctl_async_register_arguments")
            ),
            confirmed_ioctl_async_stack_arguments=tuple(
                _json_string_list(data, "confirmed_ioctl_async_stack_arguments")
            ),
            request_field_offsets=tuple(_json_string_list(data, "request_field_offsets")),
            open_async_guard_words=tuple(_json_int_list(data, "open_async_guard_words")),
            callback_signature=_json_string(data, "callback_signature"),
            preserved_registers=tuple(_json_string_list(data, "preserved_registers")),
            submit_helper_address=_json_int(data, "submit_helper_address"),
            request_allocator_address=_json_int(data, "request_allocator_address"),
            evidence_source=_json_string(data, "evidence_source"),
            confidence=_json_string(data, "confidence"),
        )
        metadata.validate()
        return metadata


@dataclasses.dataclass(frozen=True)
class Prime3RuntimeTransportMetadata:
    """Production TCP tracker configuration embedded in the CP3C runtime block."""

    transport_kind: str
    protocol_magic_hex: str
    protocol_version: int
    frame_size: int
    diagnostics_enabled: bool
    inbound_queue_depth: int
    outbound_queue_depth: int
    cp3c_config_offset: int
    cp3c_config_size: int
    server_ipv4_offset: int
    server_ipv4_size: int
    server_ipv4_byte_order: str
    server_port_offset: int
    server_port_size: int
    server_port_byte_order: str
    inventory_tracker_capability: bool
    tracker_snapshot_capability: bool
    tracker_delta_capability: bool
    resync_capability: bool
    kd_startup_capability: bool
    ip_startup_capability: bool
    tcp_connect_capability: bool
    tcp_send_capability: bool
    tcp_receive_capability: bool
    wait_connect_tcp_capability: bool

    def validate(self, *, runtime_blob_size: int) -> tuple[tuple[str, int, int], ...]:
        if self.transport_kind != "tcp" or self.protocol_magic_hex != "43503357" or self.protocol_version != 1:
            raise Prime3DolPatchError("Runtime transport metadata is not the CP3W TCP tracker schema.")
        if self.frame_size != 64 or self.diagnostics_enabled:
            raise Prime3DolPatchError("TCP tracker metadata has invalid production protocol defaults.")
        if self.inbound_queue_depth <= 0 or self.outbound_queue_depth <= 0:
            raise Prime3DolPatchError("TCP tracker queue depths must be positive.")
        if not (
            self.inventory_tracker_capability
            and self.tracker_snapshot_capability
            and self.tracker_delta_capability
            and self.resync_capability
            and self.kd_startup_capability
            and self.ip_startup_capability
            and self.tcp_connect_capability
            and self.tcp_send_capability
            and self.tcp_receive_capability
            and self.wait_connect_tcp_capability
        ):
            raise Prime3DolPatchError("TCP tracker metadata is missing required production lifecycle capabilities.")
        ranges = (
            ("cp3c_config", self.cp3c_config_offset, self.cp3c_config_size),
            ("server_ipv4", self.server_ipv4_offset, self.server_ipv4_size),
            ("server_port", self.server_port_offset, self.server_port_size),
        )
        if self.server_ipv4_size != 4 or self.server_port_size != 2:
            raise Prime3DolPatchError("CP3C endpoint fields have invalid widths.")
        if self.server_ipv4_byte_order != "big" or self.server_port_byte_order != "big":
            raise Prime3DolPatchError("CP3C endpoint fields must use network byte order.")
        for _name, offset, size in ranges:
            if offset < 0 or size <= 0 or offset + size > runtime_blob_size:
                raise Prime3DolPatchError("CP3C metadata range is outside the runtime blob.")
        if not (
            self.cp3c_config_offset <= self.server_ipv4_offset
            and self.server_ipv4_offset + 4 <= self.cp3c_config_offset + self.cp3c_config_size
            and self.cp3c_config_offset <= self.server_port_offset
            and self.server_port_offset + 2 <= self.cp3c_config_offset + self.cp3c_config_size
        ):
            raise Prime3DolPatchError("CP3C endpoint fields are outside the configuration block.")
        return (("cp3c_config", self.cp3c_config_offset, self.cp3c_config_size),)

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RuntimeTransportMetadata:
        if "udp_port" in data or "mode" in data:
            raise Prime3DolPatchError("Legacy UDP transport metadata is not accepted as TCP tracker metadata.")
        metadata = cls(
            transport_kind=_json_string(data, "transport_kind"),
            protocol_magic_hex=_json_string(data, "protocol_magic_hex"),
            protocol_version=_json_int(data, "protocol_version"),
            frame_size=_json_int(data, "frame_size"),
            diagnostics_enabled=_json_bool(data, "diagnostics_enabled"),
            inbound_queue_depth=_json_int(data, "inbound_queue_depth"),
            outbound_queue_depth=_json_int(data, "outbound_queue_depth"),
            cp3c_config_offset=_json_int(data, "cp3c_config_offset"),
            cp3c_config_size=_json_int(data, "cp3c_config_size"),
            server_ipv4_offset=_json_int(data, "server_ipv4_offset"),
            server_ipv4_size=_json_int(data, "server_ipv4_size"),
            server_ipv4_byte_order=_json_string(data, "server_ipv4_byte_order"),
            server_port_offset=_json_int(data, "server_port_offset"),
            server_port_size=_json_int(data, "server_port_size"),
            server_port_byte_order=_json_string(data, "server_port_byte_order"),
            inventory_tracker_capability=_json_bool(data, "inventory_tracker_capability"),
            tracker_snapshot_capability=_json_bool(data, "tracker_snapshot_capability"),
            tracker_delta_capability=_json_bool(data, "tracker_delta_capability"),
            resync_capability=_json_bool(data, "resync_capability"),
            kd_startup_capability=_json_bool(data, "kd_startup_capability"),
            ip_startup_capability=_json_bool(data, "ip_startup_capability"),
            tcp_connect_capability=_json_bool(data, "tcp_connect_capability"),
            tcp_send_capability=_json_bool(data, "tcp_send_capability"),
            tcp_receive_capability=_json_bool(data, "tcp_receive_capability"),
            wait_connect_tcp_capability=_json_bool(data, "wait_connect_tcp_capability"),
        )
        metadata.validate(runtime_blob_size=metadata.cp3c_config_offset + metadata.cp3c_config_size)
        return metadata


@dataclasses.dataclass(frozen=True)
class Prime3RuntimeAbiProbeMetadata:
    mode: str
    supplied_args_address: int
    supplied_args_size: int
    pre_call_args_address: int
    pre_call_args_size: int
    target_args_address: int
    target_args_size: int
    return_value_address: int
    return_value_size: int
    expected_return_value: int
    result_flags_address: int
    result_flags_size: int
    stack_pointer_before_address: int
    stack_pointer_before_size: int
    stack_pointer_after_address: int
    stack_pointer_after_size: int
    saved_lr_address: int
    saved_lr_size: int
    restored_lr_address: int
    restored_lr_size: int
    saved_r2_address: int
    saved_r2_size: int
    restored_r2_address: int
    restored_r2_size: int
    saved_r13_address: int
    saved_r13_size: int
    restored_r13_address: int
    restored_r13_size: int
    target_ctr_address: int
    target_ctr_size: int
    after_call_flag_address: int
    after_call_flag_size: int

    def validate(self, *, runtime_state_start: int, runtime_state_end: int) -> tuple[tuple[str, int, int], ...]:
        ranges = (
            ("supplied_args", self.supplied_args_address, self.supplied_args_size),
            ("pre_call_args", self.pre_call_args_address, self.pre_call_args_size),
            ("target_args", self.target_args_address, self.target_args_size),
            ("return_value", self.return_value_address, self.return_value_size),
            ("result_flags", self.result_flags_address, self.result_flags_size),
            ("stack_pointer_before", self.stack_pointer_before_address, self.stack_pointer_before_size),
            ("stack_pointer_after", self.stack_pointer_after_address, self.stack_pointer_after_size),
            ("saved_lr", self.saved_lr_address, self.saved_lr_size),
            ("restored_lr", self.restored_lr_address, self.restored_lr_size),
            ("saved_r2", self.saved_r2_address, self.saved_r2_size),
            ("restored_r2", self.restored_r2_address, self.restored_r2_size),
            ("saved_r13", self.saved_r13_address, self.saved_r13_size),
            ("restored_r13", self.restored_r13_address, self.restored_r13_size),
            ("target_ctr", self.target_ctr_address, self.target_ctr_size),
            ("after_call_flag", self.after_call_flag_address, self.after_call_flag_size),
        )
        if self.mode != "retail_wrapper_ioctl_async_abi_probe":
            raise Prime3DolPatchError(f"Unsupported ABI probe mode {self.mode!r}.")
        if self.expected_return_value <= 0 or self.expected_return_value > 0xFFFFFFFF:
            raise Prime3DolPatchError("ABI probe expected return value must be a 32-bit sentinel.")
        for name, start, size in ranges:
            if size <= 0:
                raise Prime3DolPatchError(f"ABI probe field {name} must have positive size.")
            if not (runtime_state_start <= start < runtime_state_end):
                raise Prime3DolPatchError(f"ABI probe field {name} is outside the runtime state range.")
            if start + size > runtime_state_end:
                raise Prime3DolPatchError(f"ABI probe field {name} exceeds the runtime state range.")
        return ranges

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RuntimeAbiProbeMetadata:
        metadata = cls(
            mode=_json_string(data, "mode"),
            supplied_args_address=_json_int(data, "supplied_args_address"),
            supplied_args_size=_json_int(data, "supplied_args_size"),
            pre_call_args_address=_json_int(data, "pre_call_args_address"),
            pre_call_args_size=_json_int(data, "pre_call_args_size"),
            target_args_address=_json_int(data, "target_args_address"),
            target_args_size=_json_int(data, "target_args_size"),
            return_value_address=_json_int(data, "return_value_address"),
            return_value_size=_json_int(data, "return_value_size"),
            expected_return_value=_json_int(data, "expected_return_value"),
            result_flags_address=_json_int(data, "result_flags_address"),
            result_flags_size=_json_int(data, "result_flags_size"),
            stack_pointer_before_address=_json_int(data, "stack_pointer_before_address"),
            stack_pointer_before_size=_json_int(data, "stack_pointer_before_size"),
            stack_pointer_after_address=_json_int(data, "stack_pointer_after_address"),
            stack_pointer_after_size=_json_int(data, "stack_pointer_after_size"),
            saved_lr_address=_json_int(data, "saved_lr_address"),
            saved_lr_size=_json_int(data, "saved_lr_size"),
            restored_lr_address=_json_int(data, "restored_lr_address"),
            restored_lr_size=_json_int(data, "restored_lr_size"),
            saved_r2_address=_json_int(data, "saved_r2_address"),
            saved_r2_size=_json_int(data, "saved_r2_size"),
            restored_r2_address=_json_int(data, "restored_r2_address"),
            restored_r2_size=_json_int(data, "restored_r2_size"),
            saved_r13_address=_json_int(data, "saved_r13_address"),
            saved_r13_size=_json_int(data, "saved_r13_size"),
            restored_r13_address=_json_int(data, "restored_r13_address"),
            restored_r13_size=_json_int(data, "restored_r13_size"),
            target_ctr_address=_json_int(data, "target_ctr_address"),
            target_ctr_size=_json_int(data, "target_ctr_size"),
            after_call_flag_address=_json_int(data, "after_call_flag_address"),
            after_call_flag_size=_json_int(data, "after_call_flag_size"),
        )
        return metadata


@dataclasses.dataclass(frozen=True)
class Prime3RuntimeDiagnosticMetadata:
    mode: str
    hook_wrapper_entry_count_address: int
    hook_wrapper_entry_count_size: int
    hook_wrapper_before_poll_count_address: int
    hook_wrapper_before_poll_count_size: int
    runtime_poll_entry_count_address: int
    runtime_poll_entry_count_size: int
    runtime_poll_exit_count_address: int
    runtime_poll_exit_count_size: int
    state_machine_entry_count_address: int
    state_machine_entry_count_size: int
    state_machine_exit_count_address: int
    state_machine_exit_count_size: int
    c_before_veneer_call_count_address: int
    c_before_veneer_call_count_size: int
    retail_veneer_entry_count_address: int
    retail_veneer_entry_count_size: int
    retail_target_return_count_address: int
    retail_target_return_count_size: int
    retail_veneer_exit_count_address: int
    retail_veneer_exit_count_size: int
    c_after_veneer_call_count_address: int
    c_after_veneer_call_count_size: int
    ios_submit_attempt_count_address: int
    ios_submit_attempt_count_size: int
    ios_submit_return_count_address: int
    ios_submit_return_count_size: int
    ios_submit_return_value_address: int
    ios_submit_return_value_size: int
    callback_entry_count_address: int
    callback_entry_count_size: int
    callback_exit_count_address: int
    callback_exit_count_size: int
    hook_wrapper_after_poll_count_address: int
    hook_wrapper_after_poll_count_size: int
    hook_wrapper_exit_count_address: int
    hook_wrapper_exit_count_size: int
    last_execution_marker_address: int
    last_execution_marker_size: int
    last_transport_phase_before_step_address: int
    last_transport_phase_before_step_size: int
    last_transport_phase_after_step_address: int
    last_transport_phase_after_step_size: int
    callback_result_address: int
    callback_result_size: int

    def validate(self, *, runtime_state_start: int, runtime_state_end: int) -> tuple[tuple[str, int, int], ...]:
        ranges = (
            ("hook_wrapper_entry_count", self.hook_wrapper_entry_count_address, self.hook_wrapper_entry_count_size),
            (
                "hook_wrapper_before_poll_count",
                self.hook_wrapper_before_poll_count_address,
                self.hook_wrapper_before_poll_count_size,
            ),
            ("runtime_poll_entry_count", self.runtime_poll_entry_count_address, self.runtime_poll_entry_count_size),
            ("runtime_poll_exit_count", self.runtime_poll_exit_count_address, self.runtime_poll_exit_count_size),
            ("state_machine_entry_count", self.state_machine_entry_count_address, self.state_machine_entry_count_size),
            ("state_machine_exit_count", self.state_machine_exit_count_address, self.state_machine_exit_count_size),
            (
                "c_before_veneer_call_count",
                self.c_before_veneer_call_count_address,
                self.c_before_veneer_call_count_size,
            ),
            (
                "retail_veneer_entry_count",
                self.retail_veneer_entry_count_address,
                self.retail_veneer_entry_count_size,
            ),
            (
                "retail_target_return_count",
                self.retail_target_return_count_address,
                self.retail_target_return_count_size,
            ),
            (
                "retail_veneer_exit_count",
                self.retail_veneer_exit_count_address,
                self.retail_veneer_exit_count_size,
            ),
            (
                "c_after_veneer_call_count",
                self.c_after_veneer_call_count_address,
                self.c_after_veneer_call_count_size,
            ),
            ("ios_submit_attempt_count", self.ios_submit_attempt_count_address, self.ios_submit_attempt_count_size),
            ("ios_submit_return_count", self.ios_submit_return_count_address, self.ios_submit_return_count_size),
            ("ios_submit_return_value", self.ios_submit_return_value_address, self.ios_submit_return_value_size),
            ("callback_entry_count", self.callback_entry_count_address, self.callback_entry_count_size),
            ("callback_exit_count", self.callback_exit_count_address, self.callback_exit_count_size),
            (
                "hook_wrapper_after_poll_count",
                self.hook_wrapper_after_poll_count_address,
                self.hook_wrapper_after_poll_count_size,
            ),
            ("hook_wrapper_exit_count", self.hook_wrapper_exit_count_address, self.hook_wrapper_exit_count_size),
            ("last_execution_marker", self.last_execution_marker_address, self.last_execution_marker_size),
            (
                "last_transport_phase_before_step",
                self.last_transport_phase_before_step_address,
                self.last_transport_phase_before_step_size,
            ),
            (
                "last_transport_phase_after_step",
                self.last_transport_phase_after_step_address,
                self.last_transport_phase_after_step_size,
            ),
            ("callback_result", self.callback_result_address, self.callback_result_size),
        )
        for name, start, size in ranges:
            if size <= 0:
                raise Prime3DolPatchError(f"Relocated runtime diagnostic field {name} size must be positive.")
            if not (runtime_state_start <= start < runtime_state_end):
                raise Prime3DolPatchError(
                    f"Relocated runtime diagnostic field {name} is outside the runtime state range."
                )
            if start + size > runtime_state_end:
                raise Prime3DolPatchError(f"Relocated runtime diagnostic field {name} exceeds the runtime state range.")
        _validate_non_overlapping_ranges(ranges)
        return ranges

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RuntimeDiagnosticMetadata:
        return cls(
            mode=_json_string(data, "mode"),
            hook_wrapper_entry_count_address=_json_int(data, "hook_wrapper_entry_count_address"),
            hook_wrapper_entry_count_size=_json_int(data, "hook_wrapper_entry_count_size"),
            hook_wrapper_before_poll_count_address=_json_int(data, "hook_wrapper_before_poll_count_address"),
            hook_wrapper_before_poll_count_size=_json_int(data, "hook_wrapper_before_poll_count_size"),
            runtime_poll_entry_count_address=_json_int(data, "runtime_poll_entry_count_address"),
            runtime_poll_entry_count_size=_json_int(data, "runtime_poll_entry_count_size"),
            runtime_poll_exit_count_address=_json_int(data, "runtime_poll_exit_count_address"),
            runtime_poll_exit_count_size=_json_int(data, "runtime_poll_exit_count_size"),
            state_machine_entry_count_address=_json_int(data, "state_machine_entry_count_address"),
            state_machine_entry_count_size=_json_int(data, "state_machine_entry_count_size"),
            state_machine_exit_count_address=_json_int(data, "state_machine_exit_count_address"),
            state_machine_exit_count_size=_json_int(data, "state_machine_exit_count_size"),
            c_before_veneer_call_count_address=_json_int(data, "c_before_veneer_call_count_address"),
            c_before_veneer_call_count_size=_json_int(data, "c_before_veneer_call_count_size"),
            retail_veneer_entry_count_address=_json_int(data, "retail_veneer_entry_count_address"),
            retail_veneer_entry_count_size=_json_int(data, "retail_veneer_entry_count_size"),
            retail_target_return_count_address=_json_int(data, "retail_target_return_count_address"),
            retail_target_return_count_size=_json_int(data, "retail_target_return_count_size"),
            retail_veneer_exit_count_address=_json_int(data, "retail_veneer_exit_count_address"),
            retail_veneer_exit_count_size=_json_int(data, "retail_veneer_exit_count_size"),
            c_after_veneer_call_count_address=_json_int(data, "c_after_veneer_call_count_address"),
            c_after_veneer_call_count_size=_json_int(data, "c_after_veneer_call_count_size"),
            ios_submit_attempt_count_address=_json_int(data, "ios_submit_attempt_count_address"),
            ios_submit_attempt_count_size=_json_int(data, "ios_submit_attempt_count_size"),
            ios_submit_return_count_address=_json_int(data, "ios_submit_return_count_address"),
            ios_submit_return_count_size=_json_int(data, "ios_submit_return_count_size"),
            ios_submit_return_value_address=_json_int(data, "ios_submit_return_value_address"),
            ios_submit_return_value_size=_json_int(data, "ios_submit_return_value_size"),
            callback_entry_count_address=_json_int(data, "callback_entry_count_address"),
            callback_entry_count_size=_json_int(data, "callback_entry_count_size"),
            callback_exit_count_address=_json_int(data, "callback_exit_count_address"),
            callback_exit_count_size=_json_int(data, "callback_exit_count_size"),
            hook_wrapper_after_poll_count_address=_json_int(data, "hook_wrapper_after_poll_count_address"),
            hook_wrapper_after_poll_count_size=_json_int(data, "hook_wrapper_after_poll_count_size"),
            hook_wrapper_exit_count_address=_json_int(data, "hook_wrapper_exit_count_address"),
            hook_wrapper_exit_count_size=_json_int(data, "hook_wrapper_exit_count_size"),
            last_execution_marker_address=_json_int(data, "last_execution_marker_address"),
            last_execution_marker_size=_json_int(data, "last_execution_marker_size"),
            last_transport_phase_before_step_address=_json_int(data, "last_transport_phase_before_step_address"),
            last_transport_phase_before_step_size=_json_int(data, "last_transport_phase_before_step_size"),
            last_transport_phase_after_step_address=_json_int(data, "last_transport_phase_after_step_address"),
            last_transport_phase_after_step_size=_json_int(data, "last_transport_phase_after_step_size"),
            callback_result_address=_json_int(data, "callback_result_address"),
            callback_result_size=_json_int(data, "callback_result_size"),
        )


@dataclasses.dataclass(frozen=True)
class Prime3RelocatedRuntimeMetadata:
    mode: str
    low_bootstrap_address: int
    low_bootstrap_size: int
    low_bootstrap_sha256: str
    embedded_runtime_blob_offset: int
    embedded_runtime_blob_size: int
    embedded_runtime_blob_sha256: str
    runtime_destination_address: int
    runtime_entry_address: int
    runtime_poll_entry_address: int
    runtime_poll_hook_wrapper_address: int
    runtime_code_start: int
    runtime_code_end: int
    runtime_state_start: int
    runtime_state_end: int
    runtime_stack_start: int | None
    runtime_stack_end: int | None
    required_source_alignment: int
    required_destination_alignment: int
    cache_line_size: int
    cache_range_start: int
    cache_range_size: int
    runtime_canary_address: int
    runtime_canary_size: int
    runtime_canary_sha256: str
    copy_complete_marker_address: int
    copy_complete_marker_value: int
    runtime_executed_marker_address: int
    runtime_executed_marker_value: int
    runtime_execution_counter_address: int
    runtime_execution_counter_size: int
    runtime_status_address: int
    runtime_success_status_value: int
    bootstrap_return_marker_address: int
    bootstrap_return_marker_value: int
    runtime_poll_counter_address: int
    runtime_poll_counter_size: int
    runtime_poll_heartbeat_address: int
    runtime_poll_heartbeat_size: int
    runtime_poll_last_sequence_address: int
    runtime_poll_last_sequence_size: int
    diagnostics: Prime3RuntimeDiagnosticMetadata | None = None
    ios_udp_diagnostic_enabled: bool = False
    transport: Prime3RuntimeTransportMetadata | LegacyPrime3RuntimeTransportMetadata | None = None
    abi_probe: Prime3RuntimeAbiProbeMetadata | None = None
    retail_ios_wrapper: Prime3RetailIosWrapperMetadata | None = None

    def _validate_diagnostic_configuration(self) -> tuple[tuple[str, int, int], ...]:
        if self.diagnostics is None:
            return ()
        return self.diagnostics.validate(
            runtime_state_start=self.runtime_state_start,
            runtime_state_end=self.runtime_state_end,
        )

    def _validate_transport_configuration(self) -> tuple[tuple[str, int, int], ...]:
        if self.transport is None:
            return ()
        if isinstance(self.transport, LegacyPrime3RuntimeTransportMetadata):
            if self.ios_udp_diagnostic_enabled:
                if self.mode != PRIME3_RUNTIME_PAYLOAD_MODE_RELOCATED_CONTINUE:
                    raise Prime3DolPatchError("IOS UDP diagnostic transport requires relocated_continue mode.")
            else:
                raise Prime3DolPatchError("Legacy UDP transport metadata requires ios_udp_diagnostic_enabled.")
            return self.transport.validate(
                runtime_state_start=self.runtime_state_start,
                runtime_state_end=self.runtime_state_end,
            )
        return self.transport.validate(runtime_blob_size=self.embedded_runtime_blob_size)

    def _validate_abi_probe_configuration(self) -> tuple[tuple[str, int, int], ...]:
        if self.abi_probe is None:
            return ()
        return self.abi_probe.validate(
            runtime_state_start=self.runtime_state_start,
            runtime_state_end=self.runtime_state_end,
        )

    def _validate_retail_wrapper_configuration(self) -> None:
        if self.retail_ios_wrapper is None:
            return
        self.retail_ios_wrapper.validate()

    def validate(
        self,
        *,
        payload_size: int,
        reserved_range_start: int,
        reserved_range_end: int,
        bootstrap_diagnostic_start: int,
        bootstrap_diagnostic_size: int,
    ) -> None:
        if self.mode not in PRIME3_RUNTIME_RELOCATED_MODES:
            raise Prime3DolPatchError(f"Unsupported Prime 3 relocated runtime mode {self.mode!r}.")
        if self.low_bootstrap_size <= 0 or self.low_bootstrap_size > payload_size:
            raise Prime3DolPatchError("Low bootstrap size is outside the compound payload size.")
        _validate_optional_range(
            payload_size=payload_size,
            field_name="embedded_runtime_blob_offset",
            start=self.embedded_runtime_blob_offset,
            size=self.embedded_runtime_blob_size,
        )
        if self.embedded_runtime_blob_offset < self.low_bootstrap_size:
            raise Prime3DolPatchError("Embedded runtime blob overlaps the low bootstrap bytes.")
        if self.required_source_alignment <= 0 or self.required_destination_alignment <= 0:
            raise Prime3DolPatchError("Relocated runtime alignments must be positive.")
        if self.embedded_runtime_blob_offset % self.required_source_alignment != 0:
            raise Prime3DolPatchError("Embedded runtime blob offset does not meet source alignment.")
        if self.runtime_destination_address % self.required_destination_alignment != 0:
            raise Prime3DolPatchError("Runtime destination does not meet destination alignment.")
        if self.runtime_destination_address < reserved_range_start:
            raise Prime3DolPatchError("Runtime destination is below the reserved range.")
        runtime_end = self.runtime_destination_address + self.embedded_runtime_blob_size
        if runtime_end > reserved_range_end or runtime_end <= self.runtime_destination_address:
            raise Prime3DolPatchError("Runtime destination range exceeds the reserved range.")
        if not (self.runtime_code_start <= self.runtime_entry_address < self.runtime_code_end):
            raise Prime3DolPatchError("Runtime entry address is outside the runtime code range.")
        if not (self.runtime_code_start <= self.runtime_poll_entry_address < self.runtime_code_end):
            raise Prime3DolPatchError("Runtime poll entry address is outside the runtime code range.")
        if not (self.runtime_code_start <= self.runtime_poll_hook_wrapper_address < self.runtime_code_end):
            raise Prime3DolPatchError("Runtime poll hook wrapper address is outside the runtime code range.")
        if self.runtime_code_start != self.runtime_destination_address:
            raise Prime3DolPatchError("Runtime code must begin at the destination address.")
        if self.runtime_code_end > runtime_end:
            raise Prime3DolPatchError("Runtime code range exceeds the embedded runtime size.")
        if not (self.runtime_code_end <= self.runtime_state_start <= self.runtime_state_end <= runtime_end):
            raise Prime3DolPatchError("Runtime state range is invalid or overlaps runtime code.")
        if (self.runtime_stack_start is None) != (self.runtime_stack_end is None):
            raise Prime3DolPatchError("Runtime stack range must provide both start and end together.")
        if self.runtime_stack_start is not None:
            assert self.runtime_stack_end is not None
            if not (
                self.runtime_state_start <= self.runtime_stack_start <= self.runtime_stack_end <= self.runtime_state_end
            ):
                raise Prime3DolPatchError("Runtime stack range must stay inside the runtime state range.")

        diagnostic_end = bootstrap_diagnostic_start + bootstrap_diagnostic_size
        state_ranges = (
            ("runtime_canary", self.runtime_canary_address, self.runtime_canary_size),
            ("copy_complete_marker", self.copy_complete_marker_address, 4),
            ("runtime_executed_marker", self.runtime_executed_marker_address, 4),
            ("runtime_execution_counter", self.runtime_execution_counter_address, self.runtime_execution_counter_size),
            ("runtime_status", self.runtime_status_address, 4),
            ("bootstrap_return_marker", self.bootstrap_return_marker_address, 4),
            ("runtime_poll_counter", self.runtime_poll_counter_address, self.runtime_poll_counter_size),
            ("runtime_poll_heartbeat", self.runtime_poll_heartbeat_address, self.runtime_poll_heartbeat_size),
            (
                "runtime_poll_last_sequence",
                self.runtime_poll_last_sequence_address,
                self.runtime_poll_last_sequence_size,
            ),
        )
        diagnostic_ranges = self._validate_diagnostic_configuration()
        transport_ranges = self._validate_transport_configuration()
        abi_probe_ranges = self._validate_abi_probe_configuration()
        self._validate_retail_wrapper_configuration()
        for name, start, size in state_ranges:
            if not (self.runtime_state_start <= start < self.runtime_state_end):
                raise Prime3DolPatchError(f"Relocated runtime field {name} is outside the runtime state range.")
            if start + size > self.runtime_state_end:
                raise Prime3DolPatchError(f"Relocated runtime field {name} exceeds the runtime state range.")
            if start < diagnostic_end and start + size > bootstrap_diagnostic_start:
                raise Prime3DolPatchError(f"Relocated runtime field {name} overlaps the bootstrap diagnostic block.")
        _validate_non_overlapping_ranges(state_ranges + diagnostic_ranges + transport_ranges + abi_probe_ranges)

        expected_cache_start, expected_cache_size = compute_cache_range(
            address=self.runtime_destination_address,
            size=self.embedded_runtime_blob_size,
            cache_line_size=self.cache_line_size,
        )
        if self.cache_range_start != expected_cache_start or self.cache_range_size != expected_cache_size:
            raise Prime3DolPatchError("Relocated runtime cache range does not match the aligned runtime destination.")

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RelocatedRuntimeMetadata:
        return cls(
            mode=_json_string(data, "mode"),
            low_bootstrap_address=_json_int(data, "low_bootstrap_address"),
            low_bootstrap_size=_json_int(data, "low_bootstrap_size"),
            low_bootstrap_sha256=_json_string(data, "low_bootstrap_sha256"),
            embedded_runtime_blob_offset=_json_int(data, "embedded_runtime_blob_offset"),
            embedded_runtime_blob_size=_json_int(data, "embedded_runtime_blob_size"),
            embedded_runtime_blob_sha256=_json_string(data, "embedded_runtime_blob_sha256"),
            runtime_destination_address=_json_int(data, "runtime_destination_address"),
            runtime_entry_address=_json_int(data, "runtime_entry_address"),
            runtime_poll_entry_address=_json_int(data, "runtime_poll_entry_address"),
            runtime_poll_hook_wrapper_address=_json_int(data, "runtime_poll_hook_wrapper_address"),
            runtime_code_start=_json_int(data, "runtime_code_start"),
            runtime_code_end=_json_int(data, "runtime_code_end"),
            runtime_state_start=_json_int(data, "runtime_state_start"),
            runtime_state_end=_json_int(data, "runtime_state_end"),
            runtime_stack_start=_json_optional_int(data, "runtime_stack_start"),
            runtime_stack_end=_json_optional_int(data, "runtime_stack_end"),
            required_source_alignment=_json_int(data, "required_source_alignment"),
            required_destination_alignment=_json_int(data, "required_destination_alignment"),
            cache_line_size=_json_int(data, "cache_line_size"),
            cache_range_start=_json_int(data, "cache_range_start"),
            cache_range_size=_json_int(data, "cache_range_size"),
            runtime_canary_address=_json_int(data, "runtime_canary_address"),
            runtime_canary_size=_json_int(data, "runtime_canary_size"),
            runtime_canary_sha256=_json_string(data, "runtime_canary_sha256"),
            copy_complete_marker_address=_json_int(data, "copy_complete_marker_address"),
            copy_complete_marker_value=_json_int(data, "copy_complete_marker_value"),
            runtime_executed_marker_address=_json_int(data, "runtime_executed_marker_address"),
            runtime_executed_marker_value=_json_int(data, "runtime_executed_marker_value"),
            runtime_execution_counter_address=_json_int(data, "runtime_execution_counter_address"),
            runtime_execution_counter_size=_json_int(data, "runtime_execution_counter_size"),
            runtime_status_address=_json_int(data, "runtime_status_address"),
            runtime_success_status_value=_json_int(data, "runtime_success_status_value"),
            bootstrap_return_marker_address=_json_int(data, "bootstrap_return_marker_address"),
            bootstrap_return_marker_value=_json_int(data, "bootstrap_return_marker_value"),
            runtime_poll_counter_address=_json_int(data, "runtime_poll_counter_address"),
            runtime_poll_counter_size=_json_int(data, "runtime_poll_counter_size"),
            runtime_poll_heartbeat_address=_json_int(data, "runtime_poll_heartbeat_address"),
            runtime_poll_heartbeat_size=_json_int(data, "runtime_poll_heartbeat_size"),
            runtime_poll_last_sequence_address=_json_int(data, "runtime_poll_last_sequence_address"),
            runtime_poll_last_sequence_size=_json_int(data, "runtime_poll_last_sequence_size"),
            diagnostics=_json_optional_runtime_diagnostics(data, "diagnostics"),
            ios_udp_diagnostic_enabled=_json_optional_bool(data, "ios_udp_diagnostic_enabled") or False,
            transport=_json_optional_runtime_transport(data, "transport"),
            abi_probe=_json_optional_runtime_abi_probe(data, "abi_probe"),
            retail_ios_wrapper=_json_optional_retail_ios_wrapper(data, "retail_ios_wrapper"),
        )


@dataclasses.dataclass(frozen=True)
class Prime3RuntimePayloadPatchField:
    payload_offset: int
    expected_original_bytes: str
    field_size: int
    byte_order: str

    def validate(self, *, payload_size: int) -> None:
        if self.field_size != 4:
            raise Prime3DolPatchError("Beacon IPv4 patch field must be exactly 4 bytes.")
        if self.byte_order != "big":
            raise Prime3DolPatchError("Beacon IPv4 patch field must use big-endian byte ordering.")
        _validate_optional_range(
            payload_size=payload_size,
            field_name="beacon_ipv4_patch.payload_offset",
            start=self.payload_offset,
            size=self.field_size,
        )
        try:
            expected = bytes.fromhex(self.expected_original_bytes)
        except ValueError as exc:
            raise Prime3DolPatchError("Beacon IPv4 patch expected bytes must be hexadecimal.") from exc
        if len(expected) != self.field_size:
            raise Prime3DolPatchError("Beacon IPv4 patch expected bytes must match the declared field size.")

    def to_json_dict(self) -> dict[str, object]:
        return dataclasses.asdict(self)

    @classmethod
    def from_json_dict(cls, data: dict[str, object], *, payload_size: int) -> Prime3RuntimePayloadPatchField:
        required_keys = {"payload_offset", "expected_original_bytes", "field_size", "byte_order"}
        unknown_keys = set(data) - required_keys
        if unknown_keys:
            raise Prime3DolPatchError(f"Unknown beacon IPv4 patch metadata keys: {sorted(unknown_keys)}")
        metadata = cls(
            payload_offset=_json_int(data, "payload_offset"),
            expected_original_bytes=_json_string(data, "expected_original_bytes"),
            field_size=_json_int(data, "field_size"),
            byte_order=_json_string(data, "byte_order"),
        )
        metadata.validate(payload_size=payload_size)
        return metadata


@dataclasses.dataclass(frozen=True)
class Prime3RuntimePayloadManifest:
    schema_version: int
    target_architecture: str
    target_endianness: str
    target_abi: str
    compiler_identity: str
    compiler_version: str
    linker_identity: str
    linker_version: str
    payload_sha256: str
    payload_size: int
    required_alignment: int
    entry_symbol_name: str
    entry_symbol_offset: int
    source_digest: str
    protocol_artifact_version: int
    unresolved_relocation_count: int
    dynamic_section_count: int
    payload_mode: str = PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL
    canary_start_offset: int | None = None
    canary_size: int | None = None
    counter_offset: int | None = None
    counter_size: int | None = None
    entry_bootstrap: Prime3EntryBootstrapMetadata | None = None
    relocated_runtime: Prime3RelocatedRuntimeMetadata | None = None
    beacon_ipv4_patch: Prime3RuntimePayloadPatchField | None = None

    def validate(self) -> None:
        if self.schema_version != PRIME3_RUNTIME_PAYLOAD_SCHEMA_VERSION:
            raise Prime3DolPatchError(
                f"Unsupported Prime 3 runtime payload schema version {self.schema_version}; "
                f"expected {PRIME3_RUNTIME_PAYLOAD_SCHEMA_VERSION}."
            )
        if self.target_architecture != PRIME3_RUNTIME_TARGET_ARCHITECTURE:
            raise Prime3DolPatchError(
                f"Unsupported payload architecture {self.target_architecture!r}; "
                f"expected {PRIME3_RUNTIME_TARGET_ARCHITECTURE!r}."
            )
        if self.target_endianness != PRIME3_RUNTIME_TARGET_ENDIANNESS:
            raise Prime3DolPatchError(
                f"Unsupported payload endianness {self.target_endianness!r}; "
                f"expected {PRIME3_RUNTIME_TARGET_ENDIANNESS!r}."
            )
        if self.target_abi != PRIME3_RUNTIME_TARGET_ABI:
            raise Prime3DolPatchError(
                f"Unsupported payload ABI {self.target_abi!r}; expected {PRIME3_RUNTIME_TARGET_ABI!r}."
            )
        if self.payload_size < 0:
            raise Prime3DolPatchError(f"Payload size must be non-negative, got {self.payload_size}.")
        if self.entry_symbol_offset < 0 or self.entry_symbol_offset > self.payload_size:
            raise Prime3DolPatchError(
                f"Payload entry offset {self.entry_symbol_offset} is outside payload size {self.payload_size}."
            )
        if self.unresolved_relocation_count != 0:
            raise Prime3DolPatchError(
                f"Payload manifest reports {self.unresolved_relocation_count} unresolved relocations."
            )
        if self.dynamic_section_count != 0:
            raise Prime3DolPatchError(f"Payload manifest reports {self.dynamic_section_count} dynamic sections.")
        if self.protocol_artifact_version != PROTOCOL_VERSION:
            raise Prime3DolPatchError(
                f"Payload protocol version {self.protocol_artifact_version!r} does not match {PROTOCOL_VERSION!r}."
            )
        if self.payload_mode not in (
            PRIME3_RUNTIME_PAYLOAD_MODE_NORMAL,
            PRIME3_RUNTIME_PAYLOAD_MODE_PROBE,
            *PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES,
        ):
            raise Prime3DolPatchError(f"Unsupported payload mode {self.payload_mode!r}.")
        _validate_optional_range(
            payload_size=self.payload_size,
            field_name="canary_start_offset",
            start=self.canary_start_offset,
            size=self.canary_size,
        )
        _validate_optional_range(
            payload_size=self.payload_size,
            field_name="counter_offset",
            start=self.counter_offset,
            size=self.counter_size,
        )
        if self.entry_bootstrap is None and self.payload_mode in PRIME3_RUNTIME_ENTRY_BOOTSTRAP_MODES:
            raise Prime3DolPatchError("Entry bootstrap payload mode requires entry bootstrap metadata.")
        if self.entry_bootstrap is not None:
            self.entry_bootstrap.validate(payload_size=self.payload_size)
            if self.payload_mode != self.entry_bootstrap.mode:
                raise Prime3DolPatchError("Payload mode does not match entry bootstrap metadata mode.")
        if self.relocated_runtime is None and self.payload_mode in PRIME3_RUNTIME_RELOCATED_MODES:
            raise Prime3DolPatchError("Relocated runtime payload mode requires relocated runtime metadata.")
        if self.relocated_runtime is not None:
            if self.entry_bootstrap is None:
                raise Prime3DolPatchError("Relocated runtime metadata requires entry bootstrap metadata.")
            self.relocated_runtime.validate(
                payload_size=self.payload_size,
                reserved_range_start=self.entry_bootstrap.reserved_range_start,
                reserved_range_end=self.entry_bootstrap.reserved_range_end,
                bootstrap_diagnostic_start=self.entry_bootstrap.diagnostic_address,
                bootstrap_diagnostic_size=self.entry_bootstrap.diagnostic_block_size,
            )
            if self.payload_mode != self.relocated_runtime.mode:
                raise Prime3DolPatchError("Payload mode does not match relocated runtime metadata mode.")
        if self.beacon_ipv4_patch is not None:
            self.beacon_ipv4_patch.validate(payload_size=self.payload_size)

        Prime3PayloadArtifact.create(
            payload_bytes=b"\x00" * self.payload_size,
            load_address=0,
            entry_symbol_offset=self.entry_symbol_offset,
            required_alignment=self.required_alignment,
            protocol_manifest_version=str(self.protocol_artifact_version),
            build_tool_identity=self.compiler_identity,
            build_tool_version=self.compiler_version,
            source_digest=self.source_digest,
        )

    def to_json_dict(self) -> dict[str, object]:
        result: dict[str, object] = {
            "compiler_identity": self.compiler_identity,
            "compiler_version": self.compiler_version,
            "dynamic_section_count": self.dynamic_section_count,
            "entry_symbol_name": self.entry_symbol_name,
            "entry_symbol_offset": self.entry_symbol_offset,
            "linker_identity": self.linker_identity,
            "linker_version": self.linker_version,
            "payload_sha256": self.payload_sha256,
            "payload_size": self.payload_size,
            "payload_mode": self.payload_mode,
            "protocol_artifact_version": self.protocol_artifact_version,
            "required_alignment": self.required_alignment,
            "schema_version": self.schema_version,
            "source_digest": self.source_digest,
            "target_abi": self.target_abi,
            "target_architecture": self.target_architecture,
            "target_endianness": self.target_endianness,
            "unresolved_relocation_count": self.unresolved_relocation_count,
        }
        if self.canary_start_offset is not None:
            result["canary_start_offset"] = self.canary_start_offset
            result["canary_size"] = self.canary_size
        if self.counter_offset is not None:
            result["counter_offset"] = self.counter_offset
            result["counter_size"] = self.counter_size
        if self.entry_bootstrap is not None:
            result["entry_bootstrap"] = self.entry_bootstrap.to_json_dict()
        if self.relocated_runtime is not None:
            result["relocated_runtime"] = self.relocated_runtime.to_json_dict()
        if self.beacon_ipv4_patch is not None:
            result["beacon_ipv4_patch"] = self.beacon_ipv4_patch.to_json_dict()
        return result

    def to_json_text(self) -> str:
        return json.dumps(self.to_json_dict(), indent=2, sort_keys=True) + "\n"

    @classmethod
    def from_json_dict(cls, data: dict[str, object]) -> Prime3RuntimePayloadManifest:
        required_keys = {
            "compiler_identity",
            "compiler_version",
            "dynamic_section_count",
            "entry_symbol_name",
            "entry_symbol_offset",
            "linker_identity",
            "linker_version",
            "payload_sha256",
            "payload_size",
            "payload_mode",
            "protocol_artifact_version",
            "required_alignment",
            "schema_version",
            "source_digest",
            "target_abi",
            "target_architecture",
            "target_endianness",
            "unresolved_relocation_count",
            "canary_start_offset",
            "canary_size",
            "counter_offset",
            "counter_size",
            "entry_bootstrap",
            "relocated_runtime",
            "beacon_ipv4_patch",
        }
        unknown_keys = set(data) - required_keys
        if unknown_keys:
            raise Prime3DolPatchError(f"Unknown Prime 3 runtime payload manifest keys: {sorted(unknown_keys)}")

        payload_size = _json_int(data, "payload_size")
        manifest = cls(
            schema_version=_json_int(data, "schema_version"),
            target_architecture=_json_string(data, "target_architecture"),
            target_endianness=_json_string(data, "target_endianness"),
            target_abi=_json_string(data, "target_abi"),
            compiler_identity=_json_string(data, "compiler_identity"),
            compiler_version=_json_string(data, "compiler_version"),
            linker_identity=_json_string(data, "linker_identity"),
            linker_version=_json_string(data, "linker_version"),
            payload_sha256=_json_string(data, "payload_sha256"),
            payload_size=payload_size,
            payload_mode=_json_string(data, "payload_mode"),
            required_alignment=_json_int(data, "required_alignment"),
            entry_symbol_name=_json_string(data, "entry_symbol_name"),
            entry_symbol_offset=_json_int(data, "entry_symbol_offset"),
            source_digest=_json_string(data, "source_digest"),
            protocol_artifact_version=_json_int(data, "protocol_artifact_version"),
            unresolved_relocation_count=_json_int(data, "unresolved_relocation_count"),
            dynamic_section_count=_json_int(data, "dynamic_section_count"),
            canary_start_offset=_json_optional_int(data, "canary_start_offset"),
            canary_size=_json_optional_int(data, "canary_size"),
            counter_offset=_json_optional_int(data, "counter_offset"),
            counter_size=_json_optional_int(data, "counter_size"),
            entry_bootstrap=_json_optional_entry_bootstrap(data, "entry_bootstrap", payload_size=payload_size),
            relocated_runtime=_json_optional_relocated_runtime(data, "relocated_runtime"),
            beacon_ipv4_patch=_json_optional_payload_patch_field(
                data,
                "beacon_ipv4_patch",
                payload_size=payload_size,
            ),
        )
        manifest.validate()
        return manifest

    @classmethod
    def from_json_text(cls, text: str) -> Prime3RuntimePayloadManifest:
        try:
            raw = json.loads(text)
        except json.JSONDecodeError as exc:
            raise Prime3DolPatchError(f"Invalid Prime 3 runtime payload manifest JSON: {exc}") from exc
        if not isinstance(raw, dict):
            raise Prime3DolPatchError("Prime 3 runtime payload manifest must be a JSON object.")
        return cls.from_json_dict(raw)


def compute_source_digest(source_root: Path, relative_paths: Iterable[str | Path]) -> str:
    digest = hashlib.sha256()
    for relative_path in sorted((Path(path) for path in relative_paths), key=lambda path: path.as_posix()):
        digest.update(relative_path.as_posix().encode("utf-8"))
        digest.update(b"\0")
        digest.update(source_root.joinpath(relative_path).read_bytes())
        digest.update(b"\0")
    return digest.hexdigest()


def load_prime3_runtime_payload_artifact(
    *,
    manifest_path: Path,
    payload_path: Path,
    load_address: int,
) -> Prime3PayloadArtifact:
    manifest = Prime3RuntimePayloadManifest.from_json_text(manifest_path.read_text(encoding="utf-8"))
    payload_bytes = payload_path.read_bytes()
    actual_hash = hashlib.sha256(payload_bytes).hexdigest()
    if actual_hash != manifest.payload_sha256:
        raise Prime3DolPatchError(
            f"Payload hash mismatch for {payload_path}: expected {manifest.payload_sha256}, got {actual_hash}."
        )
    if len(payload_bytes) != manifest.payload_size:
        raise Prime3DolPatchError(
            f"Payload size mismatch for {payload_path}: expected {manifest.payload_size}, got {len(payload_bytes)}."
        )

    build_tool_identity = f"{manifest.compiler_identity} + {manifest.linker_identity}"
    build_tool_version = f"{manifest.compiler_version} / {manifest.linker_version}"
    return Prime3PayloadArtifact.create(
        payload_bytes=payload_bytes,
        load_address=load_address,
        entry_symbol_offset=manifest.entry_symbol_offset,
        required_alignment=manifest.required_alignment,
        protocol_manifest_version=str(manifest.protocol_artifact_version),
        build_tool_identity=build_tool_identity,
        build_tool_version=build_tool_version,
        source_digest=manifest.source_digest,
    )


def _json_int(data: dict[str, object], key: str) -> int:
    value = data.get(key)
    if not isinstance(value, int):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an integer.")
    return value


def _json_string(data: dict[str, object], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be a string.")
    return value


def _json_optional_string(data: dict[str, object], key: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be a string.")
    return value


def _json_int_list(data: dict[str, object], key: str) -> list[int]:
    value = data.get(key)
    if not isinstance(value, list | tuple) or not all(isinstance(item, int) for item in value):
        raise Prime3DolPatchError(
            f"Prime 3 runtime payload manifest field {key!r} must be a list or tuple of integers."
        )
    return list(value)


def _json_int_dict(data: dict[str, object], key: str) -> dict[str, int]:
    value = data.get(key)
    if not isinstance(value, dict) or not all(
        isinstance(item_key, str) and isinstance(item_value, int) for item_key, item_value in value.items()
    ):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must map strings to integers.")
    return dict(value)


def _json_string_list(data: dict[str, object], key: str) -> list[str]:
    value = data.get(key)
    if not isinstance(value, list | tuple) or not all(isinstance(item, str) for item in value):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be a list or tuple of strings.")
    return list(value)


def _json_optional_int(data: dict[str, object], key: str) -> int | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, int):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an integer when present.")
    return value


def _json_bool(data: dict[str, object], key: str) -> bool:
    value = data.get(key)
    if not isinstance(value, bool):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be a bool.")
    return value


def _json_optional_bool(data: dict[str, object], key: str) -> bool | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, bool):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be a bool when present.")
    return value


def _json_optional_entry_bootstrap(
    data: dict[str, object],
    key: str,
    *,
    payload_size: int,
) -> Prime3EntryBootstrapMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3EntryBootstrapMetadata.from_json_dict(value, payload_size=payload_size)


def _json_optional_relocated_runtime(
    data: dict[str, object],
    key: str,
) -> Prime3RelocatedRuntimeMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3RelocatedRuntimeMetadata.from_json_dict(value)


def _json_optional_payload_patch_field(
    data: dict[str, object],
    key: str,
    *,
    payload_size: int,
) -> Prime3RuntimePayloadPatchField | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3RuntimePayloadPatchField.from_json_dict(value, payload_size=payload_size)


def _json_optional_runtime_transport(
    data: dict[str, object],
    key: str,
) -> Prime3RuntimeTransportMetadata | LegacyPrime3RuntimeTransportMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    if "udp_port" in value or "mode" in value:
        return LegacyPrime3RuntimeTransportMetadata.from_json_dict(value)
    return Prime3RuntimeTransportMetadata.from_json_dict(value)


def _json_optional_game_identity(
    data: dict[str, object],
    key: str,
) -> Prime3RuntimeGameIdentityMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3RuntimeGameIdentityMetadata.from_json_dict(value)


def _json_optional_inventory(
    data: dict[str, object],
    key: str,
) -> Prime3RuntimeInventoryMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3RuntimeInventoryMetadata.from_json_dict(value)


def _json_optional_runtime_diagnostics(
    data: dict[str, object],
    key: str,
) -> Prime3RuntimeDiagnosticMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3RuntimeDiagnosticMetadata.from_json_dict(value)


def _json_optional_retail_ios_wrapper(
    data: dict[str, object],
    key: str,
) -> Prime3RetailIosWrapperMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"Prime 3 runtime payload manifest field {key!r} must be an object when present.")
    return Prime3RetailIosWrapperMetadata.from_json_dict(value)


def _json_optional_runtime_abi_probe(
    data: dict[str, object],
    key: str,
) -> Prime3RuntimeAbiProbeMetadata | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, dict):
        raise Prime3DolPatchError(f"{key} must be an object when provided.")
    return Prime3RuntimeAbiProbeMetadata.from_json_dict(value)


def _validate_optional_range(*, payload_size: int, field_name: str, start: int | None, size: int | None) -> None:
    if start is None and size is None:
        return
    if start is None or size is None:
        raise Prime3DolPatchError(f"Payload manifest must provide both {field_name} and its size together.")
    if size <= 0:
        raise Prime3DolPatchError(f"Payload manifest field {field_name!r} size must be positive, got {size}.")
    if start < 0 or start + size > payload_size:
        raise Prime3DolPatchError(
            f"Payload manifest field {field_name!r} range {start}..{start + size} "
            f"is outside payload size {payload_size}."
        )


def _validate_non_overlapping_ranges(ranges: tuple[tuple[str, int, int], ...]) -> None:
    for index, (first_name, first_start, first_size) in enumerate(ranges):
        first_end = first_start + first_size
        for second_name, second_start, second_size in ranges[index + 1 :]:
            second_end = second_start + second_size
            if first_start < second_end and second_start < first_end:
                raise Prime3DolPatchError(f"Fields {first_name} and {second_name} overlap.")
