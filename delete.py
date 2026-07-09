from tkinter import*

def func():
    #root=Tk()
    root = Toplevel()
    root.title("Library Management System")
    root.geometry("930x740+200+50")
    bg=PhotoImage(file='delete.png')
    label1=Label(root,image=bg)
    label1.place(x=0,y=0)
        
      
        

    e1=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e1.place(x=540,y=198)
    e2=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e2.place(x=540,y=252)
    e3=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e3.place(x=540,y=297)
    e4=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e4.place(x=540,y=343)
    e5=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e5.place(x=540,y=393)
    e6=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e6.place(x=540,y=444)
    e7=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e7.place(x=540,y=492)
    e8=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e8.place(x=540,y=567)
    e9=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e9.place(x=540,y=610)
    e10=Entry(root,font=("arial",10),borderwidth=1,relief="solid")
    e10.place(x=540,y=658)
    b1=Button(root,text="Search",width='15').place(x=730,y=194)
    b2=Button(root,text="Exit",width='15').place(x=515,y=705)
    b3=Button(root,text="Delete",width='15').place(x=655,y=705)
    b4=Button(root,text="Update",width='15').place(x=795,y=705)



    root.mainloop()

