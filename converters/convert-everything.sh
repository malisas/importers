#!/usr/bin/env bash

CWD=$(pwd)
CONVERTER_SCRIPT=${CWD}/converter_tcga.py

OUTPATH="$HOME/Data/variant"

# for maf in $(ls ~/Data/tcga/*.maf); do
#     base=$(basename $maf)
#     echo "converting maf $maf"
#     python $CONVERTER_SCRIPT --maf $maf --out $OUTPATH/$base.json
# done

for tsv in $(ls ~/Data/tcga/*.patient.tsv); do
    base=$(basename $tsv)
    echo "converting tsv $tsv"
    python $CONVERTER_SCRIPT --tsv $tsv --out $OUTPATH/$base.json
done
