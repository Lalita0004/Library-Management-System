from tkinter import*
from tkinter import messagebox

import librariandash
import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='lalita',database="library")
cursor = conn.cursor()

def func6():
    root=Toplevel()

    root.title("Library Management System")
    root.geometry("650x500")
    bg=PhotoImage(file='login2.png')
    label1=Label(root,image=bg)
    label1.place(x=0,y=0)

    def onclicklistner():
        cursor.execute(f"select * from library.librarian_detail where username='{e1.get()}' and password='{e2.get()}'")
        row = cursor.fetchone()
        if row is not None:
            librariandash.librariandashb()
        else:
            messagebox.showinfo("Error", "Incorrect username or password")

    e1=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e1.place(x=270,y=210)
    e2=Entry(root,font=("arial",10),borderwidth=1,relief="solid", show="*")
    e2.place(x=270,y=270)
    b1=Button(root,text="Login",width='15',command=onclicklistner).place(x=276,y=340)
    b1=Button(root,text="Forget Password",width='15').place(x=420,y=341)

    root.mainloop()