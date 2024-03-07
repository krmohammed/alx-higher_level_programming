#!/usr/bin/python3
"""sends a POST request with a letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    param = {}
    if len(sys.argv) > 1:
        if type(sys.argv[1]) == "str" and len(sys.argv[1]) == 1:
            param["q"] = sys.argv[1]
        else:
            param["q"] = ""
    resp = requests.post("http://0.0.0.0:5000/search_user", params=param)
    try:
        a = resp.json()
        if a:
            print("[{}] {}".format(a.id, a.name))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
