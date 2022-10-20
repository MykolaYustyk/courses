'''
5. Написати функцію <fibonacci>, яка приймає один аргумент і виводить всі числа Фібоначчі,
що не перевищують його.
'''

def fibonacci(digit):
    fibonacci_list = [1, 1]
    i = 1
    fibonacci_current = 1
    while fibonacci_current <= digit:
        i += 1
        fibonacci_current = fibonacci_list[i-1] + fibonacci_list[i-2]
        fibonacci_list.append(fibonacci_current)
    fibonacci_list.pop() 
    return fibonacci_list

n = int(input('Input integer value : '))
print("Fibonacci list is: ", fibonacci(n))    