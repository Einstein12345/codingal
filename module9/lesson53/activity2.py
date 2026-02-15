from tkinter import *
from tkinter import messagebox
root = Tk()
root.title('image Tilte')
root.geometry('400x400')

def message():
    messagebox.showwarning("allert","stop.virus found")

button=Button(root,text="scan for virus",command=message)
button.place(x=40,y=80)
root.mainloop()