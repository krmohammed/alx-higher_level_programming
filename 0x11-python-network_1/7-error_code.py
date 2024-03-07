#!/usr/bin/python3
"""diplays the body of the response"""
import requests
import sys


if __name__ == "__main__":
    resp = requests.get(sys.argv[1])
    if resp.status_code > 400:
        print("Error code: {}".format(resp.status_code))
