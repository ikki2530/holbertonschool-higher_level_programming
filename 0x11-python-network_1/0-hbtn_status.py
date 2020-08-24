#!/usr/bin/python3
import urllib

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print(type(response))
    print(html)
    print(html.decode('UTF-8'))
