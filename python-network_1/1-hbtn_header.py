#!/usr/bin/python3
"""
This script sends an HTTP GET request to a specified URL and displays
the value of the 'X-Request-Id' variable from the response headers.

Usage:
    ./fetch_request_id.py <URL>

Requirements:
    - Only urllib and sys modules are used
    - A with statement is used for the HTTP request
"""

from urllib import request
import sys

url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.headers
    x_request_id = headers.get("X-Request-Id")
    print(x_request_id)
