clean_data_list = []

def clean_empty_data(filename):            
    for row in filename:
        if '' not in row.values():
            clean_data_list.append(row)
    return clean_data_list

test = [{'date': '25/08/2021 09:00', 'location': 'Chesterfield', 'name': 'Richard Copeland', 'order': 'Regular Flavoured iced latte - Hazelnut - 2.75, Large Latte - 2.45', 'total_price': '5.2', 'payment_type': 'CARD', 'card_no': '5494173772652516'}, {'date': '08/25/2021 09:02', 'location': '', 'name': 'Scott Owens', 'order': 'Large Flavoured iced latte - Caramel - 3.25, Regular Flavoured iced latte - Hazelnut - 2.75, Regular Flavoured iced latte - Caramel - 2.75, Large Flavoured iced latte - Hazelnut - 3.25, Regular Flavoured latte - Hazelnut - 2.55, Regular Flavoured iced latte - Hazelnut - 2.75', 'total_price': '17.3', 'payment_type': 'CARD', 'card_no': '6844802140812058'}]

clean_test = clean_empty_data(test)
print(clean_test)