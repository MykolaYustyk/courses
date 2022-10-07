'''
 Write a script which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers.
'''

list_ = input('Input a sequence of comma-separated numbers ').split(', ')
tuple_ = tuple(list_)
print(f'Output list is: {list_}')
print(f'Output tuple is: {tuple_}')