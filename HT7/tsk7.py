'''
7. Напишіть функцію, яка приймає 2 списки. Результатом має бути новий список, в якому знаходяться елементи першого списку, 
   яких немає в другому. Порядок елементів, що залишилися має відповідати порядку в першому (оригінальному) списку.
   Реалізуйте обчислення за допомогою генератора в один рядок.
    Приклад:
    array_diff([1, 2], [1]) --> [2]
    array_diff([1, 2, 2, 2, 3, 4], [2]) --> [1, 3, 4]
'''

def new_list(list1, list2):
    return [elem for elem in list1 if elem not in list2]


input_list1 = input('Input first list:').split(', ')
input_list2 = input('Input second list:').split(', ')
print(f'Result list: {list(map(int, new_list(input_list1, input_list2)))}')
