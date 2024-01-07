#!/usr/bin/python3
"""This script takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8).
"""

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlencode


if __name__ == '__main__':
    value = sys.argv[2]
    param = {'email': value}
    data = urlencode(param).encode('ascii')
    req = Request(sys.argv[1], data)
    with urlopen(req) as res:
        body = res.read()
    print(body.decode('utf-8'))
