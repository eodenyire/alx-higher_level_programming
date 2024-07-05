#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status using requests.
"""
if __name__ == "__main__":
    import requests

    response = requests.get('https://alx-intranet.hbtn.io/status')
    content = response.text
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
