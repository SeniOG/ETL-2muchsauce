from csv import DictReader
import csv

def extraction():
    #remember to change the file name so it reads the correct data
    with open('test_file.csv','r') as output:
        orders_reader = DictReader(output)
        orders = list(orders_reader)
    
    for row in orders:
        del row['Name']
        del row['Card']
    
    print(orders)
    
    fieldnames = ['Date','Location','Basket','Total','Payment']
    
    #if you want to see the differences between the old dataset and the new dataset, save it to a new file
    with open('new_test_file.csv','w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(orders)
        
    return orders

#extraction()


    




        
        

    