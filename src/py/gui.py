import customtkinter as ctk


def start():
    # Get data

    gui = GUI()
    gui.mainloop()


class GUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Work Timer")
        # self.geometry("800x450")
        self.resizable(True, True)

        # self.button = ctk.CTkButton(self, text="Click me!", command=self.click)
        # self.button.pack()

        

    def click(self):
        print("Clicked!")


if __name__ == "__main__":
    start()