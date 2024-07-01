import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as mysql
import subprocess

def open_S_home(script_name):
    subprocess.run(["python", script_name])

# Sample user data storage
users = {}

def register():
    S_id = reg_S_id_entry.get()
    S_First_Name = reg_S_First_Name_entry.get()
    S_Middle_Name= reg_S_Middle_Name_entry.get()
    S_Last_Name = reg_S_Last_Name_entry.get()
    S_Email = reg_S_Email_entry.get()
    S_Ph_No = reg_S_ph_No_entry.get()
    S_Adrs= reg_S_Adrs_entry.get()
    S_GST_No=reg_S_GST_No_entry.get()
    # S_CIN_No=reg_S_CIN_No_entry.get()
    S_license_No=reg_S_license_No_entry.get()
    S_password = reg_S_password_entry.get()
    
    if S_id in users:
        messagebox.showerror("Error", "Username already exists")
    else:
        con = mysql.connect(host="localhost", user="root", password="rohan136#@ch", database="SLR")
        cursor = con.cursor()
        cursor.execute("insert into SELL values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", 
                       (S_id, S_First_Name, S_Middle_Name, S_Last_Name, S_Email, S_Ph_No, S_Adrs, S_GST_No, S_license_No, S_password))
        con.commit()
        messagebox.showinfo("Status", "Successfully Inserted")

     # Clear the entry fields after registration
        reg_S_id_entry.delete(0, tk.END)
        reg_S_First_Name_entry.delete(0, tk.END)
        reg_S_Middle_Name_entry.delete(0, tk.END)
        reg_S_Last_Name_entry.delete(0, tk.END)
        reg_S_Email_entry.delete(0, tk.END)
        reg_S_ph_No_entry.delete(0, tk.END)
        reg_S_Adrs_entry.delete(0, tk.END)
        reg_S_password_entry.delete(0, tk.END)
        reg_S_GST_No_entry.delete(0, tk.END)
        reg_S_license_No_entry.delete(0, tk.END)
        con.close()

def login():
    S_id = login_S_id_entry.get()
    S_password = login_S_password_entry.get()
    con = mysql.connect(host="localhost", user="root", password="rohan136#@ch", database="SLR")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM SELL WHERE S_id = %s AND S_password = %s", (S_id, S_password))
    result = cursor.fetchone()
    if result:
        messagebox.showinfo("Success", "Login successful")
        open_S_home("s_home.py")
        # Proceed with login
    else:
        messagebox.showerror("Error", "Invalid username or password")

    login_S_id_entry.delete(0, tk.END)
    login_S_password_entry.delete(0, tk.END)

    con.close()

# Create main window
root = tk.Tk()
root.title("Login and Registration")

# # Load and set background image
# bg_image = Image.open("background.jpg")
# bg_photo = ImageTk.PhotoImage(bg_image)

# background_label = tk.Label(root, image=bg_photo)
# background_label.place(relwidth=1, relheight=1)

# Set the size of the window
root.geometry("700x800")

# Registration frame
reg_frame = tk.Frame(root)
reg_frame.pack(pady=10)

tk.Label(reg_frame, text="Registration", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(reg_frame, text="Seller ID").grid(row=1, column=0, sticky='e', padx=10, pady=5)
reg_S_id_entry = tk.Entry(reg_frame)
reg_S_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Seller First Name").grid(row=2, column=0, sticky='e', padx=10, pady=5)
reg_S_First_Name_entry = tk.Entry(reg_frame)
reg_S_First_Name_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Seller Middle Name").grid(row=3, column=0, sticky='e', padx=10, pady=5)
reg_S_Middle_Name_entry = tk.Entry(reg_frame)
reg_S_Middle_Name_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Seller Last Name").grid(row=4, column=0, sticky='e', padx=10, pady=5)
reg_S_Last_Name_entry = tk.Entry(reg_frame)
reg_S_Last_Name_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Seller Email").grid(row=5, column=0, sticky='e', padx=10, pady=5)
reg_S_Email_entry = tk.Entry(reg_frame)
reg_S_Email_entry.grid(row=5, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Seller Phone Number").grid(row=6, column=0, sticky='e', padx=10, pady=5)
reg_S_ph_No_entry = tk.Entry(reg_frame)
reg_S_ph_No_entry.grid(row=6, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Seller Address").grid(row=7, column=0, sticky='e', padx=10, pady=5)
reg_S_Adrs_entry = tk.Entry(reg_frame)
reg_S_Adrs_entry.grid(row=7, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="G.S.T Number").grid(row=8, column=0, sticky='e', padx=10, pady=5)
reg_S_GST_No_entry = tk.Entry(reg_frame)
reg_S_GST_No_entry.grid(row=8, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="License Number").grid(row=9, column=0, sticky='e', padx=10, pady=5)
reg_S_license_No_entry = tk.Entry(reg_frame)
reg_S_license_No_entry.grid(row=9, column=1, padx=10, pady=5)

tk.Label(reg_frame, text="Password").grid(row=10, column=0, sticky='e', padx=10, pady=5)
reg_S_password_entry = tk.Entry(reg_frame, show="*")
reg_S_password_entry.grid(row=10, column=1, padx=10, pady=5)

tk.Button(reg_frame, text="Register", command=register).grid(row=11, column=0, columnspan=2, pady=10)

# Login frame
login_frame = tk.Frame(root)
login_frame.pack(pady=20)

tk.Label(login_frame, text="Login", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(login_frame, text="Username").grid(row=1, column=0, sticky='e', padx=10, pady=5)
login_S_id_entry = tk.Entry(login_frame)
login_S_id_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(login_frame, text="Password").grid(row=2, column=0, sticky='e', padx=10, pady=5)
login_S_password_entry = tk.Entry(login_frame, show="*")
login_S_password_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Button(login_frame, text="Login", command=lambda: login()).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()