# Version 1 UDP protocol used by Corruptovania to communicate with Metroid Prime 3 Wii.
# Boundary names here: Prime3WiiProtocolError, MalformedPacketError, BadMagicError,
# UnsupportedProtocolVersionError, UnknownCommandError.
"""
Version 1 UDP protocol used by Corruptovania to communicate with Metroid Prime 3 Wii.

Version 1 preserves a fixed CP3W packet framing layer and currently defines
deterministic HELLO negotiation, PING, READ_MEMORY, and DISCONNECT command
families. Arbitrary memory writes and gameplay mailbox traffic remain deferred.

Packet format, big-endian:

- magic: 4 bytes, ASCII ``CP3W``
- protocol_version: uint8
- packet_kind: uint8
- command: uint8
- response_status: uint8
- request_id: uint32
- payload_length: uint32
- payload: ``payload_length`` bytes
- crc32: uint32 over every previous byte in the packet
"""

from __future__ import annotations

import dataclasses
import enum
import struct
import zlib

PROTOCOL_MAGIC = b"CP3W"
PROTOCOL_VERSION = 1
HEADER_FORMAT = ">4sBBBBII"
HEADER_SIZE = struct.calcsize(HEADER_FORMAT)
CRC_SIZE = 4
HELLO_REQUEST_FIXED_FORMAT = ">BBII"
HELLO_RESPONSE_FIXED_FORMAT = ">BIIIIBB"
READ_MEMORY_PAYLOAD_FORMAT = ">II"
GAME_IDENTITY_PAYLOAD_FORMAT = ">BBBBHBBIIIII"
GAME_IDENTITY_PROFILE_FINGERPRINT_FORMAT = ">BBBHIIIII"
INVENTORY_HEADER_FORMAT = ">BBBBII"
INVENTORY_RECORD_FORMAT = ">II"
ERROR_HEADER_FORMAT = ">HHH"
HELLO_NAME_LENGTH_FORMAT = ">B"
HELLO_REQUEST_FIXED_SIZE = struct.calcsize(HELLO_REQUEST_FIXED_FORMAT)
HELLO_RESPONSE_FIXED_SIZE = struct.calcsize(HELLO_RESPONSE_FIXED_FORMAT)
HELLO_NAME_LENGTH_SIZE = struct.calcsize(HELLO_NAME_LENGTH_FORMAT)
HELLO_MAX_NAME_LENGTH = 31
HELLO_METADATA_VERSION = 1
DEFAULT_RUNTIME_NAME = "Prime3 Wii Runtime"
DEFAULT_RUNTIME_BUILD_ID = 0x50335731
GAME_IDENTITY_SCHEMA_VERSION = 1
GAME_IDENTITY_PAYLOAD_SIZE = struct.calcsize(GAME_IDENTITY_PAYLOAD_FORMAT)
INVENTORY_SCHEMA_VERSION = 1
INVENTORY_ITEM_IDS = (*range(43), 44, 45, 46, 48, 49, 50, 51, 52, *range(62, 70))
INVENTORY_RECORD_COUNT = len(INVENTORY_ITEM_IDS)
INVENTORY_HEADER_SIZE = struct.calcsize(INVENTORY_HEADER_FORMAT)
INVENTORY_RECORD_SIZE = struct.calcsize(INVENTORY_RECORD_FORMAT)
INVENTORY_PAYLOAD_SIZE = INVENTORY_HEADER_SIZE + INVENTORY_RECORD_COUNT * INVENTORY_RECORD_SIZE
INVENTORY_FRAME_SIZE = HEADER_SIZE + INVENTORY_PAYLOAD_SIZE + CRC_SIZE
INVENTORY_FIELD_OFFSETS = {
    "schema_version": 0,
    "record_count": 1,
    "record_size": 2,
    "reserved0": 3,
    "availability_flags": 4,
    "snapshot_sequence": 8,
    "records": INVENTORY_HEADER_SIZE,
}
GAME_IDENTITY_FIELD_OFFSETS = {
    "schema_version": 0,
    "game_id": 1,
    "platform_id": 2,
    "region_id": 3,
    "revision_id": 4,
    "protocol_version": 6,
    "runtime_mode": 7,
    "profile_id": 8,
    "profile_fingerprint": 12,
    "runtime_build_id": 16,
    "availability_flags": 20,
    "reserved": 24,
}
PRIME3_NTSC_RETAIL_PROFILE_ID = 0x50334E41
PRIME3_NTSC_RETAIL_DOL_SHA256_PREFIX = 0x6B550F22
PRIME3_NTSC_BUILD_STRING_ADDRESS = 0x805822B0
PRIME3_NTSC_GAME_STATE_POINTER_ADDRESS = 0x8067DC0C
PRIME3_NTSC_CSTATE_MANAGER_GLOBAL_ADDRESS = 0x805C4F70
PRIME3_NTSC_CPLAYER_VTABLE = 0x80592C78
NOT_NEGOTIATED_MESSAGE = "Negotiation required before PING."
GAME_IDENTITY_NOT_NEGOTIATED_MESSAGE = "Negotiation required before GET_GAME_IDENTITY."
GAME_IDENTITY_CAPABILITY_MESSAGE = "GAME_IDENTITY capability was not negotiated."
GAME_IDENTITY_INVALID_PAYLOAD_MESSAGE = "GET_GAME_IDENTITY request payload must be empty."
INVENTORY_NOT_NEGOTIATED_MESSAGE = "Negotiation required before GET_INVENTORY."
INVENTORY_CAPABILITY_MESSAGE = "INVENTORY_STATE capability was not negotiated."
INVENTORY_INVALID_PAYLOAD_MESSAGE = "GET_INVENTORY request payload must be empty."
UNSUPPORTED_VERSION_MESSAGE = "Unsupported protocol version range."
INVALID_STATE_MESSAGE = "Session is already negotiated."
UNKNOWN_COMMAND_MESSAGE = "Command is unsupported"


