import csv
from csv import DictReader

import time

def read_file(filename):
    # Try to safely open the file if it exists
    try:
# Open the CSV file in read mode
        with open(filename, 'r') as csv_file:
    # Create a CSV reader object
            csv_reader = csv.reader(csv_file)

        # Define your own header or field names
            header = ['date','location','name','order','total_price','payment_type','card_no']  # Replace these with your actual column names

        # Initialize an empty list to store dictionaries
            data_list = []

            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Create a dictionary by zipping the header with the current row values
                row_dict = dict(zip(header, row))

                # Append the dictionary to the list
                data_list.append(row_dict)
            return data_list
        
    # An Exception throws an error message if the file does not exist
    except FileNotFoundError:
        print('Sorry - the filename you entered does not exist!')
        time.sleep(3)
        print('')
        print('EXITING THE APPLICATION...')
        time.sleep(2)
        print('')
        print('GOOD DAY! :)')
        exit()                   

test_file = read_file('test_file_backup.csv')

# print(test_file)
float_cols = []
for row in test_file: # loop through each row
    float_cols.append(['total_price']) # append the fifth column value to the list

def convert_floats_cols(test_file, float_cols):
    # loop through each dictionary in the list
    for d in test_file:
        # loop through each column name in float_cols
        for col in float_cols:
            # try to convert the value at that key to integer
            try:
                d[col] = float(d[col])
            # if there is a ValueError, set the value to None
            except ValueError:
                d[col] = None
    # return the updated list of dictionaries
    return test_file

test_file2 = convert_floats_cols(test_file,['total_price'])

print(test_file2)

