#!/bin/bash
# Takes a URL sends request to URL, and displays size of the body of response
curl -s "$1" | wc -c
