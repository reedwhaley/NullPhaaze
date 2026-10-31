# DOL edits require a supported header layout and exact instruction preimage. Append
# executable sections within the declared bounds and retain the original continuation path
# for guarded hooks. Boundary names here: Prime3DolPatchError, CorruptionDolVersionLike,
# DolSection, DolHeader, Prime3DolPatchResult.
from __future__ import annotations

import base64
import dataclasses
import hashlib
import os
import tempfile
import uuid
from pathlib import Path
from typing import TYPE_CHECKING, Protocol, cast

from open_prime_rando.dol_patching.corruption import dol_versions as corruption_dol_versions
from retro_data_structures.game_check import Game as RDSGame

if TYPE_CHECKING:
    from collections.abc import Iterable

_DOL_HEADER_SIZE = 0x100
_TEXT_SECTION_COUNT = 7
_DATA_SECTION_COUNT = 11
_DOL_SECTION_COUNT = _TEXT_SECTION_COUNT + _DATA_SECTION_COUNT
_TEXT_SECTION_OFFSET = 0
_DATA_SECTION_OFFSET = _TEXT_SECTION_COUNT
_UUID_START = 6
_UUID_LENGTH = 16
_PPC_BRANCH_OPCODE = 18
_PPC_BRANCH_MIN_DISPLACEMENT = -(1 << 25)
_PPC_BRANCH_MAX_DISPLACEMENT = (1 << 25) - 4
_PPC_ABSOLUTE_BRANCH_MAX_ADDRESS = (1 << 25) - 4


class Prime3DolPatchError(RuntimeError):
    """Raised when a Prime 3 DOL cannot be validated or patched safely."""


class CorruptionDolVersionLike(Protocol):
    game: RDSGame
    description: str
    build_string_address: int
    build_string: bytes


@dataclasses.dataclass(frozen=True)
class DolSection:
    slot_index: int
    kind: str
    kind_index: int
    file_offset: int
    address: int
    size: int

    @property
    def end_address(self) -> int:
        return self.address + self.size

    @property
    def end_offset(self) -> int:
        return self.file_offset + self.size

    @property
    def name(self) -> str:
        return f"{self.kind}{self.kind_index}"

    @property
    def is_empty(self) -> bool:
        return self.file_offset == 0 and self.address == 0 and self.size == 0


@dataclasses.dataclass(frozen=True)
class DolHeader:
    sections: tuple[DolSection, ...]
    bss_address: int
    bss_size: int
    entry_point: int

    @property
    def bss_end_address(self) -> int:
        return self.bss_address + self.bss_size

    def text_sections(self) -> tuple[DolSection, ...]:
        return tuple(section for section in self.sections if section.kind == "text" and section.size > 0)

    def data_sections(self) -> tuple[DolSection, ...]:
        return tuple(section for section in self.sections if section.kind == "data" and section.size > 0)

    def unused_text_slots(self) -> tuple[DolSection, ...]:
        return tuple(section for section in self.sections if section.kind == "text" and section.is_empty)

    def unused_data_slots(self) -> tuple[DolSection, ...]:
        return tuple(section for section in self.sections if section.kind == "data" and section.is_empty)

    def section_for_address(self, address: int) -> DolSection | None:
        for section in self.sections:
            if section.size > 0 and section.address <= address < section.end_address:
                return section
        return None

    def section_for_offset(self, offset: int) -> DolSection | None:
        for section in self.sections:
            if section.size > 0 and section.file_offset <= offset < section.end_offset:
                return section
        return None

    def offset_for_address(self, address: int) -> int | None:
        section = self.section_for_address(address)
        if section is None:
            return None
        return section.file_offset + (address - section.address)

    def address_for_offset(self, offset: int) -> int | None:
        section = self.section_for_offset(offset)
        if section is None:
            return None
        return section.address + (offset - section.file_offset)


@dataclasses.dataclass(frozen=True)
class Prime3DolPatchResult:
    version_description: str
    build_string_address: int
    build_string_offset: int
    layout_uuid: uuid.UUID
    previous_layout_uuid: uuid.UUID | None
    changed: bool
    bytes_changed: int


