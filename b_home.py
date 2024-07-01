import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime

# Sample data for products
products = [
    {"name": "Mens Shirt", "image": "mens shirt.png", "description": "A classic button-down shirt", "price": 800, "brand": "Sparky"},
    {"name": "Perfume", "image": "perfume.png", "description": "A Good and Scented.", "price": 7000, "brand": "Prak Venue"},
    {"name": "Bottle", "image": "steel bottle.png", "description": "24x7 Hot and cold water.", "price": 500, "brand": "Cello"},
    {"name": "Soap", "image": "soap_PNG24.png", "description": "A Good Mouse.", "price": 20, "brand": "Lenovo"},
    {"name": "steel bottle", "image": "Steel bottle.png", "description": "A stylish watch.", "price": 80, "brand": "Classmate"},
    {"name": "Mobile", "image": "Mobile.png", "description": "A brand new Mobile ", "price": 500, "brand": "Samsung"},
    {"name": "earbud", "image": "Earbuds.png", "description": "Wireless Earbuds", "price": 3000, "brand": "Sandisk"},
    {"name": "eraser", "image": "Eraser.png", "description": "A set of Erasers.", "price": 500, "brand": "Samsung"},
    {"name": "headphone", "image": "headphones.png", "description": "Wireless Headphones.", "price": 3000, "brand": "Sandisk"},
    {"name": "mouse", "image": "computer_mouse_PNG7678.png", "description": "A Good Mouse.", "price": 500, "brand": "Dell"},
    {"name": "mouse lenovo", "image": "PC-Mouse-PNG-Image-Transparent.png", "description": "A Good Mouse.", "price": 100, "brand": "Lenovo"},
    {"name": "Watch", "image": "Watch-High-Quality-PNG.png", "description": "A stylish watch.", "price": 7000, "brand": "Rolex"},
    {"name": "Bag", "image": "pencils.png", "description": "A bag with good storage.", "price": 500, "brand": "Skybag"},
    {"name": "Keyboard", "image": "books.png", "description": "An interesting book.", "price": 400, "brand": "Dell"},
    {"name": "Laptop Lenovo", "image": "computer_mouse_PNG7678.png", "description": "A Good Mouse.", "price": 40000, "brand": "Lenovo"},
    {"name": "cpu", "image": "PC-Mouse-PNG-Image-Transparent.png", "description": "A Good Mouse.", "price": 10000, "brand": "Lenovo"},
    {"name": "Notebook", "image": "Watch-High-Quality-PNG.png", "description": "A stylish watch.", "price": 80, "brand": "Classmate"},
    {"name": "Pendrive", "image": "pencils.png", "description": "A set of quality pencils.", "price": 500, "brand": "Samsung"},
    {"name": "hardisk", "image": "books.png", "description": "An interesting book.", "price": 3000, "brand": "Sandisk"},
    {"name": "mouse", "image": "computer_mouse_PNG7678.png", "description": "A Good Mouse.", "price": 500, "brand": "Dell"},
    #{"name": "Pens", "image": "pens.png", "description": "An interesting book.", "price": 400, "brand": "Dell"},
    #{"name": "Lunch Box", "image": "lunch box.png", "description": "A Good Mouse.", "price": 400, "brand": "Lenovo"},
]
# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rohan136#@ch",
    database="shopping_db"
)
cursor = db.cursor()


cart = []
receiver_name= None
mobile_no=None
country_name=None
state_name=None
user_pin_code = None
user_address = None
user_phone_No=None

orders = []  # To store order details

