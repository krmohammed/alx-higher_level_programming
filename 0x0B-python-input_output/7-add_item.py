#!/usr/bin/python3
"""
adds arguments to a Python List
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

if os.path.exists(filename):
    py_list = load_from_json_file(filename)
else:
    py_list = []

for i in range(1, len(sys.argv)):
    py_list.append(sys.argv[i])

save_to_json_file(py_list, filename)
