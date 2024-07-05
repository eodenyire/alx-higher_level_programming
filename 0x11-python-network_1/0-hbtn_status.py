#!/usr/bin/python3
"""
Fetches data from https://alx-intranet.hbtn.io/status
Displays the type, content, and UTF-8 encoded content of the response.
"""
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read()
            print("Body response:")
            print(f"\t- type: {type(content)}")
            print(f"\t- content: {content}")
            print(f"\t- utf8 content: {content.decode('utf-8')}")
    
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
