#!/bin/bash
# Sends a request to URL passed as argument, displays status code of response
curl -so /dev/null -w "%{http_code}" "$1"
