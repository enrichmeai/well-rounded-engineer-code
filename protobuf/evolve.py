"""Changing a schema: what is safe, and what silently corrupts data.

    python3 evolve.py

Services are upgraded one at a time, so old code reads messages from new code, and the
other way round. Version 1 of Person is name = 1, id = 2, email = 3. Three changes:

1. SAFE: add a field with a NEW number (phone = 4). Old code skips it, and keeps it as an
   unknown field, so it is not lost when the old code passes the message on.
2. UNSAFE: renumber fields (email = 2, id = 3) to make them "tidier". Old code reads number 2
   as an int32 id, but now finds a string there. The library does not raise an error: it puts the
   record aside as unknown, so id reads as 0 and email as empty.
3. UNSAFE: delete email and reuse its number 3 for phone. Old code reads the phone number as the
   email address. No error at all, and personal data ends up in the wrong field.

The protobuf language guide's rule: field numbers should never be reused; mark deleted ones `reserved`.
"""

from schema import INT32, STRING, Person, message_class

PersonV2 = message_class("v2", [("name", 1, STRING), ("id", 2, INT32), ("email", 3, STRING), ("phone", 4, STRING)])
Renumbered = message_class("renumbered", [("name", 1, STRING), ("email", 2, STRING), ("id", 3, INT32)])
Reused = message_class("reused", [("name", 1, STRING), ("id", 2, INT32), ("phone", 3, STRING)])


def safe_add():
    sent = PersonV2(name="Ana", id=1234, email="ana@example.com", phone="+44 20 7946 0000").SerializeToString()
    old = Person.FromString(sent)
    return old, old.SerializeToString() == sent       # re-sent unchanged, phone included


def unsafe_renumber():
    return Person.FromString(Renumbered(name="Ana", email="ana@example.com", id=1234).SerializeToString())


def unsafe_reuse():
    return Person.FromString(Reused(name="Ana", id=1234, phone="+44 20 7946 0000").SerializeToString())


def show(p) -> str:
    return f"name={p.name!r} id={p.id} email={p.email!r}"


if __name__ == "__main__":
    old, kept = safe_add()
    print("1. SAFE   add phone = 4          old code reads:", show(old))
    print(f"                                 and passes phone on unchanged: {kept}")
    print("2. UNSAFE renumber email/id      old code reads:", show(unsafe_renumber()))
    print("3. UNSAFE reuse 3 for phone      old code reads:", show(unsafe_reuse()))
