'''
2. Написати функцію, яка приймає два параметри: ім'я (шлях) файлу та кількість символів.
   Файл також додайте в репозиторій. На екран має бути виведений список із трьома блоками - символи з початку,
   із середини та з кінця файлу. Кількість символів в блоках - та, яка введена в другому параметрі. 
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі або,
   наприклад, файл із двох символів і треба вивести по одному символу, то що виводити на місці середнього
   блоку символів?). Не забудьте додати перевірку чи файл існує.
'''
import math
import os

def output_symbols(file_name, count):
    result = []
    with open(file_name, 'r') as input_file:
        string = input_file.read()
        print(f'Вміст файлу такий: {string}')
        if 0 < count <= len(string):
            result.append(string[:count])
            center = round(len(string)/2)
            result.append(string[center - math.floor(count/2):center + math.ceil(count/2)])
            result.append(string[-count:])
        elif count > len(string):
            result = 'Помилка. Кількість символів більша за довжину файла.'
        else:
            result = "помилка. Кількість символів не може бути від'ємним числом."
    return result


def main():
    input_filename = input("Введіть ім'я фаулу: ")
    input_count = int(input('Введіть кількість символів, яку хочете вивести: '))
    if input_filename in os.listdir():
        print(output_symbols(input_filename, input_count))
    else:
        print(f"Файлу з ім'ям {input_filename} в поточному католозі не знайдено.")

if __name__ == '__main__':
    main()