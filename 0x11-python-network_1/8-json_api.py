#!/usr/bin/python3
"""sends a POST request with a letter as a parameter"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        val = ""
    else:
        val = sys.argv[1]
    param = {"q": val}
    resp = requests.post("http://0.0.0.0:5000/search_user", data=param)
    try:
        resp_json = resp.json()
        if resp_json:
            print("[{}] {}".format(resp_json["id"], resp_json["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
