#!/usr/bin/python3
"""This script fetches the URL http://0.0.0.0:5050/status
and displays information about the body of the response using urllib.
"""

from urllib import request

url = "http://0.0.0.0:5050/status"

with request.urlopen(url) as response:
    body = response.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode('utf-8'))
