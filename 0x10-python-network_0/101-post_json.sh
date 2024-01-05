#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response
curl -sL -X POST -H "content-type:application/json" -d @"$2" "$1"
