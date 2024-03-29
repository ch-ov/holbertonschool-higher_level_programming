#!/usr/bin/python3
"""Write a Python script that fetches https://intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        data = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(data)))
        print("\t- content: {}".format(data))
        print("\t- utf8 content: {}".format(data.decode('utf-8')))
