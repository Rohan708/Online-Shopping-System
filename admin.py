import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import subprocess

# Sample user data storage
users = {}

def open_A_home(script_name):
    subprocess.run(["python", script_name])

def login():
    A_id = login_A_id_entry.get()
    A_password = login_A_password_entry.get()
    con = mysql.connect(host="localhost", user="root", password="rohan136#@ch", database="ADM")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ADMN WHERE A_id = %s AND A_password = %s", (A_id, A_password))
    result = cursor.fetchone()
    
    if result:
         messagebox.showinfo("Success", "Admin Login successful")
         open_A_home("a_home.py")
        # Optionally, close the current login window
         root.destroy()
    else:
        messagebox.showerror("Error", "Invalid Admin ID or password")

    login_A_id_entry.delete(0, tk.END)
    login_A_password_entry.delete(0, tk.END)
    
    con.close()

# Create main window
root = tk.Tk()
root.title("Admin Login")

# Set the size of the window
root.geometry("500x600")

# Login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Login", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_frame, text="Username").grid(row=1, column=0, sticky='e', padx=10, pady=5)
login_A_id_entry = tk.Entry(login_frame)
login_A_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_frame, text="Password").grid(row=2, column=0, sticky='e', padx=10, pady=5)
login_A_password_entry = tk.Entry(login_frame, show="*")
login_A_password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(login_frame, text="Login", command=lambda: login()).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
