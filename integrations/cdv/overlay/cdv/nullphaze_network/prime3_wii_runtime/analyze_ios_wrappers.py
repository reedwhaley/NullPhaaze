# Static IOS-wrapper attribution follows the supported retail DOL call sites and device
# strings. Its candidates are evidence for guarded bindings, not permission to install an
# arbitrary wrapper. Boundary names here: RetailWrapperSpec, DevicePath, StringReference,
# CallSite, WrapperCandidate.
from __future__ import annotations

import argparse
import dataclasses
import hashlib
import json
import os
import sys
from pathlib import Path

if __package__ in {None, ""}:
    _repository_root = Path(__file__).resolve().parents[2]
    _repository_root_str = os.fspath(_repository_root)
    if _repository_root_str not in sys.path:
        sys.path.insert(0, _repository_root_str)

from randovania.games.prime3.exporter.dol_patcher import decode_ppc_unconditional_branch, parse_dol_header

PRIME3_NTSC_RETAIL_DOL_SHA256 = "6b550f221602074747a2e61b0aa064203fd493f6865dfb3b1a912682065e6104"
PRIME3_NTSC_RETAIL_CLUSTER = {
    "open_async": 0x80504668,
    "open": 0x80504780,
    "close_async": 0x805048A0,
    "close": 0x80504960,
    "read_async": 0x80504A08,
    "read_sync": 0x80504B08,
    "write_async": 0x80504C10,
    "write_sync": 0x80504D10,
}

REQUEST_FIELD_OFFSETS = {
    "operation": 0x00,
    "result": 0x04,
    "fd": 0x08,
    "argument_0": 0x0C,
    "argument_1": 0x10,
    "argument_2": 0x14,
    "argument_3": 0x18,
    "argument_4": 0x1C,
    "completion": 0x20,
    "completion_userdata": 0x24,
    "special_vector_flag": 0x28,
}


@dataclasses.dataclass(frozen=True)
class RetailWrapperSpec:
    name: str
    address: int
    end_address: int
    operation: int | None
    prototype: str
    register_arguments: tuple[str, ...]
    stack_arguments: tuple[str, ...]
    request_fields: tuple[tuple[str, int, str], ...]
    fingerprint_sha256: str
    confidence: str = "verified"
    rejection_reasons: tuple[str, ...] = ()


