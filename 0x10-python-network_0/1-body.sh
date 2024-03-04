#!/bin/bash
<<<<<<< HEAD
# displays the body of the response (200 status code only)
curl -s "$1"
=======
# sends a GET request and displays the response body
response=$(curl -s -o shey.txt -w "%{http_code}" "$1"); [ "$response" -eq 200 ] && cat shey.txt
>>>>>>> eee03c3c4d224f593045199ab065e7000b18f1af
