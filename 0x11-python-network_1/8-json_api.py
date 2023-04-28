#!/usr/bin/python3
"""Sends a Post request to a given URL"""

import sys
import requests


if __name__ == '__main__':
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    var = {'q': letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=var)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
