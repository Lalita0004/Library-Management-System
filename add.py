from tkinter import*
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='lalita',database="library")
cursor = conn.cursor()

def addb():
    global bg
    root=Toplevel()
    root.title("Library Management System")
    root.geometry("725x730")
    bg=PhotoImage(file='add.png')
    label1=Label(root,image=bg)
    label1.place(x=0,y=0)
    e1=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e1.place(x=500,y=177)
    e2=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e2.place(x=500,y=223)
    e3=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e3.place(x=500,y=265)
    e4=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e4.place(x=500,y=312)
    e5=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e5.place(x=500,y=360)
    e6=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e6.place(x=500,y=406)
    e7=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e7.place(x=500,y=522)
    e8=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e8.place(x=500,y=567)
    e9=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e9.place(x=500,y=615)
    
    def saveButtonClick():
        query = f"insert into librarian_detail(fullname,gender,dob,email,phoneno,address,username,password,confirmpassword) values('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}','{e7.get()}','{e8.get()}','{e9.get()}')"
        cursor.execute(query)
        conn.commit()
        
        messagebox.showinfo('done','saved!')
        
        
        
    b1=Button(root,text="save",width='15',command=saveButtonClick).place(x=530,y=670)
    root.mainloop()
