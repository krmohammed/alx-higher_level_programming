#!/usr/bin/env bash
response=$(curl -s -o out.txt -w "%{size_download}" "$1")
echo "$response"
