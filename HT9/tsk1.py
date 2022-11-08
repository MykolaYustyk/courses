'''
Банкомат 2.0
    - усі дані зберігаються тільки в sqlite3 базі даних у відповідних таблицях. Більше ніяких файлів. Якщо в попередньому завданні ви добре продумали структуру програми то у вас не виникне проблем швидко адаптувати її до нових вимог.
    - на старті додати можливість залогінитися або створити нового користувача (при створенні нового користувача, перевіряється відповідність логіну і паролю мінімальним вимогам. Для перевірки створіть окремі функції)
    - в таблиці з користувачами також має бути створений унікальний користувач-інкасатор, який матиме розширені можливості (домовимось, що логін/пароль будуть admin/admin щоб нам було простіше перевіряти)
    - банкомат має власний баланс
    - кількість купюр в банкоматі обмежена (тобто має зберігатися номінал та кількість). Номінали купюр - 10, 20, 50, 100, 200, 500, 1000
    - змінювати вручну кількість купюр або подивитися їх залишок в банкоматі може лише інкасатор
    - користувач через банкомат може покласти на рахунок лише суму кратну мінімальному номіналу що підтримує банкомат. В іншому випадку - повернути "здачу" (наприклад при поклажі 1005 --> повернути 5). Але це не має впливати на баланс/кількість купюр банкомату, лише збільшується баланс користувача (моделюємо наявність двох незалежних касет в банкоматі - одна на прийом, інша на видачу)
    - зняти можна лише в межах власного балансу, але не більше ніж є всього в банкоматі.
    - при неможливості виконання якоїсь операції - вивести повідомлення з причиною (невірний логін/пароль, недостатньо коштів на рахунку, неможливо видати суму наявними купюрами тощо.)
    - файл бази даних з усіма створеними таблицями і даними також додайте в репозиторій, що б ми могли його використати
'''

import sqlite3
import datetime

menu_entrance = {1: 'Ввійти', 2: 'Зареєструватись', 3: 'Вихід'}
menu_admin = {1: 'Переглянути баланс банкомата', 2: 'Додати кількість кюпюр', 3: 'Вихід' }
menu_user = {1: 'Переглянути баланс', 2: 'Поповнити баланс ', 3: 'Зняти кошти', 4: 'Вихід'}
coins = {'10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0}


def my_decorator(function):
    def wrapper(*args, **kwargs):
        print('-' * 25)
        result = function(*args, **kwargs)
        print('-' * 25)
        return result
    return wrapper


@my_decorator
def output_menu(menu):
    for key, val in menu.items():
        print(f'{key}. {val}')
            
        
def get_choice(menu):
    while True:
        choice = input('Ваш вибір: ')
        if choice.isdigit() and int(choice) in range(1, len(menu) + 1):
            choice = int(choice)
            break
        else:
            print(f'Вибір повинен бути числом в межах від 1 до {len(menu)}')
            print('Повторіть ввод.')
            print()

    return choice
  
    
def user_validation():
    result = [False, '']
    attemp = 1
    while True and attemp <= 3:
        username = input("Введіть Ваше ім'я: ")
        password = input("Введіть Ваш пароль: ")
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()            
            dict_result  = {row[0]: row[1] for row in cursor.execute("SELECT user, password FROM users ")} 
        if (username, password) in dict_result.items():
            result = [True, username]
            break
        else:
            print("Користувача з таким ім'ям і/або таким паролем немає.")
            if attemp < 3:
                print('Спробуйте ще раз ввести Ваші дані.')
                print(f'У Вас ще {3 - attemp} спроби(a)')
                attemp += 1
            else:
                print('Пройдіть реєстрацію')
                start()
    return result


def user_registration():
    print()
    print('Рeєстрація:')
    print('-' * 20)
    user_name = input('Name: ')
    password = input('Password: ')
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f'INSERT INTO users VALUES(?, ?, ?)', (user_name, password, 0))
        con.commit()
    return user_name

@my_decorator
def show_balance(user_name):
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()           
        cursor.execute(f"SELECT ballance FROM users WHERE user = '{user_name}' ")
        result = cursor.fetchone()[0]
        print(f'Ваш баланс дорівнює {result}')
    return result


