import tkinter as tk
from tkinter import *
import os
import sqlite3

def center_window(self,w,h):#use the tkinter frame reference the width and the height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2)-(w/2))
    y = int((screen_height/2)-(h/2))
    centerGeo=self.master.geometry('{}x{}+{}+{}'.format(w,h,x,y))
    return centerGeo

def ask_quit(self):#run if user tries to close the program, ask if they want to close
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

def create_db(self):
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_phonebook( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            );")
        conn.commit()
        first_run(self)

def first_run(self):
    data = ('John', 'Doe', 'John Doe', '111-111-111', 'jdoe@email.com')
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""", ('John','Doe','John Doe', '111-111-1111','jdoe@email.com'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
    count = cur.fetchone()[0]
    return cur, count

def onSelect(self,event):#select item on ListBox
    #event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT col_fname,col_lname,col_phone,col_email FROM tbl_phonebook WHERE col_fullname = (?)""", [Value])
        varBody = cur.fetchall()
        for data in varBody: #returns a tuple using data[] durint the iteration
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    #normalize the data so it's consistent in the database
    var_fname = var_fname.strip() #removes blank spaces before and after
    var_lname = var_lname.strip()
    var_fname = var_fname.title()#capitalizes the first character
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    print("var_fullname: {}".format(var_fullname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format.")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0): #forces the user to provide info in all areas
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            #check for existance of the fullname
            cur.execute("""SELECT COUNT(col_fullname) FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_fullname))
            count = cur.fetchone()[0]
            chkName = count
            if chkName == 0: #if there are 0 instances of the full name
                print("chkName: {}".format(chkName))
                cur.execute("""INSERT INTO tbl_phonebook (col_fname,col_lname,col_fullname,col_phone,col_email) VALUES (?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email))
                self.lstList1.insert(END, var_fullname)
                onClear(self)
            else:
                messagebox.showerror("Name Error","'{}' already exists in the database. Please use a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure there is data in all fields.")

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection())#the list box's selected value
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        #check to make sure there is at least one record in the db or an error will occur
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm - messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\n Proceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('phonebook.db')
                with conn:
                    cur = conn.cursor()
                    cur.execute("""DELETE FROM tbl_phonebook WHERE col_fullname = '{}'""".format(var_select))
                onDeleted(self) #clear all text boxes and the selected index of listbox
                onRefresh(self) #update changes
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error","({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()

def onDeleted(self): #clear text boxes from deleted items
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    onRefresh(self)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass
    
def onRefresh(self):#refreshes the listbox with the most up-to-date info on the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('phonebook.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT(*) FROM tbl_phonebook""")
        count = cur.fetchone()[0]
        i = 0
        while i < count:
            cur.execute("""SELECT col_fullname FROM tbl_phonebook""")
            varList = cur.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i+i
    conn.close()

def onClear(self):#clear all text boxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0]#index of the list selection
        var_value = self.lstList1.get(var_select)#selected item's value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    #user will only be allowed to update phone and email
    #name changes require the user to delete the entire record and create a new one
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    if(len(var_phone) > 0) and (len(var_email) > 0): #ensure data is in the text boxes
        conn = sqlite3.connect('phonebook.db')
        with conn:
            cur = conn.cursor()
            #check to see if changes are needed
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(col_email) FROM tbl_phonebook WHERE col_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0:#if changes need to be made proceed
                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for ({}). \n\n Proceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response:
                    conn = sqlite3.connect('phonebook.db')
                    with conn:
                        cur = conn.cursor()
                        cur.execute("""UPDATE tbl_phonebook set col_phone = '{}',col_email = '{}' WHERE col_fullname = '{}'""".format(var_phone,var_email,var_value))
                        onClear(self)
                    conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone,var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Plese select a name from the list. \nThen edit the phone or email information.")
    onClear(self)

    

if __name__ == "__main__":
    pass
