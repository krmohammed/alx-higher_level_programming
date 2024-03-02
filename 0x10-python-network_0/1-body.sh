#!/bin/bash
# sends a GET request and displays the response body
#curl -s -o out.txt -w "%{http_code}" "$1"; []
response=$(curl -s -o temp_response.txt -w "%{http_code}" "$1"); http_code=$(head -n1 temp_response.txt); [ "$http_code" -eq 200 ] && sed '$d' temp_response.txt; rm temp_response.txt
