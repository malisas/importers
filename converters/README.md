converter_tcga.py converts TCGA maf and patient summary files into JSON which conforms to the prototype schema defined in simple_schema.proto.

In the resulting JSON files in the converted_data folder:

For the converted maf file, the name/value pairs on the outermost level are such that the name is the type of protobuf data structure being defined, and the value is the JSON-encoded data structure itself.

For the converted clinical data/patient summary file, the name is "Individual_list" and the value is a JSON list of the JSON-encoded Individual data structures.