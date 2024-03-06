#!/usr/bin/python3
"""
    takes in a URL, sends request to the URL and
    displays the value if `X-Request-Id
"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    print(resp.info().get("X-Request-Id"))