PRIME3_NTSC_RETAIL_WRAPPER_SPECS = (
    RetailWrapperSpec(
        "close_async",
        0x805048A0,
        0x80504960,
        2,
        "s32 close_async(s32 fd, completion_fn completion, void *userdata)",
        ("r3=fd", "r4=completion", "r5=userdata"),
        (),
        (("fd", 0x08, "r3"), ("completion", 0x20, "r4"), ("completion_userdata", 0x24, "r5")),
        "cad7a4b8950241515a9399d51c69d5680bba41fe060c37f5b6953effcdcb1288",
    ),
    RetailWrapperSpec(
        "read_async",
        0x80504A08,
        0x80504B08,
        3,
        "s32 read_async(s32 fd, void *buffer, s32 length, completion_fn completion, void *userdata)",
        ("r3=fd", "r4=buffer", "r5=length", "r6=completion", "r7=userdata"),
        (),
        (
            ("fd", 0x08, "r3"),
            ("buffer_physical", 0x0C, "physical(r4)"),
            ("length", 0x10, "r5"),
            ("completion", 0x20, "r6"),
            ("completion_userdata", 0x24, "r7"),
        ),
        "e10f84b3290812c6849eedb14dfa58498ded0cff7dfc61fb708e0849379c6709",
    ),
    RetailWrapperSpec(
        "read_sync",
        0x80504B08,
        0x80504C10,
        3,
        "s32 read_sync(s32 fd, void *buffer, s32 length)",
        ("r3=fd", "r4=buffer", "r5=length"),
        (),
        (("fd", 0x08, "r3"), ("buffer_physical", 0x0C, "physical(r4)"), ("length", 0x10, "r5")),
        "6931b9996007cc4b89d68e0fd578e0ee435012fc5ab49511c7b510ffb5676782",
    ),
    RetailWrapperSpec(
        "write_async",
        0x80504C10,
        0x80504D10,
        4,
        "s32 write_async(s32 fd, const void *buffer, s32 length, completion_fn completion, void *userdata)",
        ("r3=fd", "r4=buffer", "r5=length", "r6=completion", "r7=userdata"),
        (),
        (
            ("fd", 0x08, "r3"),
            ("buffer_physical", 0x0C, "physical(r4)"),
            ("length", 0x10, "r5"),
            ("completion", 0x20, "r6"),
            ("completion_userdata", 0x24, "r7"),
        ),
        "23fa0ab6dad16afc8c96b000004db819bba9241b1f782f707deea6fc1fb47169",
    ),
    RetailWrapperSpec(
        "write_sync",
        0x80504D10,
        0x80504E18,
        4,
        "s32 write_sync(s32 fd, const void *buffer, s32 length)",
        ("r3=fd", "r4=buffer", "r5=length"),
        (),
        (("fd", 0x08, "r3"), ("buffer_physical", 0x0C, "physical(r4)"), ("length", 0x10, "r5")),
        "e4367d4143f12abbbf7893534a1e700c7eeeba3125394fa24678f6a461f42a50",
    ),
    RetailWrapperSpec(
        "seek_async",
        0x80504E18,
        0x80504EF8,
        5,
        "s32 seek_async(s32 fd, s32 offset, s32 origin, completion_fn completion, void *userdata)",
        ("r3=fd", "r4=offset", "r5=origin", "r6=completion", "r7=userdata"),
        (),
        (
            ("fd", 0x08, "r3"),
            ("seek_offset", 0x0C, "r4"),
            ("seek_origin", 0x10, "r5"),
            ("completion", 0x20, "r6"),
            ("completion_userdata", 0x24, "r7"),
        ),
        "c798d4ec89c5176d505dcc8e468c16d2309fb29394516db0ca62b081e35c1a0d",
    ),
    RetailWrapperSpec(
        "seek_sync",
        0x80504EF8,
        0x80504FE0,
        5,
        "s32 seek_sync(s32 fd, s32 offset, s32 origin)",
        ("r3=fd", "r4=offset", "r5=origin"),
        (),
        (("fd", 0x08, "r3"), ("seek_offset", 0x0C, "r4"), ("seek_origin", 0x10, "r5")),
        "b56f1a18ec30a57ac20b2eed0d693a7199429acba3a35914437e7df8e83ddbaa",
    ),
    RetailWrapperSpec(
        "ioctl_async",
        0x80504FE0,
        0x80505118,
        6,
        "s32 ioctl_async(s32 fd, u32 command, const void *input, u32 input_length, "
        "void *output, u32 output_length, completion_fn completion, void *userdata)",
        (
            "r3=fd",
            "r4=command",
            "r5=input",
            "r6=input_length",
            "r7=output",
            "r8=output_length",
            "r9=completion",
            "r10=userdata",
        ),
        (),
        (
            ("fd", 0x08, "r3"),
            ("command", 0x0C, "r4"),
            ("input_physical", 0x10, "physical(r5)"),
            ("input_length", 0x14, "r6"),
            ("output_physical", 0x18, "physical(r7)"),
            ("output_length", 0x1C, "r8"),
            ("completion", 0x20, "r9"),
            ("completion_userdata", 0x24, "r10"),
        ),
        "031342395575c5542428b9edfcd4fd3bf9633bfb54bd39726d3766b3e6f3b17b",
    ),
    RetailWrapperSpec(
        "ioctl_sync",
        0x80505118,
        0x80505248,
        6,
        "s32 ioctl_sync(s32 fd, u32 command, const void *input, u32 input_length, "
        "void *output, u32 output_length)",
        ("r3=fd", "r4=command", "r5=input", "r6=input_length", "r7=output", "r8=output_length"),
        (),
        (
            ("fd", 0x08, "r3"),
            ("command", 0x0C, "r4"),
            ("input_physical", 0x10, "physical(r5)"),
            ("input_length", 0x14, "r6"),
            ("output_physical", 0x18, "physical(r7)"),
            ("output_length", 0x1C, "r8"),
        ),
        "c56d6b237b1da790bf6a9800ab210aa24ae3bac1fa802ece1f638c47a160fc74",
    ),
    RetailWrapperSpec(
        "vector_request_prepare",
        0x80505248,
        0x80505384,
        None,
        "s32 vector_request_prepare(request *request, u32 command, u32 input_count, "
        "u32 output_count, ioctlv *vectors)",
        ("r3=request", "r4=command", "r5=input_count", "r6=output_count", "r7=vectors"),
        (),
        (
            ("command", 0x0C, "r4"),
            ("input_vector_count", 0x10, "r5"),
            ("output_vector_count", 0x14, "r6"),
            ("vector_array_physical", 0x18, "physical(r7)"),
        ),
        "170db226dbdb29cade05435d8123a77f51954a28ed212d41d502912aef400a18",
    ),
    RetailWrapperSpec(
        "ioctlv_async",
        0x80505384,
        0x80505468,
        7,
        "s32 ioctlv_async(s32 fd, u32 command, u32 input_count, u32 output_count, "
        "ioctlv *vectors, completion_fn completion, void *userdata)",
        (
            "r3=fd",
            "r4=command",
            "r5=input_count",
            "r6=output_count",
            "r7=vectors",
            "r8=completion",
            "r9=userdata",
        ),
        (),
        (
            ("fd", 0x08, "r3"),
            ("completion", 0x20, "r8"),
            ("completion_userdata", 0x24, "r9"),
        ),
        "0e50266899f1f2bafb868ee342376c76eaf5a2df12811c782d86fd5c2cb29c83",
    ),
    RetailWrapperSpec(
        "ioctlv_sync",
        0x80505468,
        0x80505544,
        7,
        "s32 ioctlv_sync(s32 fd, u32 command, u32 input_count, u32 output_count, ioctlv *vectors)",
        ("r3=fd", "r4=command", "r5=input_count", "r6=output_count", "r7=vectors"),
        (),
        (("fd", 0x08, "r3"),),
        "b4e6880f34edbccc2508760596813617ab91239067d0dbe12c5cc477c7f48695",
    ),
    RetailWrapperSpec(
        "special_vector_sync",
        0x80505544,
        0x8050562C,
        7,
        "s32 special_vector_sync(s32 fd, u32 command, u32 input_count, u32 output_count, ioctlv *vectors)",
        ("r3=fd", "r4=command", "r5=input_count", "r6=output_count", "r7=vectors"),
        (),
        (("fd", 0x08, "r3"), ("special_vector_flag", 0x28, "1")),
        "bce6eb1e7e467c0c93cf487084ad5c30c4f75962b2de2abf99c85049d6ae5b19",
        confidence="candidate",
        rejection_reasons=("request+0x28 is set to one, so this is not the ordinary synchronous vector wrapper",),
    ),
)


