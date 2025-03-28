import pymysql
import tkinter as tk
from datetime import datetime
from tkinter import ttk,messagebox

def insert_order(oid, ord_dt, amount):
    try:
        # Open connection to the database
        conn = pymysql.connect(host='localhost', user='root', password='cha&@#12', database='restaurent_management',charset="utf8")
        cursor = conn.cursor()
        
        # Create the INSERT query
        query = "INSERT INTO orders (oid, ord_dt, amount) VALUES (%s, %s, %s)"
        
        # Execute the query with the provided data
        cursor.execute(query, (oid, ord_dt, amount))
        
        # Commit the changes
        conn.commit()
        
        # Close the connection
        cursor.close()
        conn.close()
        
        print("Order inserted successfully.")
        
    except pymysql.MySQLError as e:
        print(f"Error: {e}")
        # Handle exception and potentially rollback if necessary
        '''if conn:
            conn.rollback()
            conn.close()'''


# Connect to the MySQL database
def connect_to_database():
    try:
        connection = pymysql.connect(
            host='localhost',  # Your MySQL server
            user='root',       # Your MySQL username
            password='cha&@#12', # Your MySQL password
            database='login' # Your database name
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to database: {e}")
        return None
    



# Fetch columns and data from the database
def fetch_data():
    connection = connect_to_database()
    if connection:
        try:
            cursor = connection.cursor()
            query = "SELECT * FROM entries"  # Your table name here
            cursor.execute(query)
            data = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]  # Extract column names
            return columns, data
        except pymysql.MySQLError as e:
            print(f"Error fetching data: {e}")
            return [], []
        finally:
            connection.close()
    return [], []

# Function to display data in Tkinter GUI
def display_data():
    columns, data = fetch_data()
    
    if not columns or not data:
        print("No data fetched")
        return
    
    # Create the Tkinter window
    root = tk.Tk()
    root.title("Database Data Display")

    # Create a Treeview widget to display the data
    tree = ttk.Treeview(root, columns=columns, show='headings')
    
    # Define the columns in the treeview (based on the database columns)
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100, anchor='center')

    # Insert the fetched data into the treeview
    for row in data:
        tree.insert("", "end", values=row)
    
    # Add the treeview to the window and pack it
    tree.pack(expand=True, fill=tk.BOTH)

    # Run the Tkinter main loop
    root.mainloop()

# Call the function to display data
#display_data()
