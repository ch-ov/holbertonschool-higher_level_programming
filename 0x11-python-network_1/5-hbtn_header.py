#!/usr/bin/python3
"""Displays the value of the variable X-Request-Id in the response header"""

import sys
import requests


if __name__ == "__main__":

    url = sys.argv[1]
    reqst = requests.get(url)
    print(reqst.headers.get('X-Request-Id'))
