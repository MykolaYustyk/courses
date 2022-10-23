'''
2. Створіть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат
(напр. інпут від юзера, результат математичної операції тощо). Також створiть четверту ф-цiю, яка всередині
викликає 3 попередні, обробляє їх результат та також повертає результат своєї роботи.
Таким чином ми будемо викликати одну (четверту) функцiю, а вона в своєму тiлi - ще 3.
'''

<<<<<<< HEAD
def greeting(name):
    return f'Hello, {name}'

def square(val):
    return val ** 2

def sum_of_squares(val1, val2):
    return square(val1) + square(val2)

=======

def greeting(name):
    return f'Hello, {name}'


def square(val):
    return val ** 2


def sum_of_squares(val1, val2):
    return square(val1) + square(val2)


>>>>>>> af041d30a19bf0e05ff3c974899142f933d24df5
def make_result(name, val1, val2):
    print(greeting(name))
    return f'Your result is: {sum_of_squares(val1, val2)}'

<<<<<<< HEAD
user_name = input('What your name? ')
a, b = map(int, input('Input two coma separated integers ').split(', '))
print(make_result(user_name, a, b))
=======

user_name = input('What your name? ')
a, b = input('Input two coma separated integers ').split(', ')
if a.isdigit() and b.isdigit():
    print(make_result(user_name, int(a), int(b)))
else:
    print('Input data must be integer.')
>>>>>>> af041d30a19bf0e05ff3c974899142f933d24df5
