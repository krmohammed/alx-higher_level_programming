#!/usr/bin/python3
"""sends a POST request with a letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    param = {}
    if len(sys.argv) > 1:
        if type(str, sys.argv[1]) && len(sys.argv[1]) == 1:
            param["q"] = sys.argv[1]
        else:
            param["q"] = ""
    resp = requests.post("http://0.0.0.0:5000/search_user", params=param)
