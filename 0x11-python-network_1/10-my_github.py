#!/usr/bin/python3
"""uses the GitHub API to display your id"""

import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":

    credent = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    reqst = requests.get("https://api.github.com/user", auth=credent).json()
    print(reqst.get('id'))
