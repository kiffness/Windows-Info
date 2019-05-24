import tkinter as tk
from tkinter import ttk
from tkinter import Menu

large_font = ("Verdana", 16)

def hello():
    print("Hello")


class QueryMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)

        label = ttk.Label(self, text="Query Menu")
        label.grid(row=0)

        main_button = ttk.Button(self, text="Main Menu",
                                 command=lambda: controller.show_frame(MainMenu))
        main.button.grid(column=0, row=1)

        # TODO: add more buttons for the various script

class ScriptMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)
        label = ttk.Label(self, text="Script Menu")
        label.grid(row=0)

        main_button = ttk.Button(self, text="Main Menu",
                                 command=lambda: controller.show_frame(MainMenu))
        main.button.grid(column=0, row=1)

        # TODO: add more buttons for the various scripts

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(self, parent)

        label = ttk.Label(self, text="Main Menu", font=large_font)
        label.grid(row=0)

        script_button = ttk.Button(self, text="Scripts",
                                   command=lambda: controller.show_frame(ScriptMenu))
        script_button.grid(column=0, row=1)

        query_button = ttk.Button(self, text="Queries",
                                  command=lambda: controller.show_frame(QueryMenu))
        query_button.grid(column=1, row=1)

class MenuBar(Menu):
    """The MenuBar for our root Window"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        fileMenu = Menu(self, tearoff=False)
        self.add_cascade(label="File",underline=0, menu=fileMenu)
        fileMenu.add_command(label="Exit", underline=1, command=self.quit)


class Application(tk.Tk):
    """Main Window"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Windows Refresh Application")

        # Uncomment to not allow resizing
        # self.resizable(width=False, height=False)

        menubar = MenuBar(self)
        self.config(menu=menubar)

        ttk.Label(
            self,
            text="Windows Refresh Application",
            font=("TkDefualtFont", 16)
            ).grid(row=1)

        self.frames = {}

        container = ttk.Frame(self)
        container.grid(row=3, padx=10)

        for f in (MainMenu, ScriptMenu, QueryMenu):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=4)

        self.show_frame(MainMenu)
        
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


def main():
    app = Application()
    app.mainloop()

if __name__ == "__main__":
    main()