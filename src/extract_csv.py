import csv
from csv import DictReader

def read_csv(filename):
    with open(filename, newline='') as file:
        return list(csv.DictReader(file))
    
test_file = read_csv('test_file.csv')

print(test_file)           #To check if it reads correctly
print(len(test_file))      #To check each line in the csv file is read into 1 item in the list

