# import csv
    
# def item_price(orders, order_columns):
#     for row in orders:
#         for col in order_columns:
#             if col == 'order':
#                 # Check if 'order' key exists in the row
#                 if col in row:
#                     split_items = row[col].split(', ')
#                     item_dicts = []
#                     for item in split_items:
#                         components = item.split(' - ')
                        
#                         quantity = count_item_quantity()
                        
#                         product = {
#                             "name": components[0],
#                             "flavour": components[1] if len(components) > 1 else None,
#                             "price": components[-1]
#                             "quantity": 
#                         }
#                         item_dicts.append(product)
#                     row[col] = item_dicts
#                 else:
#                     # Handle the case where 'order' key is not present
#                     row[col] = None  # or any other default value
                
#     return orders

# def item_price(orders, order_columns):
#     for row in orders:
#         for col in order_columns:
#             if col == 'order':
#                 # Check if 'order' key exists in the row
#                 if col in row:
#                     split_items = row[col].split(', ')
#                     item_dicts = []
#                     for item in split_items:
#                         components = item.split(' - ')

#                         # Call count_item_quantity to get the quantity for each item
#                         quantity_count = count_item_quantity(components)
                        
#                         product = {
#                             "name": components[0],
#                             "flavour": components[1] if len(components) > 1 else None,
#                             "price": float(components[-1]),
#                             "quantity": quantity_count.get(components[0], 0)
#                         }
#                         item_dicts.append(product)
#                     row[col] = item_dicts
#                 else:
#                     # Handle the case where 'order' key is not present
#                     row[col] = None  # or any other default value
                
#     return orders

    
def item_price(data): #restructures the order field into a list of dictionaries
    for record in data:
        record['order'] = record['order'].split(', ')
        items = []
        for item in record['order']:
            quantity = record['order'].count(item)
            item += f' - {quantity}'
            if quantity > 1 and item in items: continue
            items.append(item)
        record['order'] = items
        for i in range(len(record['order'])):
            product_name, product_price, quantity = record['order'][i].rsplit(' - ', 2)
            if '-' in product_name:
                arr = product_name.split(' - ')
                
                product_dict = {
                    'product' : arr[0],
                    'price' : float(product_price),
                    'flavour': arr[1],
                    'quantity' : int(quantity)
                }
            else:
                product_dict = {
                    'product' : arr[0],
                    'price' : float(product_price),
                    'flavour': None,
                    'quantity' : int(quantity)
                }
            record['order'][i] = product_dict
    return data

# def item_price(orders, order_columns):
#     for row in orders:
#         for col in order_columns:
#             if col == 'order':
#                 # Check if 'order' key exists in the row
#                 if col in row:
#                     split_items = row[col].split(', ')
#                     item_dicts = []
#                     for item in split_items:
#                         components = item.split(' - ')
#                         quantity_and_price = components[-1].split(' ')
                        
#                         # Extract quantity and price
#                         quantity = float(quantity_and_price[0]) if quantity_and_price else None
#                         price = float(quantity_and_price[-1]) if quantity_and_price else None
                        
#                         product = {
#                             "name": components[0],
#                             "flavour": components[1] if len(components) > 1 else None,
#                             "quantity": quantity,
#                             "price": price
#                         }
#                         item_dicts.append(product)
#                     row[col] = item_dicts
#                 else:
#                     # Handle the case where 'order' key is not present
#                     row[col] = None  # or any other default value
                
#     return orders