class Prime3WiiProtocolError(Exception):
    pass


class MalformedPacketError(Prime3WiiProtocolError):
    pass


class BadMagicError(MalformedPacketError):
    pass


class UnsupportedProtocolVersionError(MalformedPacketError):
    pass


class UnknownCommandError(MalformedPacketError):
    pass


class InvalidPayloadLengthError(MalformedPacketError):
    pass


class CorruptedChecksumError(MalformedPacketError):
    pass


class MismatchedRequestIdError(Prime3WiiProtocolError):
    pass


class UnsupportedIdentitySchemaError(Prime3WiiProtocolError):
    pass


class UnsupportedInventorySchemaError(Prime3WiiProtocolError):
    pass


class ServerSideProtocolError(Prime3WiiProtocolError):
    def __init__(self, error_code: Prime3WiiErrorCode, message: str, command: Prime3WiiCommand):
        super().__init__(f"{error_code.name} for {command.name}: {message}")
        self.error_code = error_code
        self.message = message
        self.command = command


class Prime3WiiPacketKind(enum.IntEnum):
    REQUEST = 1
    RESPONSE = 2


class Prime3WiiCommand(enum.IntEnum):
    HELLO = 1
    READ_MEMORY = 2
    PING = 3
    DISCONNECT = 4
    GET_GAME_IDENTITY = 5
    GET_INVENTORY = 6
    EXPERIMENTAL_RECEIPT_STATE = 7
    EXPERIMENTAL_FIXED_DELIVERY = 8
    EXPERIMENTAL_TRACKER_SNAPSHOT = 9
    RESERVED_MAILBOX = 127


class Prime3WiiResponseStatus(enum.IntEnum):
    OK = 0
    ERROR = 1


class Prime3WiiCapability(enum.IntFlag):
    HELLO_NEGOTIATION = 1 << 0
    PING = 1 << 1
    STRUCTURED_ERRORS = 1 << 2
    DETERMINISTIC_SESSION_ID = 1 << 3
    READ_MEMORY = 1 << 4
    STRUCTURED_MAILBOX = 1 << 5
    MEMORY_WRITE = 1 << 6
    GAMEPLAY_MAILBOX = 1 << 7
    EVENT_STREAMING = 1 << 8
    RECONNECT = 1 << 9
    AUTHENTICATION = 1 << 10
    GAME_IDENTITY = 1 << 11
    INVENTORY_STATE = 1 << 12
    EXPERIMENTAL_RECEIPTED_DELIVERY = 1 << 13
    EXPERIMENTAL_READ_ONLY_TRACKER = 1 << 14


HELLO_RUNTIME_CAPABILITIES = (
    Prime3WiiCapability.HELLO_NEGOTIATION
    | Prime3WiiCapability.PING
    | Prime3WiiCapability.STRUCTURED_ERRORS
    | Prime3WiiCapability.DETERMINISTIC_SESSION_ID
)

READ_ONLY_RUNTIME_CAPABILITIES = HELLO_RUNTIME_CAPABILITIES | Prime3WiiCapability.READ_MEMORY
GAME_IDENTITY_RUNTIME_CAPABILITIES = HELLO_RUNTIME_CAPABILITIES | Prime3WiiCapability.GAME_IDENTITY
INVENTORY_RUNTIME_CAPABILITIES = GAME_IDENTITY_RUNTIME_CAPABILITIES | Prime3WiiCapability.INVENTORY_STATE


class Prime3WiiErrorCode(enum.IntEnum):
    MALFORMED_PACKET = 1
    BAD_MAGIC = 2
    UNSUPPORTED_VERSION = 3
    UNKNOWN_COMMAND = 4
    INVALID_PAYLOAD_LENGTH = 5
    CHECKSUM_MISMATCH = 6
    INVALID_ADDRESS = 7
    SERVER_ERROR = 8
    NOT_NEGOTIATED = 9
    INVALID_STATE = 10
    CAPABILITY_NOT_NEGOTIATED = 11


