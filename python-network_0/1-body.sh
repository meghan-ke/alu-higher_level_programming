#!/bin/bash
# Count and display number of redirections
echo "$(curl -s -L -o /dev/null -w "%{num_redirects}" "$1") redirection"
