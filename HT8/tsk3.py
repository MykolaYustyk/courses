'''
3. Програма-банкомат.
   Використовуючи функції створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.CSV>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.TXT>) та історію транзакцій
        (файл <{username_transactions.JSON>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено цифри;
        знімається не більше, ніж є на рахунку і т.д.).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Але якщо захочете реалізувати функціонал додавання нового користувача -
        не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - на початку роботи - логін користувача (програма запитує ім'я/пароль). Якщо вони неправильні - вивести повідомлення
        про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :))
      - потім - елементарне меню типн:
        Введіть дію:
           1. Подивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив, можете розширювати функціонал, але основне завдання має бути повністю реалізоване :)
    P.S. Увага! Файли мають бути саме вказаних форматів (csv, txt, json відповідно)
    P.S.S. Добре продумайте структуру програми та функцій
'''

import json
import datetime
import csv
import os
import time


def user_validation():
    result = [False, '']
    username = ''
    password = ''
    attemp = 1
    while True and attemp <= 3:
        username = input("Введіть Ваше ім'я: ")
        password = input("Введіть Ваш пароль: ")
        with open('users.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            dict_result = {row['user_name']: row['password'] for row in reader}

        if (username, password) in dict_result.items():
            result = [True, username]
            break
        else:
            print("Користувача з таким ім'ям і/або таким паролем немає.")
            if attemp < 3:
                print('Спробуйте ще раз ввести Ваші дані.')
                print(f'У Вас ще {3 - attemp} спроби(a)')
            attemp += 1

    return result


def show_balance(user_name):
    with open(user_name + "_balance.txt", 'r') as file_balance:
        current_balance = file_balance.read()
        return current_balance

def write_new_balance(user_name, current_balance):
    with open(f'{user_name}_balance.txt', 'w') as file_balance:
        file_balance.write(str(current_balance))
    return f'Ваш новий баланc становить {current_balance}'


def append_transaction(user_name, change_balance):
    with open(f'{user_name}_transaction.json', 'a') as file_json:
        now = datetime.datetime.now()
        json.dump({now.strftime(" %d.%m.%Y %X"): change_balance}, file_json)


def add_balance(user_name):
    current_balance = int(show_balance(user_name))
    print(f"Ваш баланс: {current_balance}") 
    attemp = 1
    while True and attemp <= 3:
        while True:
            add_money = input('На яку суму бажаєте поповнити свій баланс? ')
            if add_money.isdigit():
                add_money = int(add_money)
                break
            else:
                print('Сума провинна бути числом. Повторіть ввод')
        if add_money >= 0:
            current_balance += int(add_money)
            append_transaction(user_name, f'+{add_money}')
            break
        else:
            print("Ви намагаєтесь поповнити баланс від'ємною сумою")
            print('Введіть, будь ласка, іншу суму')
            print(f'У Вас ще {3 - attemp} спроби(a)')
            print()
            attemp += 1
    print(write_new_balance(user_name, str(current_balance)))
    print()
    return


def get_money(user_name):
    current_balance = int(show_balance(user_name))
    print(f"Ваш баланс: {current_balance}")
    attemp = 1
    while True and attemp <= 3:
        while True:
            sum_money = input('Яку суму бажаєте зняти? ')
            if sum_money.isdigit():
                sum_money = int(sum_money)
                break
            else:
                print('Сума провинна бути числом. Повторіть ввод')
        if 0 <= sum_money <= current_balance:
            current_balance -= sum_money
            append_transaction(user_name, f'-{sum_money}')
            break
        else:
            print('Ви намагаєтесь зняти невалідну суму. Вона повинна бути додатньою і не більше ніж є у Вас на рахунку')
            print('Введіть, будь ласка, іншу суму')
            print(f'У Вас ще {3 - attemp} спроби(a)')
            print()
            attemp += 1
    print(write_new_balance(user_name, str(current_balance)))
    print()
    return


def output_main_menu(user_name):
    choice = 0
    print()
    print(f'Привіт, {user_name}')
    print('-' * 20)
    print('Оберіть натупну дію:')
    print('1. Переглянути баланс')
    print('2. Поповнити баланс')
    print('3. Зняти кошти')
    print('4. Exit')
    print('-' * 20)
    print()
    while True:
        choice = int(input('Ваш вибір: '))
        if choice in (1, 2, 3, 4):
            break
        else:
            print('Вибір повинен бути в межах від 1 до 4')
    return choice


def start():
    valid, input_user_name = user_validation()
    while True:        
        if valid:
            choice_menu = output_main_menu(input_user_name)
            if choice_menu == 1:
                print(f'Ваш баланc: {show_balance(input_user_name)}')
                print('*' * 20)
            elif choice_menu == 2:
                add_balance(input_user_name)
            elif choice_menu == 3:
                get_money(input_user_name)
            elif choice_menu == 4:
                break
        else:
            break
    print('Програма завершила свою роботу. ')


if __name__ == "__main__":
    start()