@dataclasses.dataclass(frozen=True)
class DevicePath:
    text: str
    virtual_address: int
    file_offset: int


@dataclasses.dataclass(frozen=True)
class StringReference:
    target_address: int
    instruction_address: int
    register: int
    form: str


@dataclasses.dataclass(frozen=True)
class CallSite:
    call_address: int
    target_address: int
    path_register: int
    path_address: int


@dataclasses.dataclass(frozen=True)
class WrapperCandidate:
    address: int
    command_id: int
    alloc_helper_address: int
    submit_helper_address: int
    guard_words: tuple[int, ...]
    kind: str


def find_direct_branch_callers(dol_bytes: bytes, target_address: int) -> list[dict[str, object]]:
    return _find_direct_branch_callers_for_targets(dol_bytes, {target_address})[target_address]


def _find_direct_branch_callers_for_targets(
    dol_bytes: bytes,
    target_addresses: set[int],
) -> dict[int, list[dict[str, object]]]:
    header = parse_dol_header(dol_bytes)
    callers: dict[int, list[dict[str, object]]] = {target_address: [] for target_address in target_addresses}
    for section in header.text_sections():
        blob = dol_bytes[section.file_offset : section.file_offset + section.size]
        for offset in range(0, len(blob), 4):
            address = section.address + offset
            decoded = decode_ppc_unconditional_branch(_read_word(blob, offset), address)
            if decoded is None or decoded.target_address not in callers:
                continue
            callers[decoded.target_address].append(
                {
                    "caller_address": address,
                    "link": decoded.link,
                }
            )
    return callers


