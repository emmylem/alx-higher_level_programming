#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me to respond a message
curl -sL -X PUT -H "Origin: Header" -d "user_id=98" 0.0.0.0:5000/catch_me