class Prime3WiiGameId(enum.IntEnum):
    METROID_PRIME_3_CORRUPTION = 1


class Prime3WiiPlatformId(enum.IntEnum):
    WII = 1


class Prime3WiiRegionId(enum.IntEnum):
    NTSC_U = 1
    PAL = 2
    NTSC_J = 3


class Prime3WiiRevisionId(enum.IntEnum):
    WII_NTSC_3_436 = 1
    WII_PAL_3_453 = 2
    WII_NTSC_J_3_495 = 3


class Prime3WiiAvailability(enum.IntFlag):
    EXECUTABLE_RECOGNIZED = 1 << 0
    GAME_STATE_POINTER_VALID = 1 << 1
    PLAYER_STATE_POINTER_VALID = 1 << 2
    INVENTORY_ROOT_AVAILABLE = 1 << 3
    WORLD_STATE_AVAILABLE = 1 << 4


class Prime3WiiInventoryAvailability(enum.IntFlag):
    EXECUTABLE_RECOGNIZED = 1 << 0
    GAME_STATE_POINTER_VALID = 1 << 1
    INVENTORY_ROOT_VALID = 1 << 2
    SNAPSHOT_AVAILABLE = 1 << 3
    TEMPORARILY_UNAVAILABLE = 1 << 4
    CONSISTENCY_CHECK_PASSED = 1 << 5
    INCONSISTENT_SNAPSHOT = 1 << 6
    RANGE_VALID = 1 << 7


def derive_profile_fingerprint(
    *,
    game_id: Prime3WiiGameId,
    platform_id: Prime3WiiPlatformId,
    region_id: Prime3WiiRegionId,
    revision_id: Prime3WiiRevisionId,
    profile_id: int,
    game_state_pointer_address: int,
    cstate_manager_global_address: int,
    cplayer_vtable: int,
    dol_sha256_prefix: int,
) -> int:
    canonical = struct.pack(
        GAME_IDENTITY_PROFILE_FINGERPRINT_FORMAT,
        game_id,
        platform_id,
        region_id,
        revision_id,
        profile_id,
        game_state_pointer_address,
        cstate_manager_global_address,
        cplayer_vtable,
        dol_sha256_prefix,
    )
    return zlib.crc32(canonical) & 0xFFFFFFFF


PRIME3_NTSC_RETAIL_PROFILE_FINGERPRINT = derive_profile_fingerprint(
    game_id=Prime3WiiGameId.METROID_PRIME_3_CORRUPTION,
    platform_id=Prime3WiiPlatformId.WII,
    region_id=Prime3WiiRegionId.NTSC_U,
    revision_id=Prime3WiiRevisionId.WII_NTSC_3_436,
    profile_id=PRIME3_NTSC_RETAIL_PROFILE_ID,
    game_state_pointer_address=PRIME3_NTSC_GAME_STATE_POINTER_ADDRESS,
    cstate_manager_global_address=PRIME3_NTSC_CSTATE_MANAGER_GLOBAL_ADDRESS,
    cplayer_vtable=PRIME3_NTSC_CPLAYER_VTABLE,
    dol_sha256_prefix=PRIME3_NTSC_RETAIL_DOL_SHA256_PREFIX,
)


@dataclasses.dataclass(frozen=True)
class HelloRequestPayload:
    min_protocol_version: int
    max_protocol_version: int
    capabilities: Prime3WiiCapability
    client_nonce: int
    client_name: str = ""


@dataclasses.dataclass(frozen=True)
class HelloResponsePayload:
    selected_protocol_version: int
    runtime_capabilities: Prime3WiiCapability
    accepted_client_capabilities: Prime3WiiCapability
    session_id: int
    runtime_build_id: int
    runtime_mode: int
    runtime_metadata_version: int = HELLO_METADATA_VERSION
    runtime_name: str = DEFAULT_RUNTIME_NAME


HelloPayload = HelloResponsePayload


@dataclasses.dataclass(frozen=True)
class ReadMemoryPayload:
    address: int
    size: int


@dataclasses.dataclass(frozen=True)
class GameIdentityPayload:
    schema_version: int = GAME_IDENTITY_SCHEMA_VERSION
    game_id: Prime3WiiGameId = Prime3WiiGameId.METROID_PRIME_3_CORRUPTION
    platform_id: Prime3WiiPlatformId = Prime3WiiPlatformId.WII
    region_id: Prime3WiiRegionId = Prime3WiiRegionId.NTSC_U
    revision_id: Prime3WiiRevisionId = Prime3WiiRevisionId.WII_NTSC_3_436
    protocol_version: int = PROTOCOL_VERSION
    runtime_mode: int = 20
    profile_id: int = PRIME3_NTSC_RETAIL_PROFILE_ID
    profile_fingerprint: int = PRIME3_NTSC_RETAIL_PROFILE_FINGERPRINT
    runtime_build_id: int = DEFAULT_RUNTIME_BUILD_ID
    availability_flags: Prime3WiiAvailability = Prime3WiiAvailability(0)
    reserved: int = 0


