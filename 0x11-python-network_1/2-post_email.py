#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":

    url = sys.argv[1]
    mail = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(mail).encode('ascii')
    reqst = urllib.request.Request(url, data)
    with urllib.request.urlopen(reqst) as response:
        resp = response.read().decode('utf-8')
    print(resp)
