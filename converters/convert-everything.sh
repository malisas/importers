#!/bin/bash

CWD=$(pwd)
CONVERTER_SCRIPT=${CWD}/converter_tcga.py

OUTPATH=${CWD}"~/Data/variant"

for maf in $(ls ~/Data/tcga/*.maf); do
    python $CONVERTER_SCRIPT --maf $maf --outfile $OUTPATH/$maf.json
done

for tsv in $(ls ~/Data/tcga/*.patient.tsv); do
    python $CONVERTER_SCRIPT --tsv $tsv --outfile $OUTPATH/$tsv.json
done
