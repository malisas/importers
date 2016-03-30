converter_tcga.py is the main converter. It converts TCGA maf and patient summary files into JSON.  
The resulting JSON conforms to the prototype schema defined in simple_schema.proto.

converter_test.sh tests converter_tcga.py on data in the raw_data folder.

The resulting JSON files are in the converted_data folder:

For converted TCGA maf files (e.g. pancan12_cleaned_SHORT500.json):  
Name/value pairs on the outermost level are 1) name: the type of protobuf data structure being defined, and 2) value: the JSON-encoded data structure itself.

For converted TCGA clinical data (e.g. summary_patient_metadata_pancan12_SHORT100.json):  
On the outermost level, the name is "Individual_list" and the value is a JSON list of the JSON-encoded "Individual" data structures.