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

    def __init__(self):
        super().__init__()
        self.config = GUICONFIG()
        self.button_state = self.config.work_state
        self.create_window()
        self.main()
    
    def create_window(self):
        self.title("Work Timer")
        self.geometry("740x200")
        self.resizable(True, True)

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
        self.start_stop_button.pack(padx=10, pady=10, side="left")
        self.create_excel_sheet.pack(padx=10, pady=10, side="right")
    
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
        if self.button_state:
            self.config.wh.stop()
            self.start_stop_button.configure(text="Start Working")
            self.button_state = not self.button_state
        
        TimeSheetGenerator.create_excel_sheet(
            self.config.time_log_dir,
            self.config.program_dir
        )

    def main(self):
        self.mainloop()


if __name__ == "__main__":
    ctk.set_default_color_theme("dark-blue")
    gui = GUI()
