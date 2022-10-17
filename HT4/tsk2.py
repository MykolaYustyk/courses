'''
2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині
викликає 3 попередні, обробляє їх результат та також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
'''


def greeting(name):
    return f'Hello, {name}'


def square(val):
    return val ** 2


def sum_of_squares(val1, val2):
    return square(val1) + square(val2)


def make_result(name, val1, val2):
    print(greeting(name))
    return f'Your result is: {sum_of_squares(val1, val2)}'


user_name = input('What your name? ')
a, b = input('Input two coma separated integers ').split(', ')
if a.isdigit() and b.isdigit():
    print(make_result(user_name, int(a), int(b)))
else:
    print('Input data must be integer.')
