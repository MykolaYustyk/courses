'''
Write a script to check whether a value from user input is contained in a group of values.
'''
value_ = input('Input searching value: ')
if value_.isdigit():
    value_ = int(value_)
group_of_values = [1, 2, 'u', 'a', 4, True]
print(f'{value_} is in the {group_of_values} --> {value_ in group_of_values} ')