@dataclasses.dataclass(frozen=True)
class Prime3WiiInventoryRecord:
    amount: int
    capacity: int


@dataclasses.dataclass(frozen=True)
class Prime3WiiInventorySnapshot:
    schema_version: int = INVENTORY_SCHEMA_VERSION
    availability_flags: Prime3WiiInventoryAvailability = Prime3WiiInventoryAvailability(0)
    snapshot_sequence: int = 0
    records: tuple[Prime3WiiInventoryRecord, ...] = dataclasses.field(
        default_factory=lambda: (Prime3WiiInventoryRecord(0, 0),) * INVENTORY_RECORD_COUNT
    )

    @property
    def is_available(self) -> bool:
        return bool(self.availability_flags & Prime3WiiInventoryAvailability.SNAPSHOT_AVAILABLE)

    def record_for_item_id(self, item_id: int) -> Prime3WiiInventoryRecord:
        try:
            index = INVENTORY_ITEM_IDS.index(item_id)
        except ValueError as exc:
            raise KeyError(item_id) from exc
        return self.records[index]


@dataclasses.dataclass(frozen=True)
class Prime3WiiRequest:
    command: Prime3WiiCommand
    request_id: int
    payload: bytes = b""


@dataclasses.dataclass(frozen=True)
class Prime3WiiResponse:
    command: Prime3WiiCommand
    request_id: int
    status: Prime3WiiResponseStatus
    payload: bytes = b""


@dataclasses.dataclass(frozen=True)
class Prime3WiiErrorResponse:
    command: Prime3WiiCommand
    request_id: int
    error_code: Prime3WiiErrorCode
    message: str


def crc32_bytes(data: bytes) -> int:
    return zlib.crc32(data) & 0xFFFFFFFF


def _validate_u8(value: int, label: str) -> None:
    if value < 0 or value > 0xFF:
        raise InvalidPayloadLengthError(f"{label} must fit in uint8, got {value}.")


def _validate_u32(value: int, label: str) -> None:
    if value < 0 or value > 0xFFFFFFFF:
        raise InvalidPayloadLengthError(f"{label} must fit in uint32, got {value}.")


def _encode_bounded_name(name: str, *, field_name: str) -> bytes:
    encoded = name.encode("utf-8")
    if len(encoded) > HELLO_MAX_NAME_LENGTH:
        raise InvalidPayloadLengthError(
            f"{field_name} must be at most {HELLO_MAX_NAME_LENGTH} UTF-8 bytes, got {len(encoded)}."
        )
    return struct.pack(HELLO_NAME_LENGTH_FORMAT, len(encoded)) + encoded


def _decode_bounded_name(payload: bytes, *, offset: int, field_name: str) -> tuple[str, int]:
    if len(payload) < offset + HELLO_NAME_LENGTH_SIZE:
        raise InvalidPayloadLengthError(f"{field_name} payload is missing the name-length field.")
    (name_length,) = struct.unpack(HELLO_NAME_LENGTH_FORMAT, payload[offset : offset + HELLO_NAME_LENGTH_SIZE])
    start = offset + HELLO_NAME_LENGTH_SIZE
    end = start + name_length
    if end != len(payload):
        raise InvalidPayloadLengthError(
            f"{field_name} payload length mismatch: expected trailing name bytes {name_length}, "
            f"got {len(payload) - start}."
        )
    if name_length > HELLO_MAX_NAME_LENGTH:
        raise InvalidPayloadLengthError(
            f"{field_name} name must be at most {HELLO_MAX_NAME_LENGTH} bytes, got {name_length}."
        )
    try:
        return payload[start:end].decode("utf-8"), name_length
    except UnicodeDecodeError as exc:
        raise InvalidPayloadLengthError(f"{field_name} name is not valid UTF-8.") from exc


def negotiate_protocol_version(payload: HelloRequestPayload) -> int | None:
    if payload.min_protocol_version > payload.max_protocol_version:
        return None
    if payload.min_protocol_version <= PROTOCOL_VERSION <= payload.max_protocol_version:
        return PROTOCOL_VERSION
    return None


def compute_accepted_capabilities(
    client_capabilities: Prime3WiiCapability,
    runtime_capabilities: Prime3WiiCapability,
) -> Prime3WiiCapability:
    return Prime3WiiCapability(int(client_capabilities) & int(runtime_capabilities))


