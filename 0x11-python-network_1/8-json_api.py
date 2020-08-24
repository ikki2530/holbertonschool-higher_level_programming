#!/usr/bin/python3
"""script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q = sys.argv[1]
    response requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    print(response.headers)
    print("-------------------------")
    print(response.body)