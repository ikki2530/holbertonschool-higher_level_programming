#!/usr/bin/python3
"""
script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
"""
# import sys
# import urllib.request
# from urllib.parse import urlencode
# from urllib.request import urlopen, Request

# if __name__=="__main__":
#     url_arg = sys.argv[1]
#     email = sys.argv[2]

#     values = {'email': email}
#     data1 = urlencode(values)
#     data = data1.encode('utf-8')
#     req = Request(url_arg, data)
#     print(111111111111111)
#     with urlopen(req) as reponse:
#         print(22222222222222222)
#         the_page = reponse.read()
#         print(the_page)

# data = {}
# data['email'] = email
# url_values = urllib.parse.urlencode(data)
# full_url = url_arg + "?" +url_values
# response = urllib.request.urlopen(full_url)
# print(response)

import sys
from urllib.parse import urlencode
from urllib.request import Request, urlopen

if __name__ == "__main__":
    data = urlencode({'email': sys.argv[2]})
    reque = Request(sys.argv[1], data.encode('utf-8'))
    with urlopen(reque) as re:
        print(re.read().decode('utf-8'))