def derive_session_id(
    *,
    selected_protocol_version: int,
    client_nonce: int,
    runtime_build_id: int,
    runtime_capabilities: Prime3WiiCapability,
    accepted_client_capabilities: Prime3WiiCapability,
) -> int:
    _validate_u8(selected_protocol_version, "selected_protocol_version")
    _validate_u32(client_nonce, "client_nonce")
    _validate_u32(runtime_build_id, "runtime_build_id")
    canonical = struct.pack(
        ">BIIII",
        selected_protocol_version,
        client_nonce,
        int(runtime_build_id),
        int(runtime_capabilities),
        int(accepted_client_capabilities),
    )
    return crc32_bytes(canonical)


def _encode_packet(
    packet_kind: Prime3WiiPacketKind,
    command: Prime3WiiCommand,
    response_status: Prime3WiiResponseStatus,
    request_id: int,
    payload: bytes,
) -> bytes:
    header = struct.pack(
        HEADER_FORMAT,
        PROTOCOL_MAGIC,
        PROTOCOL_VERSION,
        packet_kind,
        command,
        response_status,
        request_id,
        len(payload),
    )
    body = header + payload
    checksum = crc32_bytes(body)
    return body + struct.pack(">I", checksum)


def _decode_packet(
    packet: bytes,
) -> tuple[Prime3WiiPacketKind, Prime3WiiCommand, Prime3WiiResponseStatus, int, bytes]:
    if len(packet) < HEADER_SIZE + CRC_SIZE:
        raise InvalidPayloadLengthError("Packet shorter than minimum header size")

    payload_end = len(packet) - CRC_SIZE
    body = packet[:payload_end]
    actual_crc = crc32_bytes(body)
    expected_crc = struct.unpack(">I", packet[payload_end:])[0]
    if actual_crc != expected_crc:
        raise CorruptedChecksumError("CRC32 mismatch")

    magic, version, packet_kind_raw, command_raw, response_status_raw, request_id, payload_length = struct.unpack(
        HEADER_FORMAT, packet[:HEADER_SIZE]
    )

    if magic != PROTOCOL_MAGIC:
        raise BadMagicError(f"Unexpected magic {magic!r}")
    if version != PROTOCOL_VERSION:
        raise UnsupportedProtocolVersionError(f"Unsupported protocol version {version}")

    try:
        packet_kind = Prime3WiiPacketKind(packet_kind_raw)
    except ValueError as e:
        raise MalformedPacketError(f"Unknown packet kind {packet_kind_raw}") from e

    try:
        command = Prime3WiiCommand(command_raw)
    except ValueError as e:
        raise UnknownCommandError(f"Unknown command {command_raw}") from e

    try:
        response_status = Prime3WiiResponseStatus(response_status_raw)
    except ValueError as e:
        raise MalformedPacketError(f"Unknown response status {response_status_raw}") from e

    actual_payload = packet[HEADER_SIZE:payload_end]
    if len(actual_payload) != payload_length:
        raise InvalidPayloadLengthError(
            f"Payload length mismatch: header says {payload_length}, packet contains {len(actual_payload)}"
        )

    return packet_kind, command, response_status, request_id, actual_payload


def encode_request(request: Prime3WiiRequest) -> bytes:
    return _encode_packet(
        Prime3WiiPacketKind.REQUEST,
        request.command,
        Prime3WiiResponseStatus.OK,
        request.request_id,
        request.payload,
    )


def decode_request(packet: bytes) -> Prime3WiiRequest:
    packet_kind, command, response_status, request_id, payload = _decode_packet(packet)
    if packet_kind is not Prime3WiiPacketKind.REQUEST:
        raise MalformedPacketError(f"Expected request packet, got {packet_kind.name}")
    if response_status is not Prime3WiiResponseStatus.OK:
        raise MalformedPacketError("Requests must use response status OK")
    return Prime3WiiRequest(command=command, request_id=request_id, payload=payload)


def encode_response(response: Prime3WiiResponse) -> bytes:
    return _encode_packet(
        Prime3WiiPacketKind.RESPONSE,
        response.command,
        response.status,
        response.request_id,
        response.payload,
    )


def decode_response(
    packet: bytes,
    *,
    expected_request_id: int | None = None,
) -> Prime3WiiResponse | Prime3WiiErrorResponse:
    packet_kind, command, response_status, request_id, payload = _decode_packet(packet)
    if packet_kind is not Prime3WiiPacketKind.RESPONSE:
        raise MalformedPacketError(f"Expected response packet, got {packet_kind.name}")
    if expected_request_id is not None and request_id != expected_request_id:
        raise MismatchedRequestIdError(f"Expected request id {expected_request_id}, got {request_id}")

    if response_status is Prime3WiiResponseStatus.ERROR:
        return decode_error_response_payload(command, request_id, payload)

    return Prime3WiiResponse(command=command, request_id=request_id, status=response_status, payload=payload)


