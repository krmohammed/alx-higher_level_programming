#!/usr/bin/python3
"""listing first 10 commit"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    resp = requests.get(url)
    if resp.status_code == 200:
        commits = resp.json()
        for commit in commits[:10]:
            print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")
                ))
