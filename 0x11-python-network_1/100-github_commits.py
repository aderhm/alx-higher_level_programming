#!/usr/bin/python3
"""This script lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    res = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    commits = res.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')
            ))
    except IndexError:
        print("Out of range!")
