#!/bin/bash
# Takes in url and displays all http methods
curl -sI "$!" | grep "Allow" | cut -d " " -f 1-
