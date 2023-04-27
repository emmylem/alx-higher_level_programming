#!/bin/bash
# Sends a JSON POST request with a json file
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
