#!/bin/bash
# sends a GET request and displays the response body
response=$(curl -s -o shey.txt -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && cat shey.txt
