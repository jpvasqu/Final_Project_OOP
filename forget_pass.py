from tkinter import *
from tkinter import messagebox

import mysql.connector
class forgotpass:
    def __init__(self):
        
        self.frm_forget=Frame(width=380,height=340,background="white")
        self.frm_forget.place(x=225,y=65)

        self.lbl_forget=Label(master=self.frm_forget,text="Find Account",font=("Goudy Old Style",20),bg="white",cursor="cross")
        self.lbl_forget.place(x=110,y=10)
        self.ent_email=Entry(master=self.frm_forget,width=30,font=("Arial",10),
                        border=2)
       
        #BINDING EMAIL
        def on_click(e):
            self.ent_email.delete(0,END)

        def off_click(e):
            name=self.ent_email.get()
            if name == "":
                self.ent_email.insert(0,"Email:")

        self.ent_email.place(x=70,y=100)
        self.ent_email.insert(0,"Email:")
        self.ent_email.bind('<FocusIn>',on_click)
        self.ent_email.bind('<FocusOut>',off_click)

        self.btn_info=Button(master=self.frm_forget,text="Find Account",command=self.find)
        self.btn_info.place(x=150,y=160)

        btn_back=Button(master=self.frm_forget,width=10,text="Back",command=self.back)
        btn_back.place(x=150,y=200)
    def find(self):
        
        email=self.ent_email.get()
        self.data= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='forecast'
                    )
        mycursor=self.data.cursor()
        sql="select * from data where email=%s or email=%s"
        var=(email,email)
        mycursor.execute(sql,var)
        result=mycursor.fetchone()

        if result != None:
            lbl_pass=Label(master=self.frm_forget,text="Change Password",font=("Goudy Old Style",20),bg="white",cursor="cross")
            lbl_pass.place(x=110,y=10)
            self.ent_pass=Entry(master=self.frm_forget,width=30,font=("Arial",10),
                            border=2)
    
            
            #BINDING EMAIL
            def on_click(e):
                self.ent_pass.delete(0,END)
            def off_click(e):
                name=self.ent_pass.get()
                if name=="":
                    self.ent_email.insert(0,"Change Password:")

            self.ent_pass.place(x=70,y=100)
            self.ent_pass.insert(0,"Change Password:")
            self.ent_pass.bind('<FocusIn>',on_click)
            self.ent_pass.bind('<FocusOut>',off_click)

            btn_info=Button(master=self.frm_forget,text="Change Password",command=self.change_password)
            btn_info.place(x=150,y=160)
            

        else:
            messagebox.showerror(title="Invalid choy",message=" Account can't find ") 
    def back(self):
        self.frm_forget.destroy() 
    def change_password(self):
        self.data= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='forecast'
                    )
        mycursor=self.data.cursor()
        p = self.ent_pass.get()
        e = self.ent_email.get()
       
        sql="UPDATE  data SET user_password = %s WHERE email = %s"
        var=(p,e)
        mycursor.execute(sql,var)
        self.data.commit()
        
        
        messagebox.showinfo(title="Invalid choy",message="Done")
        self.frm_forget.destroy()
       
        
        
        
