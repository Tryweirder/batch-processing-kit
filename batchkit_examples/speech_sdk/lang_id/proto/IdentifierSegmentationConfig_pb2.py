# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: IdentifierSegmentationConfig.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='IdentifierSegmentationConfig.proto',
  package='skyman.languageId.rpc.v1',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\"IdentifierSegmentationConfig.proto\x12\x18skyman.languageId.rpc.v1\"\xa0\x02\n\x1cIdentifierSegmentationConfig\x12\x0f\n\x07\x65nabled\x18\x01 \x01(\x08\x12Q\n\x08settings\x18\x02 \x01(\x0b\x32?.skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings\x1a\x9b\x01\n\x08Settings\x12!\n\x19phrase_silence_timeout_ms\x18\x01 \x01(\r\x12&\n\x1a\x65mpty_segment_threshold_ms\x18\x02 \x01(\rB\x02\x18\x01\x12\x16\n\x0ewindow_size_ms\x18\x03 \x01(\r\x12\x11\n\tstride_ms\x18\x04 \x01(\r\x12\x19\n\x11max_amplification\x18\x05 \x01(\rb\x06proto3'
)




_IDENTIFIERSEGMENTATIONCONFIG_SETTINGS = _descriptor.Descriptor(
  name='Settings',
  full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phrase_silence_timeout_ms', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings.phrase_silence_timeout_ms', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='empty_segment_threshold_ms', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings.empty_segment_threshold_ms', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=b'\030\001', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='window_size_ms', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings.window_size_ms', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stride_ms', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings.stride_ms', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_amplification', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings.max_amplification', index=4,
      number=5, type=13, cpp_type=3, label=1,
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
  serialized_start=198,
  serialized_end=353,
)

_IDENTIFIERSEGMENTATIONCONFIG = _descriptor.Descriptor(
  name='IdentifierSegmentationConfig',
  full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='enabled', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.enabled', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='skyman.languageId.rpc.v1.IdentifierSegmentationConfig.settings', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_IDENTIFIERSEGMENTATIONCONFIG_SETTINGS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=353,
)

_IDENTIFIERSEGMENTATIONCONFIG_SETTINGS.containing_type = _IDENTIFIERSEGMENTATIONCONFIG
_IDENTIFIERSEGMENTATIONCONFIG.fields_by_name['settings'].message_type = _IDENTIFIERSEGMENTATIONCONFIG_SETTINGS
DESCRIPTOR.message_types_by_name['IdentifierSegmentationConfig'] = _IDENTIFIERSEGMENTATIONCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IdentifierSegmentationConfig = _reflection.GeneratedProtocolMessageType('IdentifierSegmentationConfig', (_message.Message,), {

  'Settings' : _reflection.GeneratedProtocolMessageType('Settings', (_message.Message,), {
    'DESCRIPTOR' : _IDENTIFIERSEGMENTATIONCONFIG_SETTINGS,
    '__module__' : 'IdentifierSegmentationConfig_pb2'
    # @@protoc_insertion_point(class_scope:skyman.languageId.rpc.v1.IdentifierSegmentationConfig.Settings)
    })
  ,
  'DESCRIPTOR' : _IDENTIFIERSEGMENTATIONCONFIG,
  '__module__' : 'IdentifierSegmentationConfig_pb2'
  # @@protoc_insertion_point(class_scope:skyman.languageId.rpc.v1.IdentifierSegmentationConfig)
  })
_sym_db.RegisterMessage(IdentifierSegmentationConfig)
_sym_db.RegisterMessage(IdentifierSegmentationConfig.Settings)


_IDENTIFIERSEGMENTATIONCONFIG_SETTINGS.fields_by_name['empty_segment_threshold_ms']._options = None
# @@protoc_insertion_point(module_scope)
