"""
Installing:

Uninstalling:

Notes:
    - He's not working yet

ToDo:
    - add desktop entry
        (https://askubuntu.com/questions/342950/how-do-i-create-a-desktop-entry-to-launch-a-python-script)    
    - Make installer use home dir as default
    - get script to create and install venv and requirements
"""
import os
import subprocess
import pkg_resources
from pkg_resources import DistributionNotFound


# get home dir
home = bash_alias_dir = os.path.expanduser("~/")


# test if all dependencies are installed
with open('requirements.txt') as f:
    dependencies = [line.strip() for line in f.readlines()]

try: 
    pkg_resources.require(dependencies)

except DistributionNotFound as e:
    subprocess.check_call([os.getcwd() + "/src/bash/venv_helper.sh", ""])
    raise SystemExit(
        "venv was activated."
        " Created new venv and tried installing."
    )


# get data for config.ini
program_dir = os.path.dirname(os.path.abspath(__file__))
inpstr = "\n\n\nEnter the path to the time log directory (spaces are permitted)"
inpstr += f"\nDirectory: {home}"

time_log_dir = home + input(inpstr)

if not os.path.isdir(time_log_dir):
    os.makedirs(time_log_dir)
    print("Time log directory not found, created new directory")


# setup config.ini
with open(program_dir + "/config/config.ini", "w") as f:
    f.write("[DIRS]\n")
    f.write("TIME_LOG_DIR = " + time_log_dir + "\n")
    f.write("PROGRAM_DIR = " + program_dir + "\n")


# setup bash alias
if os.path.exists(home + ".bash_aliases"):
    bash_alias_dir = home + ".bash_aliases"

    with open(bash_alias_dir, "r") as f:
        lines = f.readlines()
        lines = [line.strip("\n") for line in lines]

    alias_exists = False
    for line in lines:
        if "alias timer" in line:
            alias_exists = True
    
    if alias_exists:
        write_to_file="no"
    else:
        write_to_file = "yes"
        
else:
    with open(bash_alias_dir, "w"):
        alias = 'alias timer="bash "+program_dir+"/src/bash/timer.sh"'
        write_to_file = "no"


# run install bash script with config file passed in
subprocess.check_call([
    program_dir + '/src/bash/installer.sh',
    program_dir,
    write_to_file
])
