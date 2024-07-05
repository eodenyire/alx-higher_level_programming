#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response.
"""
if __name__ == "__main__":
    import sys
    import requests
    payload = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=payload)
    print(r.text)
