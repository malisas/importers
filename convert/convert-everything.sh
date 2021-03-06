#!/usr/bin/env bash

CWD=$(pwd)
CONVERTER_SCRIPT=${CWD}/convert-tcga.py

OUTPATH="$HOME/Data/sample"

for maf in $(ls ~/Data/tcga/*.maf); do
    base=$(basename $maf)
    python $CONVERTER_SCRIPT --maf $maf --out $OUTPATH/$base.json
done

for tsv in $(ls ~/Data/tcga/*.patient.tsv); do
    base=$(basename $tsv)
    python $CONVERTER_SCRIPT --tsv $tsv --out $OUTPATH/$base.json
done

for exp in $(ls ~/Data/tcga/*RNASeq.geneExp*); do
    base=$(basename $exp)
    python $CONVERTER_SCRIPT --exp $exp --out $OUTPATH/$base.json
done
