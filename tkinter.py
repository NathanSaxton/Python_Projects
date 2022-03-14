import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title("I am the greatest")
        self.master.config(bg = "pink")










if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)

    root.mainloop()
