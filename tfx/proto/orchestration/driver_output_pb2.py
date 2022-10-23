# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tfx/proto/orchestration/driver_output.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ml_metadata.proto import metadata_store_pb2 as ml__metadata_dot_proto_dot_metadata__store__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tfx/proto/orchestration/driver_output.proto',
  package='tfx.orchestration',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+tfx/proto/orchestration/driver_output.proto\x12\x11tfx.orchestration\x1a&ml_metadata/proto/metadata_store.proto\"\x97\x03\n\x0c\x44riverOutput\x12N\n\x10output_artifacts\x18\x01 \x03(\x0b\x32\x34.tfx.orchestration.DriverOutput.OutputArtifactsEntry\x12L\n\x0f\x65xec_properties\x18\x02 \x03(\x0b\x32\x33.tfx.orchestration.DriverOutput.ExecPropertiesEntry\x1a\x38\n\x0c\x41rtifactList\x12(\n\tartifacts\x18\x01 \x03(\x0b\x32\x15.ml_metadata.Artifact\x1a\x64\n\x14OutputArtifactsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12;\n\x05value\x18\x02 \x01(\x0b\x32,.tfx.orchestration.DriverOutput.ArtifactList:\x02\x38\x01\x1aI\n\x13\x45xecPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.ml_metadata.Value:\x02\x38\x01\x62\x06proto3')
  ,
  dependencies=[ml__metadata_dot_proto_dot_metadata__store__pb2.DESCRIPTOR,])




_DRIVEROUTPUT_ARTIFACTLIST = _descriptor.Descriptor(
  name='ArtifactList',
  full_name='tfx.orchestration.DriverOutput.ArtifactList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='artifacts', full_name='tfx.orchestration.DriverOutput.ArtifactList.artifacts', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=281,
  serialized_end=337,
)

_DRIVEROUTPUT_OUTPUTARTIFACTSENTRY = _descriptor.Descriptor(
  name='OutputArtifactsEntry',
  full_name='tfx.orchestration.DriverOutput.OutputArtifactsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tfx.orchestration.DriverOutput.OutputArtifactsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tfx.orchestration.DriverOutput.OutputArtifactsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=439,
)

_DRIVEROUTPUT_EXECPROPERTIESENTRY = _descriptor.Descriptor(
  name='ExecPropertiesEntry',
  full_name='tfx.orchestration.DriverOutput.ExecPropertiesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tfx.orchestration.DriverOutput.ExecPropertiesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tfx.orchestration.DriverOutput.ExecPropertiesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=441,
  serialized_end=514,
)

_DRIVEROUTPUT = _descriptor.Descriptor(
  name='DriverOutput',
  full_name='tfx.orchestration.DriverOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='output_artifacts', full_name='tfx.orchestration.DriverOutput.output_artifacts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exec_properties', full_name='tfx.orchestration.DriverOutput.exec_properties', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_DRIVEROUTPUT_ARTIFACTLIST, _DRIVEROUTPUT_OUTPUTARTIFACTSENTRY, _DRIVEROUTPUT_EXECPROPERTIESENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=107,
  serialized_end=514,
)

_DRIVEROUTPUT_ARTIFACTLIST.fields_by_name['artifacts'].message_type = ml__metadata_dot_proto_dot_metadata__store__pb2._ARTIFACT
_DRIVEROUTPUT_ARTIFACTLIST.containing_type = _DRIVEROUTPUT
_DRIVEROUTPUT_OUTPUTARTIFACTSENTRY.fields_by_name['value'].message_type = _DRIVEROUTPUT_ARTIFACTLIST
_DRIVEROUTPUT_OUTPUTARTIFACTSENTRY.containing_type = _DRIVEROUTPUT
_DRIVEROUTPUT_EXECPROPERTIESENTRY.fields_by_name['value'].message_type = ml__metadata_dot_proto_dot_metadata__store__pb2._VALUE
_DRIVEROUTPUT_EXECPROPERTIESENTRY.containing_type = _DRIVEROUTPUT
_DRIVEROUTPUT.fields_by_name['output_artifacts'].message_type = _DRIVEROUTPUT_OUTPUTARTIFACTSENTRY
_DRIVEROUTPUT.fields_by_name['exec_properties'].message_type = _DRIVEROUTPUT_EXECPROPERTIESENTRY
DESCRIPTOR.message_types_by_name['DriverOutput'] = _DRIVEROUTPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DriverOutput = _reflection.GeneratedProtocolMessageType('DriverOutput', (_message.Message,), {

  'ArtifactList' : _reflection.GeneratedProtocolMessageType('ArtifactList', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEROUTPUT_ARTIFACTLIST,
    '__module__' : 'tfx.proto.orchestration.driver_output_pb2'
    # @@protoc_insertion_point(class_scope:tfx.orchestration.DriverOutput.ArtifactList)
    })
  ,

  'OutputArtifactsEntry' : _reflection.GeneratedProtocolMessageType('OutputArtifactsEntry', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEROUTPUT_OUTPUTARTIFACTSENTRY,
    '__module__' : 'tfx.proto.orchestration.driver_output_pb2'
    # @@protoc_insertion_point(class_scope:tfx.orchestration.DriverOutput.OutputArtifactsEntry)
    })
  ,

  'ExecPropertiesEntry' : _reflection.GeneratedProtocolMessageType('ExecPropertiesEntry', (_message.Message,), {
    'DESCRIPTOR' : _DRIVEROUTPUT_EXECPROPERTIESENTRY,
    '__module__' : 'tfx.proto.orchestration.driver_output_pb2'
    # @@protoc_insertion_point(class_scope:tfx.orchestration.DriverOutput.ExecPropertiesEntry)
    })
  ,
  'DESCRIPTOR' : _DRIVEROUTPUT,
  '__module__' : 'tfx.proto.orchestration.driver_output_pb2'
  # @@protoc_insertion_point(class_scope:tfx.orchestration.DriverOutput)
  })
_sym_db.RegisterMessage(DriverOutput)
_sym_db.RegisterMessage(DriverOutput.ArtifactList)
_sym_db.RegisterMessage(DriverOutput.OutputArtifactsEntry)
_sym_db.RegisterMessage(DriverOutput.ExecPropertiesEntry)


_DRIVEROUTPUT_OUTPUTARTIFACTSENTRY._options = None
_DRIVEROUTPUT_EXECPROPERTIESENTRY._options = None
# @@protoc_insertion_point(module_scope)
