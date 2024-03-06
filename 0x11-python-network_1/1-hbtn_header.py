#!/usr/bin/python3
"""
    takes in a URL, sends request to the URL and
    displays the value if `X-Request-Id
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as resp:
        res = resp.info()

    print(res.get("X-Request-Id"))
