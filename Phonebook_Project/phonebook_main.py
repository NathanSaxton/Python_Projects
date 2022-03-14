"""
Python version 3.10

Author: Nathan Saxton

Purpose: Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
         using Tkinter parent and child relatiionships. 

Tested OS: This was written to work with Windows 10
"""

import tkinter as tk
from tkinter import *

#import other modules we will be using
import phonebook_gui
import phonebook_func


class ParentWindow(Frame):
    def __init__(self, master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        #define master frame config
        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)
        #center app on user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title("Phonebook Demo using Tkinter")
        self.master.configure(bg="lightgray")
        #method to close the window using the x
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master
        #load GUI widgets from other module
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk()
    app = ParentWindow(root)
    root.mainloop()