def encode_hello_request_payload(payload: HelloRequestPayload) -> bytes:
    _validate_u8(payload.min_protocol_version, "min_protocol_version")
    _validate_u8(payload.max_protocol_version, "max_protocol_version")
    _validate_u32(payload.client_nonce, "client_nonce")
    name_bytes = _encode_bounded_name(payload.client_name, field_name="HELLO request")
    return (
        struct.pack(
            HELLO_REQUEST_FIXED_FORMAT,
            payload.min_protocol_version,
            payload.max_protocol_version,
            int(payload.capabilities),
            payload.client_nonce,
        )
        + name_bytes
    )


def decode_hello_request_payload(payload: bytes) -> HelloRequestPayload:
    if len(payload) < HELLO_REQUEST_FIXED_SIZE + HELLO_NAME_LENGTH_SIZE:
        raise InvalidPayloadLengthError(
            f"HELLO request payload must be at least {HELLO_REQUEST_FIXED_SIZE + HELLO_NAME_LENGTH_SIZE} bytes, "
            f"got {len(payload)}"
        )
    min_protocol_version, max_protocol_version, capabilities, client_nonce = struct.unpack(
        HELLO_REQUEST_FIXED_FORMAT, payload[:HELLO_REQUEST_FIXED_SIZE]
    )
    client_name, _ = _decode_bounded_name(payload, offset=HELLO_REQUEST_FIXED_SIZE, field_name="HELLO request")
    return HelloRequestPayload(
        min_protocol_version=min_protocol_version,
        max_protocol_version=max_protocol_version,
        capabilities=Prime3WiiCapability(capabilities),
        client_nonce=client_nonce,
        client_name=client_name,
    )


def encode_hello_response_payload(payload: HelloResponsePayload) -> bytes:
    _validate_u8(payload.selected_protocol_version, "selected_protocol_version")
    _validate_u32(payload.session_id, "session_id")
    _validate_u32(payload.runtime_build_id, "runtime_build_id")
    _validate_u8(payload.runtime_mode, "runtime_mode")
    _validate_u8(payload.runtime_metadata_version, "runtime_metadata_version")
    name_bytes = _encode_bounded_name(payload.runtime_name, field_name="HELLO response")
    return (
        struct.pack(
            HELLO_RESPONSE_FIXED_FORMAT,
            payload.selected_protocol_version,
            int(payload.runtime_capabilities),
            int(payload.accepted_client_capabilities),
            payload.session_id,
            payload.runtime_build_id,
            payload.runtime_mode,
            payload.runtime_metadata_version,
        )
        + name_bytes
    )


def decode_hello_response_payload(payload: bytes) -> HelloResponsePayload:
    if len(payload) < HELLO_RESPONSE_FIXED_SIZE + HELLO_NAME_LENGTH_SIZE:
        raise InvalidPayloadLengthError(
            f"HELLO response payload must be at least {HELLO_RESPONSE_FIXED_SIZE + HELLO_NAME_LENGTH_SIZE} bytes, "
            f"got {len(payload)}"
        )
    (
        selected_protocol_version,
        runtime_capabilities,
        accepted_client_capabilities,
        session_id,
        runtime_build_id,
        runtime_mode,
        runtime_metadata_version,
    ) = struct.unpack(HELLO_RESPONSE_FIXED_FORMAT, payload[:HELLO_RESPONSE_FIXED_SIZE])
    runtime_name, _ = _decode_bounded_name(payload, offset=HELLO_RESPONSE_FIXED_SIZE, field_name="HELLO response")
    return HelloResponsePayload(
        selected_protocol_version=selected_protocol_version,
        runtime_capabilities=Prime3WiiCapability(runtime_capabilities),
        accepted_client_capabilities=Prime3WiiCapability(accepted_client_capabilities),
        session_id=session_id,
        runtime_build_id=runtime_build_id,
        runtime_mode=runtime_mode,
        runtime_metadata_version=runtime_metadata_version,
        runtime_name=runtime_name,
    )


def encode_hello_payload(payload: HelloPayload) -> bytes:
    return encode_hello_response_payload(payload)


def decode_hello_payload(payload: bytes) -> HelloPayload:
    return decode_hello_response_payload(payload)


def encode_read_memory_payload(payload: ReadMemoryPayload) -> bytes:
    return struct.pack(READ_MEMORY_PAYLOAD_FORMAT, payload.address, payload.size)


def decode_read_memory_payload(payload: bytes) -> ReadMemoryPayload:
    expected_size = struct.calcsize(READ_MEMORY_PAYLOAD_FORMAT)
    if len(payload) != expected_size:
        raise InvalidPayloadLengthError(f"READ_MEMORY payload must be {expected_size} bytes, got {len(payload)}")
    address, size = struct.unpack(READ_MEMORY_PAYLOAD_FORMAT, payload)
    return ReadMemoryPayload(address=address, size=size)


