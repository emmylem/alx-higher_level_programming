#!/bin/bash
# Sends POST request to a url
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
