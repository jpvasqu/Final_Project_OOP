import tkinter as tk
from tkinter import messagebox 
import mysql.connector
from PIL import Image, ImageTk

class user:
    def __init__(self,name):
        self.frm_search=tk.Frame(width=600,height=400,bg="#a6a5a4",)
        self.frm_search.place(x=100,y=70)

        self.data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
        )
        cursor = self.data.cursor()
        cursor.execute("use  forecast")
        mycursor=self.data.cursor()
        sql="select * from data where user_name = %s or user_name = %s"
        var=(name,name)
        mycursor.execute(sql,var)
        result=mycursor.fetchone()
        print(result[2])

        #Profile
        frm_profile=tk.Frame(master=self.frm_search,width=550,height=550,)
        frm_profile.place(x=230,y=30)
        sql="SELECT post from data where user_name=%s or  user_password=%s"
        var=(name,'123')
        cursor.execute(sql,var)
        prof=cursor.fetchone()
        print("Unsa Ni:",prof[0])
        
        image = Image.open(prof[0])

        # Resize the image using resize() method
        resize_image = image.resize((150, 150))

        img = ImageTk.PhotoImage(resize_image)

        # create label and add resize image
        label1 = tk.Label(master=frm_profile,image=img)
        label1.image = img
        label1.pack()




        #Label
        move_down=190
        left=190
        post_color="#a6a5a4"

        lbl_name=tk.Label(self.frm_search,text=f"NAME: {result[1]}",font=("times new romans",13),background=post_color)
        lbl_name.place(x=left,y=move_down)

        lbl_email=tk.Label(self.frm_search,text=f"Email: {result[3]}",font=("times new romans",13),background=post_color)
        lbl_email.place(x=left,y=move_down+40)

        lbl_address=tk.Label(self.frm_search,text=f"ADDRESS: {result[4]}",font=("times new romans",13),background=post_color)
        lbl_address.place(x=left,y=move_down+80)

        lbl_address=tk.Label(self.frm_search,text=f"BIRTH YEAR: {result[6]}",font=("times new romans",13),background=post_color)
        lbl_address.place(x=left,y=move_down+120)

        btn_up_profile = tk.Button(self.frm_search, text='Back to my Profile', font=("times new romans",13), width=15,command=self.back) 
        btn_up_profile.place(x=240,y=340)
    def back(self):
        self.frm_search.destroy()
  

