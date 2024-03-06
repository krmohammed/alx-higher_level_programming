#!/usr/bin/python3
"""fetches from a url"""
import requests


if __name__ == "__main__":
    resp = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response\n\t- type: {}\n\t- content: {}".format(
            type(resp), resp.text))
