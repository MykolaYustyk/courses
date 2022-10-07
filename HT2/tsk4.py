'''
Write a script which accepts a <number> from user and then <number> times asks user for string input.
At the end script must print out result of concatenating all <number> strings.
'''

temp_list =[]
num = int(input('Input positive integer number of strings: '))
for i in range(num):
    temp_list.append(input(f'{i+1} string = '))
print('Out result:', ''.join(temp_list))