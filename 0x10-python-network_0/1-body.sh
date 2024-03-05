#!/bin/bash
# sends a GET request and displays the response body
response=$(curl -s -o out.txt -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && curl -s "$1"
echo "$response"
