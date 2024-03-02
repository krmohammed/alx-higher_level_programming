#!/bin/bash
#takes in a URL and displays the size of the body of the response
echo $(curl -s -o out.txt -w "%{size_download}" "$1")
