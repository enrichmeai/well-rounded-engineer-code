"""The protobuf wire format, by hand: encode and decode a Person with no library at all.

    python3 wire.py

A protobuf message on the wire is a list of records. Each record is:

    tag     a varint: (field_number << 3) | wire_type
    value   for wire type 0 (VARINT): a varint
            for wire type 2 (LEN): a varint length, then that many bytes

A varint stores 7 bits per byte, lowest bits first; the top bit of each byte says
"another byte follows". So 150 is 0b10010110 -> bytes 96 01.

Field NAMES never go on the wire. Only the numbers do, which is why the numbers are the contract.
"""

VARINT, LEN = 0, 2


def encode_varint(n: int) -> bytes:
    if n < 0:
        n += 1 << 64                     # int32/int64 negatives: two's complement, always 10 bytes
    out = bytearray()
    while True:
        low7 = n & 0x7F
        n >>= 7
        if n:
            out.append(low7 | 0x80)      # top bit set: more bytes follow
        else:
            out.append(low7)
            return bytes(out)


def decode_varint(data: bytes, pos: int) -> tuple[int, int]:
    """Read a varint starting at pos. Returns (value, position after it)."""
    result, shift = 0, 0
    while True:
        byte = data[pos]
        pos += 1
        result |= (byte & 0x7F) << shift
        if not byte & 0x80:
            return result, pos
        shift += 7


def encode_field(number: int, value) -> bytes:
    if isinstance(value, int):
        return encode_varint(number << 3 | VARINT) + encode_varint(value)
    raw = value.encode("utf-8") if isinstance(value, str) else bytes(value)
    return encode_varint(number << 3 | LEN) + encode_varint(len(raw)) + raw


def encode_person(name: str, id: int, email: str) -> bytes:
    """Fields in number order. proto3 leaves out fields that hold their default (0 or "")."""
    out = b""
    for number, value in ((1, name), (2, id), (3, email)):
        if value not in (0, ""):
            out += encode_field(number, value)
    return out


def decode(data: bytes) -> list[tuple[int, int, object]]:
    """Read any message as (field_number, wire_type, value) records, without knowing its schema."""
    records, pos = [], 0
    while pos < len(data):
        tag, pos = decode_varint(data, pos)
        number, wire_type = tag >> 3, tag & 7
        if wire_type == VARINT:
            value, pos = decode_varint(data, pos)
        elif wire_type == LEN:
            length, pos = decode_varint(data, pos)
            value, pos = data[pos:pos + length], pos + length
        else:
            raise ValueError(f"wire type {wire_type} is not handled in this small example")
        records.append((number, wire_type, value))
    return records


def explain(data: bytes) -> str:
    """Print each record with the bytes that make it, so every byte is accounted for."""
    lines, pos = [], 0
    while pos < len(data):
        start = pos
        tag, pos = decode_varint(data, pos)
        number, wire_type = tag >> 3, tag & 7
        if wire_type == VARINT:
            value, pos = decode_varint(data, pos)
            shown = str(value)
        else:
            length, pos = decode_varint(data, pos)
            value, pos = data[pos:pos + length], pos + length
            shown = f"{length} bytes {value.decode('utf-8', 'replace')!r}"
        kind = {VARINT: "VARINT", LEN: "LEN"}[wire_type]
        lines.append(f"{data[start:pos].hex(' '):<52} field {number}, {kind:<6} {shown}")
    return "\n".join(lines)


if __name__ == "__main__":
    print("150 as a varint:", encode_varint(150).hex(" "))
    msg = encode_person("Ana", 1234, "ana@example.com")
    print(f"Person(name='Ana', id=1234, email='ana@example.com') is {len(msg)} bytes:")
    print(explain(msg))
