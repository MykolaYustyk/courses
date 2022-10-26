'''
3. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції. Тобто щоб її можна було використати у вигляді:
    for i in my_range(1, 10, 2):
        print(i)
    1
    3
    5
    7
    9
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
   P.P.P.S Не забудьте обробляти невалідні ситуації (типу range(1, -10, 5) тощо). Подивіться як веде себе стандартний range в таких випадках.
'''
class ValueErrorException(Exception):
    pass


def my_range(start, stop = None, step = None):
    if stop is None:
        stop = start
        start = 0
        step = 1
    if step is None:
        step = 1
           
    if start < stop and step > 0:
        while start < stop:
            yield start
            start += step
    elif stop < start and step <0:
        while start > stop:
            yield start
            start -= abs(step)
    else:
        raise ValueErrorException('Помилка введених даних. ')
                 

try:
    for i in my_range(10, -30, -5):
        print(i, end = ' ')
    print()       
except ValueErrorException as exc:
    print(exc)