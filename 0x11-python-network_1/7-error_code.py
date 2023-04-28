#!/usr/bin/python3
"""Sends a Request to a given URL"""

import sys
import requests


if __name__ == '__main__':
    url = sys.argv[1]

    r = requests.get(url)
    stat = r.status_code()
    if stat >= 400:
        print("Error code: {}".format(stat))
    else:
        print(r.text)
