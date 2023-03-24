import customtkinter as ctk
from .structures import Page
from abc import ABC, abstractmethod, abstractproperty



class Abstract_GUI(ctk.CTk, ABC):
    x_size: int = None
    y_size: int = None
    x_pad_percent: float = 0.05
    y_pad_percent: float = 0.02
    x_size: int = 1200
    y_size: int = 1000

    button_font_size: int = None
    text_font_size: int = None

    @abstractproperty
    def current_page(self) -> list:
        pass

    def __init__(self, start_page: Page) -> None:
        super().__init__()
        self.title("Work Timer")
        self.geometry(f"{self.x_size}x{self.y_size}")
        self.resizable(False, False)

        self.button_font_size = int(max(self.x_size, self.y_size) / 25)
        self.text_font_size = int(max(self.x_size, self.y_size) / 35)

    
    @abstractmethod
    def flush_page(self) -> None:
        pass

    @abstractmethod
    def change_page(self, page: Page) -> None:
        pass

    @abstractmethod
    def fill_page(self,) -> None:
        pass
