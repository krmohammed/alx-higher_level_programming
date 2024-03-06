#!/usr/bin/python3
""" fetches from a url """
import urllib


with urllib.Request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    res = resp.read()
print(res)
