#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""
import sys
from urllib.parse import urlencode
from urllib.request import urlopen, Request
from urllib.error import URLError


if __name__ == "__main__":
    url_arg = sys.argv[1]
    req = Request(url_arg)

    try:
        with urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print(e.code)
