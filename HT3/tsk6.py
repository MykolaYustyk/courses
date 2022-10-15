'''
6. Write a script to get the maximum and minimum VALUE in a dictionary.
'''

inp_dict ={'a': 1, 'b':2, 'd':100, 'c': 'aaaa', 'e': 'h2332jjkhjkj'}
print(f'Input dict: {inp_dict}')
print(f'Minimal value of dict: {min(num for num in inp_dict.values() if str(num).isdigit())}')
print(f"Maximal value of dict: {max(num for num in inp_dict.values() if str(num).isdigit())}")