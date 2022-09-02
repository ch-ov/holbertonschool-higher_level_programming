#!/bin/bash
# Sends a DELETE request to URL pass as first arg and show body of response
curl -sX DELETE "$1"
