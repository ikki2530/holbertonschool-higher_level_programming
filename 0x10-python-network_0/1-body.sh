#!/bin/bash
# takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -w "%{size_download}\n" -s -o /dev/null -X GET "$1")
echo "Hello $response"
