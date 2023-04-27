#!/bin/bash
# Sends a request to a url with a header variable
curl -sH "X-School-User-Id: 98" "$1"
