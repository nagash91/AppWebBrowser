# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: temporary.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='temporary.proto',
  package='temporary',
  serialized_pb=_b('\n\x0ftemporary.proto\x12\ttemporary\"\xe7\x01\n\x06WebApp\x12\x0f\n\x07\x61ppName\x18\x01 \x02(\t\x12\x1f\n\tindexFile\x18\x02 \x01(\t:\x0cindex.bundle\x12.\n\x10indexFileAndroid\x18\x03 \x01(\t:\x14index.android.bundle\x12&\n\x0cindexFileIos\x18\x04 \x01(\t:\x10index.ios.bundle\x12\x17\n\tMainClass\x18\x05 \x01(\t:\x04main\x12\x1e\n\x10MainAndroidClass\x18\x06 \x01(\t:\x04main\x12\x1a\n\x0cMainIosClass\x18\x07 \x01(\t:\x04main\")\n\x07\x41ppList\x12\x1e\n\x03\x61pp\x18\x01 \x03(\x0b\x32\x11.temporary.WebApp')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_WEBAPP = _descriptor.Descriptor(
  name='WebApp',
  full_name='temporary.WebApp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appName', full_name='temporary.WebApp.appName', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexFile', full_name='temporary.WebApp.indexFile', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("index.bundle").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexFileAndroid', full_name='temporary.WebApp.indexFileAndroid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("index.android.bundle").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='indexFileIos', full_name='temporary.WebApp.indexFileIos', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("index.ios.bundle").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MainClass', full_name='temporary.WebApp.MainClass', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("main").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MainAndroidClass', full_name='temporary.WebApp.MainAndroidClass', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("main").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='MainIosClass', full_name='temporary.WebApp.MainIosClass', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("main").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=262,
)


_APPLIST = _descriptor.Descriptor(
  name='AppList',
  full_name='temporary.AppList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app', full_name='temporary.AppList.app', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=264,
  serialized_end=305,
)

_APPLIST.fields_by_name['app'].message_type = _WEBAPP
DESCRIPTOR.message_types_by_name['WebApp'] = _WEBAPP
DESCRIPTOR.message_types_by_name['AppList'] = _APPLIST

WebApp = _reflection.GeneratedProtocolMessageType('WebApp', (_message.Message,), dict(
  DESCRIPTOR = _WEBAPP,
  __module__ = 'temporary_pb2'
  # @@protoc_insertion_point(class_scope:temporary.WebApp)
  ))
_sym_db.RegisterMessage(WebApp)

AppList = _reflection.GeneratedProtocolMessageType('AppList', (_message.Message,), dict(
  DESCRIPTOR = _APPLIST,
  __module__ = 'temporary_pb2'
  # @@protoc_insertion_point(class_scope:temporary.AppList)
  ))
_sym_db.RegisterMessage(AppList)


# @@protoc_insertion_point(module_scope)
