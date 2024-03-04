#!/bin/bash
# sends a GET request and displays the response body
curl -s -o out.txt -w "%{http_code}" "$1"
