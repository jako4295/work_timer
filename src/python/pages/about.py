import customtkinter as ctk
from .abstract_page import Abstract_GUI
from .structures import Page


class About(Abstract_GUI):
    page = Page.ABOUT
    current_page = None

    def __init__(self,):
        super().__init__(start_page = self.page)
        self.fill_page(self.page)

    def flush_page(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()

    def change_page(self, page: Page) -> None:
        pass

    def fill_page(self, page: Page) -> None:
        self.test = ctk.CTkLabel(self, text="About")
        self.test.pack()
