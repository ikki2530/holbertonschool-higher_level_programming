#!/bin/bash
curl -w "%{http_code}" -s -o /dev/null "$1"
