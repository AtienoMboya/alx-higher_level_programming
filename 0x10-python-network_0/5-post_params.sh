#!/bin/bash
# sends a POST request to URL and displays response body
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
