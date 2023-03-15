#!/bin/bash

if [ -f venv/bin/activate ]
then
    source /home/all/Git/work_timer/venv/bin/activate
else
    printf 'Missing venv/bin/activate. Please Create venv\n'
    exit
fi

python stop.py