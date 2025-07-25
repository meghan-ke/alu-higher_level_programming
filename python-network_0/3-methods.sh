#!/bin/bash
# Display allowed HTTP methods for the given URL
curl -sI "$1" | grep -i '^Allow:' | cut -d' ' -f2-
