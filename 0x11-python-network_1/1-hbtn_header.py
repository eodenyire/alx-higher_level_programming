#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the 'X-Request-Id' variable found
in the header of the response.

Usage:
    ./script_name.py <URL>

Example:
    ./script_name.py https://alx-intranet.hbtn.io
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
