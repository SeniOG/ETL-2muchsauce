import csv
import pandas as pd
import json
from csv import DictReader
import psycopg2
import os
import dotenv
from dotenv import load_dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Get database credentials from environment variables
db_host = os.environ.get("mysql_host")
db_user = os.environ.get("mysql_user")
db_password = os.environ.get("mysql_pass")
db_name = os.environ.get("mysql_db")

# Establish connection to PostgreSQL database
with psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password
) as connection:
    # Create a cursor object using the connection
    cur = connection.cursor()
    
    # # Define the SQL statements as a single string
sql_query =  """CREATE TABLE Orders (
    Orders_id SERIAL PRIMARY KEY,
    Order_date TIMESTAMP,
    Payment_type VARCHAR(255),
    Branch VARCHAR(255)
);

CREATE TABLE Products (
    Product_id SERIAL PRIMARY KEY,
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
); """

    # Execute the entire query
cur.execute(sql_query)

    # Commit the changes
connection.commit()

    # Close cursor and connection

file_path = 'new_separated_orders.csv'



csv_data = pd.read_csv(file_path)

# Correct date format
csv_data['Date'] = pd.to_datetime(csv_data['Date'], format='%d/%m/%Y %H:%M').dt.strftime('%Y-%m-%d %H:%M:%S')

# Iterate through the DataFrame and correct 'Basket' column content
for index, row in csv_data.iterrows():
    try:
        # Attempt to load the 'Basket' column as JSON
        basket_data = json.loads(row['Basket'].replace("'", "\"").replace('None', 'null'))
    except json.JSONDecodeError:
        # If JSON decoding fails, handle or log the error as needed
        print(f"JSON decoding error in row {index + 1}. Skipping this row.")
        continue

    # Update 'Basket' column with the corrected JSON string
    csv_data.at[index, 'Basket'] = json.dumps(basket_data)

# Establish connection to your PostgreSQL database
conn = psycopg2.connect(
    host=db_host,
    database=db_name,
    user=db_user,
    password=db_password)
cur = conn.cursor()

# Iterate through the corrected DataFrame for database insertion
for index, row in csv_data.iterrows():
    order_date = row['Date']
    payment_type = row['Payment']
    branch = row['Location']

    # Insert data into Orders table
    cur.execute("""
        INSERT INTO Orders (Order_date, Payment_type, Branch)
        VALUES (%s, %s, %s)
        RETURNING Orders_id
    """, (order_date, payment_type, branch))
    order_id = cur.fetchone()[0]

    # Retrieve basket data after correction
    basket_data = json.loads(row['Basket'])

    for item in basket_data:
        product_name = item['name']
        price = float(item['price'])
        quantity = 1  # Assuming quantity as 1 for each item

        # Insert data into Products table
        cur.execute("""
            INSERT INTO Products (product_name, Price)
            VALUES (%s, %s)
            RETURNING Product_id
        """, (product_name, price))
        product_id = cur.fetchone()[0]

        # Insert data into Order_breakdown table
        cur.execute("""
            INSERT INTO Order_breakdown (Order_ID, Product_ID, Quantity, Branch)
            VALUES (%s, %s, %s, %s)
        """, (order_id, product_id, quantity, branch))

# Commit changes and close connections
conn.commit()
cur.close()
conn.close()
