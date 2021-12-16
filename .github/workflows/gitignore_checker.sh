#!/bin/bash

if grep -Fxq ".env" .gitignore; then echo 'true'; else echo 'false'; fi