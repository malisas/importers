#!/usr/bin/env python

import re
import os
import sys
import csv
import json
import string
import argparse
import sample_pb2 as schema
from google.protobuf import json_format

def parse_args(args):
    args = args[1:]
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--inpath', type=str, help='Path to the directcory containing the json signatures to import')
    parser.add_argument('--outpath', type=str, help='Path to output json file')
    parser.add_argument('--metapath', type=str, help='Path to metadata file')
    return parser.parse_args(args)

# JSON signatures have the following format:
# -----------------------------------------
    
# {
#   "intercept": -11.309385,
#   "coeff": [{
#     "feature": "NQO1",
#     "coeff": 0.3110879
#   }, {
#     "feature": "ZNF248",
#     "coeff": -0.28585953
#   }]
# }

def build_signature(name, data, meta):
    signature = schema.LinearSignature()
    signature.name = 'linearSignature:' + name
    signature.predicts = 'drug response'
    signature.intercept = data['intercept']
    drug_name = name.split('_')[0]
    signature.signatureForEdgesDrug.append('drug:' + meta['cpd_name'])
    for coefficient in data['coeff']:
        signature.coefficients[coefficient['feature']] = coefficient['coeff']

    return signature

def message_to_json(message):
    json = json_format.MessageToJson(message)
    return re.sub(r' +', ' ', json.replace('\n', ''))

def output_messages(outpath, messages):
    if len(messages) > 0:
        out = string.join(messages, '\n')
        outhandle = open(outpath, 'wb')
        outhandle.write(out)
        outhandle.close()

def load_metadata(path):
    metadata = {}
    with open(path) as metadata_file:
        reader = csv.DictReader(metadata_file)
        for line in reader:
            metadata[line['classifierName']] = line

    return metadata

def convert_json_signatures(inpath, outpath, metapath):
    metadata = load_metadata(metapath)
    signatures = []
    files = os.listdir(inpath)
    for filename in files:
        fileparts = filename.split('.')
        if fileparts[-1] == 'json':
            with open(inpath + '/' + filename) as raw:
                data = json.load(raw)
            name = fileparts[0]
            key = string.join(name.split('_')[:-1], '_')
            meta = metadata[key]
            signature = build_signature(name, data, meta)
            signatures.append(signature)

    messages = map(message_to_json, signatures)
    output_messages(outpath, messages)

if __name__ == '__main__':
    options = parse_args(sys.argv)
    convert_json_signatures(options.inpath, options.outpath, options.metapath)