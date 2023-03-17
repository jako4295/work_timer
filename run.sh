#!/bin/bash

# get script path
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
cd "$SCRIPTPATH"

# read the config file
TIME_LOG_DIR=$(grep -Po '(?<=TIME_LOG_DIR = ).*' config.ini)
PROGRAM_DIR=$(grep -Po '(?<=PROGRAM_DIR = ).*' config.ini)
TMP_GUI_PATH="/src/py/gui.py"
GUI_PATH="$PROGRAM_DIR$TMP_GUI_PATH"

# check if venv exists
TMP_VENV_PATH="/venv/bin/activate"
VENV_PATH="$PROGRAM_DIR$TMP_VENV_PATH"
if [ -f "$VENV_PATH" ]
then
    source venv/bin/activate
else
    printf 'Missing venv/bin/activate. Please Create venv\n'
    exit
fi

# source the environment and run the GUI
source "$VENV_PATH"
python "$GUI_PATH"