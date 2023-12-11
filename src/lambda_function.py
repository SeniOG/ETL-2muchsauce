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
                    'name' : arr[0],
                    'price' : float(product_price),
                    'flavour': arr[1],
                    'quantity' : int(quantity)
                }
            else:
                product_dict = {
                    'name' : product_name,
                    'price' : float(product_price),
                    'flavour': None,
                    'quantity' : int(quantity)
                }
            record['order'][i] = product_dict
    return data


