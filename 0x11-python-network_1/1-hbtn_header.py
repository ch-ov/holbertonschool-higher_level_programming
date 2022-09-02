#!/usr/bin/python3
"""displays value of X-Request-Id variable found in header of response"""

import sys
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.headers
        print(header['X-Request-Id'])
