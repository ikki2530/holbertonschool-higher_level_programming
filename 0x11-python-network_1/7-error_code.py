#!/usr/bin/python3
"""script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""
import requests
import sys


if __name__ == "__main__":
    url_arg = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url_arg)
    print(response.status_code)
