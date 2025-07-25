#!/bin/bash
response=$(curl -s -w "%{http_code}" "$1")
[ "${response: -3}" = "200" ] && echo "${response::-3}"

