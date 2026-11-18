"""Build the Person message classes in code, from the same fields as person.proto.

Normally you run the protoc compiler on person.proto to generate a Python module. Building
the descriptor here does the same job without an extra tool, and it lets evolve.py make
several versions of the schema side by side. The fields are written exactly as in the
.proto file: a name, a NUMBER and a type.
"""

from google.protobuf import descriptor_pb2, descriptor_pool, message_factory

F = descriptor_pb2.FieldDescriptorProto
STRING, INT32 = F.TYPE_STRING, F.TYPE_INT32


def message_class(package: str, fields: list[tuple[str, int, int]]):
    """Make a Person class in `package` with the given (name, number, type) fields."""
    fdp = descriptor_pb2.FileDescriptorProto(name=f"{package}.proto", package=package, syntax="proto3")
    msg = fdp.message_type.add(name="Person")
    for name, number, type_ in fields:
        msg.field.add(name=name, number=number, type=type_, label=F.LABEL_OPTIONAL)
    pool = descriptor_pool.DescriptorPool()
    pool.Add(fdp)
    return message_factory.GetMessageClass(pool.FindMessageTypeByName(f"{package}.Person"))


# person.proto, version 1
Person = message_class("example", [("name", 1, STRING), ("id", 2, INT32), ("email", 3, STRING)])
