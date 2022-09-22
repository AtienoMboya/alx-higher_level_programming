#!/bin/bash
# sends a DELETE request to url passed as first arg and displays response body
curl -s "$1" -X DELETE
