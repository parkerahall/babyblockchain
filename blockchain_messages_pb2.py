# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: blockchain_messages.proto

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
  name='blockchain_messages.proto',
  package='blockchain',
  syntax='proto3',
  serialized_pb=_b('\n\x19\x62lockchain_messages.proto\x12\nblockchain\"\x85\x01\n\x0e\x43onnectMessage\x12\x0e\n\x06update\x18\x01 \x01(\x05\x12\x0e\n\x06verify\x18\x02 \x01(\x05\x12\x11\n\tclient_id\x18\x03 \x01(\x05\x12 \n\x05\x63hain\x18\x04 \x01(\x0b\x32\x11.blockchain.Chain\x12\x0c\n\x04mine\x18\x05 \x01(\x05\x12\x10\n\x08miner_id\x18\x06 \x01(\x05\"/\n\x0bMineMessage\x12\x12\n\ndifficulty\x18\x01 \x01(\x05\x12\x0c\n\x04hash\x18\x02 \x01(\t\"/\n\x0cNonceMessage\x12\r\n\x05nonce\x18\x01 \x01(\x05\x12\x10\n\x08miner_id\x18\x02 \x01(\x05\"\xab\x01\n\rUpdateMessage\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.blockchain.UpdateMessage.UpdateType\x12 \n\x05\x65ntry\x18\x02 \x01(\x0b\x32\x11.blockchain.Entry\x12 \n\x05\x62lock\x18\x03 \x01(\x0b\x32\x11.blockchain.Block\"\"\n\nUpdateType\x12\t\n\x05\x45NTRY\x10\x00\x12\t\n\x05\x42LOCK\x10\x01\"9\n\x05\x45ntry\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0e\n\x06\x61mount\x18\x03 \x01(\x05\">\n\x05\x42lock\x12\x11\n\tprev_hash\x18\x01 \x01(\t\x12\"\n\x07\x65ntries\x18\x03 \x03(\x0b\x32\x11.blockchain.Entry\">\n\x05\x43hain\x12\x12\n\nblock_size\x18\x01 \x01(\x05\x12!\n\x06\x62locks\x18\x02 \x03(\x0b\x32\x11.blockchain.Blockb\x06proto3')
)



_UPDATEMESSAGE_UPDATETYPE = _descriptor.EnumDescriptor(
  name='UpdateType',
  full_name='blockchain.UpdateMessage.UpdateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ENTRY', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BLOCK', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=413,
  serialized_end=447,
)
_sym_db.RegisterEnumDescriptor(_UPDATEMESSAGE_UPDATETYPE)


_CONNECTMESSAGE = _descriptor.Descriptor(
  name='ConnectMessage',
  full_name='blockchain.ConnectMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='update', full_name='blockchain.ConnectMessage.update', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verify', full_name='blockchain.ConnectMessage.verify', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='client_id', full_name='blockchain.ConnectMessage.client_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain', full_name='blockchain.ConnectMessage.chain', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mine', full_name='blockchain.ConnectMessage.mine', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='miner_id', full_name='blockchain.ConnectMessage.miner_id', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=42,
  serialized_end=175,
)


_MINEMESSAGE = _descriptor.Descriptor(
  name='MineMessage',
  full_name='blockchain.MineMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='difficulty', full_name='blockchain.MineMessage.difficulty', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash', full_name='blockchain.MineMessage.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=177,
  serialized_end=224,
)


_NONCEMESSAGE = _descriptor.Descriptor(
  name='NonceMessage',
  full_name='blockchain.NonceMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonce', full_name='blockchain.NonceMessage.nonce', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='miner_id', full_name='blockchain.NonceMessage.miner_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=226,
  serialized_end=273,
)


_UPDATEMESSAGE = _descriptor.Descriptor(
  name='UpdateMessage',
  full_name='blockchain.UpdateMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='blockchain.UpdateMessage.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entry', full_name='blockchain.UpdateMessage.entry', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block', full_name='blockchain.UpdateMessage.block', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _UPDATEMESSAGE_UPDATETYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=276,
  serialized_end=447,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='blockchain.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sender', full_name='blockchain.Entry.sender', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='blockchain.Entry.receiver', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='blockchain.Entry.amount', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=449,
  serialized_end=506,
)


_BLOCK = _descriptor.Descriptor(
  name='Block',
  full_name='blockchain.Block',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prev_hash', full_name='blockchain.Block.prev_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='entries', full_name='blockchain.Block.entries', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=508,
  serialized_end=570,
)


_CHAIN = _descriptor.Descriptor(
  name='Chain',
  full_name='blockchain.Chain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_size', full_name='blockchain.Chain.block_size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks', full_name='blockchain.Chain.blocks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=572,
  serialized_end=634,
)

_CONNECTMESSAGE.fields_by_name['chain'].message_type = _CHAIN
_UPDATEMESSAGE.fields_by_name['type'].enum_type = _UPDATEMESSAGE_UPDATETYPE
_UPDATEMESSAGE.fields_by_name['entry'].message_type = _ENTRY
_UPDATEMESSAGE.fields_by_name['block'].message_type = _BLOCK
_UPDATEMESSAGE_UPDATETYPE.containing_type = _UPDATEMESSAGE
_BLOCK.fields_by_name['entries'].message_type = _ENTRY
_CHAIN.fields_by_name['blocks'].message_type = _BLOCK
DESCRIPTOR.message_types_by_name['ConnectMessage'] = _CONNECTMESSAGE
DESCRIPTOR.message_types_by_name['MineMessage'] = _MINEMESSAGE
DESCRIPTOR.message_types_by_name['NonceMessage'] = _NONCEMESSAGE
DESCRIPTOR.message_types_by_name['UpdateMessage'] = _UPDATEMESSAGE
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['Block'] = _BLOCK
DESCRIPTOR.message_types_by_name['Chain'] = _CHAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConnectMessage = _reflection.GeneratedProtocolMessageType('ConnectMessage', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTMESSAGE,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.ConnectMessage)
  ))
_sym_db.RegisterMessage(ConnectMessage)

MineMessage = _reflection.GeneratedProtocolMessageType('MineMessage', (_message.Message,), dict(
  DESCRIPTOR = _MINEMESSAGE,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.MineMessage)
  ))
_sym_db.RegisterMessage(MineMessage)

NonceMessage = _reflection.GeneratedProtocolMessageType('NonceMessage', (_message.Message,), dict(
  DESCRIPTOR = _NONCEMESSAGE,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.NonceMessage)
  ))
_sym_db.RegisterMessage(NonceMessage)

UpdateMessage = _reflection.GeneratedProtocolMessageType('UpdateMessage', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEMESSAGE,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.UpdateMessage)
  ))
_sym_db.RegisterMessage(UpdateMessage)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), dict(
  DESCRIPTOR = _ENTRY,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Entry)
  ))
_sym_db.RegisterMessage(Entry)

Block = _reflection.GeneratedProtocolMessageType('Block', (_message.Message,), dict(
  DESCRIPTOR = _BLOCK,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Block)
  ))
_sym_db.RegisterMessage(Block)

Chain = _reflection.GeneratedProtocolMessageType('Chain', (_message.Message,), dict(
  DESCRIPTOR = _CHAIN,
  __module__ = 'blockchain_messages_pb2'
  # @@protoc_insertion_point(class_scope:blockchain.Chain)
  ))
_sym_db.RegisterMessage(Chain)


# @@protoc_insertion_point(module_scope)
