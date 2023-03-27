import customtkinter as ctk
import configparser
from file_handler import WorkHandler
from tkcalendar import Calendar, DateEntry
import datetime

# import tkinter as tk
# from tkinter import ttk


class GUICONFIG(configparser.ConfigParser):
    time_log_dir: str = None
    program_dir: str = None
    wh: WorkHandler = None
    work_state: bool = None

    def __init__(self):
        super().__init__()
        self.read("config.ini")
        self.time_log_dir = self.get("DIRS", "TIME_LOG_DIR")
        self.program_dir = self.get("DIRS", "PROGRAM_DIR")

        self.wh = WorkHandler(self.time_log_dir)
        self.work_state = self.wh.get_work_state()



class GUI(ctk.CTk):
    button_state: bool = False

    def __init__(self):
        super().__init__()
        self.config = GUICONFIG()
        self.button_state = self.config.work_state
        self.create_window()
        self.main()
    
    def create_window(self):
        self.title("Work Timer")
        self.geometry("400x240")
        self.resizable(True, True)

        btt_txt = "Start Working" if not self.button_state else "Stop Working"

        self.start_stop_button = ctk.CTkButton(
            self,
            text=btt_txt,
            command=self.click_ss,
            width=380,
            height=70,
            # font=("Arial", 46),
        )
        self.start_stop_button.place(relx=0.5, rely=0.05, anchor=ctk.N)

        self.create_excel_sheet = ctk.CTkButton(
            self,
            text="Create Time Sheet",
            command=self.click_sheet,
            width=380,
            height=70,
            # font=("Arial", 46),
        )
        self.create_excel_sheet.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        self.edit_excel_layout = ctk.CTkButton(
            self,
            text="Create custom time",
            command=self.custom_time,
            width=380,
            height=70,
            # font=("Arial", 46),
        )
        self.edit_excel_layout.place(relx=0.5, rely=0.95, anchor=ctk.S)
        
        # self.start_stop_button.pack(padx=10, pady=10, side="top")
        # self.create_excel_sheet.pack(padx=10, pady=10, side="bottom")
    
    def click_ss(self):
        # use button state to call either start or stop
        self.button_state = not self.button_state

        if self.button_state:
            self.config.wh.start()
            self.start_stop_button.configure(text="Stop Working")
        else:
            self.config.wh.stop()
            self.start_stop_button.configure(text="Start Working")
    
    
    def click_sheet(self):
        print("I am not implemented yet lmao")

    def custom_time(self):
        def check_date():
            print(f'Date: {time_picked["date"].get_date()}')
            print(f'\nStart Time: {time_picked["start_time"]["hour"].get()}:{time_picked["start_time"]["minute"].get()}')
            print(f'\nEnd Time: {time_picked["end_time"]["hour"].get()}:{time_picked["end_time"]["minute"].get()}')
            print(f'\nPause Time: {time_picked["pause_time"]["hour"].get()}:{time_picked["pause_time"]["minute"].get()}')

        today = datetime.date.today()
        print('custom_time')
        newWindow = ctk.CTkToplevel(self)
        newWindow.title("Edit excel layout")
        newWindow.geometry("400x240")
        newWindow.resizable(True, True)
        today = datetime.date.today()
        time_picked = {"date": None, "start_time": {}, "end_time": {}, "pause_time": {} }

        # Date
        ctk.CTkLabel(newWindow,
          text ="Date:").grid(column=0, row=0, sticky=ctk.W, padx=5, pady=5)
        time_picked["date"] = DateEntry(newWindow, width=12, borderwidth=2)
        time_picked["date"].grid(column=1, row=0, sticky=ctk.E, padx=5, pady=5)
        
        # Start Time
        ctk.CTkLabel(newWindow,
          text ="Start Time:").grid(column=0, row=1, sticky=ctk.W, padx=5, pady=5)
        time_picked["start_time"]["hour"] = ctk.CTkEntry(newWindow, fg_color='white', text_color='black', 
                                                   placeholder_text='Hours')
        time_picked["start_time"]["hour"].grid(column=1, row=1, sticky=ctk.E, padx=5, pady=5)
        time_picked["start_time"]["minute"] = ctk.CTkEntry(newWindow, fg_color='white', text_color='black', 
                                                   placeholder_text='Minutes')
        time_picked["start_time"]["minute"].grid(column=2, row=1, sticky=ctk.E, padx=5, pady=5)

        # End Time
        ctk.CTkLabel(newWindow,
          text ="End Time:").grid(column=0, row=2, sticky=ctk.W, padx=5, pady=5)
        time_picked["end_time"]["hour"] = ctk.CTkEntry(newWindow, fg_color='white', text_color='black', 
                                                   placeholder_text='Hours')
        time_picked["end_time"]["hour"].grid(column=1, row=2, sticky=ctk.E, padx=5, pady=5)
        time_picked["end_time"]["minute"] = ctk.CTkEntry(newWindow, fg_color='white', text_color='black', 
                                                   placeholder_text='Minutes')
        time_picked["end_time"]["minute"].grid(column=2, row=2, sticky=ctk.E, padx=5, pady=5)

        # Pause
        ctk.CTkLabel(newWindow,
          text = "Pause Time:").grid(column=0, row=3, sticky=ctk.W, padx=5, pady=5)
        time_picked["pause_time"]["hour"] = ctk.CTkEntry(newWindow, fg_color='white', text_color='black', 
                                                   placeholder_text='Hours')
        time_picked["pause_time"]["hour"].grid(column=1, row=3, sticky=ctk.E, padx=5, pady=5)
        time_picked["pause_time"]["minute"] = ctk.CTkEntry(newWindow, fg_color='white', text_color='black', 
                                                   placeholder_text='Minutes')
        time_picked["pause_time"]["minute"].grid(column=2, row=3, sticky=ctk.E, padx=5, pady=5)

        newWindow.check_date = ctk.CTkButton(
            newWindow,
            text="Save work hours",
            command=check_date,
            # width=380,
            # height=70,
        )
        newWindow.check_date.place(relx=0.5, rely=0.95, anchor=ctk.S)

    def main(self):
        self.mainloop()


if __name__ == "__main__":
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    gui = GUI()
