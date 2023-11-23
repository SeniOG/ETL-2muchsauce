import csv
from csv import DictReader
import time

# The read_file function is the Extraction phase of our ETL pipeline, and returns the CSV file as a list 
# of Dictionary records
def read_file(filename):    
    
    # Try to safely open the CSV file if it exists
    try:
    # Open the CSV file in read mode
        with open(filename, 'r') as csv_file:
    
    # Create a CSV reader object. ONLY use the "reader" class to read each row, otherwise DictReader will 
    # treat 1st row as KEYS
            csv_reader = csv.reader(csv_file)

            # Initialise the 1st dictionary list to be populated by looping through the csv_reader object
            initial_dictionary = []

            # Initialise the final dictionary list to be returned by the function
            final_dictionary = []

            # Extract each dictionary row/record (within the csv_reader object) to the initial_dictionary list
            for row in csv_reader:
                initial_dictionary.append(row)

            # Create the header column names for each field of the CSV file. These are also dictionary KEYS
            header = ['date','location','name','order','total_price','payment_type','card_no']

            # Loop through the row of dictionary records contained within the initial_dictionary list
            for values in initial_dictionary:
                # Zip column names & values to synchronise KEYS with corresponding VALUES for each dictionary row
                zipped_data = zip(header, values)
                # Convert the zipped KEY-VALUE pairs into dictionary format, & append to final_dictionary list.
                final_dictionary.append(dict(zipped_data))
        
        # return the final_dictionary list
        return final_dictionary
    
    # An Exception throws an error message if the file does not exist
    except FileNotFoundError:
        print('')
        time.sleep(2)
        print('Sorry - the filename you entered does not exist!')
        time.sleep(3)
        print('')
        print('EXITING THE APPLICATION...')
        time.sleep(2)
        print('')
        print('HAVE A PLEASANT FRIDAY! :)')
        print('')
        time.sleep(2)
        exit()

# Call the 'read_file' function in order to EXTRACT the data from the client's CSV file
# test_file = read_file('test_file.csv')

# Print out the final EXTRACTED data from CSV file, in Dictionary format.
# print('\n')
# time.sleep(2)
# print('RAW DATA FROM CUSTOMER CSV FILE - NO CHANGES MADE YET:')
# time.sleep(3)
# print('')
# print(test_file)
# time.sleep(2)

