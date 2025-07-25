#!/bin/bash
#the script that a URL as input and display the size of the response body
curl -s "$URL" | wc -c
