#!/usr/bin/python3
"""Sends POST request to a given url"""

import sys
import urllib.request
import urllib.parse


if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(page.decode("utf-8"))
