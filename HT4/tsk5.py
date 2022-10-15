'''
 Калькулятор. Повинна бути 1 функцiя, яка приймає 3 аргументи - один з яких операцiя,
 яку зробити! Аргументи брати від юзера (можна по одному - окремо 2, окремо +, окремо 2;
 можна всі разом - типу 2 + 2). Операції що мають бути присутні: +, -, *, /, %, //, **.
'''
def calculation(first_digit, operation, second_digit) :
    result = None
    if operation == '+' :
        result = float(first_digit) + float(second_digit)
    elif operation == '-' : 
        result = float(first_digit) - float(second_digit)
    elif operation == "/":
        try:
            result = float(first_digit) / float(second_digit)
        except ZeroDivisionError:
            print('ERROR. Division by zero.')
    elif operation == "*" :
        result = float(first_digit) * float(second_digit)
    elif operation == '**':
        result = float(first_digit) ** float(second_digit)
    elif operation == '//':
        result = float(first_digit) // float(second_digit)  
    return result
    
print("Введіть числа і операцію розділені пробілами. \n Наприклад: 2 + 5. \n", end = '')
val1, operation, val2 = input().split()
res = calculation(val1, operation, val2)
if res is not None :
    print(f"= {res :.2f}")