#!/usr/bin/env bash
# takes in a url and sends a request to the url
# displays the size of the body of the response


response=$(curl -s -o out.txt -w "%{size_download}" "$1")

echo "$response"

rm out.txt
