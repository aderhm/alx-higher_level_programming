#!/usr/bin/python3
"""This script takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import Request, urlopen
from urllib.error import HTTPError


if __name__ == '__main__':
    req = Request(sys.argv[1])
    try:
        with urlopen(req) as res:
            body = res.read()
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    print(body.decode('utf-8'))
