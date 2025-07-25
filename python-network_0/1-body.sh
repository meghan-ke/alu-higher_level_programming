#!/bin/bash
# Script that prints the number of redirections for a given URL
n=$(curl -s -L -o /dev/null -w "%{num_redirects}" "$1"); [ "$n" -eq 0 ] && echo "no redirection" || echo "$n redirection"
