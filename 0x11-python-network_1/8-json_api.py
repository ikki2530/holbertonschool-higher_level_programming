#!/usr/bin/python3
"""script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    lg = len(sys.argv)
    if lg == 2:
        q = sys.argv[1]
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': q})
    try:
        json_cont = response.json()
        if len(json_cont) == 0:
            print("No result")
        else:
            print("[{}] {}".format(json_cont['id'], json_cont['name']))
    except Exception:
        print("Not a valid JSON")

    # if cond == 'application/json' and response.json():
    #     dic = response.json()
    #     print("[{}] {}".format(dic['id'], dic['name']))
    # else:
    #     if response.headers.get('content-type') != 'application/json':
    #         print("Not a valid JSON")
    #     elif not response.json():
    #         print("No result")
