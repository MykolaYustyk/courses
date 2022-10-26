'''
6. Напишіть функцію,яка приймає рядок з декількох слів і повертає довжину найкоротшого слова.
   Реалізуйте обчислення за допомогою генератора в один рядок.
   
'''

def word_with_minimal_length(string):
    return min(len(word) for word in string.split())


input_string = input('Input string is: ')
print(f'Shortest word of string have length: {word_with_minimal_length(input_string)}')
