'''
1. Write a script that will run through a list of tuples and replace the last value for each tuple.
The list of tuples can be hardcoded.
The "replacement" value is entered by user.
The number of elements in the tuples must be different.
'''
list_of_tuples =[(1, 2, 3), (), ('a', 'b'), (100,), (12, 'a', 177, 400),(18,'aaaaa', 10, 12, 14),()]
result = []
print(f'Input list is: {list_of_tuples}')
replacement_value = input('Input replacement value: ')
for current_tuple in list_of_tuples:
    if current_tuple:
        current_tuple = list(current_tuple)
        current_tuple[-1] = replacement_value
        result.append(tuple(current_tuple))
    else:
        result.append(current_tuple)  

print(f'Output list is: {result}')
