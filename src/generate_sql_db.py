from connect_to_db import *

def create_db_tables(connection, cursor) -> bool:
    print('create_db_tables started')
    try:
        #Drop tables if they exist
        # drop_tables_sql = (
        #     "DROP TABLE IF EXISTS Order_breakdown;",
        #     "DROP TABLE IF EXISTS Orders ;",
        #     "DROP TABLE IF EXISTS products;"
        # )
        
        # for command in drop_tables_sql:
        #     cursor.execute(command)
        
        # Create tables
        create_tables_sql = ("""
            CREATE TABLE IF NOT EXISTS Orders (
                Order_id VARCHAR(36) PRIMARY KEY,
                order_date TIMESTAMP,
                Payment_type VARCHAR(255),
                Branch VARCHAR(255)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS Products (
                Product_id VARCHAR(36) PRIMARY KEY,
                product_name VARCHAR(255) NOT NULL,
                Price DECIMAL(10,2) NOT NULL -- Changing data type to NUMERIC
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS Order_breakdown (
                Order_ID VARCHAR(36),
                Product_ID VARCHAR(36),
                Quantity NUMERIC,
                Flavour VARCHAR(36),
                Total_price DECIMAL(10,2),
                PRIMARY KEY (Order_ID, Product_ID),
                FOREIGN KEY (Order_ID) REFERENCES Orders(Order_id),
                FOREIGN KEY (Product_ID) REFERENCES Products(Product_id)
            );
            """
            )
        for command in create_tables_sql:
            cursor.execute(command)

        connection.commit()
        print('...committed')
        print('create_db_tables done')
        return True
    except Exception as ex:
        print(f'create_db_tables failed to generate table/s:\n{ex}')
        return False