@dataclasses.dataclass(frozen=True)
class ExecutableTextSectionInsertResult:
    text_slot_index: int
    text_kind_index: int
    file_offset: int
    virtual_address: int
    payload_size: int
    alignment_padding: int
    resulting_file_size: int
    entry_symbol_address: int | None


@dataclasses.dataclass(frozen=True)
class GuardedInstructionPatchResult:
    address: int
    file_offset: int
    original_word: int
    replacement_word: int
    changed: bool


@dataclasses.dataclass(frozen=True)
class BranchPatch:
    source_address: int
    target_address: int
    instruction_word: int
    absolute: bool
    link: bool


@dataclasses.dataclass(frozen=True)
class DecodedBranchInstruction:
    instruction_address: int
    instruction_word: int
    target_address: int
    absolute: bool
    link: bool

    @property
    def continuation_address(self) -> int:
        return checked_add_u32(self.instruction_address, 4, "branch continuation address")


@dataclasses.dataclass(frozen=True)
class TrampolinePlan:
    hook_patch: BranchPatch
    trampoline_address: int
    displaced_instruction_word: int
    return_branch: BranchPatch
    payload_entry_address: int
    return_address: int


@dataclasses.dataclass(frozen=True)
class Prime3PayloadArtifact:
    payload_bytes: bytes
    load_address: int
    entry_symbol_offset: int
    required_alignment: int
    protocol_manifest_version: str
    build_tool_identity: str
    build_tool_version: str
    source_digest: str
    payload_sha256: str

    @property
    def entry_symbol_address(self) -> int:
        return checked_add_u32(self.load_address, self.entry_symbol_offset, "entry symbol address")

    @property
    def as_json(self) -> dict[str, object]:
        return {
            "build_tool_identity": self.build_tool_identity,
            "build_tool_version": self.build_tool_version,
            "entry_symbol_offset": self.entry_symbol_offset,
            "load_address": self.load_address,
            "payload_base64": base64.b64encode(self.payload_bytes).decode("ascii"),
            "payload_sha256": self.payload_sha256,
            "protocol_manifest_version": self.protocol_manifest_version,
            "required_alignment": self.required_alignment,
            "source_digest": self.source_digest,
        }

    def validate(self) -> None:
        if self.required_alignment <= 0 or (self.required_alignment & (self.required_alignment - 1)) != 0:
            raise Prime3DolPatchError(
                f"Payload artifact alignment must be a positive power of two, got {self.required_alignment}."
            )
        if self.entry_symbol_offset < 0 or self.entry_symbol_offset > len(self.payload_bytes):
            raise Prime3DolPatchError(
                "Payload entry symbol offset "
                f"{self.entry_symbol_offset} is outside payload size {len(self.payload_bytes)}."
            )
        actual_hash = hashlib.sha256(self.payload_bytes).hexdigest()
        if actual_hash != self.payload_sha256:
            raise Prime3DolPatchError(
                f"Payload artifact hash mismatch: expected {self.payload_sha256}, got {actual_hash}."
            )
        checked_add_u32(self.load_address, len(self.payload_bytes), "payload virtual range")
        checked_add_u32(self.load_address, self.entry_symbol_offset, "entry symbol address")

    @classmethod
    def create(
        cls,
        *,
        payload_bytes: bytes,
        load_address: int,
        entry_symbol_offset: int,
        required_alignment: int,
        protocol_manifest_version: str,
        build_tool_identity: str,
        build_tool_version: str,
        source_digest: str,
    ) -> Prime3PayloadArtifact:
        artifact = cls(
            payload_bytes=payload_bytes,
            load_address=load_address,
            entry_symbol_offset=entry_symbol_offset,
            required_alignment=required_alignment,
            protocol_manifest_version=protocol_manifest_version,
            build_tool_identity=build_tool_identity,
            build_tool_version=build_tool_version,
            source_digest=source_digest,
            payload_sha256=hashlib.sha256(payload_bytes).hexdigest(),
        )
        artifact.validate()
        return artifact

    @classmethod
    def from_json(cls, data: dict[str, object]) -> Prime3PayloadArtifact:
        required_keys = {
            "build_tool_identity",
            "build_tool_version",
            "entry_symbol_offset",
            "load_address",
            "payload_base64",
            "payload_sha256",
            "protocol_manifest_version",
            "required_alignment",
            "source_digest",
        }
        unknown_keys = set(data) - required_keys
        if unknown_keys:
            raise Prime3DolPatchError(f"Unknown payload artifact keys: {sorted(unknown_keys)}")

        artifact = cls(
            payload_bytes=base64.b64decode(_json_string(data, "payload_base64"), validate=True),
            load_address=_json_int(data, "load_address"),
            entry_symbol_offset=_json_int(data, "entry_symbol_offset"),
            required_alignment=_json_int(data, "required_alignment"),
            protocol_manifest_version=_json_string(data, "protocol_manifest_version"),
            build_tool_identity=_json_string(data, "build_tool_identity"),
            build_tool_version=_json_string(data, "build_tool_version"),
            source_digest=_json_string(data, "source_digest"),
            payload_sha256=_json_string(data, "payload_sha256"),
        )
        artifact.validate()
        return artifact