def _read_word(data: bytes, offset: int) -> int:
    return int.from_bytes(data[offset : offset + 4], "big")


def _decode_simm(word: int) -> int:
    value = word & 0xFFFF
    return value if value < 0x8000 else value - 0x10000


def find_device_paths(dol_bytes: bytes) -> list[DevicePath]:
    header = parse_dol_header(dol_bytes)
    found: list[DevicePath] = []
    seen: set[str] = set()
    for section in header.sections:
        if section.size <= 0:
            continue
        blob = dol_bytes[section.file_offset : section.file_offset + section.size]
        cursor = 0
        while True:
            start = blob.find(b"/dev/", cursor)
            if start < 0:
                break
            end = blob.find(b"\x00", start)
            if end < 0:
                break
            text = blob[start:end].decode("ascii", "replace")
            if text not in seen:
                seen.add(text)
                found.append(
                    DevicePath(
                        text=text,
                        virtual_address=section.address + start,
                        file_offset=section.file_offset + start,
                    )
                )
            cursor = end + 1
    return found


def find_string_references(
    dol_bytes: bytes,
    target_address: int,
    *,
    max_gap_instructions: int = 8,
) -> list[StringReference]:
    header = parse_dol_header(dol_bytes)
    results: list[StringReference] = []
    target_hi = (target_address >> 16) & 0xFFFF
    for section in header.text_sections():
        blob = dol_bytes[section.file_offset : section.file_offset + section.size]
        for offset in range(0, len(blob) - 4, 4):
            word = _read_word(blob, offset)
            if word >> 26 != 15 or (word & 0xFFFF) != target_hi:
                continue
            reg = (word >> 21) & 31
            base = (_decode_simm(word) << 16) & 0xFFFFFFFF
            for gap in range(1, max_gap_instructions + 1):
                next_offset = offset + gap * 4
                if next_offset >= len(blob):
                    break
                next_word = _read_word(blob, next_offset)
                op = next_word >> 26
                rt = (next_word >> 21) & 31
                ra = (next_word >> 16) & 31
                if rt != reg or ra != reg:
                    continue
                value = None
                form = None
                if op == 14:
                    value = (base + _decode_simm(next_word)) & 0xFFFFFFFF
                    form = "lis/addi"
                elif op == 24:
                    value = (base | (next_word & 0xFFFF)) & 0xFFFFFFFF
                    form = "lis/ori"
                if value == target_address and form is not None:
                    results.append(
                        StringReference(
                            target_address=target_address,
                            instruction_address=section.address + offset,
                            register=reg,
                            form=form,
                        )
                    )
                    break
    return results


def find_calls_following_string_reference(
    dol_bytes: bytes,
    reference: StringReference,
    *,
    search_span_instructions: int = 10,
) -> list[CallSite]:
    header = parse_dol_header(dol_bytes)
    section = header.section_for_address(reference.instruction_address)
    if section is None:
        return []
    results: list[CallSite] = []
    start = header.offset_for_address(reference.instruction_address)
    assert start is not None
    end = min(section.end_offset, start + (search_span_instructions + 1) * 4)
    for offset in range(start + 4, end, 4):
        address = header.address_for_offset(offset)
        assert address is not None
        decoded = decode_ppc_unconditional_branch(_read_word(dol_bytes, offset), address)
        if decoded is None or not decoded.link:
            continue
        results.append(
            CallSite(
                call_address=address,
                target_address=decoded.target_address,
                path_register=reference.register,
                path_address=reference.target_address,
            )
        )
    return results


