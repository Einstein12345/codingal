from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('main Tilte')
root.geometry('400x400')

def topwindow():
    top=Toplevel()
    top.geometry("180x100")
    top.title("top level")
    l2=Label(top,text="this is top level window")
    l2.pack()
button=Button(root,text="click here",command=topwindow)
button.pack()
root.mainloop()