#!/bin/bash
printf 'Specify absolute directory for saving timer logs: '
read -r log_dir
TIMER_LOG_DIR=$log_dir

if ! [ -f "$TIMER_LOG_DIR" ]
then
    printf 'Directory did not exist, creating now\n'
    mkdir $TIMER_LOG_DIR
fi

tester="$(cat tester.txt)"
echo $tester