def score_wrapper_cluster(candidates: list[WrapperCandidate]) -> int:
    if len(candidates) < 4:
        return 0
    command_ids = {candidate.command_id for candidate in candidates}
    if not {1, 2, 3, 4}.issubset(command_ids):
        return 0
    alloc_helpers = {candidate.alloc_helper_address for candidate in candidates}
    submit_helpers = {candidate.submit_helper_address for candidate in candidates}
    if len(alloc_helpers) != 1 or len(submit_helpers) != 1:
        return 0
    if any(len(candidate.guard_words) < 2 for candidate in candidates):
        return 0
    async_kinds = {candidate.kind for candidate in candidates if candidate.kind.endswith("_async")}
    sync_kinds = {candidate.kind for candidate in candidates if not candidate.kind.endswith("_async")}
    if len(async_kinds) < 2 or len(sync_kinds) < 2:
        return 0
    return len(candidates)


def read_virtual_range(dol_bytes: bytes, start_address: int, end_address: int) -> bytes:
    if end_address <= start_address:
        raise ValueError("Function end must be greater than its start.")
    header = parse_dol_header(dol_bytes)
    start_offset = header.offset_for_address(start_address)
    end_offset = header.offset_for_address(end_address - 1)
    if start_offset is None or end_offset is None or end_offset - start_offset + 1 != end_address - start_address:
        raise ValueError(
            f"Virtual range 0x{start_address:08x}..0x{end_address:08x} is not contiguous in the DOL."
        )
    return dol_bytes[start_offset : end_offset + 1]


def validate_function_fingerprints(
    dol_bytes: bytes,
    specs: tuple[RetailWrapperSpec, ...],
) -> dict[str, str]:
    fingerprints: dict[str, str] = {}
    for spec in specs:
        observed = hashlib.sha256(read_virtual_range(dol_bytes, spec.address, spec.end_address)).hexdigest()
        if observed != spec.fingerprint_sha256:
            raise ValueError(
                f"Function fingerprint mismatch for {spec.name} at 0x{spec.address:08x}: "
                f"expected {spec.fingerprint_sha256}, got {observed}."
            )
        fingerprints[spec.name] = observed
    return fingerprints


def classify_request_shape(
    *,
    operation: int | None,
    request_fields: set[str],
    completion_present: bool,
    vector_elements_processed: bool = False,
) -> tuple[str, tuple[str, ...]]:
    required_common = {"fd"}
    if not required_common.issubset(request_fields):
        return "unknown_helper", ("fd field is not proven",)

    suffix = "async" if completion_present else "sync"
    if operation == 3 and {"buffer_physical", "length"}.issubset(request_fields):
        return f"{suffix}_read", ()
    if operation == 4 and {"buffer_physical", "length"}.issubset(request_fields):
        return f"{suffix}_write", ()
    if operation == 5 and {"seek_offset", "seek_origin"}.issubset(request_fields):
        return f"{suffix}_seek", ()
    ioctl_fields = {"command", "input_physical", "input_length", "output_physical", "output_length"}
    if operation == 6 and ioctl_fields.issubset(request_fields):
        return f"{suffix}_ioctl", ()
    vector_fields = {"command", "input_vector_count", "output_vector_count", "vector_array_physical"}
    if operation == 7 and vector_fields.issubset(request_fields) and vector_elements_processed:
        return f"{suffix}_vector_ioctl", ()

    reasons: list[str] = []
    if operation not in {3, 4, 5, 6, 7}:
        reasons.append("request operation is not a classified IPC operation")
    if operation == 6:
        missing = sorted(ioctl_fields - request_fields)
        reasons.append(f"missing ioctl fields: {', '.join(missing)}")
    if operation == 7:
        missing = sorted(vector_fields - request_fields)
        if missing:
            reasons.append(f"missing vector fields: {', '.join(missing)}")
        if not vector_elements_processed:
            reasons.append("vector element pointer and length processing is not proven")
    return "unknown_helper", tuple(reasons or ["request shape is incomplete"])


