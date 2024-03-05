#!/bin/bash
# displays all HTTP methos allowed by the server
curl -s -I "$1" | grep "Allow" | cut -d" " -f2- 
