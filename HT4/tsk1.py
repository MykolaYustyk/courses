'''
1. Написати функцiю season, яка приймає один аргумент (номер мiсяця вiд 1 до 12) та яка буде повертати
пору року, до якої цей мiсяць належить (зима, весна, лiто або осiнь).
У випадку некоректного введеного значення - виводити відповідне повідомлення.
'''
<<<<<<< HEAD

=======
>>>>>>> af041d30a19bf0e05ff3c974899142f933d24df5
def season(month):
    if month in [1, 2, 12]:
        return 'winter'
    elif month in [3, 4, 5]:
        return 'spring'
    elif month in [6, 7, 8]:
        return 'summer'
    elif month in [9, 10, 11]:
        return 'autumn'
    else:
        return 'Illegal number of month '
    
<<<<<<< HEAD
input_month = int(input('Input number of month: '))
print(f'It is {season(input_month)} month')
=======
input_month = input('Input number of month: ')
if input_month.isdigit():
    print(f"It's a {season(int(input_month))} month")
else:
    print('Wrong input. Data must be integer. ')
>>>>>>> af041d30a19bf0e05ff3c974899142f933d24df5
