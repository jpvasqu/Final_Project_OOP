import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
import mysql.connector
from PIL import Image, ImageTk
import subprocess

def edit(name):
    root=tk.Tk()

    width=400
    height=200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    data = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
    )
    cursor = data.cursor()
    cursor.execute("use  forecast")
    mycursor=data.cursor()
    sql="select * from data where user_name = %s or user_name = %s"
    var=(name,name)
    mycursor.execute(sql,var)
    result=mycursor.fetchone()
    print(result[2])


    fullname = tk.Label(root, text="Full Name")
    fullname.grid(row=1, column=0)
    fullname = tk.Entry(root,width=30)
    fullname.grid(row=1, column=1)
    fullname.insert(0,result[1])

    password = tk.Label(root, text="Password")
    password.grid(row=2, column=0)
    password = tk.Entry(root,width=30)
    password.grid(row=2, column=1)
    password.insert(0,result[2])

    email = tk.Label(root, text="Email")
    email.grid(row=3, column=0)
    email = tk.Entry(root,width=30)
    email.grid(row=3, column=1)
    email.insert(0,result[3])

    address = tk.Label(root, text="Address")
    address.grid(row=4, column=0)
    address = tk.Entry(root,width=30)
    address.grid(row=4, column=1)
    address.insert(0,result[4])

    birth = tk.Label(root, text="Birth Year")
    birth.grid(row=5, column=0)
    birth = tk.Entry(root,width=30)
    birth.grid(row=5, column=1)
    birth.insert(0,result[6])

    

    def submit():

        data= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='forecast'
                    )
        mycursor=data.cursor()
        sql="update data set user_name=%s,user_password=%s,email=%s,address=%s,birth=%s where user_name=%s"
        var=(fullname.get(),password.get(),email.get(),address.get(),birth.get(),name)
        mycursor=data.cursor()
        mycursor.execute(sql,var)
        data.commit()
        
        root.destroy()
        import Log_in_app
        Log_in_app.mygui()

    def upload_file():
        
        global img
        f_types = [('Jpg Files', '*.jpg')]
        filename = filedialog.askopenfilename(filetypes=f_types)
        img = ImageTk.PhotoImage(file=filename)
        print(filename)
        sql="update data set post=%s where user_name=%s"
        var=(filename,fullname.get())
        mycursor=data.cursor()
        mycursor.execute(sql,var)
        data.commit()

    btn_submit=tk.Button(root, text="Update Data", command=submit)
    btn_submit.grid(row=6,column=0)
    btn_profile = tk.Button(root, text='Update Profile Picture', command = lambda:upload_file()) 
    btn_profile.grid(row=6,column=1) 

    root.mainloop()
if __name__ == '__main__':
    edit("John")