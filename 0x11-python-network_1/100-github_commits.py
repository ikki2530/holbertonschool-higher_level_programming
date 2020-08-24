#!/usr/bin/python3
"""
evaluates candidates applying for a back-end position with
multiple technical challenges
"""
import requests
import sys


if __name__ == "__main__":
    rep = sys.argv[1]
    own = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(own, rep)
    response = requests.get(url)
    print(type(response.content))