def load_image(image_path, size=(100, 100)):
    try:
        img = Image.open(image_path)
        img = img.resize(size, Image.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error loading image {image_path}: {e}")
        return None

def view_products(limit=None):
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    row = 0
    col = 0
    for product in products[:limit]:
        product_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
        product_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        product_frame.bind("<Button-1>", lambda e, p=product: view_product_details(p))

        img = load_image(product["image"])
        
        if img:
            img_label = tk.Label(product_frame, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack(side="top", padx=10, pady=10)
        else:
            img_label = tk.Label(product_frame, text="No Image Available", width=12, height=6)
            img_label.pack(side="top", padx=10, pady=10)

        name_label = tk.Label(product_frame, text=product["name"], font=("Helvetica", 16))
        name_label.pack(anchor="w")

        desc_label = tk.Label(product_frame, text=product["description"], font=("Helvetica", 12))
        desc_label.pack(anchor="w")

        price_label = tk.Label(product_frame, text=f"Rs{product['price']}", font=("Helvetica", 14))
        price_label.pack(anchor="w")

        add_button = tk.Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
        add_button.pack(anchor="w", pady=5)
        
        buy_button = tk.Button(product_frame, text="Buy Now", command=lambda p=product: buy_now(p))
        buy_button.pack(anchor="w", pady=5)

        col += 1
        if col == 6:  # Change this value based on the number of columns you want
            col = 0
            row += 1

def view_product_details(product):
    for widget in content_frame.winfo_children():
        widget.destroy()

    details_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
    details_frame.pack(padx=10, pady=10, fill="both", expand=True)

    img = load_image(product["image"], size=(300, 300))
    if img:
        img_label = tk.Label(details_frame, image=img)
        img_label.image = img  # Keep a reference to avoid garbage collection
        img_label.pack(side="top", padx=10, pady=10)
    else:
        img_label = tk.Label(details_frame, text="No Image Available", width=30, height=15)
        img_label.pack(side="top", padx=10, pady=10)

    name_label = tk.Label(details_frame, text=product["name"], font=("Helvetica", 24))
    name_label.pack(anchor="w")

    desc_label = tk.Label(details_frame, text=product["description"], font=("Helvetica", 16))
    desc_label.pack(anchor="w")

    price_label = tk.Label(details_frame, text=f"Rs{product['price']}", font=("Helvetica", 20))
    price_label.pack(anchor="w")

    add_button = tk.Button(details_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p), font=("Helvetica", 14))
    add_button.pack(anchor="w", pady=5)
    
    buy_button = tk.Button(details_frame, text="Buy Now", command=lambda : buy_now(p), font=("Helvetica", 14))
    buy_button.pack(anchor="w", pady=5)

def view_profile():
    for widget in content_frame.winfo_children():
        widget.destroy()


    profile_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
    profile_frame.pack(padx=10, pady=10, fill="both", expand=True)

    receiver_label = tk.Label(profile_frame, text=f"Name: {receiver_name or 'Not Set'}", font=("Helvetica", 16))
    receiver_label.pack(anchor="w", pady=5)

    mobile_no_label = tk.Label(profile_frame, text=f"Mobile No: {mobile_no or 'Not Set'}", font=("Helvetica", 16))
    mobile_no_label.pack(anchor="w", pady=5)

    country_label = tk.Label(profile_frame, text=f"Country Name: {country_name or 'Not Set'}", font=("Helvetica", 16))
    country_label.pack(anchor="w", pady=5)

    state_label = tk.Label(profile_frame, text=f"State Name: {state_name or 'Not Set'}", font=("Helvetica", 16))
    state_label.pack(anchor="w", pady=5)

    pin_code_label = tk.Label(profile_frame, text=f"Pin Code: {user_pin_code or 'Not Set'}", font=("Helvetica", 16))
    pin_code_label.pack(anchor="w", pady=5)

    address_label = tk.Label(profile_frame, text=f"Address: {user_address or 'Not Set'}", font=("Helvetica", 16))
    address_label.pack(anchor="w", pady=5)

    set_address_button = tk.Button(profile_frame, text="Set Address", command=set_address)
    set_address_button.pack(anchor="w", pady=5)

    edit_button = tk.Button(profile_frame, text="Edit Profile", command=edit_profile)
    edit_button.pack(anchor="w", pady=5)

def edit_profile():
    global country_name ,state_name,mobile_no,receiver_name, user_address, user_pin_code
    receiver_name = simpledialog.askstring("Edit Profile", "Enter your name:")
    mobile_no=simpledialog.askstring("Edit Profile", "Enter your mobile no:")
    country_name=simpledialog.askstring("Edit Profile", "Enter your country:")
    state_name=simpledialog.askstring("Edit Profile", "Enter your state:")
    user_pin_code = simpledialog.askstring("Edit Profile", "Enter your pin code:")
    user_address = simpledialog.askstring("Edit Profile", "Enter your address:")
    view_profile()

def set_address():
    global country_name,state_name,mobile_no,receiver_name, user_address, user_pin_code
    receiver_name = simpledialog.askstring("User Name", "Enter your name:")
    mobile_no=simpledialog.askstring("Edit Profile", "Enter your mobile no:")
    country_name=simpledialog.askstring("Edit Profile", "Enter your country:")
    state_name=simpledialog.askstring("Edit Profile", "Enter your state:")
    user_pin_code = simpledialog.askinteger("User Pin Code", "Enter your pin code:")
    user_address = simpledialog.askstring("User Address", "Enter your address:")

    if  country_name and state_name and mobile_no and receiver_name and  user_address and user_pin_code:
        messagebox.showinfo("Success", "Name and Address and pin code have been set!")
    else:
        messagebox.showwarning("Invalid Input", "Please enter name and address and pin code.")


def add_to_cart(product):
    cart.append(product)
    messagebox.showinfo("Cart", f"Added {product['name']} to cart.")

def view_cart():
    for widget in content_frame.winfo_children():
        widget.destroy()

    if not cart:
        empty_label = tk.Label(content_frame, text="Your cart is empty.", font=("Helvetica", 16))
        empty_label.pack(pady=20)
        return
    
    total_price = sum(item['price'] for item in cart)
    total_label = tk.Label(content_frame, text=f"Total Price: Rs{total_price}", font=("Helvetica", 16))
    total_label.pack(pady=10)

    for product in cart:
        product_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
        product_frame.pack(fill="x", padx=10, pady=10)

        name_label = tk.Label(product_frame, text=product["name"], font=("Helvetica", 16))
        name_label.pack(side="left")

        price_label = tk.Label(product_frame, text=f"Rs{product['price']}", font=("Helvetica", 14))
        price_label.pack(side="left", padx=10)

        remove_button = tk.Button(product_frame, text="Remove", command=lambda p=product: remove_from_cart(p))
        remove_button.pack(side="left", padx=10)

        buy_button = tk.Button(product_frame, text="Buy Now", command=lambda p=product: buy_now(p))
        buy_button.pack(side="left", padx=10)

    buy_all_button = tk.Button(content_frame, text="Buy All", command=buy_all, font=("Helvetica", 14))
    buy_all_button.pack(pady=20)

def remove_from_cart(product):
    cart.remove(product)
    messagebox.showinfo("Cart", f"Removed {product['name']} from cart.")
    view_cart()

# Function to handle product purchase
def buy_now(product):
    customer_name = simpledialog.askstring("Customer Name", "Enter your name:")
    if not customer_name:
        messagebox.showwarning("Input Error", "Please enter a valid name.")
        return

    customer_address = simpledialog.askstring("Address", "Enter your delivery address:")
    if not customer_address:
        messagebox.showwarning("Input Error", "Please enter a valid address.")
        return

    customer_phone = simpledialog.askstring("Phone No", "Enter your phone number:")
    if not customer_phone:
        messagebox.showwarning("Input Error", "Please enter a valid phone number.")
        return

    customer_pincode = simpledialog.askstring("Pin Code", "Enter your area pin code:")
    if not customer_pincode:
        messagebox.showwarning("Input Error", "Please enter a valid pin code.")
        return

    order_details = {
        "product_name": product["name"],
        "product_price": product["price"],
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "customer_pincode": customer_pincode,
        "order_status": "Processing",
        "order_date": datetime.now()
    }

    # Insert order details into the database
    query = """
    INSERT INTO ODR (product_name, product_price, customer_name, customer_address, customer_phone, customer_pincode, order_status, order_date)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        order_details["product_name"],
        order_details["product_price"],
        order_details["customer_name"],
        order_details["customer_address"],
        order_details["customer_phone"],
        order_details["customer_pincode"],
        order_details["order_status"],
        order_details["order_date"]
    )
    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Order Details", f"Order placed for {product['name']} at Rs{product['price']}.\n"
                                         f"Customer Name: {customer_name}\n"
                                         f"Delivery Address: {customer_address}\n"
                                         f"Phone No: {customer_phone}\n"
                                         f"Pin Code: {customer_pincode}\n"
                                         f"Thank you for your purchase!")
    



# Function to insert order details into the database
def insert_order(order_details):
    db
    cursor = db.cursor()
    
    sql = """
    INSERT INTO ODR (customer_name, customer_address, customer_phone, customer_pincode, product_name, product_price, order_status)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        order_details["customer_name"],
        order_details["customer_address"],
        order_details["customer_phone"],
        order_details["customer_pincode"],
        order_details["product_name"],
        order_details["price"],
        order_details["status"]
    )
    
    cursor.execute(sql, values)
    db.commit()
    
    cursor.close()
    db.close()
    
