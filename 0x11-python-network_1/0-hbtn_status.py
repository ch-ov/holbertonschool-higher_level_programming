#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        if response.readable():
            data = response.read()
            print("Body response:")
            print(f"\t- type: {type(data)}")
            print(f"\t- content: {data}")
            print(f"\t- utf8 content: {data.decode('utf-8')}")
