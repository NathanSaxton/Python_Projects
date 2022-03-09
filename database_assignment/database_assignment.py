#Assignment to connect to a database. 
#imports sqlite3
import sqlite3
#file list to be read
fileList = ('information.docx','Hello.txt', 'myImage.png',\
            'myMovie.mpg','World.txt', 'data.pdf', 'myPhoto.jpg')
#connect to db
conn = sqlite3.connect("test.db")
#create the table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                file_name TEXT)")
    conn.commit()
#read through fileList 
for x in fileList:
    if x.endswith('.txt'): #fine the ones that end with .txt
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (x,))#add the selected files to the table
            print(x)#print the added files
conn.close()
