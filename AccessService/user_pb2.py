# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: user.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'user.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nuser.proto\x12\x04user\"\x07\n\x05\x45mpty\"3\n\x04User\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05\x65mail\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\x19\n\x0bUserRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"(\n\x0cUserResponse\x12\x18\n\x04user\x18\x01 \x01(\x0b\x32\n.user.User\"*\n\rUsersResponse\x12\x19\n\x05users\x18\x01 \x03(\x0b\x32\n.user.User\"2\n\x0fValidateRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"$\n\x10ValidateResponse\x12\x10\n\x08is_valid\x18\x01 \x01(\x08\x32\xb6\x01\n\x0bUserService\x12\x30\n\x07GetUser\x12\x11.user.UserRequest\x1a\x12.user.UserResponse\x12/\n\x0bGetAllUsers\x12\x0b.user.Empty\x1a\x13.user.UsersResponse\x12\x44\n\x13ValidateCredentials\x12\x15.user.ValidateRequest\x1a\x16.user.ValidateResponseB\x0c\xaa\x02\tUserProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'user_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\252\002\tUserProto'
  _globals['_EMPTY']._serialized_start=20
  _globals['_EMPTY']._serialized_end=27
  _globals['_USER']._serialized_start=29
  _globals['_USER']._serialized_end=80
  _globals['_USERREQUEST']._serialized_start=82
  _globals['_USERREQUEST']._serialized_end=107
  _globals['_USERRESPONSE']._serialized_start=109
  _globals['_USERRESPONSE']._serialized_end=149
  _globals['_USERSRESPONSE']._serialized_start=151
  _globals['_USERSRESPONSE']._serialized_end=193
  _globals['_VALIDATEREQUEST']._serialized_start=195
  _globals['_VALIDATEREQUEST']._serialized_end=245
  _globals['_VALIDATERESPONSE']._serialized_start=247
  _globals['_VALIDATERESPONSE']._serialized_end=283
  _globals['_USERSERVICE']._serialized_start=286
  _globals['_USERSERVICE']._serialized_end=468
# @@protoc_insertion_point(module_scope)
