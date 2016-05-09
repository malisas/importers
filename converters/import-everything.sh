#!/usr/bin/env bash

INPATH="$HOME/Data/variant/"

for variant in $(ls $INPATH); do
    echo "importing $variant"
    curl -H "Content-Type: application/json" -X POST --data-binary @$INPATH$variant http://localhost:11223/individuals
    # sleep 180
done

