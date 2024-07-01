import tkinter as tk
from PIL import Image, ImageTk
import subprocess

# Function to open secondary script
def open_secondary(script_name):
    subprocess.run(["python", script_name])

# Main application window
root = tk.Tk()
root.title("Online Shopping System")

# Set the size of the window
root.geometry("800x600")

# Create a frame for the welcome message
welcome_frame = tk.Frame(root, bg="white", bd=5)
welcome_frame.place(relx=0.5, rely=0.1, anchor="n")

# Welcome message
welcome_label = tk.Label(welcome_frame, text="Welcome to the Online Shopping System !", font=("Helvetica", 16))
welcome_label.pack()

# Create a frame for the buttons and center it horizontally
button_frame = tk.Frame(root, bg="white", bd=5)
button_frame.place(relx=0.5, rely=0.4, anchor="n")

# Buyer login button
buyer_button = tk.Button(button_frame, text="Buyer Login", command=lambda: open_secondary("buyer.py"),)
buyer_button.grid(row=0, column=0, padx=10, pady=10)

# Seller login button
seller_button = tk.Button(button_frame, text="Seller Login", command=lambda: open_secondary("seller.py"))
seller_button.grid(row=0, column=1, padx=10, pady=10)

# Admin login button
admin_button = tk.Button(button_frame, text="Admin Login", command=lambda: open_secondary("admin.py"))
admin_button.grid(row=1, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()