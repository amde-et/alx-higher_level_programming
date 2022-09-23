#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""
import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    hdrs = {"Accept": "application/vnd.github.v3+json"}
    url = "https://api.github.com/user"
    req = requests.get(url,  auth=(username, passwd), headers=hdrs)
    if req:
        print(req.json()["id"])
    else:
        print(None)
