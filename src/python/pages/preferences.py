import customtkinter as ctk


class PreferencesFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name: str="PreferencesFrame", **kwargs):
        super().__init__(*args, **kwargs)
        self.header_name = header_name
        self.header = ctk.CTkLabel(self, text=self.header_name)
        self.header.grid(row=0, column=0, padx=10, pady=10)
        
