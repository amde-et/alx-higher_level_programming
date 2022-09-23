#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and displays the value
 of the variable X-Request-Id in the response header
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers["X-Request-Id"]
          if "X-Request-Id" in req.headers else None)
