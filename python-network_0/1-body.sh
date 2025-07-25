#!/bin/bash
# Only display body if status code is 200
[ "$(curl -s -o body.txt -w "%{http_code}" "$1")" = "200" ] && cat body.txt
