#  Write a script to remove empty elements from a list.
# Test list: [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]

test_list =  [(), ('hey'), ('',), ('ma', 'ke', 'my'), [''], {}, ['d', 'a', 'y'], '', []]
print(f'Input list: {test_list}')
result = [elem for elem in test_list if elem]
print(f'Result list: {result}')