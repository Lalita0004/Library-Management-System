from tkinter import *
from tkinter import messagebox
import login
import login2


root = Tk()
root.title("Library Manaagement System")
root.geometry("822x488")
img = PhotoImage(file="login.png")
bg_image = Label(root, image=img).place(x=0, y=0)

def adminBtnClick():

    login.func6()
loginBtn = Button(root,text= "adminlogin",command=adminBtnClick)
loginBtn.place(x=490, y=345)
def staffBtnClick():
    login2.func6()
newBtn = Button(root,text= "librarianlogin",command=staffBtnClick)
newBtn.place(x=253, y=345)

root.mainloop()