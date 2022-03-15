from tkinter import *
import tkinter as tk
from tkinter import filedialog
import webbrowser
import os

class main(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        #create and title the window
        self.master = master
        window = self.master
        window.minsize(400,300)
        window.maxsize(400,300)
        window.title("Widget Challenge")
        
        #askdirectory button        
        window.btn = tk.Button(window,width=12,height=2,text="File...", command = lambda: tk.filedialog.askdirectory())
        window.btn.grid(row=1,column=0,padx=(10,10),pady=(10,10))

        #button and entry to update the webpage
        window.announcement = tk.Entry(window,text="")
        window.announcement.grid(row=1,column=2,rowspan=1,columnspan=3,padx=(10,10),pady=(10,10),sticky=N+E+W+S)
        window.web = tk.Button(window,width=12,height=2,text="Announcement",command = lambda: self.announce(window.announcement.get().strip()))
        window.web.grid(row=1,column=1,padx=(10,10),pady=(10,10))
        
    def announce(self,body):#function to create/edit the HTML file and open it in a new tab
        f=open("announcement.html", "w")
        f.write("<DOCTYPE!> \
                <html><body><h1> \
                "+ body +" \
                </h1></body></html> \
                ")
        f.close()
        webbrowser.open_new_tab(os.fspath("announcement.html"))


if __name__ == "__main__"
    root = tk.Tk()
    app = main(root)
    root.mainloop()
