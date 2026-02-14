import tkinter as tk
# Create the GUI application main Window
window = tk.Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300') # 'width x height'
# Label
greeting = tk.Label(text="Hello User", fg='black', bg='white')
# Button
button = tk.Button(text="Click here", bg='green', fg='red')
# Entry
entry = tk.Entry(fg="yellow", bg="blue", width=50)
# here we have the widgets :lable,button,entry.
# Pack widgets
greeting.pack()
button.pack()
entry.pack()
# Frame
frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
frame.pack()
# Label inside frame
label = tk.Label(master=frame, text='Sample Frame')
label.pack()
# Text widget inside frame
textbox = tk.Text(frame, fg='green', bg='yellow', height=5, width=30)
textbox.pack()
# Run the main event loop
window.mainloop()