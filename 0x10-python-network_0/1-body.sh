#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -w "%{http_code}\n" -s -o /dev/null -X GET -L "$1")

if [ "$response" -eq 200 ]; then
    curl -X GET -L "$1" "$1"
fi