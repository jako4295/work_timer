import numpy as np
import os
import argparse
import pandas as pd


# functions
def check_file(lines, filename):
    if lines[0][:5] != "start":
        raise Exception(f"First line in file {filename} is not 'start'")
    elif lines[-1][:4] != "stop":
        raise Exception(f"Last line in file {filename} is not 'stop'")
    else:
        pass


def check_start_stop_shift(lines, filename):
    # check even index is start and odd index is stop
    for i, line in enumerate(lines):
        if i % 2 == 0:
            if line[:5] != "start":
                raise Exception(
                    f"In file {filename}, an even index started with something other than 'start' which is unexpected"
                )
        else:
            if line[:4] != "stop":
                raise Exception(
                    f"In file {filename}, an odd index started with something other than 'stop' which is unexpected"
                )
    pass


def round_time(lines, time="15min"):
    rounded_lines = []
    for i, line in enumerate(lines):
        if i % 2 == 0:
            rounded_lines.append(
                "start " + str(pd.Timestamp(line[6:]).round(time))[:-3]
            )
        else:
            rounded_lines.append("stop " + str(pd.Timestamp(line[5:]).round(time))[:-3])
    return rounded_lines


def date(filename):
    day = pd.Timestamp(filename[:10]).day_name()
    date = filename[8:10]
    month = pd.Timestamp(filename[:10]).month_name()
    year = filename[:4]
    return f"{day}, {date} {month} {year}"


# inputs
print("Type the months you want to convert to xlsx")
folder = input("Press enter to continue\n")

# clean up input
if folder[-1] != "/":
    folder += "/"

if folder[:-1] not in os.listdir():
    options = []
    for filename in os.listdir():
        if filename != ".":
            options.append(filename)

    raise Exception(f"Folder doesn't exist. Choose from {options}")

files = sorted(os.listdir(folder))

idx = []
for i, filename in enumerate(files):
    if filename[-4:] != ".txt":
        idx.append(i)
files = np.delete(files, idx)

# try:
#     files = os.listdir(folder)

#     for i, filename in files:
#         if '.txt' != filename:
#             files.pop(i)

# except:
#     options = []
#     for filename in os.listdir():
#         if filename != '.':
#             options.append(filename)
#     assert f"Folder doesn't exist. Choose from {options}"


# file check and convert to xlsx
df_excel = pd.DataFrame()
for file_temp in files:
    with open(folder + file_temp, "r") as f:
        lines = f.readlines()

    check_file(lines, file_temp)
    check_start_stop_shift(lines, file_temp)

    round_lines = round_time(lines)
    date_str = date(file_temp)
    start_time = round_lines[0][-5:]
    stop_time = round_lines[-1][-5:]

    if len(round_lines) <= 2:
        pause = pd.Timedelta(0)
    else:
        pause = pd.Timedelta(0)
        for i in range(2, len(round_lines), 2):
            pause += pd.Timestamp(round_lines[i][-5:]) - pd.Timestamp(
                round_lines[i - 1][-5:]
            )

    total_time = (pd.Timestamp(stop_time) - pd.Timestamp(start_time)) - pd.Timedelta(
        pause
    )
    total_time = str(total_time)[7:-3]

    pause = str(pause)[7:-3]

    df = pd.DataFrame(
        {
            "Dato": [date_str],
            "Start": [start_time],
            "Slut": [stop_time],
            "Pause": [pause],
            "Antal Timer": [total_time],
        }
    )

    df_excel = pd.concat([df_excel, df])

time_d = pd.Timedelta(0)
for i in df_excel["Antal Timer"].values:
    time_d += pd.Timedelta(i + ":00")

sum_d = time_d / pd.Timedelta("1 hour")
h, m = str(sum_d).split(".")
if len(h) < 2:
    h = "0" + h
m = str(int(float("0." + m) * 60))
if len(m) < 2:
    m = m + "0"

df_sum = pd.DataFrame(
    {
        "Dato": ["I alt"],
        "Start": [None],
        "Slut": [None],
        "Pause": [None],
        "Antal Timer": [str(h + ":" + m)],
    }
)

df_excel = pd.concat([df_excel, df_sum])

df_excel = df_excel.reset_index(drop=True)

with pd.ExcelWriter(folder + "hours.xlsx") as writer:
    df_excel.style.applymap(lambda _: "text-align: center").to_excel(
        writer, sheet_name="timer", index=False
    )

    # Auto-adjust columns' width
    for column in df_excel:
        column_width = (
            max(df_excel[column].astype(str).map(len).max(), len(column)) * 1.1
        )
        if column_width < 18.5:
            column_width = 18.5
        col_idx = df_excel.columns.get_loc(column)
        writer.sheets["timer"].set_column(col_idx, col_idx, column_width)

# df_excel.to_excel(folder+'hours.xlsx', index=False)
