#!/usr/bin/python3
"""
Lists the 10 most recent commits of a repository using the GitHub API.

Usage:
    ./script_name.py <repository_name> <owner_name>

Example:
    ./script_name.py rails rails

This script fetches the 10 most recent commits from the specified repository
owned by the specified user using the GitHub API. It prints each commit in the format:
<sha>: <author name>

Arguments:
    repository_name: The name of the repository (e.g., 'rails')
    owner_name: The owner of the repository (e.g., 'rails')
"""
if __name__ == "__main__":
    import sys
    import requests
    repo = sys.argv[2] + "/" + sys.argv[1]
    url = 'https://api.github.com/repos/{0}/commits?per_page=10'.format(repo)
    r = requests.get(url)
    commits = r.json()
    for commit in commits:
        sha = commit.get('sha')
        name = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, name))
