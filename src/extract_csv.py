import csv
from csv import DictReader
import time

def read_file(filename):
    # Try to safely open the file if it exists
    try:
# Open the CSV file in read mode
        with open('test_file.csv', 'r') as csv_file:
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

test_file = read_file('test_file.csv')
print(test_file)