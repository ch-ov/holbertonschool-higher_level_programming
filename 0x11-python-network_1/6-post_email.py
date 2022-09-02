#!/usr/bin/python3
"""send POST request to URL with email as parameter display body of response"""

import sys
import requests


if __name__ == "__main__":

    url =  sys.argv[1]
    mail = {'email': sys.argv[2]}
    reqst = requests.post(url, mail)
    print(reqst.text)