def _wrapper_report(
    dol_bytes: bytes,
    spec: RetailWrapperSpec,
    direct_branch_callers: list[dict[str, object]],
) -> dict[str, object]:
    request_fields = [
        {"name": name, "offset": offset, "source": source}
        for name, offset, source in spec.request_fields
    ]
    direct_callees = [0x80505960, 0x8050441C]
    if spec.name == "vector_request_prepare":
        direct_callees = [0x804DF8F4]
    elif spec.name in {"ioctlv_async", "ioctlv_sync", "special_vector_sync"}:
        direct_callees = [0x80505960, 0x80505248, 0x8050441C]
    elif spec.name.startswith("seek_"):
        direct_callees = [0x80505960, 0x8050441C]
    elif spec.name.startswith("read_"):
        direct_callees = [0x80505960, 0x804DF8C8, 0x8050441C]
    elif spec.name.startswith("write_") or spec.name.startswith("ioctl_"):
        direct_callees = [0x80505960, 0x804DF8F4, 0x8050441C]

    frame_sizes = {
        0x80504A08: 0x30,
        0x80504B08: 0x20,
        0x80504C10: 0x30,
        0x80504D10: 0x20,
        0x80504E18: 0x30,
        0x80504EF8: 0x20,
        0x80504FE0: 0x40,
        0x80505118: 0x30,
        0x80505248: 0x20,
        0x80505384: 0x30,
        0x80505468: 0x30,
        0x80505544: 0x30,
    }
    saved_registers = {
        0x80504A08: ["lr", "r26-r31"],
        0x80504B08: ["lr", "r28-r31"],
        0x80504C10: ["lr", "r26-r31"],
        0x80504D10: ["lr", "r28-r31"],
        0x80504E18: ["lr", "r26-r31"],
        0x80504EF8: ["lr", "r28-r31"],
        0x80504FE0: ["lr", "r23-r31"],
        0x80505118: ["lr", "r25-r31"],
        0x80505248: ["lr", "r26-r31"],
        0x80505384: ["lr", "r24-r31"],
        0x80505468: ["lr", "r26-r31"],
        0x80505544: ["lr", "r26-r31"],
    }
    async_wrapper = spec.name.endswith("_async")
    return {
        "name": spec.name,
        "classification": spec.name,
        "start_address": spec.address,
        "end_address": spec.end_address,
        "size": spec.end_address - spec.address,
        "stack_frame_size": frame_sizes[spec.address],
        "saved_registers": saved_registers[spec.address],
        "incoming_registers": list(spec.register_arguments),
        "incoming_stack_arguments": list(spec.stack_arguments),
        "request_operation": spec.operation,
        "request_fields": request_fields,
        "request_allocator_call": 0x80505960 if spec.name != "vector_request_prepare" else None,
        "submit_helper_call": 0x8050441C if spec.name != "vector_request_prepare" else None,
        "submit_helper_completion_argument": "user completion" if async_wrapper else "NULL",
        "direct_callees": direct_callees,
        "indirect_calls": [],
        "prototype": spec.prototype,
        "fingerprint_sha256": hashlib.sha256(
            read_virtual_range(dol_bytes, spec.address, spec.end_address)
        ).hexdigest(),
        "direct_branch_callers": direct_branch_callers,
        "return_value_source": "submit helper result or local -4/-22 error",
        "error_returns": [-4, -22],
        "confidence": spec.confidence,
        "rejection_reasons": list(spec.rejection_reasons),
    }


