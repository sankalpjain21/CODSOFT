# ----------------PASSWORD GENERATOR-------------------------

import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip  # pip install 'pyperclip' for copying text

def generate_password():
    try:
        length = int(entry_length.get())
        if length < 4:
            raise ValueError("Password length should be at least 4 characters.")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
        return

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    all_characters = upper + lower + digits + special

    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]

    password += random.choices(all_characters, k=length-4)
    random.shuffle(password)
    final_password = ''.join(password)
    
    entry_password.config(state=tk.NORMAL)
    entry_password.delete(0, tk.END)
    entry_password.insert(0, final_password)
    entry_password.config(state=tk.DISABLED)

    # Enable the "Copy Password" button after generating the password
    btn_copy_password.config(state=tk.NORMAL)

def copy_password():
    # Copy the generated password to the clipboard
    generated_password = entry_password.get()
    pyperclip.copy(generated_password)
    messagebox.showinfo("Password Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x300")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

label_length = tk.Label(frame, text="Enter password length (min. 4 characters):", font=("Helvetica", 12), bg="#f0f0f0")
label_length.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

entry_length = tk.Entry(frame, width=30, font=("Helvetica", 12))
entry_length.grid(row=0, column=1, padx=10, pady=10)

btn_generate = tk.Button(frame, text="Generate Password", command=generate_password, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", padx=10, pady=5)
btn_generate.grid(row=1, column=0, columnspan=2, pady=20)

label_password = tk.Label(frame, text="Generated Password:", font=("Helvetica", 12), bg="#f0f0f0")
label_password.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

entry_password = tk.Entry(frame, width=40, font=("Helvetica", 12), state=tk.DISABLED)
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Add a button to copy the generated password
btn_copy_password = tk.Button(frame, text="Copy Password", command=copy_password, font=("Helvetica", 12), state=tk.DISABLED)
btn_copy_password.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
