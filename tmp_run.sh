#!/bin/bash
#
#TODO: switch order of checks, so that a venv is created if it is missing
#     and a config.ini is created if it is missing (using py installer)
#
# check if config file exists and is not empty
if [ -s "config.ini" ]
then
    stopper=false
else
    stopper=true
fi

if "$stopper" = true
then
    printf 'Missing config.ini. Please Create config.ini\n'
    exit
fi

# check if venv exists
if [ -f venv/bin/activate ]
then
    source venv/bin/activate
else
    printf 'Missing venv/bin/activate. Please Create venv\n'
    exit
fi

# read the config file
TIME_LOG_DIR=$(grep -Po '(?<=TIME_LOG_DIR = ).*' config.ini)
PROGRAM_DIR=$(grep -Po '(?<=TIME_LOG_DIR = ).*' config.ini)

