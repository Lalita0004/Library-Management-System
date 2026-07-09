from tkinter import*
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(host='localhost',user='root',password='lalita',database="library")
cursor = conn.cursor()


def manage():
    global bg
    root=Toplevel()
    root.title("Library Management System")
    root.geometry("745x740")
    bg=PhotoImage(file='managestudent.png')
    label1=Label(root,image=bg)
    label1.place(x=0,y=0)
    e1=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e1.place(x=500,y=115)
    e2=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e2.place(x=500,y=180)
    e3=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e3.place(x=500,y=250)
    e4=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e4.place(x=500,y=325)
    e5=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e5.place(x=500,y=396)
    e6=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e6.place(x=500,y=470)
    e7=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e7.place(x=500,y=542)

    def saveButtonClick():
        query = f"INSERT INTO `library`.`student_detail` ( `name`, ` father's name`, `gender`, `course`, `contact`, ` email id`, `roll  no`) values('{e1.get()}','{e2.get()}','{e3.get()}','{e4.get()}','{e5.get()}','{e6.get()}','{e7.get()}')"
        cursor.execute(query)
        conn.commit()
        messagebox.showinfo("saved","data saved succesfully")
    
    b1=Button(root,text="Insert",width='15',command=saveButtonClick).place(x=140,y=600)
    b2=Button(root,text="Delete",width='15').place(x=270,y=600)
    b3=Button(root,text="Search",width='15').place(x=400,y=600)
    b4=Button(root,text="Update",width='15').place(x=530,y=600)
    root.mainloop()

