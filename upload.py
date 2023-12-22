from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import mysql.connector
class ups:
    def __init__(self,user):
        self.frm_upload=Frame(width=380,height=340,background="white")
        self.frm_upload.place(x=225,y=65)
        btn_lbl=Button(master=self.frm_upload,text="Upload a Profile \nPicture to create your account",
                            font=("Goudy Old Style",15),background="white",
                            border=0)
        btn_lbl.place(x=70,y=100)
        btn_profile = Button(self.frm_upload,text='Upload',font=("Alkatra",15),bg="#7be1e8",fg="#0347ad",border=0,width=15,activebackground="white", command = lambda:upload_file()) 
        btn_profile.place(x=110,y=200)

        def upload_file():
            data= mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='forecast'
                    )
            mycursor=data.cursor()
            global img
            f_types = [('Jpg Files', '*.jpg')]
            filename = filedialog.askopenfilename(filetypes=f_types)
            img = ImageTk.PhotoImage(file=filename)
            print(filename)
            sql="update data set post=%s where user_name=%s"
            var=(filename,user)
            mycursor=data.cursor()
            mycursor.execute(sql,var)
            data.commit()
            self.frm_upload.destroy()
if __name__ == '__main__':
    main=Tk()
    width = 800 
    height = 480

    screen_width = main.winfo_screenwidth()
    screen_height = main.winfo_screenheight()


    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    main.geometry('%dx%d+%d+%d' % (width, height, x, y))

    ups("pol")
    mainloop()        

