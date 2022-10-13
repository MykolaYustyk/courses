'''
 Write a script which accepts a <number> from user and print out a sum of the first <number> positive integers.
'''

num = int(input('Input integer number: '))
if num > 0:
    print(f'Sum of first positive numbers is: {sum(range(1, num+1))}')
else:
    print('Non correct input. Number must be greater then zero.')