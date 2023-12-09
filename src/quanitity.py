def quantity(data):
    for record in data:
        record['order'] = record['order'].split(', ')
        items = []
        for item in record['order']:
            quantity = record['order'].count(item)
            item += f' - {quantity}'
            if quantity > 1 and item in items: continue
            items.append(item)
            
        record['order'] = items
      

    return data
    
def your_modification_function(data):
    for record in data:
        record['basket'] = record['basket'].split(', ')
        items = []
        for item in record['basket']:
            quantity = record['basket'].count(item)
            item += f' - {quantity}'
            if quantity > 1 and item in items: continue
            items.append(item)
            
        record['basket'] = items
        
        for i in range(len(record['basket'])):
            product_name, product_price, quantity = record['basket'][i].rsplit(' - ', 2)
                
            product_dict = {
                'product' : product_name,
                'price' : float(product_price),
                'quantity' : int(quantity)
            }
            record['basket'][i] = product_dict
            
    for row in data:
            del row["name"]
            del row["card_number"]

    return data