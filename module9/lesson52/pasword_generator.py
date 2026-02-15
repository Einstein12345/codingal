import tkinter as tk
from tkinter import messagebox
import random
import string
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Error", "Please enter a positive number")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
# Main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x250")
root.resizable(False, False)
# Variables
password_var = tk.StringVar()
# UI Elements
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=10)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack()
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=15)
tk.Entry(root, textvariable=password_var, font=("Arial", 12), width=30).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=10)
root.mainloop()