#!/usr/bin/env bash

CWD=$(pwd)
INPATH="$HOME/Data/variant/"

for variant in $(ls $INPATH); do
    curl -H "Content-Type: application/json" -X POST -d @$INPATH$variant http://localhost:11223/individual-list
done

