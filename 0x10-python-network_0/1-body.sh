#!/bin/bash
# sends a GET request to URL and displays the response body
curl -sfL "$1" -X GET
