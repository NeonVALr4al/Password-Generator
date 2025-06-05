import tkinter as tk
from tkinter import messagebox
import random
import string

def evaluate_strength(password):
    length = len(password)
    strength = "Weak"
    types = 0
    if any(c.islower() for c in password): types += 1
    if any(c.isupper() for c in password): types += 1
    if any(c.isdigit() for c in password): types += 1
    if any(c in string.punctuation for c in password): types += 1

    if length >= 12 and types >= 3:
        strength = "Strong"
    elif length >= 8 and types >= 2:
        strength = "Medium"

    strength_label.config(
        text=f"Strength: {strength}",
        fg={"Weak": "red", "Medium": "orange", "Strong": "lightgreen"}[strength]
    )

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
        messagebox.showerror("Error", "Select at least one character type.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_var.set(password)
    evaluate_strength(password)

def copy_to_clipboard():
    password = password_var.get()
    if not password:
        messagebox.showerror("Error", "No password to copy.")
        return
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Final Password Generator")
root.geometry("400x450")
root.config(bg="#1e1e1e")


length_var = tk.IntVar(value=12)
password_var = tk.StringVar()
use_upper = tk.BooleanVar()
use_numbers = tk.BooleanVar()
use_symbols = tk.BooleanVar()


tk.Label(root, text="Password Length:", fg="white", bg="#1e1e1e", font=('Arial', 12)).pack(pady=(20, 5))
tk.Scale(root, from_=8, to=32, orient="horizontal", variable=length_var,
         bg="#1e1e1e", fg="white", troughcolor="#333", length=250).pack(pady=5)

tk.Checkbutton(root, text="Include Uppercase", variable=use_upper,
               fg="white", bg="#1e1e1e", selectcolor="#333").pack(pady=5)
tk.Checkbutton(root, text="Include Numbers", variable=use_numbers,
               fg="white", bg="#1e1e1e", selectcolor="#333").pack(pady=5)
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols,
               fg="white", bg="#1e1e1e", selectcolor="#333").pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password,
          bg="#444", fg="white", font=('Arial', 11), width=22).pack(pady=15)

tk.Entry(root, textvariable=password_var, font=('Courier', 12), width=30,
         justify='center').pack(pady=8, ipady=4)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          bg="#444", fg="white", font=('Arial', 10), width=18).pack(pady=10)

strength_label = tk.Label(root, text="Strength: ", fg="white", bg="#1e1e1e",
                          font=('Arial', 10, 'italic'))
strength_label.pack(pady=5)

root.mainloop()
