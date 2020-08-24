#!/usr/bin/python3
"""sends a request to the URL and displays the value of X-Request-Id"""
import sys
import urllib.request

if __name__ == "__main__":
    url_arg = sys.argv[1]
    with urllib.request.urlopen(url_arg) as response:
        variable = response.info()['X-Request-Id']
        print(variable)
