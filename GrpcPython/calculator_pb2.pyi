from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddReply(_message.Message):
    __slots__ = ["sum"]
    SUM_FIELD_NUMBER: _ClassVar[int]
    sum: float
    def __init__(self, sum: _Optional[float] = ...) -> None: ...

class AddRequest(_message.Message):
    __slots__ = ["a", "b"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: float
    b: float
    def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ...) -> None: ...

class RandomReply(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class RandomRequest(_message.Message):
    __slots__ = ["max", "min"]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    max: _wrappers_pb2.Int32Value
    min: _wrappers_pb2.Int32Value
    def __init__(self, min: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ..., max: _Optional[_Union[_wrappers_pb2.Int32Value, _Mapping]] = ...) -> None: ...
