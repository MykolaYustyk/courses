'''
3. Написати функцию <is_prime>, яка прийматиме 1 аргумент - число від 0 до 1000,
и яка вертатиме True, якщо це число просте і False - якщо ні.
'''

def is_prime(num):
    if num <= 1:
        result = False
    else:
        result = True
    for i in range(2, num):
        if num % i == 0:
            result = False
            break  
    return result


input_num = input('Введіть число між 0 та 1000:')
if input_num.isdigit():
    input_num = int(input_num)
    if 0 <= input_num <= 1000:
        print(f'Це число просте? {is_prime(input_num)}')
    else:
        print('Введене неправильне число.')
else:
    print('Введені символи.')