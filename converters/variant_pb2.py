# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: variant.proto

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
  name='variant.proto',
  package='bmeg.gaea.schema',
  syntax='proto3',
  serialized_pb=_b('\n\rvariant.proto\x12\x10\x62meg.gaea.schema\"I\n\x08Position\x12\x11\n\treference\x18\x01 \x01(\t\x12\r\n\x05start\x18\x02 \x01(\x03\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x03\x12\x0e\n\x06strand\x18\x04 \x01(\t\"\xbe\x01\n\x07\x46\x65\x61ture\x12,\n\x08position\x18\x01 \x01(\x0b\x32\x1a.bmeg.gaea.schema.Position\x12\x13\n\x0b\x66\x65\x61tureType\x18\x02 \x01(\t\x12=\n\nattributes\x18\x03 \x03(\x0b\x32).bmeg.gaea.schema.Feature.AttributesEntry\x1a\x31\n\x0f\x41ttributesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xf7\x01\n\x11VariantCallEffect\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0f\n\x07\x66\x65\x61ture\x18\x02 \x01(\t\x12\x1d\n\x15variantClassification\x18\x03 \x01(\t\x12\x0f\n\x07\x64omains\x18\x04 \x03(\t\x12\x0f\n\x07\x64\x62snpRS\x18\x05 \x01(\t\x12\x16\n\x0e\x64\x62snpValStatus\x18\x06 \x01(\t\x12;\n\x04info\x18\x07 \x03(\x0b\x32-.bmeg.gaea.schema.VariantCallEffect.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xc3\x03\n\x0bVariantCall\x12\x0e\n\x06source\x18\x01 \x01(\t\x12,\n\x08position\x18\x02 \x01(\x0b\x32\x1a.bmeg.gaea.schema.Position\x12\x13\n\x0bvariantType\x18\x03 \x01(\t\x12\x17\n\x0freferenceAllele\x18\x04 \x01(\t\x12\x15\n\rnormalAllele1\x18\x05 \x01(\t\x12\x15\n\rnormalAllele2\x18\x06 \x01(\t\x12\x14\n\x0ctumorAllele1\x18\x07 \x01(\t\x12\x14\n\x0ctumorAllele2\x18\x08 \x01(\t\x12\x11\n\tsequencer\x18\t \x01(\t\x12\x17\n\x0ftumorSampleUUID\x18\n \x01(\t\x12\x1d\n\x15matchedNormSampleUUID\x18\x0b \x01(\t\x12?\n\x12variantCallEffects\x18\x0c \x03(\x0b\x32#.bmeg.gaea.schema.VariantCallEffect\x12\x35\n\x04info\x18\r \x03(\x0b\x32\'.bmeg.gaea.schema.VariantCall.InfoEntry\x1a+\n\tInfoEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"v\n\tBioSample\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12\x16\n\x0eindividualName\x18\x03 \x01(\t\x12\x33\n\x0cvariantCalls\x18\x04 \x03(\x0b\x32\x1d.bmeg.gaea.schema.VariantCall\"\xd6\x01\n\nIndividual\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06source\x18\x02 \x01(\t\x12/\n\nbioSamples\x18\x03 \x03(\x0b\x32\x1b.bmeg.gaea.schema.BioSample\x12\x44\n\x0cobservations\x18\x04 \x03(\x0b\x32..bmeg.gaea.schema.Individual.ObservationsEntry\x1a\x33\n\x11ObservationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"C\n\x0eIndividualList\x12\x31\n\x0bindividuals\x18\x01 \x03(\x0b\x32\x1c.bmeg.gaea.schema.Individualb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_POSITION = _descriptor.Descriptor(
  name='Position',
  full_name='bmeg.gaea.schema.Position',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reference', full_name='bmeg.gaea.schema.Position.reference', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start', full_name='bmeg.gaea.schema.Position.start', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='bmeg.gaea.schema.Position.end', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strand', full_name='bmeg.gaea.schema.Position.strand', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=108,
)


_FEATURE_ATTRIBUTESENTRY = _descriptor.Descriptor(
  name='AttributesEntry',
  full_name='bmeg.gaea.schema.Feature.AttributesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.gaea.schema.Feature.AttributesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.gaea.schema.Feature.AttributesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=252,
  serialized_end=301,
)

_FEATURE = _descriptor.Descriptor(
  name='Feature',
  full_name='bmeg.gaea.schema.Feature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='bmeg.gaea.schema.Feature.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='featureType', full_name='bmeg.gaea.schema.Feature.featureType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='bmeg.gaea.schema.Feature.attributes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_FEATURE_ATTRIBUTESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=301,
)


_VARIANTCALLEFFECT_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='bmeg.gaea.schema.VariantCallEffect.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.gaea.schema.VariantCallEffect.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.gaea.schema.VariantCallEffect.InfoEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=551,
)

