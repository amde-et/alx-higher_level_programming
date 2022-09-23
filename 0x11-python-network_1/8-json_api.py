#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    args = sys.argv[1] if len(sys.argv) >= 2 else ""

    req = requests.post(url, {"q": args})
    try:
        json_r = req.json()
        if not json_r:
            print("No result")
        else:
            print("[{}] {}".format(json_r["id"], json_r["name"]))
    except Exception as e:
        print("Not a valid JSON")
