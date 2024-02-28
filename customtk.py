import datetime as dt
import os

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        """
        Constructor for custom tkinter. This is the main loop
        of the application.
        """
        super().__init__()

        # Config window:
        self.title("CustomTkinter work hours")
        self.geometry(f"{510}x{360}")

        # Add tabs
        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, sticky="nsew")
        self.tabview.add("Work Timer")
        self.tabview.tab("Work Timer").grid_columnconfigure((0, 1), weight=0)
        self.tabview.tab("Work Timer").grid_rowconfigure((0))

        self.tabview.add("Convert txt to xlsx")
        #self.tabview.tab("Convert txt to xlsx").grid_columnconfigure((0), weight=0)
        #self.tabview.tab("Convert txt to xlsx").grid_rowconfigure((0), weight=0)

        # sidebar start/stop:
        self.sidebar_frame = customtkinter.CTkFrame(self.tabview.tab("Work Timer"), width=250, height=305)
        self.sidebar_frame.grid(column=0, row=0, sticky="nsew")
        self.btn_start = customtkinter.CTkButton(self.sidebar_frame, width=250, height=150, text="Start", command=self.button_start)
        self.btn_start.pack(pady=5)
        self.btn_stop = customtkinter.CTkButton(self.sidebar_frame, width=250, height=150, text="Stop", command=self.button_stop)
        self.btn_stop.pack()

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self.tabview.tab("Work Timer"), width=250, height=305)
        self.textbox.grid(column=1, row=0, pady=(5, 0), sticky="nsew")
        self.textbox.configure(state="disabled")

        # Excel tab:
        self.frame_excel = customtkinter.CTkFrame(self.tabview.tab("Convert txt to xlsx"), width=500, height=305)
        self.frame_excel.grid(column=0, row=0, sticky="")

        self.option_menu_label = customtkinter.CTkLabel(self.tabview.tab("Convert txt to xlsx"), text="Choose months:")
        self.option_menu_label.grid(row=0, column=0, padx=0, pady=(10, 200))
        self.option_menu = customtkinter.CTkOptionMenu(self.tabview.tab("Convert txt to xlsx"), values=["Jan_Feb", "..."], command=None)
        self.option_menu.grid(row=0, column=0, padx=0, pady=(10, 125))

        self.btn_generate_xlsx_label = customtkinter.CTkLabel(self.tabview.tab("Convert txt to xlsx"), text="Generate excel file from the chosen months:")
        self.btn_generate_xlsx_label.grid(row=0, column=0, padx=0, pady=(100, 50))
        self.btn_generate_xlsx = customtkinter.CTkButton(self.tabview.tab("Convert txt to xlsx"), width=150, height=50, text="Generate xlsx file", command=None)
        self.btn_generate_xlsx.grid(row=0, column=0, padx=0, pady=(150, 0))

    def button_start(self):
        self._init_folder()  # Perhaps make split date an option

        now = str(dt.datetime.now())[:16]
        filename = "/" + now[:10] + ".txt"
        if not os.path.isfile(self.mypath + self.foldername + filename):
            with open(self.mypath + self.foldername + filename, 'w') as f:
                f.write('start ' + now)
            print("file created and timer started")
        else:
            with open(self.mypath + self.foldername + filename, 'r') as f:
                lines = f.readlines()
                if lines[-1][:5] == 'start':
                    raise Exception("You need to stop a timer first")

            with open(self.mypath + self.foldername + filename, "a") as f:
                f.write('\nstart ' + now)
                print('Timer started')

        self._insert_log_to_textbox(filename)

    def button_stop(self):
        self._init_folder()  # Perhaps make split date an option

        then = str(dt.datetime.now())[:16]
        filename = "/" + then[:10] + ".txt"
        if not os.path.isfile(self.mypath + self.foldername + filename):
            raise Exception("You need to start a timer first to create a file")
        else:
            with open(self.mypath + self.foldername + filename, 'r') as f:
                lines = f.readlines()
                if not lines[-1][:5] == 'start':
                    raise Exception("You need to start a timer first")

        with open(self.mypath + self.foldername + filename, "a") as f:
            f.write('\nstop ' + then)
            print('Timer stopped')

        self._insert_log_to_textbox(filename)

    def _init_folder(self) -> None:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        self.foldername = ""
        if dt.datetime.now().day <= 15:
            idx = dt.datetime.now().month - 1
            self.foldername += months[idx - 1]
            self.foldername += "_" + months[idx]
        else:
            idx = dt.datetime.now().month - 1
            self.foldername += months[idx]
            self.foldername += "_" + months[(idx + 1) % 12]

        self.mypath = ""
        if not os.path.isdir(self.mypath + self.foldername):
            os.makedirs(self.mypath + self.foldername)
            print("folder created")

    def _insert_log_to_textbox(self, filename) -> None:
        with open(self.mypath + self.foldername + filename, 'r') as f:
            _text = f.readlines()
            text = "".join(map(str, _text))
            self.textbox.configure(state="normal")
            self.textbox.delete("0.0", customtkinter.END)
            self.textbox.insert("0.0", text)
            self.textbox.configure(state="disabled")


if __name__ == "__main__":
    app = App()
    app.mainloop()
