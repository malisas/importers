#!/usr/bin/env bash

protoc -I=schema/bmeg/gaea/schema/ --python_out=convert/ schema/bmeg/gaea/schema/variant.proto 
