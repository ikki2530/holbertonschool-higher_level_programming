#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -w "%{http_code}\n" -s -X GET -L "$1")

if [ "$response" == "200" ]; then
    $response
fi
