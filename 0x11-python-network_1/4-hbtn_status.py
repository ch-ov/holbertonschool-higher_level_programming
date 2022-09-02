#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""

import requests


if __name__ == "__main__":

    reqst = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(reqst.text)}")
    print(f"\t- content: {reqst.text}")
