from tkinter import*
import managestudent
import searchbook
import issuebook
import returnbook
def librariandashb():
    
    global bg
    root=Toplevel()
    root.title("Library Manaagement System")
    root.geometry("990x1000")
    bg=PhotoImage(file='librariandash.png')
    label1=Label(root,image=bg)
    label1.place(x=0,y=0)
        
        
    def onclicklistner():
       managestudent.manage()
       
    def searchclicklistner():
       searchbook.search()
       
    def issueclicklistner():
       issuebook.issue()
       
    def returnclicklistner():
       returnbook.returnb()      
   

    b1=Button(root,text="Manage Student",width='15',command=onclicklistner).place(x=250,y=275)
    b2=Button(root,text="Search Book",width='15',command=searchclicklistner).place(x=440,y=275)
    b3=Button(root,text="Issue Book",width='15',command=issueclicklistner).place(x=625,y=275)
    b4=Button(root,text="Return Book",width='15',command=returnclicklistner).place(x=250,y=470)
    b5=Button(root,text="List of all issued Book",width='15').place(x=437,y=470)
    b6=Button(root,text="Fine",width='15').place(x=625,y=470)
    b7=Button(root,text="Help Desk",width='15').place(x=250,y=660)
    b8=Button(root,text="Software Developer",width='15').place(x=437,y=660)
    

        

