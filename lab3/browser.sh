#!/bin/bash
export http_proxy=http://localhost:8080
export https_proxy=http://localhost:8080
export HTTP_PROXY=http://localhost:8080
export HTTPS_PROXY=http://localhost:8080
mitmdump -s redirect.py 2>&1 1>/dev/null &