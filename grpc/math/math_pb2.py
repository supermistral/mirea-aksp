# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: math.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmath.proto\";\n\x18QuadraticEquationRequest\x12\t\n\x01\x61\x18\x01 \x01(\x01\x12\t\n\x01\x62\x18\x02 \x01(\x01\x12\t\n\x01\x63\x18\x03 \x01(\x01\"#\n\tRealRoots\x12\n\n\x02x1\x18\x01 \x01(\x01\x12\n\n\x02x2\x18\x02 \x01(\x01\"%\n\rComplexNumber\x12\t\n\x01x\x18\x01 \x01(\x01\x12\t\n\x01y\x18\x02 \x01(\x01\"F\n\x0c\x43omplexRoots\x12\x1a\n\x02x1\x18\x01 \x01(\x0b\x32\x0e.ComplexNumber\x12\x1a\n\x02x2\x18\x02 \x01(\x0b\x32\x0e.ComplexNumber\"b\n\x19QuadraticEquationResponse\x12\x1a\n\x04real\x18\x01 \x01(\x0b\x32\n.RealRootsH\x00\x12 \n\x07\x63omplex\x18\x02 \x01(\x0b\x32\r.ComplexRootsH\x00\x42\x07\n\x05roots2R\n\x04Math\x12J\n\x11QuadraticEquation\x12\x19.QuadraticEquationRequest\x1a\x1a.QuadraticEquationResponseb\x06proto3')



_QUADRATICEQUATIONREQUEST = DESCRIPTOR.message_types_by_name['QuadraticEquationRequest']
_REALROOTS = DESCRIPTOR.message_types_by_name['RealRoots']
_COMPLEXNUMBER = DESCRIPTOR.message_types_by_name['ComplexNumber']
_COMPLEXROOTS = DESCRIPTOR.message_types_by_name['ComplexRoots']
_QUADRATICEQUATIONRESPONSE = DESCRIPTOR.message_types_by_name['QuadraticEquationResponse']
QuadraticEquationRequest = _reflection.GeneratedProtocolMessageType('QuadraticEquationRequest', (_message.Message,), {
  'DESCRIPTOR' : _QUADRATICEQUATIONREQUEST,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:QuadraticEquationRequest)
  })
_sym_db.RegisterMessage(QuadraticEquationRequest)

RealRoots = _reflection.GeneratedProtocolMessageType('RealRoots', (_message.Message,), {
  'DESCRIPTOR' : _REALROOTS,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:RealRoots)
  })
_sym_db.RegisterMessage(RealRoots)

ComplexNumber = _reflection.GeneratedProtocolMessageType('ComplexNumber', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXNUMBER,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:ComplexNumber)
  })
_sym_db.RegisterMessage(ComplexNumber)

ComplexRoots = _reflection.GeneratedProtocolMessageType('ComplexRoots', (_message.Message,), {
  'DESCRIPTOR' : _COMPLEXROOTS,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:ComplexRoots)
  })
_sym_db.RegisterMessage(ComplexRoots)

QuadraticEquationResponse = _reflection.GeneratedProtocolMessageType('QuadraticEquationResponse', (_message.Message,), {
  'DESCRIPTOR' : _QUADRATICEQUATIONRESPONSE,
  '__module__' : 'math_pb2'
  # @@protoc_insertion_point(class_scope:QuadraticEquationResponse)
  })
_sym_db.RegisterMessage(QuadraticEquationResponse)

_MATH = DESCRIPTOR.services_by_name['Math']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUADRATICEQUATIONREQUEST._serialized_start=14
  _QUADRATICEQUATIONREQUEST._serialized_end=73
  _REALROOTS._serialized_start=75
  _REALROOTS._serialized_end=110
  _COMPLEXNUMBER._serialized_start=112
  _COMPLEXNUMBER._serialized_end=149
  _COMPLEXROOTS._serialized_start=151
  _COMPLEXROOTS._serialized_end=221
  _QUADRATICEQUATIONRESPONSE._serialized_start=223
  _QUADRATICEQUATIONRESPONSE._serialized_end=321
  _MATH._serialized_start=323
  _MATH._serialized_end=405
# @@protoc_insertion_point(module_scope)