def encode_game_identity_payload(payload: GameIdentityPayload) -> bytes:
    _validate_u8(payload.schema_version, "schema_version")
    _validate_u8(payload.game_id, "game_id")
    _validate_u8(payload.platform_id, "platform_id")
    _validate_u8(payload.region_id, "region_id")
    if payload.revision_id < 0 or payload.revision_id > 0xFFFF:
        raise InvalidPayloadLengthError(f"revision_id must fit in uint16, got {payload.revision_id}.")
    _validate_u8(payload.protocol_version, "protocol_version")
    _validate_u8(payload.runtime_mode, "runtime_mode")
    _validate_u32(payload.profile_id, "profile_id")
    _validate_u32(payload.profile_fingerprint, "profile_fingerprint")
    _validate_u32(payload.runtime_build_id, "runtime_build_id")
    _validate_u32(payload.availability_flags, "availability_flags")
    _validate_u32(payload.reserved, "reserved")
    if payload.reserved != 0:
        raise InvalidPayloadLengthError("GET_GAME_IDENTITY reserved field must be zero.")
    return struct.pack(
        GAME_IDENTITY_PAYLOAD_FORMAT,
        payload.schema_version,
        payload.game_id,
        payload.platform_id,
        payload.region_id,
        payload.revision_id,
        payload.protocol_version,
        payload.runtime_mode,
        payload.profile_id,
        payload.profile_fingerprint,
        payload.runtime_build_id,
        int(payload.availability_flags),
        payload.reserved,
    )


def decode_game_identity_payload(payload: bytes) -> GameIdentityPayload:
    if len(payload) != GAME_IDENTITY_PAYLOAD_SIZE:
        raise InvalidPayloadLengthError(
            f"GET_GAME_IDENTITY response payload must be {GAME_IDENTITY_PAYLOAD_SIZE} bytes, got {len(payload)}"
        )
    (
        schema_version,
        game_id,
        platform_id,
        region_id,
        revision_id,
        protocol_version,
        runtime_mode,
        profile_id,
        profile_fingerprint,
        runtime_build_id,
        availability_flags,
        reserved,
    ) = struct.unpack(GAME_IDENTITY_PAYLOAD_FORMAT, payload)
    if schema_version != GAME_IDENTITY_SCHEMA_VERSION:
        raise UnsupportedIdentitySchemaError(
            f"Unsupported GET_GAME_IDENTITY schema {schema_version}; expected {GAME_IDENTITY_SCHEMA_VERSION}."
        )
    if reserved != 0:
        raise InvalidPayloadLengthError("GET_GAME_IDENTITY reserved field must be zero.")
    try:
        decoded_game_id = Prime3WiiGameId(game_id)
        decoded_platform_id = Prime3WiiPlatformId(platform_id)
        decoded_region_id = Prime3WiiRegionId(region_id)
        decoded_revision_id = Prime3WiiRevisionId(revision_id)
    except ValueError as exc:
        raise InvalidPayloadLengthError(f"GET_GAME_IDENTITY contains an unknown identity enum: {exc}") from exc
    return GameIdentityPayload(
        schema_version=schema_version,
        game_id=decoded_game_id,
        platform_id=decoded_platform_id,
        region_id=decoded_region_id,
        revision_id=decoded_revision_id,
        protocol_version=protocol_version,
        runtime_mode=runtime_mode,
        profile_id=profile_id,
        profile_fingerprint=profile_fingerprint,
        runtime_build_id=runtime_build_id,
        availability_flags=Prime3WiiAvailability(availability_flags),
        reserved=reserved,
    )


def encode_inventory_payload(snapshot: Prime3WiiInventorySnapshot) -> bytes:
    if snapshot.schema_version != INVENTORY_SCHEMA_VERSION:
        raise UnsupportedInventorySchemaError(
            f"Unsupported GET_INVENTORY schema {snapshot.schema_version}; expected {INVENTORY_SCHEMA_VERSION}."
        )
    if len(snapshot.records) != INVENTORY_RECORD_COUNT:
        raise InvalidPayloadLengthError(
            f"GET_INVENTORY requires {INVENTORY_RECORD_COUNT} records, got {len(snapshot.records)}."
        )
    _validate_u32(int(snapshot.availability_flags), "availability_flags")
    _validate_u32(snapshot.snapshot_sequence, "snapshot_sequence")
    header = struct.pack(
        INVENTORY_HEADER_FORMAT,
        snapshot.schema_version,
        INVENTORY_RECORD_COUNT,
        INVENTORY_RECORD_SIZE,
        0,
        int(snapshot.availability_flags),
        snapshot.snapshot_sequence,
    )
    records = bytearray()
    for record in snapshot.records:
        _validate_u32(record.amount, "inventory amount")
        _validate_u32(record.capacity, "inventory capacity")
        records.extend(struct.pack(INVENTORY_RECORD_FORMAT, record.amount, record.capacity))
    return header + records


