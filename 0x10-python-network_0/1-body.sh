#!/bin/bash
# This script sends a request to a URL and displays the body of the response
curl -sfLX GET "$1"
