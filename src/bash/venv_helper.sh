#!/bin/bash

# get script path
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd "$SCRIPTPATH"
cd ..
cd ..
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python install.py
