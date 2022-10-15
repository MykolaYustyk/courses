input_list =[0, 1, 12.3, 1, 'foo', [1, 2], True, 'foo', [1, 2], False, 2 ,False, True, 12, 12.3, 0]
import operator
result = []
for val in input_list:
    if (val not in result) and (val is not True) and (val is not False):
        result.append(val)
if True in input_list:
   result.append(True)
if False in input_list:
    result.append(False)
print(result)
for val in result:
    count = 0
    for i in range(len(input_list)):
        if input_list[i] is val:
            count += 1
    print(f'{val} -->  {count}   ' , end = '')
