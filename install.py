"""
Installing:

Uninstalling:

Notes:
    - He's not working yet

ToDo:
    - add desktop entry
        (https://askubuntu.com/questions/342950/how-do-i-create-a-desktop-entry-to-launch-a-python-script)    
"""
import os
import subprocess


# test if all dependencies are installed
import pkg_resources
from pkg_resources import DistributionNotFound

with open('requirements.txt') as f:
    dependencies = [line.strip() for line in f.readlines()]

try: 
    pkg_resources.require(dependencies)

except DistributionNotFound as e:
    print("Distribution not found: ", e)

# get data for config.ini
program_dir = os.path.dirname(os.path.abspath(__file__))
inpstr = "Enter the path to the time log directory (spaces are permitted): "
time_log_dir = input(inpstr)

if not os.path.isdir(time_log_dir):
    os.makedirs(time_log_dir)
    print("Time log directory not found, created new directory")

# setup config.ini
# check if config.ini exists
with open(program_dir + "/config.ini", "r") as f:
    pass

# config.ini exists, ask if it should be overwritten
overwrite = input("config.ini already exists, overwrite? (y/n): ")
if overwrite == "y":
    with open(program_dir + "/config.ini", "w") as f:
        f.write("[DIRS]\n")
        f.write("TIME_LOG_DIR = " + time_log_dir + "\n")
        f.write("PROGRAM_DIR = " + program_dir + "\n")
else:
    print("config.ini not overwritten")


# run install bash script with config file passed in
subprocess.check_call([
    program_dir + '/src/bash/installer.sh',
    program_dir,
    time_log_dir
])
