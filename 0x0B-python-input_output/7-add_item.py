#!/usr/bin/python3
"""
adds arguments to a Python List
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    filename = 'add_item.json'
    py_list = []

    for i in range(1, len(sys.argv)):
        py_list.append(sys.argv[i])

    save_to_json_file(py_list, filename)
    return load_from_json_file(filename)


if __name__ == "__main__":
    main()
