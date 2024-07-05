#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8).
If an HTTP error occurs, it prints the error code.

Usage:
    ./script_name.py <URL>

Example:
    ./script_name.py http://example.com

This script sends a GET request to the specified URL and prints the response body.
If the request results in an HTTP error, it prints the error code instead.
"""
if __name__ == "__main__":
    import sys
    import urllib.request
    request = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(request) as response:
            the_page = response.read().decode('utf-8')
            print(the_page)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