_VARIANTCALLEFFECT = _descriptor.Descriptor(
  name='VariantCallEffect',
  full_name='bmeg.gaea.schema.VariantCallEffect',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.gaea.schema.VariantCallEffect.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='feature', full_name='bmeg.gaea.schema.VariantCallEffect.feature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variantClassification', full_name='bmeg.gaea.schema.VariantCallEffect.variantClassification', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domains', full_name='bmeg.gaea.schema.VariantCallEffect.domains', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbsnpRS', full_name='bmeg.gaea.schema.VariantCallEffect.dbsnpRS', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dbsnpValStatus', full_name='bmeg.gaea.schema.VariantCallEffect.dbsnpValStatus', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='bmeg.gaea.schema.VariantCallEffect.info', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VARIANTCALLEFFECT_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=304,
  serialized_end=551,
)


_VARIANTCALL_INFOENTRY = _descriptor.Descriptor(
  name='InfoEntry',
  full_name='bmeg.gaea.schema.VariantCall.InfoEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.gaea.schema.VariantCall.InfoEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.gaea.schema.VariantCall.InfoEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=551,
)

_VARIANTCALL = _descriptor.Descriptor(
  name='VariantCall',
  full_name='bmeg.gaea.schema.VariantCall',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.gaea.schema.VariantCall.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='bmeg.gaea.schema.VariantCall.position', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variantType', full_name='bmeg.gaea.schema.VariantCall.variantType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='referenceAllele', full_name='bmeg.gaea.schema.VariantCall.referenceAllele', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalAllele1', full_name='bmeg.gaea.schema.VariantCall.normalAllele1', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalAllele2', full_name='bmeg.gaea.schema.VariantCall.normalAllele2', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumorAllele1', full_name='bmeg.gaea.schema.VariantCall.tumorAllele1', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumorAllele2', full_name='bmeg.gaea.schema.VariantCall.tumorAllele2', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sequencer', full_name='bmeg.gaea.schema.VariantCall.sequencer', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tumorSampleUUID', full_name='bmeg.gaea.schema.VariantCall.tumorSampleUUID', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matchedNormSampleUUID', full_name='bmeg.gaea.schema.VariantCall.matchedNormSampleUUID', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variantCallEffects', full_name='bmeg.gaea.schema.VariantCall.variantCallEffects', index=11,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='info', full_name='bmeg.gaea.schema.VariantCall.info', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VARIANTCALL_INFOENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=1005,
)


_BIOSAMPLE = _descriptor.Descriptor(
  name='BioSample',
  full_name='bmeg.gaea.schema.BioSample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.gaea.schema.BioSample.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.gaea.schema.BioSample.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individualName', full_name='bmeg.gaea.schema.BioSample.individualName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variantCalls', full_name='bmeg.gaea.schema.BioSample.variantCalls', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1007,
  serialized_end=1125,
)


_INDIVIDUAL_OBSERVATIONSENTRY = _descriptor.Descriptor(
  name='ObservationsEntry',
  full_name='bmeg.gaea.schema.Individual.ObservationsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='bmeg.gaea.schema.Individual.ObservationsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='bmeg.gaea.schema.Individual.ObservationsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1291,
  serialized_end=1342,
)

_INDIVIDUAL = _descriptor.Descriptor(
  name='Individual',
  full_name='bmeg.gaea.schema.Individual',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='bmeg.gaea.schema.Individual.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='bmeg.gaea.schema.Individual.source', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bioSamples', full_name='bmeg.gaea.schema.Individual.bioSamples', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='observations', full_name='bmeg.gaea.schema.Individual.observations', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_INDIVIDUAL_OBSERVATIONSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1128,
  serialized_end=1342,
)


_INDIVIDUALLIST = _descriptor.Descriptor(
  name='IndividualList',
  full_name='bmeg.gaea.schema.IndividualList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='individuals', full_name='bmeg.gaea.schema.IndividualList.individuals', index=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1344,
  serialized_end=1411,
)

