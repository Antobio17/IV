#!/bin/bash

if grep -Fxq ".env" .gitignore; then echo "TRUE"; else echo "FALSE"; fi