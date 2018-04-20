# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: communicator/unity_initialization_input.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from communicator import python_parameters_pb2 as communicator_dot_python__parameters__pb2
from communicator import header_pb2 as communicator_dot_header__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='communicator/unity_initialization_input.proto',
  package='communicator',
  syntax='proto3',
  serialized_pb=_b('\n-communicator/unity_initialization_input.proto\x12\x0c\x63ommunicator\x1a$communicator/python_parameters.proto\x1a\x19\x63ommunicator/header.proto\"{\n\x18UnityInitializationInput\x12$\n\x06header\x18\x01 \x01(\x0b\x32\x14.communicator.Header\x12\x39\n\x11python_parameters\x18\x02 \x01(\x0b\x32\x1e.communicator.PythonParametersB\x18\xaa\x02\x15MLAgents.Communicatorb\x06proto3')
  ,
  dependencies=[communicator_dot_python__parameters__pb2.DESCRIPTOR,communicator_dot_header__pb2.DESCRIPTOR,])




_UNITYINITIALIZATIONINPUT = _descriptor.Descriptor(
  name='UnityInitializationInput',
  full_name='communicator.UnityInitializationInput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='header', full_name='communicator.UnityInitializationInput.header', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='python_parameters', full_name='communicator.UnityInitializationInput.python_parameters', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=251,
)

_UNITYINITIALIZATIONINPUT.fields_by_name['header'].message_type = communicator_dot_header__pb2._HEADER
_UNITYINITIALIZATIONINPUT.fields_by_name['python_parameters'].message_type = communicator_dot_python__parameters__pb2._PYTHONPARAMETERS
DESCRIPTOR.message_types_by_name['UnityInitializationInput'] = _UNITYINITIALIZATIONINPUT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UnityInitializationInput = _reflection.GeneratedProtocolMessageType('UnityInitializationInput', (_message.Message,), dict(
  DESCRIPTOR = _UNITYINITIALIZATIONINPUT,
  __module__ = 'communicator.unity_initialization_input_pb2'
  # @@protoc_insertion_point(class_scope:communicator.UnityInitializationInput)
  ))
_sym_db.RegisterMessage(UnityInitializationInput)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\252\002\025MLAgents.Communicator'))
# @@protoc_insertion_point(module_scope)
