"""Tests for the protobuf examples: the hand encoder matches the library byte for byte."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import evolve  # noqa: E402
import wire  # noqa: E402
from schema import Person  # noqa: E402


@pytest.mark.parametrize("n,hexed", [(0, "00"), (1, "01"), (127, "7f"), (128, "80 01"), (150, "96 01"), (300, "ac 02")])
def test_varints(n, hexed):
    assert wire.encode_varint(n).hex(" ") == hexed
    assert wire.decode_varint(wire.encode_varint(n), 0) == (n, len(wire.encode_varint(n)))


def test_negative_int32_takes_ten_bytes():
    # The encoding guide: intN negatives are two's complement, so all ten bytes are used.
    assert len(wire.encode_varint(-2)) == 10
    assert wire.encode_varint(-2) == Person(id=-2).SerializeToString()[1:]


def test_encoding_guide_example():
    # The guide's Test1 message: field 1 set to 150 encodes as 08 96 01.
    assert wire.encode_field(1, 150).hex(" ") == "08 96 01"


@pytest.mark.parametrize("name,id_,email", [
    ("Ana", 1234, "ana@example.com"),
    ("", 0, ""),                             # all defaults: proto3 writes nothing
    ("Zoë", 7, ""),                          # UTF-8, and one field left out
    ("x" * 200, 2**31 - 1, "e"),             # a length that needs a two-byte varint
])
def test_hand_encoder_matches_library(name, id_, email):
    assert wire.encode_person(name, id_, email) == Person(name=name, id=id_, email=email).SerializeToString()


def test_decode_reads_records_without_a_schema():
    records = wire.decode(Person(name="Ana", id=1234, email="ana@example.com").SerializeToString())
    assert records == [(1, wire.LEN, b"Ana"), (2, wire.VARINT, 1234), (3, wire.LEN, b"ana@example.com")]


def test_protobuf_is_smaller_than_json_here():
    assert len(wire.encode_person("Ana", 1234, "ana@example.com")) == 25


def test_adding_a_field_is_safe_and_kept():
    old, kept = evolve.safe_add()
    assert (old.name, old.id, old.email) == ("Ana", 1234, "ana@example.com")
    assert kept


def test_renumbering_loses_data_silently():
    p = evolve.unsafe_renumber()
    assert (p.id, p.email) == (0, "")


def test_reusing_a_number_puts_data_in_the_wrong_field():
    assert evolve.unsafe_reuse().email == "+44 20 7946 0000"
