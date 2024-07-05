#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL with the 
email as a parameter, and displays the body of the response (decoded in utf-8).

Usage:
    ./script_name.py <URL> <email>

Example:
    ./script_name.py http://example.com hr@example.com

This script sends a POST request to the specified URL with the provided email 
as a parameter and prints the response body.
"""
if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(sys.argv[1], data=data)
    with urllib.request.urlopen(request) as response:
        the_page = response.read().decode('utf-8')
        print(the_page)
