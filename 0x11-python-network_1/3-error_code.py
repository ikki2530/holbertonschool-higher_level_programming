#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and 
displays the body of the response (decoded in utf-8).
"""
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request


if __name__ == "__main__":
    url_arg = sys.argv[1]
    req = Request(url_arg)
    try:
        urlopen(req)
    except urllib.error.URLError as e:
        print(e.reason)
