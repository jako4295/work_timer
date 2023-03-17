import customtkinter as ctk
import configparser
from file_handler import WorkHandler, TimeSheetGenerator


class GUICONFIG(configparser.ConfigParser):
    time_log_dir: str = None
    program_dir: str = None
    wh: WorkHandler = None
    work_state: bool = None

    def __init__(self):
        super().__init__()
        self.read("config/config.ini")
        self.time_log_dir = self.get("DIRS", "TIME_LOG_DIR")
        self.program_dir = self.get("DIRS", "PROGRAM_DIR")

        self.wh = WorkHandler(self.time_log_dir)
        self.work_state = self.wh.get_work_state()



class GUI(ctk.CTk):
    button_state: bool = False
    log_started: bool = False

    def __init__(self):
        super().__init__()
        self.config = GUICONFIG()
        self.button_state = self.config.work_state
        self.create_window()
        self.main()
    
    def create_window(self):
        self.title("Work Timer")
        self.geometry("740x500")
        self.resizable(True, True)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        btt_txt = "Start Working" if not self.button_state else "Stop Working"

        self.start_stop_button = ctk.CTkButton(
                self,
                text=btt_txt,
                command=self.click_ss,
                width=350,
                height=180,
                font=("Arial", 46),
            )
        self.create_excel_sheet = ctk.CTkButton(
                self,
                text="Create Time Sheet",
                command=self.click_sheet,
                width=350,
                height=180,
                font=("Arial", 46),
            )
        self.daily_log = ctk.CTkTextbox(
                self,
                width=740,
                height=200,
                font=("Arial", 34),
            )
        
        self.start_stop_button.grid(row=0, column=0, sticky="nsew")
        self.create_excel_sheet.grid(row=0, column=1, sticky="nsew")
        self.daily_log.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.update_log()

    
    def click_ss(self):
        # use button state to call either start or stop
        self.button_state = not self.button_state
        self.update_log()

        if self.button_state:
            self.config.wh.start()
            self.start_stop_button.configure(text="Stop Working")
        else:
            self.config.wh.stop()
            self.start_stop_button.configure(text="Start Working")
    
    def click_sheet(self):
        if self.button_state:
            self.config.wh.stop()
            self.start_stop_button.configure(text="Start Working")
            self.button_state = not self.button_state
        
        TimeSheetGenerator.create_excel_sheet(
            self.config.time_log_dir,
            self.config.program_dir
        )
    
    def update_log(self):
        self.daily_log.delete("0.0", "end")
        self.daily_log.insert("0.0", self.config.wh.get_daily_log())

    def main(self):
        self.mainloop()


if __name__ == "__main__":
    ctk.set_default_color_theme("dark-blue")
    gui = GUI()
