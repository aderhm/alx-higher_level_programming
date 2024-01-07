#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    try:
        with urlopen(sys.argv[1]) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
