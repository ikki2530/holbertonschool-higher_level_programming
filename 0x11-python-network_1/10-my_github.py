#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
import sys


if __name__ == "__main__":
    heads = {'Authorization': 'token {}'.format("5c9fe4c2b803b4bed78d04e37a9aa60a0e3db6cb")}
    url = "https://api.github.com/user"
    response = requests.post(url, headers=heads)
    print(response.content)