# Function to handle purchase of all items in the cart
def buy_all():
    global cart  # Access the global cart variable

    if not cart:
        messagebox.showwarning("Cart Error", "Your cart is empty.")
        return

    customer_name = simpledialog.askstring("Name", "Enter your name:")
    if not customer_name:
        messagebox.showwarning("Input Error", "Please enter a valid name.")
        return

    customer_address = simpledialog.askstring("Address", "Enter your delivery address:")
    if not customer_address:
        messagebox.showwarning("Input Error", "Please enter a valid address.")
        return

    customer_phone = simpledialog.askstring("Phone No", "Enter your phone number:")
    if not customer_phone:
        messagebox.showwarning("Input Error", "Please enter a valid phone number.")
        return

    customer_pincode = simpledialog.askstring("Pin Code", "Enter your area pin code:")
    if not customer_pincode:
        messagebox.showwarning("Input Error", "Please enter a valid pin code.")
        return

    for product in cart:
        cursor.execute("""
            INSERT INTO ODR (customer_name, customer_address, customer_phone, customer_pincode, product_name, product_price, order_status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (customer_name, customer_address, customer_phone, customer_pincode, product["name"], product["price"], "Processing"))

    db.commit()
    
    messagebox.showinfo("Order Details", f"Order placed for all items in the cart.\n"
                                         f"Customer Name: {customer_name}\n"
                                         f"Delivery Address: {customer_address}\n"
                                         f"Phone No: {customer_phone}\n"
                                         f"Pin Code: {customer_pincode}\n"
                                         "Thank you for your purchase!")
    cart.clear()
    # Optionally, update the cart view here




        # Function to close the database connection when done
def close_db():
    cursor.close()
    db.close()

def show_orders():
    for widget in content_frame.winfo_children():
        widget.destroy()

    if not orders:
        empty_label = tk.Label(content_frame, text="No orders placed yet.", font=("Helvetica", 16))
        empty_label.pack(pady=20)
        return

    for order in orders:
        order_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
        order_frame.pack(fill="x", padx=10, pady=10)

        product_name_label = tk.Label(order_frame, text=f"Product: {order['product_name']}", font=("Helvetica", 16))
        product_name_label.pack(anchor="w")

        price_label = tk.Label(order_frame, text=f"Price: Rs{order['price']}", font=("Helvetica", 14))
        price_label.pack(anchor="w")

        address_label = tk.Label(order_frame, text=f"Address: {order['address']}", font=("Helvetica", 12))
        address_label.pack(anchor="w")

        phone_label = tk.Label(order_frame, text=f"Phone Number: {order['userphoneNo']}", font=("Helvetica", 12))
        phone_label.pack(anchor="w")

        pin_code_label = tk.Label(order_frame, text=f"Pin Code: {order['pin_code']}", font=("Helvetica", 12))
        pin_code_label.pack(anchor="w")

        status_label = tk.Label(order_frame, text=f"Status: {order['status']}", font=("Helvetica", 12))
        status_label.pack(anchor="w")



def search_products():
    query = search_entry.get().lower()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a items to be serached.")
        return

    results = [product for product in products if query in product["name"].lower()]
    for widget in content_frame.winfo_children():
        widget.destroy()

    if not results:
        no_results_label = tk.Label(content_frame, text="No products found.", font=("Helvetica", 16))
        no_results_label.pack(pady=20)
        return

    row = 0
    col = 0
    for product in results:
        product_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
        product_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        img = load_image(product["image"])
        
        if img:
            img_label = tk.Label(product_frame, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack(side="top", padx=10, pady=10)
        else:
            img_label = tk.Label(product_frame, text="No Image Available", width=12, height=6)
            img_label.pack(side="top", padx=10, pady=10)

        name_label = tk.Label(product_frame, text=product["name"], font=("Helvetica", 16))
        name_label.pack(anchor="w")

        desc_label = tk.Label(product_frame, text=product["description"], font=("Helvetica", 12))
        desc_label.pack(anchor="w")

        price_label = tk.Label(product_frame, text=f"Rs{product['price']}", font=("Helvetica", 14))
        price_label.pack(anchor="w")

        add_button = tk.Button(product_frame, text="Add to Cart", command=lambda p=product: add_to_cart(p))
        add_button.pack(anchor="w", pady=5)
        
        buy_button = tk.Button(product_frame, text="Buy Now", command=lambda p=product: buy_now(p))
        buy_button.pack(anchor="w", pady=5)

        col += 1
        if col == 6:  # Change this value based on the number of columns you want
            col = 0
            row += 1



def search_by_brand():
    brand = simpledialog.askstring("Search by Brand", "Enter the brand name:")
    if not brand:
        messagebox.showwarning("Input Error", "Please enter a brand name.")
        return
    
    brand = brand.lower()
    results = [product for product in products if '' in product["name"].lower() and brand in product["brand"].lower()]

    for widget in content_frame.winfo_children():
        widget.destroy()

    if not results:
        no_results_label = tk.Label(content_frame, text="No mice found for this brand.", font=("Helvetica", 16))
        no_results_label.pack(pady=20)
        return

    row = 0
    col = 0
    for product in results:
        product_frame = tk.Frame(content_frame, pady=10, padx=10, borderwidth=1, relief="solid")
        product_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        img = load_image(product["image"])
        
        if img:
            img_label = tk.Label(product_frame, image=img)
            img_label.image = img  # Keep a reference to avoid garbage collection
            img_label.pack(side="top", padx=10, pady=10)
        else:
            img_label = tk.Label(product_frame, text="No Image Available", width=12, height=6)
            img_label.pack(side="top", padx=10, pady=10)

        name_label = tk.Label( text=product["name"], font=("Helvetica", 16)) 
        name_label.pack(anchor="w")

        desc_label = tk.Label( text=product["description"], font=("Helvetica", 12))
        desc_label.pack(anchor="w")

        price_label = tk.Label( text=f"Rs{product['price']}", font=("Helvetica", 14))
        price_label.pack(anchor="w")

        add_button = tk.Button( text="Add to Cart", command=lambda p=product: add_to_cart(p))
        add_button.pack(anchor="w", pady=5)
        
        buy_button = tk.Button( text="Buy Now", command=lambda p=product: buy_now(p))
        buy_button.pack(anchor="w", pady=5)

        col += 1
        if col == 6:  # Change this value based on the number of columns you want
            col = 0
            row += 1

# Initialize the main application window
app = tk.Tk()
app.title("Online Shopping System")
app.geometry("1400x1000")

# Create a welcome label
welcome_label = tk.Label(app, text="Welcome to the Online Shopping System!", font=("Arial Black", 24))
welcome_label.pack(pady=20)

# Create a search bar
search_frame = tk.Frame(app)
search_frame.pack(pady=10)

search_label = tk.Label(search_frame, text="Search Products:", font=("Helvetica", 14))
search_label.pack(side=tk.LEFT, padx=10)

search_entry = tk.Entry(search_frame, width=30, font=("Helvetica", 14))
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Search", command=search_products, font=("Helvetica", 14))
search_button.pack(side=tk.LEFT, padx=10)

# Create a content frame
content_canvas = tk.Canvas(app)
content_canvas.pack(side=tk.LEFT, fill="both", expand=True)

# Create a scrollbar
scrollbar = tk.Scrollbar(app, orient="vertical", command=content_canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill="y")

# Configure the canvas
content_canvas.configure(yscrollcommand=scrollbar.set)
content_canvas.bind('<Configure>', lambda e: content_canvas.configure(scrollregion=content_canvas.bbox("all")))

# Create another frame inside the canvas
content_frame = tk.Frame(content_canvas)
content_canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Create buttons for navigation

profile_button = tk.Button(app, text="Profile", command=view_profile,width=20, height=2)
profile_button.pack(pady=10, padx=50)

btn_view_products = tk.Button(app, text="Home", command=view_products, width=20, height=2)
btn_view_products.pack(pady=10,padx=50)

btn_view_cart = tk.Button(app, text="View Cart", command=view_cart, width=20, height=2)
btn_view_cart.pack(pady=10,padx=50)

btn_search_mouse = tk.Button(app, text="Search by Brand", command=search_by_brand, width=20, height=2)
btn_search_mouse.pack(pady=10,padx=50)

orders_button = tk.Button(app, text="Orders", command=show_orders,width=20, height=2)
orders_button.pack(pady=10, padx=50)

# Function to handle scrollbar with canvas
def on_content_frame_configure(event):
 content_canvas.configure(scrollregion=content_canvas.bbox("all"))

content_frame.bind("<Configure>", on_content_frame_configure)

# Show default products on startup
view_products(limit=12)

# Function to close the database connection when done
def close_db():
    cursor.close()
    db.close()
# Main loop to run the application
app.mainloop()
