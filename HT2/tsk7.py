'''
Write a script to concatenate all elements in a list into a string and print it.
List must include both strings and integers and must be hardcoded.
'''
input_list = [1, 2, 3, '4', '5', '6', 10, 576, 'asdf']
print(''.join(str(elem) for elem in input_list))