def _read_u32_be(data: bytes | bytearray, offset: int) -> int:
    end = offset + 4
    if end > len(data):
        raise Prime3DolPatchError("DOL header is truncated.")
    return int.from_bytes(data[offset:end], "big")


def _json_int(data: dict[str, object], key: str) -> int:
    value = data[key]
    if not isinstance(value, int):
        raise Prime3DolPatchError(f"Payload artifact field {key!r} must be an integer.")
    return value


def _json_string(data: dict[str, object], key: str) -> str:
    value = data[key]
    if not isinstance(value, str):
        raise Prime3DolPatchError(f"Payload artifact field {key!r} must be a string.")
    return value


def checked_add_u32(base: int, size: int, label: str) -> int:
    if base < 0 or size < 0:
        raise Prime3DolPatchError(f"{label} must use non-negative values, got base={base}, size={size}.")
    result = base + size
    if result > 0x1_0000_0000 or result < base:
        raise Prime3DolPatchError(f"{label} overflows 32-bit address space.")
    return result


def align_up(value: int, alignment: int) -> int:
    if alignment <= 0 or (alignment & (alignment - 1)) != 0:
        raise Prime3DolPatchError(f"Alignment must be a positive power of two, got {alignment}.")
    return (value + alignment - 1) & ~(alignment - 1)


def parse_dol_header(data: bytes | bytearray) -> DolHeader:
    if len(data) < _DOL_HEADER_SIZE:
        raise Prime3DolPatchError("DOL file is truncated before the header is complete.")

    sections: list[DolSection] = []
    for slot_index in range(_DOL_SECTION_COUNT):
        file_offset = _read_u32_be(data, slot_index * 4)
        address = _read_u32_be(data, 0x48 + (slot_index * 4))
        size = _read_u32_be(data, 0x90 + (slot_index * 4))

        kind = "text" if slot_index < _TEXT_SECTION_COUNT else "data"
        kind_index = slot_index if kind == "text" else slot_index - _DATA_SECTION_OFFSET
        section = DolSection(
            slot_index=slot_index,
            kind=kind,
            kind_index=kind_index,
            file_offset=file_offset,
            address=address,
            size=size,
        )

        if size == 0:
            if file_offset != 0 or address != 0:
                raise Prime3DolPatchError(
                    f"DOL {section.name} slot is malformed: empty sections must be fully zeroed."
                )
            sections.append(section)
            continue

        if address == 0:
            raise Prime3DolPatchError(f"DOL {section.name} slot is malformed: mapped sections need an address.")
        if file_offset < _DOL_HEADER_SIZE:
            raise Prime3DolPatchError(
                f"DOL {section.name} slot is malformed: file offset 0x{file_offset:08x} overlaps the header."
            )
        if checked_add_u32(file_offset, size, f"{section.name} file range") > len(data):
            raise Prime3DolPatchError(
                f"DOL {section.name} slot is truncated: "
                f"0x{file_offset:08x}+0x{size:x} exceeds file length 0x{len(data):x}."
            )
        checked_add_u32(address, size, f"{section.name} virtual range")
        sections.append(section)

    header = DolHeader(
        sections=tuple(sections),
        bss_address=_read_u32_be(data, 0xD8),
        bss_size=_read_u32_be(data, 0xDC),
        entry_point=_read_u32_be(data, 0xE0),
    )
    _validate_header_layout(header)
    return header


