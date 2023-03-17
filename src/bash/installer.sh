#!/bin/bash
# take input from python installer 
#   ($1 program_dir, $append_to_bash_profile)
program_dir=$1
write_to_file=$2

if [ $write_to_file = "yes" ]; then
    # write to bash_profile
    start_str="alias timer="
    middle_str="bash $program_dir"
    end_str="/run.sh"
    echo "$start_str'$middle_str$end_str'" >> ~/.bash_aliases
fi