import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    chars = string.ascii_lowercase
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_numbers.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation

    if not chars:
        messagebox.showerror("Error", "Please select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator - Sprint 1")
root.geometry("400x350")
root.config(bg="#1e1e1e")

length_var = tk.IntVar(value=12)
password_var = tk.StringVar()
use_upper = tk.BooleanVar()
use_numbers = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Label(root, text="Password Length:", fg="white", bg="#1e1e1e", font=('Arial', 12)).pack(pady=(10, 0))
tk.Scale(root, from_=8, to=32, orient="horizontal", variable=length_var, bg="#1e1e1e", fg="white").pack()

tk.Checkbutton(root, text="Include Uppercase", variable=use_upper, fg="white", bg="#1e1e1e").pack()
tk.Checkbutton(root, text="Include Numbers", variable=use_numbers, fg="white", bg="#1e1e1e").pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols, fg="white", bg="#1e1e1e").pack()

tk.Button(root, text="Generate Password", command=generate_password, bg="#3e3e3e", fg="white").pack(pady=10)
tk.Entry(root, textvariable=password_var, width=30, font=('Courier', 12)).pack()
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg="#3e3e3e", fg="white").pack(pady=5)

root.mainloop()
