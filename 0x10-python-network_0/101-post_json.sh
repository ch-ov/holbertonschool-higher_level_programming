#!/bin/bash
# Sends a JSON POST request to URL, displays the body of response.
curl -sH "Content-Type: application/json" -d @"$2" @"$1"
