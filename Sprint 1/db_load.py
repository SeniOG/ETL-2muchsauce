import csv
import psycopg2
import os
import dotenv
from dotenv import load_dotenv
# Open the CSV file

import psycopg2
db_host = os.environ.get("mysql_host")
db_user = os.environ.get("mysql_user")
db_password = os.environ.get("mysql_pass")
db_name = os.environ.get("mysql_db")


with psycopg2.connect(
    host = db_host,
    database = db_name,
    user = db_user,
    password = db_password
) as connection:
# Establish connection to your PostgreSQL database
#conn = psycopg2.connect(
#    dbname="postgres",
#   user="postgres",
#   password="password",
#  host="localhost",
#  port="8080"
#)

# Create a cursor object using the connection


# Define the SQL statements as a single string
sql_query =  """
    CREATE TABLE Orders (
        Orders_id INT PRIMARY KEY,
        Order_date TIMESTAMP,
        Payment_type VARCHAR(255),
        Branch VARCHAR(255)
    );

    CREATE TABLE Products (
        Product_id INT PRIMARY KEY,
        product_name VARCHAR(255) NULL,
        Price INT NULL
    );

    CREATE TABLE Order_breakdown (
        Order_ID INT,
        Product_ID INT,
        Quantity VARCHAR(255),
        Branch VARCHAR(255),
        PRIMARY KEY (Order_ID, Product_ID),
        FOREIGN KEY (Order_ID) REFERENCES Orders(Orders_id),
        FOREIGN KEY (Product_ID) REFERENCES Products(Product_id)
    );
"""
connection.commit()
# Execute the entire query
cur.execute(sql_query)

# Commit the changes
#conn.commit()

# Close cursor and connection
cur.close()
#conn.close()



csv_file_path =  r'C:\Users\kamau\OneDrive\Documents\Python\2muchsauce\Sprint 1\new_separated_orders.csv'


# Read data from CSV and insert into tables
with open(new_seperate_orders, 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header if present in the CSV

    for row in reader:
        date = row[0]
        location = row[1]
        basket_data = row[2].split(',')  # Splitting the Basket data within the column

        total = row[3]
        payment = row[4]

        # Insert data into Orders table
        cur.execute("""
            INSERT INTO Orders (Order_date, Payment_type, Branch)
            VALUES (%s, %s, %s)
        """, (date, payment, location))
        # Note: Assuming 'Branch' corresponds to 'Location' and 'Payment_type' corresponds to 'Payment'

        # Fetch the last inserted Orders_id
        cur.execute("SELECT LASTVAL()")
        order_id = cur.fetchone()[0]

        for item in basket_data:
            product_name, price, quantity = item.split(':')  # Assuming each item is 'Product:Price:Quantity'
            price = int(price)
            quantity = int(quantity)

            # Insert data into Products table
            cur.execute("""
                INSERT INTO Products (product_name, Price)
                VALUES (%s, %s)
            """, (product_name, price))

            # Fetch the last inserted Product_id
            cur.execute("SELECT LASTVAL()")
            product_id = cur.fetchone()[0]

            # Insert data into Order_breakdown table
            cur.execute("""
                INSERT INTO Order_breakdown (Order_ID, Product_ID, Quantity, Branch)
                VALUES (%s, %s, %s, %s)
            """, (order_id, product_id, quantity, location))

# Commit the changes
conn.commit()

# Close cursor and connection
cur.close()