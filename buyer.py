import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
import subprocess

# Function to open secondary script
def open_tertiory(script_name):
    subprocess.run(["python", script_name])

def register():
    B_id = reg_B_id_entry.get()
    B_First_Name = reg_B_First_Name_entry.get()
    B_Middle_Name= reg_B_Middle_Name_entry.get()
    B_Last_Name = reg_B_Last_Name_entry.get()
    B_Email = reg_B_Email_entry.get()
    B_Ph_No = reg_B_ph_No_entry.get()
    B_Adrs= reg_B_Adrs_entry.get()
    B_password = reg_B_password_entry.get()

    con = mysql.connect(host="localhost", user="root", password="rohan136#@ch", database="BYR")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM BUY WHERE B_id = %s", (B_id,))
    result = cursor.fetchone()

    if result:
        messagebox.showerror("Error", "Buyer ID already exists")
    else:
        cursor.execute("INSERT INTO BUY (B_id, B_First_Name, B_Middle_Name, B_Last_Name, B_Email, B_Ph_No, B_Adrs, B_password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (B_id, B_First_Name, B_Middle_Name, B_Last_Name, B_Email, B_Ph_No, B_Adrs, B_password))
        con.commit()
        messagebox.showinfo("Status", "Buyer Successfully Registered")

        # Clear the entry fields after registration
        reg_B_id_entry.delete(0, tk.END)
        reg_B_First_Name_entry.delete(0, tk.END)
        reg_B_Middle_Name_entry.delete(0, tk.END)
        reg_B_Last_Name_entry.delete(0, tk.END)
        reg_B_Email_entry.delete(0, tk.END)
        reg_B_ph_No_entry.delete(0, tk.END)
        reg_B_Adrs_entry.delete(0, tk.END)
        reg_B_password_entry.delete(0, tk.END)

    con.close()

def login():
    B_id = login_B_id_entry.get()
    B_password = login_B_password_entry.get()
    con = mysql.connect(host="localhost", user="root", password="rohan136#@ch", database="BYR")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM BUY WHERE B_id = %s AND B_password = %s", (B_id, B_password))
    result = cursor.fetchone()
    
    if result:
        messagebox.showinfo("Success", " Buyer's Login successful")
        open_tertiory("b_home.py")
        # Proceed with login
    else:
        messagebox.showerror("Error", "Invalid Buyer ID or password")

  # Clear the entry fields after Login
    login_B_id_entry.delete(0, tk.END)
    login_B_password_entry.delete(0, tk.END)

    con.close()

# Create main window
root = tk.Tk()
root.title("Login and Registration")
root.geometry("500x600")

# Registration frame
reg_frame = tk.Frame(root)
reg_frame.pack(pady=10)

tk.Label(reg_frame, text="Registration", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(reg_frame, text="Buyer ID").grid(row=1, column=0, sticky='e', padx=10, pady=5)
reg_B_id_entry = tk.Entry(reg_frame)
reg_B_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Buyer First Name").grid(row=2, column=0, sticky='e', padx=10, pady=5)
reg_B_First_Name_entry = tk.Entry(reg_frame)
reg_B_First_Name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Buyer Middle Name").grid(row=3, column=0, sticky='e', padx=10, pady=5)
reg_B_Middle_Name_entry = tk.Entry(reg_frame)
reg_B_Middle_Name_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Buyer Last Name").grid(row=4, column=0, sticky='e', padx=10, pady=5)
reg_B_Last_Name_entry = tk.Entry(reg_frame)
reg_B_Last_Name_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Buyer Email").grid(row=5, column=0, sticky='e', padx=10, pady=5)
reg_B_Email_entry = tk.Entry(reg_frame)
reg_B_Email_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Buyer Phone Number").grid(row=6, column=0, sticky='e', padx=10, pady=5)
reg_B_ph_No_entry = tk.Entry(reg_frame)
reg_B_ph_No_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Buyer Address").grid(row=7, column=0, sticky='e', padx=10, pady=5)
reg_B_Adrs_entry = tk.Entry(reg_frame)
reg_B_Adrs_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Password").grid(row=8, column=0, sticky='e', padx=10, pady=5)
reg_B_password_entry = tk.Entry(reg_frame, show="*")
reg_B_password_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Button(reg_frame, text="Register", command=register).grid(row=9, column=0, columnspan=2, pady=10)

# Login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Login", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_frame, text="Buyer ID").grid(row=1, column=0, sticky='e', padx=10, pady=5)
login_B_id_entry = tk.Entry(login_frame)
login_B_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_frame, text="Password").grid(row=2, column=0, sticky='e', padx=10, pady=5)
login_B_password_entry = tk.Entry(login_frame, show="*")
login_B_password_entry.grid(row=2, column=1, padx=10, pady=5)


tk.Button(login_frame, text="Login", command=lambda:login() ).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
