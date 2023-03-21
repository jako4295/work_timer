import customtkinter as ctk


class GUI(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Hello World")
        self.geometry("740x500")
        self.resizable(True, True)
        self.button = ctk.CTkButton(
            self, text="Hello World", command=self.click
        )
        self.button.pack()
        self.mainloop()
    
    def click(self) -> None:
        print("Hello World")


if __name__ == "__main__":
    gui = GUI()