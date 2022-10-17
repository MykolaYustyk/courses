'''
3. Користувач вводить змінні "x" та "y" з довільними цифровими значеннями.
   Створіть просту умовну конструкцію (звiсно вона повинна бути в тiлi ф-цiї),
   під час виконання якої буде перевірятися рівність змінних "x" та "y" 
   та у випадку нерівності - виводити ще і різницю.
    Повинні працювати такі умови (x, y, z заміність на відповідні числа):
    x > y;       вiдповiдь - "х бiльше нiж у на z"
    x < y;       вiдповiдь - "у бiльше нiж х на z"
    x == y.      відповідь - "х дорівнює y"
'''
def compare(x, y) : 
    if x > y :
        z = x - y
        return f'{x} більше ніж {y} на {z}'
    elif x < y : 
        z = y - x
        return f'{y} більше ніж {x} на {z}'
    else : 
        return f"{x} дорівнює {y}"

x, y = input('Введіть два числа, розділені комою, які бажаєте порівняти ').split(',')
if x.isdigit() and y.isdigit():
    print(compare(x, y))
else:
    print('Вхідні данні мають бути цілими числами.')