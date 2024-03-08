#!/usr/bin/python3
"""displays GitHub id"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    resp = requests.get(url, auth=(username, password))
    if resp.status_code == 200:
        info = resp.json()
        print(info.get("id"))
    else:
        print(None)
