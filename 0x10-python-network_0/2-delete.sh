#!/bin/bash
# sends a DELTE request to the URL passed and displays the body of the response
curl -s "$1" -X DELETE
