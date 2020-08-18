#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -w "%{http_code}" -s -o /dev/null -X GET -L "$1")

if [ "$response" == "200" ]; then
    curl -s -X GET -L "$1"
fi