def _validate_header_layout(header: DolHeader) -> None:
    mapped_sections = [section for section in header.sections if section.size > 0]
    sorted_by_offset = sorted(mapped_sections, key=lambda section: section.file_offset)
    for previous, current in zip(sorted_by_offset, sorted_by_offset[1:], strict=False):
        if current.file_offset < previous.end_offset:
            raise Prime3DolPatchError(f"DOL sections {previous.name} and {current.name} overlap in file space.")

    sorted_by_address = sorted(mapped_sections, key=lambda section: section.address)
    for previous, current in zip(sorted_by_address, sorted_by_address[1:], strict=False):
        if current.address < previous.end_address:
            raise Prime3DolPatchError(
                f"DOL sections {previous.name} and {current.name} overlap in virtual address space."
            )


def parse_dol_sections(data: bytes | bytearray) -> tuple[DolSection, ...]:
    return tuple(section for section in parse_dol_header(data).sections if section.size > 0)


def virtual_address_to_file_offset(
    sections: Iterable[DolSection],
    address: int,
    size: int = 1,
) -> int:
    if size <= 0:
        raise Prime3DolPatchError(f"Address mapping size must be positive, got {size}.")
    checked_add_u32(address, size, "virtual address mapping")

    for section in sections:
        if section.size > 0 and section.address <= address and address + size <= section.end_address:
            return section.file_offset + (address - section.address)

    raise Prime3DolPatchError(
        f"Virtual address 0x{address:08x} (+0x{size:x}) is not mapped by any DOL section."
    )


def _iter_supported_corruption_versions(
    versions: Iterable[CorruptionDolVersionLike] | None = None,
) -> tuple[CorruptionDolVersionLike, ...]:
    raw_versions: tuple[CorruptionDolVersionLike, ...]
    if versions is None:
        raw_versions = cast("tuple[CorruptionDolVersionLike, ...]", tuple(corruption_dol_versions.ALL_VERSIONS))
    else:
        raw_versions = tuple(versions)

    result = []
    for version in raw_versions:
        if version.game is not RDSGame.CORRUPTION:
            raise Prime3DolPatchError(f"Unsupported non-Corruption DOL version candidate: {version.description}")
        result.append(version)
    return tuple(result)


def _read_build_string_at_version(
    data: bytes | bytearray,
    sections: tuple[DolSection, ...],
    version: CorruptionDolVersionLike,
) -> tuple[int, bytes]:
    file_offset = virtual_address_to_file_offset(sections, version.build_string_address, len(version.build_string))
    return file_offset, bytes(data[file_offset : file_offset + len(version.build_string)])


def identify_supported_corruption_version(
    data: bytes | bytearray,
    versions: Iterable[CorruptionDolVersionLike] | None = None,
) -> CorruptionDolVersionLike:
    sections = parse_dol_sections(data)
    matches = []
    for version in _iter_supported_corruption_versions(versions):
        try:
            _file_offset, observed = _read_build_string_at_version(data, sections, version)
        except Prime3DolPatchError:
            continue

        expected = bytearray(version.build_string)
        expected[_UUID_START : _UUID_START + _UUID_LENGTH] = observed[_UUID_START : _UUID_START + _UUID_LENGTH]
        if observed == expected:
            matches.append(version)

    if not matches:
        raise Prime3DolPatchError("Unsupported or unknown Metroid Prime 3: Corruption DOL version.")
    if len(matches) > 1:
        descriptions = ", ".join(version.description for version in matches)
        raise Prime3DolPatchError(f"Ambiguous Corruption DOL version match: {descriptions}")
    return matches[0]