def analyze_known_retail_wrapper_sequence(dol_bytes: bytes) -> dict[str, object]:
    digest = hashlib.sha256(dol_bytes).hexdigest()
    if digest != PRIME3_NTSC_RETAIL_DOL_SHA256:
        raise ValueError(
            f"Unsupported retail DOL SHA-256 {digest}; expected {PRIME3_NTSC_RETAIL_DOL_SHA256}."
        )
    validate_function_fingerprints(dol_bytes, PRIME3_NTSC_RETAIL_WRAPPER_SPECS)
    caller_map = _find_direct_branch_callers_for_targets(
        dol_bytes,
        {spec.address for spec in PRIME3_NTSC_RETAIL_WRAPPER_SPECS},
    )
    return {
        "supported_dol_sha256": digest,
        "request_size": 0x40,
        "request_alignment": 0x20,
        "request_field_offsets": REQUEST_FIELD_OFFSETS,
        "request_completion_contract": "request+0x20(request+0x04, request+0x24)",
        "request_submit_helper": 0x8050441C,
        "request_allocator": 0x80505960,
        "wrappers": [
            _wrapper_report(dol_bytes, spec, caller_map[spec.address])
            for spec in PRIME3_NTSC_RETAIL_WRAPPER_SPECS
        ],
        "non_wrapper_functions": [
            {
                "name": "pool_initialize",
                "start_address": 0x8050562C,
                "end_address": 0x8050575C,
                "size": 0x130,
                "classification": "allocator_support",
                "stack_frame_size": 0x20,
                "saved_registers": ["lr", "r29-r31"],
                "incoming_registers": ["r3=pool_start", "r4=pool_size"],
                "incoming_stack_arguments": [],
                "direct_callees": [0x804E3CBC, 0x804E3CE4],
                "indirect_calls": [],
                "return_value_source": "allocated pool index or local -4/-5 error",
                "error_returns": [-4, -5],
            },
            {
                "name": "pool_allocate",
                "start_address": 0x8050575C,
                "end_address": 0x80505960,
                "size": 0x204,
                "classification": "allocator_support",
                "stack_frame_size": 0x20,
                "saved_registers": ["lr", "r28-r31"],
                "incoming_registers": ["r3=pool_index", "r4=size", "r5=alignment"],
                "incoming_stack_arguments": [],
                "direct_callees": [0x804E3CBC, 0x804E3CE4],
                "indirect_calls": [],
                "return_value_source": "allocated aligned pointer or NULL",
                "error_returns": [0],
            },
            {
                "name": "request_allocator_thunk",
                "start_address": 0x80505960,
                "end_address": 0x80505964,
                "size": 4,
                "classification": "allocator_support",
                "stack_frame_size": 0,
                "saved_registers": [],
                "incoming_registers": ["r3=pool_index", "r4=size", "r5=alignment"],
                "incoming_stack_arguments": [],
                "direct_callees": [0x8050575C],
                "indirect_calls": [],
                "return_value_source": "tail call to pool_allocate",
                "error_returns": [0],
                "tail_target": 0x8050575C,
            },
        ],
        "confirmed_ioctl_async_target": 0x80504FE0,
        "runtime_submission_enabled": False,
    }


def _default_report(dol_bytes: bytes) -> dict[str, object]:
    digest = hashlib.sha256(dol_bytes).hexdigest()
    device_paths = [dataclasses.asdict(path) for path in find_device_paths(dol_bytes)]
    report: dict[str, object] = {
        "dol_sha256": digest,
        "device_paths": device_paths,
        "verified_cluster": None,
    }
    if digest == PRIME3_NTSC_RETAIL_DOL_SHA256:
        report["verified_cluster"] = {
            "supported_dol_sha256": PRIME3_NTSC_RETAIL_DOL_SHA256,
            "functions": PRIME3_NTSC_RETAIL_CLUSTER,
            "submit_helper_address": 0x8050441C,
            "request_allocator_address": 0x80505960,
            "callback_signature": "s32 callback(s32 result, void *userdata)",
            "evidence": [
                "open/close wrappers remain directly supported by callsite analysis",
                "operation values 3 and 4 plus buffer cache direction prove the read/write wrapper pairs",
                "operation value 6 and complete fd/command/input/output/completion fields prove ioctl wrappers",
                "operation value 7 plus vector count, element, and array handling prove vector ioctl wrappers",
            ],
            "wrapper_sequence": analyze_known_retail_wrapper_sequence(dol_bytes),
        }
    return report


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("dol_path", type=Path)
    parser.add_argument("--output", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    report = _default_report(args.dol_path.read_bytes())
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        sys.stdout.write(text)
    else:
        args.output.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
