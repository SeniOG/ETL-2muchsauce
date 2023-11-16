def remove_duplicate(filename):
    i = 0 
    while i < len(filename):
        dict1 = filename[i]
        j = i + 1

        while j < len(filename):
            dict2 = filename[j]
            
            if sorted(dict1.items()) == sorted(dict2.items()):
               filename.pop(j)

            else: j += 1

        i += 1

    return filename

list_of_dict = [
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 1, 'b': 2, 'c': 3},
    {'a': 4, 'b': 5, 'c': 6}]

remove_duplicate(list_of_dict)

print(list_of_dict)