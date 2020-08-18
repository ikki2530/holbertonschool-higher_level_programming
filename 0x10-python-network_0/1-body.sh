#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -w "%{http_code}" -sL -o /dev/null -X GET "$1")

if [ "$response" == "200" ]; then
    curl -sL -X GET "$1"
fi
