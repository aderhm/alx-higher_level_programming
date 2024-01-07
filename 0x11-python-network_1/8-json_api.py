#!/usr/bin/python3
"""This script takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    res = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_formatted_res = res.json()
        if json_formatted_res:
            print("[{}] {}".format(res.get('id'), res.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
