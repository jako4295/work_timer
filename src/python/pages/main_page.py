import customtkinter as ctk
from .structures import Page
from .about import AboutFrame
from .preferences import PreferencesFrame
from .timer import TimerFrame


class WindowVars(object):
    font_size: int = 24
    default_font: tuple = ("Arial", font_size)


class MainWindow(ctk.CTk):
    current_page: Page = None
    frame: ctk.CTkFrame = None

    x_size: int = 1200
    x_pad_button: int = None
    x_pad_text: int = None

    y_size: int = 800
    y_pad_button: int = None
    y_pad_text: int = None

    def __init__(self, start_page: Page) -> None:
        super().__init__()
        self.current_page = start_page
        
        self.x_pad_button = int(0.02 * self.x_size)
        self.x_pad_text = int(0.05 * self.x_size)

        self.y_pad_button = int(0.02 * self.y_size)
        self.y_pad_text = int(0.05 * self.y_size)

        self.title("Work Timer")
        self.geometry(f"{self.x_size}x{self.y_size}")
        self.resizable(False, False)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)
        self.grid_columnconfigure(0, weight=1)

        self.dropdown_frame = ctk.CTkFrame(self)
        self.dropdown_frame.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        self.dropdown_var = ctk.StringVar(value=self.current_page.name.title())
        self.page_dropdown = ctk.CTkComboBox(
            self.dropdown_frame,
            values=[page.name.title() for page in Page if page != Page.MAINPAGE],
            variable=self.dropdown_var,
            command=self.change_page,
            state="readonly",
            font=WindowVars.default_font,
            dropdown_font=WindowVars.default_font,
        )
        self.page_dropdown.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=self.x_pad_button,
            pady=self.y_pad_button,
        )

        self.run_frame()

    def run_frame(self,) -> None:
        if self.current_page == Page.TIMER:
            self.frame = TimerFrame(self)
        elif self.current_page == Page.PREFERENCES:
            self.frame = PreferencesFrame(self)
        elif self.current_page == Page.ABOUT:
            self.frame = AboutFrame(self)
        else:
            raise ValueError("Invalid page")
        
        self.frame.grid(row=1, column=0, sticky="nsew")

    def change_page(self, page_name: str) -> None:
        print(page_name)
