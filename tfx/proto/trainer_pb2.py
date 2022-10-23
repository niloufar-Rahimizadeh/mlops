# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfx/proto/trainer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfx/proto/trainer.proto',
  package='tfx.components.trainer',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17tfx/proto/trainer.proto\x12\x16tfx.components.trainer\"X\n\tTrainArgs\x12\x0e\n\x06splits\x18\x01 \x03(\t\x12\x11\n\tnum_steps\x18\x02 \x01(\x05J\x04\x08\x03\x10\x04J\x04\x08\x04\x10\x05J\x04\x08\x05\x10\x06J\x04\x08\x06\x10\x07J\x04\x08\x07\x10\x08J\x04\x08\x08\x10\tJ\x04\x08\t\x10\n\"3\n\x08\x45valArgs\x12\x0e\n\x06splits\x18\x01 \x03(\t\x12\x11\n\tnum_steps\x18\x02 \x01(\x05J\x04\x08\x03\x10\x04\x62\x06proto3')
)




_TRAINARGS = _descriptor.Descriptor(
  name='TrainArgs',
  full_name='tfx.components.trainer.TrainArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='splits', full_name='tfx.components.trainer.TrainArgs.splits', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_steps', full_name='tfx.components.trainer.TrainArgs.num_steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=51,
  serialized_end=139,
)


_EVALARGS = _descriptor.Descriptor(
  name='EvalArgs',
  full_name='tfx.components.trainer.EvalArgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='splits', full_name='tfx.components.trainer.EvalArgs.splits', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_steps', full_name='tfx.components.trainer.EvalArgs.num_steps', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=141,
  serialized_end=192,
)

DESCRIPTOR.message_types_by_name['TrainArgs'] = _TRAINARGS
DESCRIPTOR.message_types_by_name['EvalArgs'] = _EVALARGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TrainArgs = _reflection.GeneratedProtocolMessageType('TrainArgs', (_message.Message,), {
  'DESCRIPTOR' : _TRAINARGS,
  '__module__' : 'tfx.proto.trainer_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.trainer.TrainArgs)
  })
_sym_db.RegisterMessage(TrainArgs)

EvalArgs = _reflection.GeneratedProtocolMessageType('EvalArgs', (_message.Message,), {
  'DESCRIPTOR' : _EVALARGS,
  '__module__' : 'tfx.proto.trainer_pb2'
  # @@protoc_insertion_point(class_scope:tfx.components.trainer.EvalArgs)
  })
_sym_db.RegisterMessage(EvalArgs)


# @@protoc_insertion_point(module_scope)
