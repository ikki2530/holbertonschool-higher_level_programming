#!/usr/bin/python3
"""script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    lg = len(sys.argv)
    if lg != 2:
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post(
        'http://cb6c4d06c482.22216bed.hbtn-cod.io:5000/search_user',
        data={'q': q})

    dic = response.json()
    if response.headers['content-type'] == 'application/json' and dic:
        print("[{}] {}".format(dic['id'], dic['name']))
    else:
        if response.headers['content-type'] != 'application/json':
            print("Not a valid JSON")
        elif not response.json():
            print("No result")
