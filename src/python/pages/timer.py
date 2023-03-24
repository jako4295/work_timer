from .abstract_page import Abstract_GUI
import customtkinter as ctk
from .structures import Page
import os


class Timer(Abstract_GUI):
    page = Page.TIMER
    current_page = None

    def __init__(self) -> None:
        super().__init__(start_page=self.page)
        self.fill_page()

    def flush_page(self) -> None:
        print(self.winfo_children())

    def change_page(self, page: Page) -> None:
        self.page = page
        self.flush_page()
        
        if page == Page.PREFERENCES:
            from .preferences import Preferences
            self.current_page = Preferences()
        elif page == Page.ABOUT:
            from .about import About
            self.current_page = About()
        

    def fill_page(self,) -> None:
        self._create_grids()
        self._create_things()
        self._pack_things()
    
    def update_log(self, update: str) -> None:
        self.daily_log.insert("end", update)

    def start_stop_timer(self) -> None:
        self.update_log("Start/Stop Timer\n")
    
    def create_excel(self) -> None:
        self.update_log("Create Excel\n")

    def preferences(self) -> None:
        self.change_page(Page.PREFERENCES)
    
    def about(self) -> None:
        self.change_page(Page.ABOUT)
    
    def _create_grids(self,):
        self.timers_text_frame = ctk.CTkFrame(self)
        self.other_pages_frame = ctk.CTkFrame(self)

        self.timers_text_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )
        self.other_pages_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            pady=int(self.y_size * self.y_pad_percent * 0.1),
        )

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=10)
        self.grid_rowconfigure(1, weight=1)

        self.timers_text_frame.grid_columnconfigure(0, weight=4)
        self.timers_text_frame.grid_columnconfigure(1, weight=1)
        self.timers_text_frame.grid_columnconfigure(2, weight=4)
        self.timers_text_frame.grid_rowconfigure(0, weight=1)
        self.timers_text_frame.grid_rowconfigure(1, weight=20)

        self.other_pages_frame.grid_columnconfigure(0, weight=1)
        self.other_pages_frame.grid_columnconfigure(1, weight=1)

    def _create_things(self):
        self.start_stop_button = ctk.CTkButton(
            self.timers_text_frame,
            text="Start/Stop Timer",
            command=self.start_stop_timer,
            font=("Arial", self.button_font_size),
        )

        self.create_excel_sheet = ctk.CTkButton(
            self.timers_text_frame,
            text="Create Excel",
            command=self.create_excel,
            font=("Arial", self.button_font_size),
        )

        self.daily_log = ctk.CTkTextbox(
            self.timers_text_frame,
            font=("Arial", self.text_font_size),
        )

        self.about_button = ctk.CTkButton(
            self.other_pages_frame,
            text="About",
            command=self.about,
            font=("Arial", self.button_font_size),
        )

        self.preferences_button = ctk.CTkButton(
            self.other_pages_frame,
            text="Preferences",
            command=self.preferences,
            font=("Arial", self.button_font_size),
        )
    
    def _pack_things(self):
        self.start_stop_button.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=int(self.x_size * self.x_pad_percent),
            pady=int(self.y_size * self.y_pad_percent),
        )

        self.create_excel_sheet.grid(
            row=0,
            column=2,
            sticky="nsew",
            padx=int(self.x_size * self.x_pad_percent),
            pady=int(self.y_size * self.y_pad_percent),
        )

        self.daily_log.grid(
            row=1,
            column=0,
            columnspan=3,
            sticky="nsew",
            padx=int(self.x_size * self.x_pad_percent),
            pady=int(self.y_size * self.y_pad_percent),
        )

        self.about_button.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=int(self.x_size * self.x_pad_percent),
            pady=int(self.y_size * self.y_pad_percent),
        )

        self.preferences_button.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=int(self.x_size * self.x_pad_percent),
            pady=int(self.y_size * self.y_pad_percent),
        )
