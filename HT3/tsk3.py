'''
3. Write a script to concatenate the following dictionaries to create a NEW one.
    dict_1 = {'foo': 'bar', 'bar': 'buz'}
    dict_2 = {'dou': 'jones', 'USD': 36}
    dict_3 = {'AUD': 19.2, 'name': 'Tom'}
'''

result = {}
dict_1 = {'foo': 'bar', 'bar': 'buz'}
dict_2 = {'dou': 'jones', 'USD': 36}
dict_3 = {'AUD': 19.2, 'name': 'Tom'}
result.update(dict_1)
result.update(dict_2)
result.update(dict_3)
print(f'Result dict: {result}')