def patch_prime3_corruption_dol(
    data: bytes | bytearray,
    layout_uuid: uuid.UUID,
    *,
    version: CorruptionDolVersionLike | None = None,
    versions: Iterable[CorruptionDolVersionLike] | None = None,
) -> tuple[bytes, Prime3DolPatchResult]:
    mutable = bytearray(data)
    sections = parse_dol_sections(mutable)
    selected_version = identify_supported_corruption_version(mutable, versions) if version is None else version
    selected_version = _iter_supported_corruption_versions((selected_version,))[0]

    build_string_offset, observed = _read_build_string_at_version(mutable, sections, selected_version)

    expected = bytearray(selected_version.build_string)
    current_uuid_bytes = observed[_UUID_START : _UUID_START + _UUID_LENGTH]
    expected[_UUID_START : _UUID_START + _UUID_LENGTH] = current_uuid_bytes
    if observed != expected:
        raise Prime3DolPatchError(
            "Unexpected build string bytes for "
            f"{selected_version.description} at 0x{selected_version.build_string_address:08x}."
        )

    retail_bytes = selected_version.build_string[_UUID_START : _UUID_START + _UUID_LENGTH]
    previous_layout_uuid = None if current_uuid_bytes == retail_bytes else uuid.UUID(bytes=bytes(current_uuid_bytes))
    if previous_layout_uuid is not None and previous_layout_uuid != layout_uuid:
        raise Prime3DolPatchError(
            f"DOL already embeds conflicting layout UUID {previous_layout_uuid} for {selected_version.description}."
        )

    changed = current_uuid_bytes != layout_uuid.bytes
    mutable[build_string_offset + _UUID_START : build_string_offset + _UUID_START + _UUID_LENGTH] = layout_uuid.bytes

    result = Prime3DolPatchResult(
        version_description=selected_version.description,
        build_string_address=selected_version.build_string_address,
        build_string_offset=build_string_offset + _UUID_START,
        layout_uuid=layout_uuid,
        previous_layout_uuid=previous_layout_uuid,
        changed=changed,
        bytes_changed=_UUID_LENGTH if changed else 0,
    )
    return bytes(mutable), result


def append_executable_text_section(
    data: bytes | bytearray,
    *,
    payload_bytes: bytes,
    payload_virtual_address: int,
    required_alignment: int,
    entry_symbol_offset: int | None = None,
) -> tuple[bytes, ExecutableTextSectionInsertResult]:
    mutable = bytearray(data)
    header = parse_dol_header(mutable)
    empty_slots = header.unused_text_slots()
    if not empty_slots:
        raise Prime3DolPatchError("DOL has no unused text section slots available for payload insertion.")
    if not payload_bytes:
        raise Prime3DolPatchError("Executable payload bytes must not be empty.")

    payload_end_address = checked_add_u32(payload_virtual_address, len(payload_bytes), "payload virtual range")
    if entry_symbol_offset is not None:
        if entry_symbol_offset < 0 or entry_symbol_offset > len(payload_bytes):
            raise Prime3DolPatchError(
                f"Entry symbol offset {entry_symbol_offset} is outside payload size {len(payload_bytes)}."
            )
        entry_symbol_address = checked_add_u32(payload_virtual_address, entry_symbol_offset, "entry symbol address")
    else:
        entry_symbol_address = None

    sorted_by_address = sorted(
        (section for section in header.sections if section.size > 0),
        key=lambda section: section.address,
    )
    for section in sorted_by_address:
        if payload_virtual_address < section.end_address and section.address < payload_end_address:
            raise Prime3DolPatchError(f"Payload virtual range overlaps existing {section.name} section.")

    if (
        header.bss_size > 0
        and payload_virtual_address < header.bss_end_address
        and header.bss_address < payload_end_address
    ):
        raise Prime3DolPatchError("Payload virtual range overlaps the DOL BSS range.")

    file_offset = align_up(len(mutable), required_alignment)
    alignment_padding = file_offset - len(mutable)
    payload_file_end = checked_add_u32(file_offset, len(payload_bytes), "payload file range")

    for section in header.sections:
        if section.size == 0:
            continue
        if file_offset < section.end_offset and section.file_offset < payload_file_end:
            raise Prime3DolPatchError(f"Payload file range overlaps existing {section.name} section.")

    mutable.extend(b"\x00" * alignment_padding)
    mutable.extend(payload_bytes)

    new_sections = list(header.sections)
    selected_slot = empty_slots[0]
    new_sections[selected_slot.slot_index] = dataclasses.replace(
        selected_slot,
        file_offset=file_offset,
        address=payload_virtual_address,
        size=len(payload_bytes),
    )
    new_header = dataclasses.replace(header, sections=tuple(new_sections))
    _validate_header_layout(new_header)
    mutable[:_DOL_HEADER_SIZE] = build_dol_header_bytes(new_header)

    result = ExecutableTextSectionInsertResult(
        text_slot_index=selected_slot.slot_index,
        text_kind_index=selected_slot.kind_index,
        file_offset=file_offset,
        virtual_address=payload_virtual_address,
        payload_size=len(payload_bytes),
        alignment_padding=alignment_padding,
        resulting_file_size=len(mutable),
        entry_symbol_address=entry_symbol_address,
    )
    return bytes(mutable), result


