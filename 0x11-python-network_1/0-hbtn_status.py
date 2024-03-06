#!/usr/bin/python3
""" fetches from a url """
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        res = resp.read()

    print("Body response:")
    print("\t- type: {}\n\t- content: {}\n\t- utf8 content: {}".format(
              type(res), res, res.decode("utf-8")))
