import csv
from dateutil import parser
from datetime import datetime

#Ensure date in one format
def format_date (dict_list, date_cols):
    formatted_data = []

    for dict in dict_list:
        for col in date_cols:
            try:
                date_object = parser.parse(dict[col], dayfirst=True)
                formatted_date = datetime.strftime(date_object,'%d/%m/%Y %I:%M %p') 
                dict[col] = formatted_date
            except ValueError as e:
                print(f"Error parsing value '{dict[col]}' in column '{col}': {e}")
                dict[col] = None

        formatted_data.append(dict_list)

    return formatted_data

# test = [{'date': '25/08/2021 09:00', 'location': 'Chesterfield', 'name': 'Richard Copeland', 'order': 'Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45', 'total_price': '5.2', 'payment_type': 'CARD', 'card_no': '5494173772652516'}, {'date': '08/25/2021 09:02', 'location': '', 'name': 'Scott Owens', 'order': 'Large Flavoured iced latte - Caramel - 3.25, Regular Flavoured iced latte - Hazelnut - 2.75, Regular Flavoured iced latte - Caramel - 2.75, Large Flavoured iced latte - Hazelnut - 3.25, Regular Flavoured latte - Hazelnut - 2.55, Regular Flavoured iced latte - Hazelnut - 2.75', 'total_price': '17.3', 'payment_type': 'CARD', 'card_no': '6844802140812058'},
#         {'date': '24/08/2021 07:00', 'location': 'Chesterfield', 'name': 'Richard Copeland', 'order': 'Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45', 'total_price': '5.2', 'payment_type': 'CARD', 'card_no': '5494173772652516'}, {'date': '08/25/2021 09:02', 'location': '', 'name': 'Scott Owens', 'order': 'Large Flavoured iced latte - Caramel - 3.25, Regular Flavoured iced latte - Hazelnut - 2.75, Regular Flavoured iced latte - Caramel - 2.75, Large Flavoured iced latte - Hazelnut - 3.25, Regular Flavoured latte - Hazelnut - 2.55, Regular Flavoured iced latte - Hazelnut - 2.75', 'total_price': '17.3', 'payment_type': 'CARD', 'card_no': '6844802140812058'}]

# format_date(test,['date'])


# format_date(test,['date'])

# print('\nFORMATED DATE - DATA LIST:')
# for line in test:
#      print(line)
