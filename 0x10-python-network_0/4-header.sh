#!/bin/bash
# Takes a URL as argument, sends GET request to URL, displays body of response
curl -sL -H "X-HolbertonSchool-User-Id: 98" "$1"
