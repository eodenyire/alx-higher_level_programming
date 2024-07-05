# 0x11. Python - Network #1

## Description
This repository contains solutions to various network-related tasks using Python, focusing on fetching internet resources, making HTTP requests, handling responses, and interacting with APIs.

## Learning Objectives
By the end of this project, you should be able to explain to anyone, without the help of Google:
- How to fetch internet resources with the Python package urllib
- How to decode urllib body response
- How to use the Python package requests for simpler HTTP requests than urllib
- How to make HTTP GET requests and handle responses
- How to make HTTP POST/PUT/etc. requests
- How to fetch JSON resources
- How to manipulate data from an external service

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A README.md file at the root of the repo, containing a description of the repository
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (python3 -c 'print(__import__("my_module").__doc__)')
- You must use `get` to access dictionary values by key
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class, or method
- Your code should not be executed when imported (by using `if __name__ == "__main__":`)

## Directory Structure
- **0-hbtn_status.py**: Fetches and displays the status of https://alx-intranet.hbtn.io/status using urllib.
- **1-hbtn_header.py**: Takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header using urllib.
- **2-post_email.py**: Sends a POST request with an email parameter to a given URL using urllib.
- **3-error_code.py**: Takes a URL, sends a request, and displays the body of the response. Handles urllib.error.HTTPError exceptions.
- **4-hbtn_status.py**: Fetches and displays the status of https://alx-intranet.hbtn.io/status using requests.
- **5-hbtn_header.py**: Takes a URL, sends a request, and displays the value of the X-Request-Id variable in the response header using requests.
- **6-post_email.py**: Sends a POST request with an email parameter to a given URL using requests.
- **7-error_code.py**: Takes a URL, sends a request, and displays the body of the response. Prints the HTTP status code for errors >= 400.
- **8-json_api.py**: Sends a POST request with a letter parameter to http://0.0.0.0:5000/search_user. Handles JSON responses and displays results.
- **10-my_github.py**: Uses Basic Authentication with GitHub API to display the user ID based on credentials.

## Collaboration
For collaborations or inquiries, contact Emmanuel Odenyire Anyira at eodenyire@gmail.com or via [LinkedIn](https://www.linkedin.com/in/emmanuelodenyire/).

---

**GitHub Repository**: [alx-higher_level_programming](https://github.com/eodenyire/alx-higher_level_programming)

**Directory**: 0x11-python-network_1

