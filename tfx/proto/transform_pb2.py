# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfx/proto/transform.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfx/proto/transform.proto',
  package='tfx.components.transform',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19tfx/proto/transform.proto\x12\x18tfx.components.transform\"2\n\x0cSplitsConfig\x12\x0f\n\x07\x61nalyze\x18\x01 \x03(\t\x12\x11\n\ttransform\x18\x02 \x03(\tb\x06proto3')
)




_SPLITSCONFIG = _descriptor.Descriptor(
  name='SplitsConfig',
  full_name='tfx.components.transform.SplitsConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyze', full_name='tfx.components.transform.SplitsConfig.analyze', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transform', full_name='tfx.components.transform.SplitsConfig.transform', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['SplitsConfig'] = _SPLITSCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SplitsConfig = _reflection.GeneratedProtocolMessageType('SplitsConfig', (_message.Message,), {
  'DESCRIPTOR' : _SPLITSCONFIG,
  '__module__' : 'tfx.proto.transform_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.transform.SplitsConfig)
  })
_sym_db.RegisterMessage(SplitsConfig)


# @@protoc_insertion_point(module_scope)
