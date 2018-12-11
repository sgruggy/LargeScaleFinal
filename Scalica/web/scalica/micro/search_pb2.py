# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: search.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='search.proto',
  package='TextSearch',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0csearch.proto\x12\nTextSearch\"G\n\x0eMessageRequest\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\ndatePosted\x18\x03 \x01(\t\"\x1c\n\x0cMessageReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t2P\n\nTextSearch\x12\x42\n\ngetMessage\x12\x1a.TextSearch.MessageRequest\x1a\x18.TextSearch.MessageReplyb\x06proto3')
)




_MESSAGEREQUEST = _descriptor.Descriptor(
  name='MessageRequest',
  full_name='TextSearch.MessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='TextSearch.MessageRequest.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='TextSearch.MessageRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='datePosted', full_name='TextSearch.MessageRequest.datePosted', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=28,
  serialized_end=99,
)


_MESSAGEREPLY = _descriptor.Descriptor(
  name='MessageReply',
  full_name='TextSearch.MessageReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='TextSearch.MessageReply.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=101,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['MessageRequest'] = _MESSAGEREQUEST
DESCRIPTOR.message_types_by_name['MessageReply'] = _MESSAGEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessageRequest = _reflection.GeneratedProtocolMessageType('MessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEREQUEST,
  __module__ = 'search_pb2'
  # @@protoc_insertion_point(class_scope:TextSearch.MessageRequest)
  ))
_sym_db.RegisterMessage(MessageRequest)

MessageReply = _reflection.GeneratedProtocolMessageType('MessageReply', (_message.Message,), dict(
  DESCRIPTOR = _MESSAGEREPLY,
  __module__ = 'search_pb2'
  # @@protoc_insertion_point(class_scope:TextSearch.MessageReply)
  ))
_sym_db.RegisterMessage(MessageReply)



_TEXTSEARCH = _descriptor.ServiceDescriptor(
  name='TextSearch',
  full_name='TextSearch.TextSearch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=131,
  serialized_end=211,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMessage',
    full_name='TextSearch.TextSearch.getMessage',
    index=0,
    containing_service=None,
    input_type=_MESSAGEREQUEST,
    output_type=_MESSAGEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEXTSEARCH)

DESCRIPTOR.services_by_name['TextSearch'] = _TEXTSEARCH

# @@protoc_insertion_point(module_scope)
