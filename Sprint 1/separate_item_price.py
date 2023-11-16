from csv import DictReader
import csv

def read_file(filename):
    with open(filename,'r') as output:
        orders_reader = DictReader(output)
        orders = list(orders_reader)
        
    return orders
#def item_price(orders,order_columns):

def item_price(orders, order_columns):
    for row in orders:
        for col in order_columns:
            if col == 'Basket':
                split_items = row[col].split(', ')
                
                double_split_items = [item.split(' - ') for item in split_items]

                item_dicts = []  

                for item in double_split_items:
                    products = {}  
                    try:
                        products.update({
                            "name": item[0],
                            "flavour": item[1],
                            "price": item[2],
                        }) 
                    except IndexError:
                        products.update({
                            "name": item[0],
                            "flavour": None,
                            "price": item[1],
                        }) 
                    item_dicts.append(products)

                row[col] = item_dicts
                
    print(orders)
                
    #if you want to see the differences between the old dataset and the new dataset, save it to a new file
    with open('new_separated_orders.csv','w') as csvfile:
        fieldnames = ['Date', 'Location', 'Basket', 'Total', 'Payment']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)
                

data_list = read_file('new_orders.csv')
#data_list = item_price(data_list)
data_list = item_price(data_list, ['Basket'])