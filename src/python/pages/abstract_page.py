import customtkinter as ctk
from .structures import Page
from abc import ABC, abstractmethod, abstractproperty



class Abstract_GUI(ctk.CTk, ABC):
    @abstractproperty
    def current_page(self) -> list:
        pass

    def __init__(self, start_page: Page) -> None:
        super().__init__()
        self.title("Work Timer")
        self.geometry("800x600")
        self.resizable(True, True)
    
    @abstractmethod
    def flush_page(self) -> None:
        pass

    @abstractmethod
    def change_page(self, page: Page) -> None:
        pass

    @abstractmethod
    def fill_page(self, page: Page) -> None:
        pass
