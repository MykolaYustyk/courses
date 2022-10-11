'''
5. Write a script to remove values duplicates from dictionary. Feel free to hardcode your dictionary.
'''
test_dict = {'a': 12, 'b': 3, 'c': 1, 'd': 5,'e': [1], 'f': "a", 'g': "a", 'h': 12}
print("The original dictionary is : " , test_dict)

temp = []
result_dict = {}
for key, val in test_dict.items():
    if val not in temp:
        temp.append(val)
        result_dict[key] = val

print("The dictionary after values removal : " , result_dict)