def build_dol_header_bytes(header: DolHeader) -> bytes:
    result = bytearray(_DOL_HEADER_SIZE)
    for section in header.sections:
        result[section.slot_index * 4 : (section.slot_index + 1) * 4] = section.file_offset.to_bytes(4, "big")
        base = 0x48 + (section.slot_index * 4)
        result[base : base + 4] = section.address.to_bytes(4, "big")
        size_base = 0x90 + (section.slot_index * 4)
        result[size_base : size_base + 4] = section.size.to_bytes(4, "big")
    result[0xD8:0xDC] = header.bss_address.to_bytes(4, "big")
    result[0xDC:0xE0] = header.bss_size.to_bytes(4, "big")
    result[0xE0:0xE4] = header.entry_point.to_bytes(4, "big")
    return bytes(result)


def encode_ppc_unconditional_branch(
    source_address: int,
    target_address: int,
    *,
    link: bool = False,
    absolute: bool = False,
) -> int:
    if source_address & 0x3:
        raise Prime3DolPatchError(f"Branch source address 0x{source_address:08x} must be 4-byte aligned.")
    if target_address & 0x3:
        raise Prime3DolPatchError(f"Branch target address 0x{target_address:08x} must be 4-byte aligned.")

    if absolute:
        if target_address < 0 or target_address > _PPC_ABSOLUTE_BRANCH_MAX_ADDRESS:
            raise Prime3DolPatchError(
                f"Absolute branch target 0x{target_address:08x} is outside the supported 26-bit absolute range."
            )
        li_field = target_address
    else:
        displacement = target_address - source_address
        if displacement < _PPC_BRANCH_MIN_DISPLACEMENT or displacement > _PPC_BRANCH_MAX_DISPLACEMENT:
            raise Prime3DolPatchError(
                f"Relative branch displacement {displacement} is outside the signed 26-bit branch range."
            )
        li_field = displacement & 0x03FFFFFC

    return (_PPC_BRANCH_OPCODE << 26) | li_field | (int(absolute) << 1) | int(link)


def decode_ppc_unconditional_branch(instruction_word: int, instruction_address: int) -> DecodedBranchInstruction | None:
    opcode = instruction_word >> 26
    if opcode != _PPC_BRANCH_OPCODE:
        return None

    li_field = instruction_word & 0x03FFFFFC
    if li_field & 0x02000000:
        li_field -= 0x04000000
    absolute = bool(instruction_word & 0x2)
    link = bool(instruction_word & 0x1)
    target_address = li_field if absolute else instruction_address + li_field
    return DecodedBranchInstruction(
        instruction_address=instruction_address,
        instruction_word=instruction_word,
        target_address=target_address,
        absolute=absolute,
        link=link,
    )


