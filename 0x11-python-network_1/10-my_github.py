#!/usr/bin/python3
"""script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    url = "https://api.github.com/users/{}".format(sys.argv[1])
    response = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(response.json().get('id'))
