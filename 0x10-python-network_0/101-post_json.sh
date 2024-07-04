#!/bin/bash
# Sends a JSON POST request to a given URL with a given JSON file.

# Validate if the JSON file is valid
if ! jq . "$2" >/dev/null 2>&1; then
    echo "Not a valid JSON"
    exit 1
fi

# Send POST request with JSON file contents
curl -s -H "Content-Type: application/json" -d "@$2" "$1"
