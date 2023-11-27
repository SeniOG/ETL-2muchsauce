from check_floats import convert_floats_cols
from format_date import format_date
from remove_duplicate import remove_duplicate
from remove_empty_value import clean_empty_data
from remove_sens_data import remove_sens
from seperate_item_price import item_price

# set file names and extract data
# raw_data = read_file('test_file.csv')

# test code
# print('\napp.py test\n')
# print(raw_data)
# print('\n end of app')


# transform data
def transform(raw_data):
    step_one = clean_empty_data(raw_data)
    step_two= remove_duplicate(step_one)
    step_three = remove_sens(step_two)
    step_four = convert_floats_cols(step_three,['total_price'])
    step_five = item_price(step_four, ['Basket'])
    step_six =  format_date(step_five,['date'])

    final_step = step_six
    return final_step

# # test code
# print('\n >>>>>TRANSFORMED DATA<<<<<<<<<<')
# transformed_data = transform()

# print('\n')
# for line in transformed_data:
#     print(f'{line}\n')


# load data