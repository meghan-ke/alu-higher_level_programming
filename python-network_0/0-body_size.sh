#!/bin/bash
# Script Name: body_size.sh
# Description: Sends a GET request to a given URL and displays the body size in bytes

# Check if a URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL
URL="$1"

# Send request silently (-s) and measure only the body size in bytes
curl -s "$URL" | wc -c
