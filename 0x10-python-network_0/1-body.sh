#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -w "%{http_code}\n" -s -o /dev/null -X GET "$1")
echo "$response"
if [ "$response" -eq 200 ]; then
    
else
    echo "dont display the body"
fi