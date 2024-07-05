#!/usr/bin/python3
"""
This script takes your GitHub credentials (username and password)
and uses the GitHub API to display your user ID.

Usage:
    ./script_name.py <username> <password>

Example:
    ./script_name.py myusername mypassword

The script uses the 'requests' library to send a GET request to the
GitHub API endpoint 'https://api.github.com/user' with basic
authentication. It then prints the user ID from the JSON response.
"""
if __name__ == "__main__":
    import sys
    import requests
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get('id'))
