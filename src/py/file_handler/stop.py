import numpy as np
import datetime as dt
import os

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

foldername = ""
if dt.datetime.now().day <= 15:
    idx = dt.datetime.now().month-1
    foldername += months[idx-1]
    foldername += "_"+ months[idx]
else:
    idx = dt.datetime.now().month-1
    foldername += months[idx]
    foldername += "_"+ months[(idx+1)%12]

mypath = ""

if not os.path.isdir(mypath+foldername):
    raise Exception("You need to start a timer first to create a folder")

# stop timer
then = str(dt.datetime.now())[:16]
filename = "/"+then[:10]+".txt"
if not os.path.isfile(mypath+foldername+filename):
    raise Exception("You need to start a timer first to create a file")
else:
    with open(mypath+foldername+filename, 'r') as f:
        lines = f.readlines()
        if not lines[-1][:5] == 'start':
            raise Exception("You need to start a timer first")


with open(mypath+foldername+filename, "a") as f:
        f.write('\nstop '+then)
        print('Timer stopped')
