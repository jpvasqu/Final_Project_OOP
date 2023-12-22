import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector

class mygui:
    def __init__(self):
        self.data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
        )

        cursor = self.data.cursor()

        cursor.execute("show databases like %s", ("forecast",))
        result = cursor.fetchone()

        if result is None:

            cursor.execute("create database  forecast")
            cursor.execute("use forecast")
            cursor.execute("create table data(id int not null primary key auto_increment,user_name varchar(30),user_password varchar(30),email varchar(30),address varchar(100),post varchar(100), birth varchar(100), time  timestamp)")
            self.data.commit()
            
        else:
            cursor.execute("use forecast")
            self.data.commit()

        self.main=tk.Tk()
        self.main.title("Barangay Information")
        photo = ImageTk.PhotoImage(file = "python\Final\icon.jpg")
        self.main.iconphoto(False, photo)
        width = 800 
        height = 480
        
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()
        

        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
        
        self.main.geometry('%dx%d+%d+%d' % (width, height, x, y))

        self.main.config(bg="white")
        self.main.resizable(False,False)

        self.photo =ImageTk.PhotoImage(Image.open("python\Final\800px-Riga_(33844464828).jpg"))
        self.frm_main=tk.Frame(width=854,height=480,background="black")
        self.lbl_bg=tk.Label(self.frm_main,image=self.photo)
        
        
        self.frm_main.pack()
        self.lbl_bg.pack()

        #BINDING THE ENTRY USER
        def on_click(e):
            self.ent_name.delete(0,tk.END)

        def off_click(e):
             name=self.ent_name.get()
             if name=="":
                self.ent_name.insert(0,"User Name:")

        #BINDING THE ENTRY PASSWORD
        def on_click_pass(e):
            self.ent_password.delete(0,tk.END)
            self.ent_password.config(show="*")

        def off_click_pass(e):
             psw=self.ent_password.get()
             if psw=="":
                self.ent_password.config(show="")
                self.ent_password.insert(0,"Password:")


            

        #FRAME FOR SIGN IN
        self.frm_log=tk.Frame(master=self.frm_main,width=380,height=340,background="white")
        self.frm_log.place(x=225,y=65)

        #USER NAME ENRTY
        lbl_sign=tk.Label(master=self.frm_log,text="Sign In",font=("Goudy Old Style",20),bg="white",cursor="cross")
        self.ent_name=tk.Entry(master=self.frm_log,width=30,font=("Goudy Old Style",15),border=0)
        self.ent_password=tk.Entry(master=self.frm_log,width=30,font=("Goudy Old Style",15),border=0)
        
        lbl_sign.place(x=150,y=10)
        

        #POSSITION AND MORE
        self.ent_name.place(x=20,y=70)
        self.ent_name.insert(0,"User name:")
        self.ent_name.bind('<FocusIn>',on_click)
        self.ent_name.bind('<FocusOut>',off_click)
        tk.Frame(self.frm_log,width=315,height=2,background='black').place(x=20,y=94)

        
        self.ent_password.place(x=20,y=120)
        self.ent_password.insert(0,"Password:")
        self.ent_password.bind('<FocusIn>',on_click_pass)
        self.ent_password.bind('<FocusOut>',off_click_pass)
        tk.Frame(self.frm_log,width=315,height=2,background='black').place(x=20,y=145)
        
        #BUTTONS
        btn_signin=tk.Button(master=self.frm_log,text="Sign In",font=("Alkatra",15),
                             bg="#7be1e8",fg="#0347ad",border=0,width=15,activebackground="white",cursor='hand2',command=self.sign)
        btn_signin.place(x=109,y=160)

        lbl_create=tk.Label(master=self.frm_log,text="Don't have any account?",
                            font=("Goudy Old Style",11),bg='white')
        lbl_create.place(x=110,y=225)

        btn_yes=tk.Button(master=self.frm_log,text="YES",font=("Alkatra",8),bg="white",
                          fg="#0347ad",cursor="hand2",border=0,activebackground="white",command=self.create_account)
        btn_yes.place(x=256,y=228)


        btn_forget=tk.Button(master=self.frm_log,text="Forget Password?",font=("Alkatra",11),bg="white",fg="#0347ad",cursor="hand2",
                             border=0,activebackground="white",command=self.forgot)
        btn_forget.place(x=135,y=200)
        
        self.btn_show=tk.Button(master=self.frm_log,text="Show",font=("Alkatra",11),bg="white",fg="Black",cursor="hand2",border=0,activebackground="white",command=self.show_password)
        self.btn_show.place(x=290,y=115)
        self.main.mainloop()
        
    def forgot(self):
        import forget_pass
        forget_pass.forgotpass()
    def sign(self):
        user=self.ent_name.get()
        passowrd=self.ent_password.get()

        mycursor=self.data.cursor()
        sql="select * from  data where user_name=%s and user_password=%s"
        var=(user,passowrd)
        mycursor.execute(sql,var)
        result=mycursor.fetchone()

        if result != None:
            self.main.destroy()
            import forecast
            forecast.app(user)
        else:
            messagebox.showerror(title="Invalid choy",message="Invalid User Name Or Password")
    def create_account(self):

        
        import Create_account
        Create_account.create()
        
      
    def show_password(self):
        if  self.btn_show["text"]=="Show":
             self.ent_password.config(show="")
             self.btn_show.config(text="Hide")

        else:
             self.ent_password.config(show="*")
             self.btn_show.config(text="Show")
if __name__ == "__main__":   
    mygui()