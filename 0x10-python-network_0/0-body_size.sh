#!/bin/bash
# This script sends a request to a URL and displays the size of the response
curl -sI "$1" | grep -i Content-Length | cut -d " " -f2
