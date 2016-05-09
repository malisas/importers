#!/bin/bash

# Test converter_tcga.py. Convert data from raw_data folder into json format in converted_data folder.

#identify the files/filepaths of working directory and converter script
CWD=$(pwd)
CONVERTER_SCRIPT=${CWD}/convert-tcga.py

#Convert maf file
TCGA_PANCAN12_MAF_PATH=${CWD}"/raw-data/pancan12_cleaned_SHORT500.maf"
TCGA_PANCAN12_CLINICAL_PATH=${CWD}"/raw-data/summary_patient_metadata_pancan12_SHORT100.tsv"
JSON_OUT_PATH=${CWD}"/protobuf/pancan_patients_binary_3.pbf"
python $CONVERTER_SCRIPT --maf $TCGA_PANCAN12_MAF_PATH --tsv $TCGA_PANCAN12_CLINICAL_PATH --outfile $JSON_OUT_PATH
