from extract_csv import read_file
import time

# Call the 'read_file' function in order to EXTRACT the data from the client's CSV file
test_file = read_file('test_file.csv')

# Print out the final EXTRACTED data from CSV file, in Dictionary format.
print('\n')
time.sleep(2)
print(test_file)
print('')
time.sleep(2)