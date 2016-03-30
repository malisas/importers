#!/bin/bash

# Test converter_tcga.py. Convert data from raw_data folder into json format in converted_data folder.

#identify the files/filepaths of working directory and converter script
CWD=$(pwd)
CONVERTER_SCRIPT=${CWD}/converter_tcga.py

#Convert maf file
TCGA_PANCAN12_MAF_PATH=${CWD}"/raw_data/pancan12_cleaned_SHORT500.maf"
MAF_JSON_OUT_PATH=${CWD}"/converted_data/pancan12_cleaned_SHORT500.json"
python $CONVERTER_SCRIPT --datatype "TCGA_maf" --data $TCGA_PANCAN12_MAF_PATH --outfile $MAF_JSON_OUT_PATH

# Convert clinical file
TCGA_PANCAN12_CLINICAL_PATH=${CWD}"/raw_data/summary_patient_metadata_pancan12_SHORT100.tsv"
CLINICAL_JSON_OUT_PATH=${CWD}"/converted_data/summary_patient_metadata_pancan12_SHORT100.json"
python $CONVERTER_SCRIPT --datatype "TCGA_patients" --data $TCGA_PANCAN12_CLINICAL_PATH --outfile $CLINICAL_JSON_OUT_PATH
