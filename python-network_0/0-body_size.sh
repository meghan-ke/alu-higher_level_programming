#!/bin/bash
# Get response body size in bytes using GET
curl -s -X GET "$1" | wc -c
