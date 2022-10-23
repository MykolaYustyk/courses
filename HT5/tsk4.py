'''
4. Написати функцію <prime_list>, яка прийматиме 2 аргументи - початок і кінець
діапазона, і вертатиме список простих чисел всередині цього діапазона.
Не забудьте про перевірку на валідність введених даних та у випадку
невідповідності - виведіть повідомлення.
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

def prime_list(start, stop):
    result = [num for num in range(start, stop + 1) if is_prime(num)]
    return result


start, stop = map(int, input('Input star and stop: ').split())
print(F'Result list is: {prime_list(start, stop)}')  