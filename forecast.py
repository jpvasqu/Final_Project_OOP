import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from tkinter import messagebox 
import mysql.connector
from PIL import Image, ImageTk


class app:
    def __init__(self,user):
        self.current_user=user
        self.main=tk.Tk()

        self.photo =ImageTk.PhotoImage(Image.open("python\Final\800px-Riga_(33844464828).jpg"))
        self.frm_main=tk.Frame(self.main,width=800,height=480,background="black")
        self.lbl_bg=tk.Label(self.frm_main,image=self.photo)
        self.frm_main.pack()
        self.lbl_bg.pack()
        self.main.title("Log In")
        width = 800 
        height = 480
        self.main.title("Barangay Information")
        photo = ImageTk.PhotoImage(file = "python\Final\icon.jpg")
        self.main.iconphoto(False, photo)
        screen_width = self.main.winfo_screenwidth()
        screen_height = self.main.winfo_screenheight()


        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)

        self.main.geometry('%dx%d+%d+%d' % (width, height, x, y))


        self.data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
        )
        cursor = self.data.cursor()

        cursor.execute("use forecast")
        self.data.commit()
        cursor.execute("SELECT distinct(user_name) as class FROM data")

        myresult = cursor.fetchall()
        print(myresult)

        
        
        en_entry=tk.Entry(master=self.main,font=("times new romans",13),width=40)
        en_entry.place(x=120,y=35) 


        

        #frames of post
        post_color="white"
        frm_post=tk.Frame(master=self.main,width=600,height=400,bg=post_color)
        frm_post.place(x=100,y=70)

        #frame profile pic
        frm_profile=tk.Frame(master=frm_post,width=550,height=550,)
        frm_profile.place(x=230,y=30)
        sql="SELECT post from data where user_name=%s or  user_password=%s"
        var=(self.current_user,'123')
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

        #INFORMATION DETAILS
        
        self.data = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = ''
        )
        cursor = self.data.cursor()
        cursor.execute("use  forecast")
        mycursor=self.data.cursor()
        sql="select * from data where user_name = %s or user_name = %s"
        var=(self.current_user,self.current_user)
        mycursor.execute(sql,var)
        result=mycursor.fetchone()
        user_name=result[1]
        self.user_email=result[3]

        move_down=270
        left=200
        lbl_name=tk.Label(master=frm_post,text=f"NAME: {user_name}",font=("times new romans",13),background=post_color)
        lbl_name.place(x=left,y=move_down)

        lbl_address=tk.Label(master=frm_post,text=f"ADDRESS: {result[4]}",font=("times new romans",13),background=post_color)
        lbl_address.place(x=left,y=move_down+40)

        lbl_address=tk.Label(master=frm_post,text=f"BIRTH YEAR: {result[6]}",font=("times new romans",13),background=post_color)
        lbl_address.place(x=left,y=move_down+80)


        
        def search():
            name=en_entry.get()
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
            

            
            en_entry.delete(0,tk.END)
            if name == self.current_user:
                 messagebox.showerror(title="Warning",message="Can't search your own info")
            if  result == None:
                 messagebox.showerror(title="Warning",message="Account does not exist" )
            else:
                import info
                info.user(name)
            

           
        
        
        #Buttons
        submit_button = tk.Button(self.main, text='Search', command=search,font=("times new romans",13)) 
        submit_button.place(x=490,y=33) 

        out_button = tk.Button(self.main, text='Log out',bg="red",font=("times new romans",13),command=self.out) 
        out_button.place(x=560,y=33) 

        btn_up_profile = tk.Button(self.main, text='Update Profile', font=("times new romans",13), width=15,command=self.update_pro) 
        btn_up_profile.place(x=335,y=260)

        btn_up_profile = tk.Button(self.main, text='Delete Info', font=("times new romans",13),background="red",activebackground="white", width=15,command=self.delete) 
        btn_up_profile.place(x=335,y=300)


        self.main.mainloop()
    def update_pro(self):
            self.main.destroy()
            import update
            update.edit(self.current_user)
    def out(self):
        self.main.destroy() 
        import Log_in_app
        Log_in_app.mygui()   
    def delete(self):
        
        msg=messagebox.askokcancel(message="Are you sure you want to delete your info?",icon='warning')
        if msg=='yes':
            print(self.current_user)
            self.data = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = ''
            )
            cursor = self.data.cursor()
            cursor.execute("use  forecast")
            mycursor=self.data.cursor()
            
            sql="delete from data where user_name= %s and email= %s"
            var=(self.current_user,self.user_email)
            mycursor.execute(sql,var)
            self.data.commit()
            print(type(self.current_user), type(self.user_email))
            self.main.destroy() 
            import Log_in_app
            Log_in_app.mygui() 

       
      


                  
    

if __name__ == '__main__':
     
        app('john')