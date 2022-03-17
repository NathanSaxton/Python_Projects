import shutil
import os
import time as tm
from datetime import *
import datetime as dt
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import threading        

    
class mainWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        
        #set variables that will be used later
        self.dailySet = False
        self.timer = None
        
        #window size and title
        self.master = master
        window = self.master
        window.minsize(500, 300)
        window.maxsize(500, 300)
        window.title("File Transfer")
        
        #label, entry, and directory for folder to be checked
        window.lbl_source = tk.Label(window, text = "Folder path to be checked:")
        window.lbl_source.grid(row = 0, column = 0,rowspan = 1, columnspan = 3, padx = (10,0), pady = (20,0), sticky = N+W)
        window.txt_source = tk.Entry(window)
        window.txt_source.insert(0, "./Folder_A/")
        window.txt_source.grid(row = 0, column = 4, rowspan = 1, columnspan = 6, padx = (10,0), pady = (20,0), sticky = N+S+W+E)
        window.btn_source = tk.Button(window, width = 10, height = 1, text = "Directory...", command = lambda: self.selectFolder(window.txt_source))
        window.btn_source.grid(row = 0, column = 10, rowspan = 1, columnspan = 2, padx = (10,0), pady = (20,0), sticky = W)

        #label, entry, and directory for folder destination
        window.lbl_destination = tk.Label(window, text = "Folder to recieve copies:")
        window.lbl_destination.grid(row = 2, column = 0,rowspan = 1, columnspan = 3, padx = (10,0), pady = (20,0), sticky = N+W)
        window.txt_destination = tk.Entry(window)
        window.txt_destination.insert(0, "./Folder_B/")
        window.txt_destination.grid(row = 2, column = 4, rowspan = 1, columnspan = 6, padx = (10,0), pady = (20,0), sticky = N+S+W+E)
        window.btn_destination = tk.Button(window, width = 10, height = 1, text = "Directory...", command = lambda: self.selectFolder(window.txt_destination))
        window.btn_destination.grid(row = 2, column = 10, rowspan = 1, columnspan = 2, padx = (10,0), pady = (20,0), sticky = W)

        #buttons to call the main functions
        window.btn_daily_transfer = tk.Button(window, width = 10, height = 2, text = "Set Daily Check", command = lambda: self.setDailyTransfer(True))
        window.btn_daily_transfer.grid(row = 4, column = 0, rowspan = 1, columnspan = 2, padx = (10,0), pady = (20,0), sticky = W+E)
        window.btn_transfer_now = tk.Button(window, width = 10, height = 2, text = "Check Files Now", command = lambda: self.dailyTransfer(False))
        window.btn_transfer_now.grid(row = 4, column = 3, rowspan = 1, columnspan = 6, padx = (10,0), pady = (20,0), sticky = W+E)
        window.btn_cancel_daily = tk.Button(window, width = 10, height = 2, text = "Cancel Daily Check", command = lambda: self.cancelDailyTransfer())
        window.btn_cancel_daily.grid(row = 4, column = 9, rowspan = 1, columnspan = 6, padx = (10,0), pady = (20,0), sticky = W+E)


    def setDailyTransfer(self, initialSet = False): #function used to set up the daily check for folders and to be looped daily
        if self.timer == None and self.dailySet == False: #initial iteration
            self.timer = threading.Timer(2, self.dailyTransfer) #sets timer for 24 hours to execute the dailyTransfer function
            self.dailySet = True
            self.timer.start()
            self.activeTimer = True
            self.dailyTransfer()
            messagebox.showinfo("Daily Check Set","Daily Check has been set.")
        elif self.timer != None and self.dailySet == True: #subsequential iterations
            if initialSet == True:
                messagebox.showinfo("Daily Check Set","You can only have one Daily Check set at a time.")
            else:
                self.timer.cancel()
                self.activeTimer = False
                self.timer = threading.Timer(2, self.dailyTransfer) #reset the timer for 24 hours
                self.timer.start()
                self.activeTimer = True


    def dailyTransfer(self, loop = True):#get the file paths and check if there are files modded between today and yesterday and copy it
        source = self.master.txt_source.get()
        destination = self.master.txt_destination.get()
        files = os.listdir(source)
        for i in files:
            timeStamp = os.path.getmtime(source+i)
            modTime = str(tm.strftime("%Y-%m-%d", tm.localtime(timeStamp)))
            today = str(date.today())
            yesterday = str(date.today() - timedelta(days=1))
            if modTime == yesterday or modTime == today:
                shutil.copy(source+i, destination)
            else: 
                continue
        if loop == True:#Loop back through if initiated by the daily loop
            self.setDailyTransfer()
        else:
            messagebox.showinfo("Transfer Complete","Files have been checked and copied if applicable.")


    def cancelDailyTransfer(self):#Stop and delete the loop
        if self.timer == None:
            messagebox.showinfo("Cancel request failed","Daily Check not set.")
        else:
            if self.timer.is_alive() == True:
                self.timer.cancel()
                self.timer = None
                self.dailySet = False
                messagebox.showinfo("Cancel request successful","Daily Check cancelled.")
            else:
                messagebox.showinfo("Cancel request failed","Daily Check not set.")

 
    def selectFolder(self, path): #Get the file path from the directory and apply it to the text boxes
        folder = str(tk.filedialog.askdirectory() + "/")
        path.delete(0,END)
        path.insert(0,folder)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = mainWindow(root)
    root.mainloop()


