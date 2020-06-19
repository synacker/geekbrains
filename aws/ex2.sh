#!/bin/bash

set -e

mkdir first
mkdir second

touch first/first.py
touch second/second.py

mv second/second.py first
rm -r second

mv first first_second
rm -rf first_second