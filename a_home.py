import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

class AdminPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Admin Page - Online Shopping System")
        self.geometry("800x600")

        # Create tabs
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(expand=1, fill='both')

        # Create tabs for different functionalities
        self.create_manage_buyers_tab()
        self.create_manage_sellers_tab()
        self.create_review_orders_tab()
        self.create_manage_app_tab()
        self.create_additional_features_tab()

    def create_manage_buyers_tab(self):
        self.buyers_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.buyers_tab, text="Manage Buyers")

        tk.Label(self.buyers_tab, text="Manage Buyers' Accounts", font=("Arial", 16)).pack(pady=10)

        self.buyer_list = ttk.Treeview(self.buyers_tab, columns=("ID", "First Name", "Middle Name", "Last Name", "Email", "Phone", "Address"), show='headings')
        self.buyer_list.heading("ID", text="ID")
        self.buyer_list.heading("First Name", text="First Name")
        self.buyer_list.heading("Middle Name", text="Middle Name")
        self.buyer_list.heading("Last Name", text="Last Name")
        self.buyer_list.heading("Email", text="Email")
        self.buyer_list.heading("Phone", text="Phone")
        self.buyer_list.heading("Address", text="Address")
        self.buyer_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.load_buyers()

        tk.Button(self.buyers_tab, text="Add Buyer", command=self.add_buyer).pack(side=tk.LEFT, padx=10)
        tk.Button(self.buyers_tab, text="Edit Buyer", command=self.edit_buyer).pack(side=tk.LEFT, padx=10)
        tk.Button(self.buyers_tab, text="Delete Buyer", command=self.delete_buyer).pack(side=tk.LEFT, padx=10)

    def create_manage_sellers_tab(self):
        self.sellers_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.sellers_tab, text="Manage Sellers")

        tk.Label(self.sellers_tab, text="Manage Sellers' Accounts", font=("Arial", 16)).pack(pady=10)

        self.seller_list = ttk.Treeview(self.sellers_tab, columns=("ID", "First Name", "Middle Name", "Last Name", "Email", "Phone", "Address", "GST No", "License"), show='headings')
        self.seller_list.heading("ID", text="ID")
        self.seller_list.heading("First Name", text="First Name")
        self.seller_list.heading("Middle Name", text="Middle Name")
        self.seller_list.heading("Last Name", text="Last Name")
        self.seller_list.heading("Email", text="Email")
        self.seller_list.heading("Phone", text="Phone")
        self.seller_list.heading("Address", text="Address")
        self.seller_list.heading("GST No", text="GST No")
        self.seller_list.heading("License", text="License")
        self.seller_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.load_sellers()

        tk.Button(self.sellers_tab, text="Add Seller", command=self.add_seller).pack(side=tk.LEFT, padx=10)
        tk.Button(self.sellers_tab, text="Edit Seller", command=self.edit_seller).pack(side=tk.LEFT, padx=10)
        tk.Button(self.sellers_tab, text="Delete Seller", command=self.delete_seller).pack(side=tk.LEFT, padx=10)

    def create_review_orders_tab(self):
        self.orders_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.orders_tab, text="Review Orders")

        tk.Label(self.orders_tab, text="Review Shopping Orders", font=("Arial", 16)).pack(pady=10)

        self.order_list = ttk.Treeview(self.orders_tab, columns=("Order ID", "Product ID", "Quantity", "Total Price", "Customer Name", "Address", "Phone Number", "Pin Code"), show='headings')
        self.order_list.heading("Order ID", text="Order ID")
        self.order_list.heading("Product ID", text="Product ID")
        self.order_list.heading("Quantity", text="Quantity")
        self.order_list.heading("Total Price", text="Total Price")
        self.order_list.heading("Customer Name", text="Customer Name")
        self.order_list.heading("Address", text="Address")
        self.order_list.heading("Phone Number", text="Phone Number")
        self.order_list.heading("Pin Code", text="Pin Code")
        self.order_list.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        self.load_orders()

    def create_manage_app_tab(self):
        self.app_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.app_tab, text="Manage App")

        tk.Label(self.app_tab, text="Manage App Settings", font=("Arial", 16)).pack(pady=10)
        # Add functionality to manage app settings here (e.g., configure settings, view logs)

    def create_additional_features_tab(self):
        self.additional_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.additional_tab, text="Additional Features")

        tk.Label(self.additional_tab, text="Additional Features", font=("Arial", 16)).pack(pady=10)
        # Add additional functionalities here (e.g., manage products, view analytics)

    def load_buyers(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rohan136#@ch",
            database="BYR"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM BUY")
        rows = cursor.fetchall()
        for row in rows:
            self.buyer_list.insert('', tk.END, values=row)

        conn.close()

    def load_sellers(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rohan136#@ch",
            database="SLR"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM SELL")
        rows = cursor.fetchall()
        for row in rows:
            self.seller_list.insert('', tk.END, values=row)

        conn.close()

    def load_orders(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rohan136#@ch",
            database="shopping_db"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM ODR")
        rows = cursor.fetchall()
        for row in rows:
            self.order_list.insert('', tk.END, values=row)

        conn.close()

    def add_buyer(self):
        self.open_buyer_form("Add Buyer")

    def edit_buyer(self):
        selected_item = self.buyer_list.selection()
        if not selected_item:
            self.show_info_message("Please select a buyer to edit.")
            return
        buyer_id = self.buyer_list.item(selected_item, "values")[0]
        self.open_buyer_form("Edit Buyer", buyer_id)

    def delete_buyer(self):
        selected_item = self.buyer_list.selection()
        if not selected_item:
            self.show_info_message("Please select a buyer to delete.")
            return
        buyer_id = self.buyer_list.item(selected_item, "values")[0]

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rohan136#@ch",
            database="BYR"
        )
        cursor = conn.cursor()

        cursor.execute("DELETE FROM BUY WHERE B_id=%s", (buyer_id,))
        conn.commit()
        conn.close()

        self.buyer_list.delete(selected_item)

    def add_seller(self):
        self.open_seller_form("Add Seller")

    def edit_seller(self):
        selected_item = self.seller_list.selection()
        if not selected_item:
            self.show_info_message("Please select a seller to edit.")
            return
        seller_id = self.seller_list.item(selected_item, "values")[0]
        self.open_seller_form("Edit Seller", seller_id)

    def delete_seller(self):
        selected_item = self.seller_list.selection()
        if not selected_item:
            self.show_info_message("Please select a seller to delete.")
            return
        seller_id = self.seller_list.item(selected_item, "values")[0]

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rohan136#@ch",
            database="SLR"
        )
        cursor = conn.cursor()

        cursor.execute("DELETE FROM SELL WHERE S_id=%s", (seller_id,))
        conn.commit()
        conn.close()

        self.seller_list.delete(selected_item)

    def open_buyer_form(self, title, buyer_id=None):
        BuyerForm(self, title, buyer_id)

    def open_seller_form(self, title, seller_id=None):
        SellerForm(self, title, seller_id)

    def show_info_message(self, message):
        messagebox.showinfo("Information", message)

    def show_error_message(self, message):
        messagebox.showerror("Error", message)

class BuyerForm(tk.Toplevel):
    def __init__(self, parent, title, buyer_id=None):
        super().__init__(parent)
        self.parent = parent
        self.title(title)
        self.geometry("400x300")

        self.buyer_id = buyer_id

        self.create_widgets()

    def create_widgets(self):
        # Add form elements for buyer details (e.g., entry fields, labels, buttons)
        pass

class SellerForm(tk.Toplevel):
    def __init__(self, parent, title, seller_id=None):
        super().__init__(parent)
        self.parent = parent
        self.title(title)
        self.geometry("400x300")

        self.seller_id = seller_id

        self.create_widgets()

    def create_widgets(self):
        # Add form elements for seller details (e.g., entry fields, labels, buttons)
        pass

if __name__ == "__main__":
    app = AdminPage()
    app.mainloop()
