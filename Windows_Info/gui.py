import tkinter as tk
from tkinter import ttk
from tkinter import Menu

import misc_func
import db

LARGE_FONT= ("Verdana", 12)



class AllWidgets(tk.Frame):
    """A class for all my widgets"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)


        # Script Menu section 
        script_menu = tk.LabelFrame(self, text="PowerShell",
                                    font=("TkDefualtFont", 14))
        description_label = tk.Label(script_menu, text="Button Descriptions\nRefresh runs a script to refresh all the computer names\n" + 
                                     "Add runs the script that gets the info about a computer and the adds it to the database")

        # All Buttons for Powershell menu
        refresh_bt = ttk.Button(script_menu,
                                text="Refresh",
                                command=misc_func.refresh_list).grid(row=1, column=1)
        add_bt = ttk.Button(script_menu,
                            text="Add",
                            command=misc_func.powershell).grid(row=1, column=3)

        

        script_menu.grid(row=0, column=0, sticky=tk.W + tk.E)
        description_label.grid(row=0, columnspan=5)


class MenuBar(Menu):
    """The MenuBar for our root Window"""
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.title("Windows Refresh Application")
        
        # Uncomment to dis-allow resizing
        # self.resizable(width=False, height=False)

        ttk.Label(
            self,
            text="Windows Refresh Application",
            font=("TkDefualtFont", 16)
            ).grid(row=0, columnspan=5, padx=5, pady=5)

        self.widgets = AllWidgets(self)
        self.widgets.grid(row=1)

        
        

def main():
    db.connect()
    app = Application()
    app.mainloop()
    db.close()

if __name__ == "__main__":
    main()