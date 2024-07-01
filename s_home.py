import tkinter as tk
from tkinter import filedialog, messagebox
import mysql.connector

class SellerHomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Seller's Home Page")

        # Add heading
        self.heading = tk.Label(root, text="SELL YOUR PRODUCTS HERE !!", font=('Helvetica', 16, 'bold'))
        self.heading.grid(row=0, column=0, columnspan=3, pady=10)

        # Create and place labels and entry fields
        tk.Label(root, text="Product Name:").grid(row=1, column=0, padx=10, pady=10)
        self.product_name = tk.Entry(root, width=50)
        self.product_name.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="Product Description:").grid(row=2, column=0, padx=10, pady=10)
        self.product_description = tk.Entry(root, width=50)
        self.product_description.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(root, text="Brand:").grid(row=3, column=0, padx=10, pady=10)
        self.product_brand = tk.Entry(root, width=50)
        self.product_brand.grid(row=3, column=1, padx=10, pady=10)

        tk.Label(root, text="Price (₹):").grid(row=4, column=0, padx=10, pady=10)
        self.product_price = tk.Entry(root, width=20)
        self.product_price.grid(row=4, column=1, padx=10, pady=10, sticky='w')

        tk.Label(root, text="Quantity:").grid(row=5, column=0, padx=10, pady=10)
        self.product_quantity = tk.Entry(root, width=20)
        self.product_quantity.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        tk.Label(root, text="Upload Image:").grid(row=6, column=0, padx=10, pady=10)
        self.upload_button = tk.Button(root, text="Browse", command=self.upload_image)
        self.upload_button.grid(row=6, column=1, padx=10, pady=10, sticky='w')

        self.image_path = tk.StringVar()
        self.image_path_label = tk.Label(root, textvariable=self.image_path)
        self.image_path_label.grid(row=7, column=1, padx=10, pady=10, sticky='w')

        # Submit button
        self.submit_button = tk.Button(root, text="Submit Product", command=self.submit_product)
        self.submit_button.grid(row=8, column=1, padx=10, pady=10, sticky='w')

        # Right-side frame for additional buttons
        self.side_frame = tk.Frame(root)
        self.side_frame.grid(row=1, column=2, rowspan=8, padx=20, pady=10, sticky='n')

        # Additional buttons
        self.add_side_buttons()

    def add_side_buttons(self):
        button_texts = ["Profile", "Previously Sold Products", "Buy Requests", "Support", "Settings", "Logout"]
        for text in button_texts:
            button = tk.Button(self.side_frame, text=text, width=20, command=lambda t=text: self.handle_button(t))
            button.pack(pady=5)

    def handle_button(self, button_text):
        messagebox.showinfo("Button Clicked", f"You clicked the {button_text} button!")

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.image_path.set(file_path)

    def submit_product(self):
        product_name = self.product_name.get()
        product_description = self.product_description.get()
        product_brand = self.product_brand.get()
        product_price = self.product_price.get()
        product_quantity = self.product_quantity.get()
        image_path = self.image_path.get()

        if not all([product_name, product_description, product_brand, product_price, product_quantity, image_path]):
            messagebox.showwarning("Incomplete Data", "Please fill out all fields and upload an image.")
            return

        try:
            price = float(product_price)
            quantity = int(product_quantity)
        except ValueError:
            messagebox.showerror("Invalid Data", "Price must be a number and Quantity must be an integer.")
            return

        # Save product to database
        if self.save_product_to_database(product_name, product_description, product_brand, price, quantity, image_path):
            messagebox.showinfo("Product Submitted", "Product details submitted successfully!")
            # Clear the input fields after successful submission
            self.clear_input_fields()
        else:
            messagebox.showerror("Database Error", "Failed to submit product details. Please try again.")

    def save_product_to_database(self, name, description, brand, price, quantity, image_path):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="rohan136#@ch",
                database="PRD"  # Replace with your actual database name
            )
            cursor = conn.cursor()

            # Insert product details into the database
            cursor.execute('''
                INSERT INTO products (name, description, brand, price, quantity, image_path)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (name, description, brand, price, quantity, image_path))

            conn.commit()
            conn.close()
            return True
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error: {str(e)}")
            return False

    def clear_input_fields(self):
        self.product_name.delete(0, tk.END)
        self.product_description.delete(0, tk.END)
        self.product_brand.delete(0, tk.END)
        self.product_price.delete(0, tk.END)
        self.product_quantity.delete(0, tk.END)
        self.image_path.set("")

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    app = SellerHomePage(root)
    root.mainloop()
