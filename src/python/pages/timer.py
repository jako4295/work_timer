from .abstract_page import Abstract_GUI
from .structures import Page
import os


class Timer(Abstract_GUI):
    page = Page.TIMER
    current_page = None

    def __init__(self) -> None:
        super().__init__(start_page=self.page)

    def flush_page(self) -> None:
        pass

    def change_page(self, page: Page) -> None:
        pass

    def fill_page(self, page: Page) -> None:
        pass

