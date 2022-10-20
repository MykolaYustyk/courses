'''
1. Написати функцію <square>, яка прийматиме один аргумент - сторону квадрата,
і вертатиме 3 значення у вигляді кортежа: периметр квадрата, площа квадрата та 
його діагональ.
'''

def square(side):
    result =[]
    result.append(4 * side)
    result.append(side ** 2)
    result.append(side * 2 ** 0.5)
    return tuple(result)


input_side = input('Введіть сторону квадрата: ')
if input_side.isdigit():
    input_side = int(input_side)
    print(f'Периметр квадрата {square(input_side)[0]}')
    print(f'Площа квадрата {square(input_side)[1]}')
    print(f'Діагональ квадрата {square(input_side)[2]:.2f}')
else:
    print('Неправилльні данні. Повинно бути введене число.')