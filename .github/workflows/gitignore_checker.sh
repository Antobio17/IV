#!/bin/bash

if grep -Fxq "config.yml" .gitignore; then echo 'true'; else echo 'false'; fi