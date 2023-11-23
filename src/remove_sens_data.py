import csv
from csv import DictReader

def remove_sens(orders):
    
    for row in orders:
        row.pop('name', None)
        row.pop('card_no', None)

        
    return orders



    




        
        

    