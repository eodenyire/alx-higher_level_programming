# 0x10. Python - Network #0

This repository contains solutions to the project tasks for `0x10. Python - Network #0`, part of the ALX Software Engineering Program. The focus of this project is to learn about network programming in Python, including making HTTP requests and interacting with web servers.

## Project Overview

In this project, you will learn how to send HTTP requests, handle HTTP responses, and perform various operations using Python scripts. You will explore different HTTP methods such as GET, POST, DELETE, and more.

## Directory Structure

```plaintext
.
├── 0-body_size.sh
├── 1-body.sh
├── 100-status_code.sh
├── 2-delete.sh
├── 3-methods.sh
├── 4-header.sh
├── 5-post_params.sh
└── README.md
```plaintext

Files and Tasks
0-body_size.sh
Description: A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response.
Usage: ./0-body_size.sh <URL>
Example:
sh
Copy code
./0-body_size.sh http://example.com
1-body.sh
Description: A Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response.
Usage: ./1-body.sh <URL>
Example:
sh
Copy code
./1-body.sh http://example.com
100-status_code.sh
Description: A Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
Usage: ./100-status_code.sh <URL>
Example:
sh
Copy code
./100-status_code.sh http://example.com
2-delete.sh
Description: A Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response.
Usage: ./2-delete.sh <URL>
Example:
sh
Copy code
./2-delete.sh http://example.com/resource
3-methods.sh
Description: A Bash script that takes in a URL and displays all HTTP methods the server will accept.
Usage: ./3-methods.sh <URL>
Example:
sh
Copy code
./3-methods.sh http://example.com
4-header.sh
Description: A Bash script that takes in a URL as an argument, sends a GET request to the URL, and displays the body of the response. A header variable X-School-User-Id must be sent with the value 98.
Usage: ./4-header.sh <URL>
Example:
sh
Copy code
./4-header.sh http://example.com
5-post_params.sh
Description: A Bash script that takes in a URL, sends a POST request to the passed URL, and displays the body of the response. A variable email must be sent with the value test@gmail.com and a variable subject with the value I will always be here for PLD.
Usage: ./5-post_params.sh <URL>
Example:
sh
Copy code
./5-post_params.sh http://example.com
Learning Objectives
How to send HTTP/HTTPS requests in Bash
How to handle HTTP responses
How to use various HTTP methods (GET, POST, DELETE, etc.)
How to handle and manipulate HTTP headers
How to work with query strings and request bodies
Author
Emmanuel Odenyire Anyira

Email: eodenyire@gmail.com
LinkedIn: Emmanuel Odenyire Anyira
License
This project is licensed under the MIT License - see the LICENSE file for details.
