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
    os.makedirs(mypath+foldername)
    print("folder created")

# start timer
now = str(dt.datetime.now())[:16]
filename = "/"+now[:10]+".txt"
if not os.path.isfile(mypath+foldername+filename):
    with open(mypath+foldername+filename, 'w') as f:
        f.write('start '+now)
    print("file created and timer started")
else:
    with open(mypath+foldername+filename, 'r') as f:
        lines = f.readlines()
        if lines[-1][:5] == 'start':
            raise Exception("You need to stop a timer first")

    with open(mypath+foldername+filename, "a") as f:
        f.write('\nstart '+now)
        print('Timer started')
