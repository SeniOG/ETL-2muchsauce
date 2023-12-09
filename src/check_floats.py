# The "convert_floats_cols" function trys to typecast each 'total price' column value to a float, 
# and sets it to 'None' if the value does not represent a float data type
def convert_floats_cols(test_file, float_cols):
    # Loop through each dictionary ROW in the 'test_file' list of dictionaries
    for d in test_file:
        # Loop through each KEY with the name 'total_price' and TRY to set it to a float data type
        for col in float_cols:
            # Check if the value is not None before attempting to convert
            if d[col] is not None:
                try:
                    d[col] = float(d[col])
                except ValueError:
                    # If there is a ValueError, set the value to None
                    d[col] = None
            else:
                # If the value is None, leave it as None
                d[col] = None
    # Return the updated list of dictionaries
    return test_file


# Calling "test_floats" function to cast each "total_price" column value to a FLOAT for each dictionary record
# test_floats = convert_floats_cols(test_file,['total_price'])

# Print out the newly updated CSV list of dictionary values with "total_price" column casted to FLOAT or None
# print('\n')
# time.sleep(2)
# print("CLEANING CUSTOMER CSV FILE - 'total_price' COLUMN VALUES ARE TYPE CASTED TO 'Float' or None:")
# time.sleep(5)
# print('')
# print(test_floats)
# print('\n')
# time.sleep(3)