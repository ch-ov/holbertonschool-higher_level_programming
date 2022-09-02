#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)"""

import sys
import urllib.error.HTTPError
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.getcode))
