#!/bin/bash
# Sends a request to a url and displays status code
curl -s -o /path/file -w "%(http_code)" "$1"
