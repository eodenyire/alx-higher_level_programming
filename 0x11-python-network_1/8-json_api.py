#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter. Parses the JSON response and prints the user's
ID and name if available, or prints a message if no user is found or if the
response is not valid JSON.
"""
if __name__ == "__main__":
    import sys
    import requests
    if len(sys.argv) > 1:
        value = sys.argv[1]
    else:
        value = ""
    params = {'q': value}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=params)
    if r.headers.get('content-type') == 'application/json':
        if r.json() == {}:
            print("No result")
        else:
            id_ = r.json().get('id')
            name = r.json().get('name')
            print("[{}] {}".format(id_, name))
    else:
        print("Not a valid JSON")