@my_decorator
def print_new_balance(user_name, current_balance):
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f"UPDATE users SET ballance = {current_balance} WHERE user = '{user_name}'")
        con.commit()
    print(f'Ваш новий баланc становить {current_balance}')


def append_transaction(user_name, change_balance):
    now = datetime.datetime.now()
    now = now.strftime(" %d.%m.%Y %X")
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f"INSERT INTO user_trans VALUES(?, ?, ?)", (user_name, now, change_balance))
        con.commit()


def add_balance(user_name):
    current_balance = show_balance(user_name)
    attemp = 1
    while True and attemp <= 3:
        add_money = input('На яку суму бажаєте поповнити свій баланс? ')
        if add_money.isdigit():
            add_money = int(add_money)
            if add_money % 10 != 0:
                print(f'Вам повертається {add_money % 10}')
                add_money = add_money - (add_money % 10)                
            current_balance += int(add_money)
            append_transaction(user_name, f'+{add_money}')
            break
        else:
            print("Ви намагаєтесь поповнити баланс неприйнятними даними ")
            print('Введіть, будь ласка, іншу суму')
            print(f'У Вас ще {3 - attemp} спроби(a)')
            attemp += 1
    print_new_balance(user_name, current_balance)
    return


def get_money(user_name):
    current_balance = show_balance(user_name)
    attemp = 1
    while True and attemp <= 3:
        while True:
            sum_money = input('Яку суму бажаєте зняти? ')
            if sum_money.isdigit():
                sum_money = int(sum_money)
                break
            else:
                print('Сума провинна бути додатнім числом. Повторіть ввод')
        if 0 <= sum_money <= current_balance:
            current_balance -= sum_money
            append_transaction(user_name, f'-{sum_money}')
            break
        else:
            print('Ви намагаєтесь зняти суму, яка більше ніж є у Вас на рахунку')
            print('Введіть, будь ласка, іншу суму')
            print(f'У Вас ще {3 - attemp} спроби(a)')
            attemp += 1
    print_new_balance(user_name, str(current_balance))
    return
    

def show_bank_balance():
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        for row in cursor.execute(f'SELECT * FROM coins'):
            print(row[1], 'кюпюр номінала ', row[0])
        cursor.execute(f'SELECT * FROM coins')
        result = sum(coin * coin_count for coin, coin_count in cursor.fetchall())
        print(f'Баланс банкомата дорівнює: {result}')


def add_coins():
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT coin, coin_count FROM coins')
        for current_coin in cursor.fetchall():
            current_count = int(input(f'Скільки купюр номіналом {current_coin[0]} додаєте? '))
            coins_count_now = current_coin[1]
            cursor.execute(f'UPDATE coins SET coin_count = {current_count + coins_count_now} WHERE coin = {current_coin[0]}')
        con.commit()
        show_bank_balance()


def start():
    output_menu(menu_entrance)
    enter_choice = get_choice(menu_entrance)
    while True:
        if enter_choice == 1:
            valid, current_user = user_validation()
            if valid and current_user != 'admin':
                while True:
                    output_menu(menu_user)
                    user_choice = get_choice(menu_user)
                    if user_choice == 1:
                        show_balance(current_user) 
                    elif user_choice == 2:
                        add_balance(current_user)
                    elif user_choice == 3:
                        get_money(current_user)
                    elif user_choice == 4:
                        break
            elif valid and current_user == 'admin':
                while True:
                    output_menu(menu_admin)
                    admin_choice = get_choice(menu_admin)
                    if admin_choice == 1:
                        show_bank_balance()
                    elif admin_choice == 2:
                        add_coins()
                    elif admin_choice == 3:
                        break
        elif enter_choice == 2:
            current_user = user_registration()
            while True:
                output_menu(menu_user)
                user_choice = get_choice(menu_user)
                if user_choice == 1:
                    show_balance(current_user) 
                elif user_choice == 2:
                    add_balance(current_user)
                elif user_choice == 3:
                    get_money(current_user)
                elif user_choice == 4:
                    break
        elif enter_choice == 3:
            break
        break   

            
if __name__ == "__main__":
    start()
    print('Програма закінчила свою роботу')
