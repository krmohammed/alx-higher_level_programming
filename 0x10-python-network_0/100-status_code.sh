#!/bin/bash
# displays the status code
curl -s -o out.txt -w "%{http_code}" "$1"
