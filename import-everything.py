#!/usr/bin/env python

import os
import httplib
import argparse

already_imported = []

def import_json(data_type, path):
    if not data_type == 'GeneExpression' and path not in already_imported:
        print("importing " + data_type + " - " + path)
        headers = {'Content-Type': 'application/octet-stream'}

        try:
            conn = httplib.HTTPConnection('localhost:11223')
            conn.request('POST', '/message/' + data_type, open(path, 'rb'), headers)
            response = conn.getresponse()
            success = response.read()
        except:
            success = "failed!"

        conn.close()
        print success

def find_data_type(path):
    parts = path.split('.')
    return parts[-2]

def import_everything(data_path):
    files = os.listdir(data_path)
    for path in files:
        data_type = find_data_type(path)
        import_json(data_type, data_path + '/' + path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='IMPORT EVERYTHING')
    parser.add_argument('--data-path', help="path to all the data", default="/Users/spanglry/Data/sample")
    args = parser.parse_args()

    import_everything(args.data_path)
