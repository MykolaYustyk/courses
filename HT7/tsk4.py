'''
4. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає
   генератор,який буде повертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із
   послідовності - ітерація починається знову. Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   for elem in my_generator([1, 2, 3]):
       print(elem)
   1
   2
   3
   1
   2
   3
   1
   .......
'''


def my_generator(sequence):
    for item in sequence:
        yield item


input_sequence = '123'
while True:
    result = my_generator(input_sequence)
    for i in result:
        print(i)
