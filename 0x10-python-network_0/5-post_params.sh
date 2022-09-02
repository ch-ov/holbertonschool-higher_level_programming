#!/bin/bash
# Takes a URL, sends POST request to passed URL, and displays body of response
curl -sL -X POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
