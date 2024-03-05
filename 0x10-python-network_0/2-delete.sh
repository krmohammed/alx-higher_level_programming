#!/bin/bash
# sends a delete request
response=$(curl -s -X DELETE "$1"); echo "$response"
