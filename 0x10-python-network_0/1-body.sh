#!/bin/bash
# takes a URL, sends a GET request and displays the body of the response
curl -sfL "$1" -X GET