def patch_guarded_instruction_word(
    data: bytes | bytearray,
    *,
    address: int,
    expected_original_word: int,
    replacement_word: int,
) -> tuple[bytes, GuardedInstructionPatchResult]:
    mutable = bytearray(data)
    header = parse_dol_header(mutable)
    section = header.section_for_address(address)
    if section is None:
        raise Prime3DolPatchError(f"Instruction patch target 0x{address:08x} is not mapped in the DOL.")
    if section.kind != "text":
        raise Prime3DolPatchError(f"Instruction patch target 0x{address:08x} is inside {section.name}, not text.")
    if address & 0x3:
        raise Prime3DolPatchError(f"Instruction patch target 0x{address:08x} must be 4-byte aligned.")

    file_offset = header.offset_for_address(address)
    assert file_offset is not None
    if file_offset + 4 > len(mutable):
        raise Prime3DolPatchError(f"Instruction patch target 0x{address:08x} is truncated.")

    observed_word = int.from_bytes(mutable[file_offset : file_offset + 4], "big")
    if observed_word == replacement_word and observed_word != expected_original_word:
        raise Prime3DolPatchError(f"Instruction at 0x{address:08x} already contains the replacement word.")
    if observed_word != expected_original_word:
        raise Prime3DolPatchError(
            f"Instruction at 0x{address:08x} was 0x{observed_word:08x}, expected 0x{expected_original_word:08x}."
        )

    mutable[file_offset : file_offset + 4] = replacement_word.to_bytes(4, "big")
    result = GuardedInstructionPatchResult(
        address=address,
        file_offset=file_offset,
        original_word=expected_original_word,
        replacement_word=replacement_word,
        changed=expected_original_word != replacement_word,
    )
    return bytes(mutable), result


def _is_supported_displaced_instruction(word: int) -> bool:
    opcode = word >> 26
    if opcode in {16, 18}:
        return False
    if opcode == 19:
        xo = (word >> 1) & 0x3FF
        if xo in {16, 528}:
            return False
    return True


def build_single_instruction_trampoline(
    *,
    hook_address: int,
    expected_original_instruction: int,
    payload_entry_address: int,
    return_address: int | None = None,
    trampoline_address: int | None = None,
    trampoline_offset_from_payload: int | None = None,
) -> TrampolinePlan:
    if trampoline_address is None and trampoline_offset_from_payload is None:
        raise Prime3DolPatchError("A trampoline address or payload-relative trampoline offset is required.")
    if trampoline_address is not None and trampoline_offset_from_payload is not None:
        raise Prime3DolPatchError("Specify either trampoline_address or trampoline_offset_from_payload, not both.")
    if trampoline_offset_from_payload is not None:
        trampoline_address = checked_add_u32(
            payload_entry_address,
            trampoline_offset_from_payload,
            "payload-relative trampoline address",
        )
    assert trampoline_address is not None

    if not _is_supported_displaced_instruction(expected_original_instruction):
        raise Prime3DolPatchError(
            f"Instruction 0x{expected_original_instruction:08x} at hook 0x{hook_address:08x} is not safe to displace."
        )

    if return_address is None:
        return_address = checked_add_u32(hook_address, 4, "default trampoline return address")

    hook_word = encode_ppc_unconditional_branch(hook_address, payload_entry_address)
    return_branch_source = checked_add_u32(trampoline_address, 4, "trampoline return branch source")
    return_word = encode_ppc_unconditional_branch(return_branch_source, return_address)

    return TrampolinePlan(
        hook_patch=BranchPatch(
            source_address=hook_address,
            target_address=payload_entry_address,
            instruction_word=hook_word,
            absolute=False,
            link=False,
        ),
        trampoline_address=trampoline_address,
        displaced_instruction_word=expected_original_instruction,
        return_branch=BranchPatch(
            source_address=return_branch_source,
            target_address=return_address,
            instruction_word=return_word,
            absolute=False,
            link=False,
        ),
        payload_entry_address=payload_entry_address,
        return_address=return_address,
    )


def atomic_replace_file(path: Path, data: bytes) -> None:
    path = Path(path)
    temp_fd, temp_name = tempfile.mkstemp(dir=path.parent, prefix=f"{path.name}.", suffix=".tmp")
    temp_path = Path(temp_name)
    try:
        with os.fdopen(temp_fd, "wb") as temp_file:
            temp_file.write(data)
        temp_path.replace(path)
    except Exception:
        try:
            temp_path.unlink()
        except FileNotFoundError:
            pass
        raise


def patch_prime3_corruption_dol_file_atomic(
    path: Path,
    layout_uuid: uuid.UUID,
    *,
    versions: Iterable[CorruptionDolVersionLike] | None = None,
) -> Prime3DolPatchResult:
    original_data = path.read_bytes()
    patched_data, result = patch_prime3_corruption_dol(original_data, layout_uuid, versions=versions)
    atomic_replace_file(path, patched_data)
    return result
