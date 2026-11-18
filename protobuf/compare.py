"""The official protobuf library produces exactly the bytes wire.py builds by hand. And JSON, for size.

    python3 compare.py
"""

import json

import wire
from schema import Person

if __name__ == "__main__":
    by_library = Person(name="Ana", id=1234, email="ana@example.com").SerializeToString()
    by_hand = wire.encode_person("Ana", 1234, "ana@example.com")
    as_json = json.dumps({"name": "Ana", "id": 1234, "email": "ana@example.com"}).encode()

    print(f"protobuf library : {len(by_library):>3} bytes  {by_library.hex(' ')}")
    print(f"by hand (wire.py): {len(by_hand):>3} bytes  {'identical' if by_hand == by_library else 'DIFFERENT'}")
    print(f"JSON             : {len(as_json):>3} bytes  {as_json.decode()}")
    back = Person.FromString(by_hand)
    print(f"read back        : name={back.name!r} id={back.id} email={back.email!r}")
