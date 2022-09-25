#!/bin/bash
# sends a GET request and displays the body of the response
# - The header variable `X-School-User-Id` must be sent with the value 98
curl -sH "X-School-User-Id: 98" "$1"