def decode_inventory_payload(payload: bytes) -> Prime3WiiInventorySnapshot:
    if len(payload) != INVENTORY_PAYLOAD_SIZE:
        raise InvalidPayloadLengthError(
            f"GET_INVENTORY response payload must be {INVENTORY_PAYLOAD_SIZE} bytes, got {len(payload)}"
        )
    schema_version, record_count, record_size, reserved0, availability, sequence = struct.unpack(
        INVENTORY_HEADER_FORMAT, payload[:INVENTORY_HEADER_SIZE]
    )
    if schema_version != INVENTORY_SCHEMA_VERSION:
        raise UnsupportedInventorySchemaError(
            f"Unsupported GET_INVENTORY schema {schema_version}; expected {INVENTORY_SCHEMA_VERSION}."
        )
    if record_count != INVENTORY_RECORD_COUNT:
        raise InvalidPayloadLengthError(
            f"GET_INVENTORY record count must be {INVENTORY_RECORD_COUNT}, got {record_count}."
        )
    if record_size != INVENTORY_RECORD_SIZE:
        raise InvalidPayloadLengthError(
            f"GET_INVENTORY record size must be {INVENTORY_RECORD_SIZE}, got {record_size}."
        )
    if reserved0 != 0:
        raise InvalidPayloadLengthError("GET_INVENTORY reserved field must be zero.")
    known_flags = 0
    for flag in Prime3WiiInventoryAvailability:
        known_flags |= int(flag)
    if availability & ~known_flags:
        raise InvalidPayloadLengthError(f"GET_INVENTORY contains unknown availability bits 0x{availability:x}.")
    records = tuple(
        Prime3WiiInventoryRecord(*struct.unpack_from(INVENTORY_RECORD_FORMAT, payload, offset))
        for offset in range(INVENTORY_HEADER_SIZE, INVENTORY_PAYLOAD_SIZE, INVENTORY_RECORD_SIZE)
    )
    flags = Prime3WiiInventoryAvailability(availability)
    if flags & Prime3WiiInventoryAvailability.SNAPSHOT_AVAILABLE:
        required = (
            Prime3WiiInventoryAvailability.EXECUTABLE_RECOGNIZED
            | Prime3WiiInventoryAvailability.GAME_STATE_POINTER_VALID
            | Prime3WiiInventoryAvailability.INVENTORY_ROOT_VALID
            | Prime3WiiInventoryAvailability.RANGE_VALID
            | Prime3WiiInventoryAvailability.CONSISTENCY_CHECK_PASSED
        )
        if flags & required != required or flags & Prime3WiiInventoryAvailability.TEMPORARILY_UNAVAILABLE:
            raise InvalidPayloadLengthError("GET_INVENTORY available snapshot has inconsistent availability flags.")
    elif any(record.amount or record.capacity for record in records):
        raise InvalidPayloadLengthError("GET_INVENTORY unavailable snapshot records must be zero.")
    return Prime3WiiInventorySnapshot(
        schema_version=schema_version,
        availability_flags=flags,
        snapshot_sequence=sequence,
        records=records,
    )


def encode_error_response(
    command: Prime3WiiCommand,
    request_id: int,
    error_code: Prime3WiiErrorCode,
    message: str,
) -> bytes:
    message_bytes = message.encode("utf-8")
    payload = struct.pack(ERROR_HEADER_FORMAT, error_code, command, len(message_bytes)) + message_bytes
    return encode_response(
        Prime3WiiResponse(
            command=command,
            request_id=request_id,
            status=Prime3WiiResponseStatus.ERROR,
            payload=payload,
        )
    )


def decode_error_response_payload(
    command: Prime3WiiCommand,
    request_id: int,
    payload: bytes,
) -> Prime3WiiErrorResponse:
    minimum_size = struct.calcsize(ERROR_HEADER_FORMAT)
    if len(payload) < minimum_size:
        raise InvalidPayloadLengthError("Error payload shorter than minimum size")

    error_code_raw, command_raw, message_length = struct.unpack(ERROR_HEADER_FORMAT, payload[:minimum_size])
    message_bytes = payload[minimum_size:]
    if len(message_bytes) != message_length:
        raise InvalidPayloadLengthError(
            f"Error payload length mismatch: header says {message_length}, packet contains {len(message_bytes)}"
        )
    try:
        error_code = Prime3WiiErrorCode(error_code_raw)
    except ValueError as e:
        raise MalformedPacketError(f"Unknown error code {error_code_raw}") from e

    try:
        payload_command = Prime3WiiCommand(command_raw)
    except ValueError as e:
        raise UnknownCommandError(f"Unknown error payload command {command_raw}") from e

    if payload_command is not command:
        raise MalformedPacketError(
            f"Error payload command {payload_command.name} does not match response command {command.name}"
        )

    return Prime3WiiErrorResponse(
        command=command,
        request_id=request_id,
        error_code=error_code,
        message=message_bytes.decode("utf-8"),
    )
