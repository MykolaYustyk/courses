'''
7. Написати функцію, яка приймає на вхід список (через кому), підраховує кількість однакових елементів у ньому
   і виводить результат. Елементами списку можуть бути дані будь-яких типів.
   Наприклад:
    1, 1, 'foo', [1, 2], True, 'foo', 1, [1, 2] ----> "1 -> 3, foo -> 2, [1, 2] -> 2, True -> 1"
'''


def counter_of_values(input_list):
    result = []
    out_result = ''

    for val in input_list:
        if (val not in result) and (val is not True) and (val is not False):
            result.append(val)
    if True in input_list:
        result.append(True)
    if False in input_list:
        result.append(False)

    for val in result:
        count = 0
        for i in range(len(input_list)):
            if input_list[i] is val:
                count += 1
        out_result += f'{val} --> {count}  '
    return out_result


input_list = [0, 1, 12.3, 1, 'foo', [1, 2], True, 'foo', [1, 2], False, 2, False, True, 12, 12.3, 0, 1]
print(counter_of_values(input_list))