_FEATURE_ATTRIBUTESENTRY.containing_type = _FEATURE
_FEATURE.fields_by_name['position'].message_type = _POSITION
_FEATURE.fields_by_name['attributes'].message_type = _FEATURE_ATTRIBUTESENTRY
_VARIANTCALLEFFECT_INFOENTRY.containing_type = _VARIANTCALLEFFECT
_VARIANTCALLEFFECT.fields_by_name['info'].message_type = _VARIANTCALLEFFECT_INFOENTRY
_VARIANTCALL_INFOENTRY.containing_type = _VARIANTCALL
_VARIANTCALL.fields_by_name['position'].message_type = _POSITION
_VARIANTCALL.fields_by_name['variantCallEffects'].message_type = _VARIANTCALLEFFECT
_VARIANTCALL.fields_by_name['info'].message_type = _VARIANTCALL_INFOENTRY
_BIOSAMPLE.fields_by_name['variantCalls'].message_type = _VARIANTCALL
_INDIVIDUAL_OBSERVATIONSENTRY.containing_type = _INDIVIDUAL
_INDIVIDUAL.fields_by_name['bioSamples'].message_type = _BIOSAMPLE
_INDIVIDUAL.fields_by_name['observations'].message_type = _INDIVIDUAL_OBSERVATIONSENTRY
_INDIVIDUALLIST.fields_by_name['individuals'].message_type = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['Position'] = _POSITION
DESCRIPTOR.message_types_by_name['Feature'] = _FEATURE
DESCRIPTOR.message_types_by_name['VariantCallEffect'] = _VARIANTCALLEFFECT
DESCRIPTOR.message_types_by_name['VariantCall'] = _VARIANTCALL
DESCRIPTOR.message_types_by_name['BioSample'] = _BIOSAMPLE
DESCRIPTOR.message_types_by_name['Individual'] = _INDIVIDUAL
DESCRIPTOR.message_types_by_name['IndividualList'] = _INDIVIDUALLIST

Position = _reflection.GeneratedProtocolMessageType('Position', (_message.Message,), dict(
  DESCRIPTOR = _POSITION,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.Position)
  ))
_sym_db.RegisterMessage(Position)

Feature = _reflection.GeneratedProtocolMessageType('Feature', (_message.Message,), dict(

  AttributesEntry = _reflection.GeneratedProtocolMessageType('AttributesEntry', (_message.Message,), dict(
    DESCRIPTOR = _FEATURE_ATTRIBUTESENTRY,
    __module__ = 'variant_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.Feature.AttributesEntry)
    ))
  ,
  DESCRIPTOR = _FEATURE,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.Feature)
  ))
_sym_db.RegisterMessage(Feature)
_sym_db.RegisterMessage(Feature.AttributesEntry)

VariantCallEffect = _reflection.GeneratedProtocolMessageType('VariantCallEffect', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _VARIANTCALLEFFECT_INFOENTRY,
    __module__ = 'variant_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.VariantCallEffect.InfoEntry)
    ))
  ,
  DESCRIPTOR = _VARIANTCALLEFFECT,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.VariantCallEffect)
  ))
_sym_db.RegisterMessage(VariantCallEffect)
_sym_db.RegisterMessage(VariantCallEffect.InfoEntry)

VariantCall = _reflection.GeneratedProtocolMessageType('VariantCall', (_message.Message,), dict(

  InfoEntry = _reflection.GeneratedProtocolMessageType('InfoEntry', (_message.Message,), dict(
    DESCRIPTOR = _VARIANTCALL_INFOENTRY,
    __module__ = 'variant_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.VariantCall.InfoEntry)
    ))
  ,
  DESCRIPTOR = _VARIANTCALL,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.VariantCall)
  ))
_sym_db.RegisterMessage(VariantCall)
_sym_db.RegisterMessage(VariantCall.InfoEntry)

BioSample = _reflection.GeneratedProtocolMessageType('BioSample', (_message.Message,), dict(
  DESCRIPTOR = _BIOSAMPLE,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.BioSample)
  ))
_sym_db.RegisterMessage(BioSample)

Individual = _reflection.GeneratedProtocolMessageType('Individual', (_message.Message,), dict(

  ObservationsEntry = _reflection.GeneratedProtocolMessageType('ObservationsEntry', (_message.Message,), dict(
    DESCRIPTOR = _INDIVIDUAL_OBSERVATIONSENTRY,
    __module__ = 'variant_pb2'
    # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.Individual.ObservationsEntry)
    ))
  ,
  DESCRIPTOR = _INDIVIDUAL,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.Individual)
  ))
_sym_db.RegisterMessage(Individual)
_sym_db.RegisterMessage(Individual.ObservationsEntry)

IndividualList = _reflection.GeneratedProtocolMessageType('IndividualList', (_message.Message,), dict(
  DESCRIPTOR = _INDIVIDUALLIST,
  __module__ = 'variant_pb2'
  # @@protoc_insertion_point(class_scope:bmeg.gaea.schema.IndividualList)
  ))
_sym_db.RegisterMessage(IndividualList)


_FEATURE_ATTRIBUTESENTRY.has_options = True
_FEATURE_ATTRIBUTESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_VARIANTCALLEFFECT_INFOENTRY.has_options = True
_VARIANTCALLEFFECT_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_VARIANTCALL_INFOENTRY.has_options = True
_VARIANTCALL_INFOENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_INDIVIDUAL_OBSERVATIONSENTRY.has_options = True
_INDIVIDUAL_OBSERVATIONSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
