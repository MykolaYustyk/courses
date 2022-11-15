'''
Банкомат 3.0
- реалізуйте видачу купюр за логікою видавання найменшої кількості купюр, але в межах наявних в банкоматі.
  Наприклад: 2560 --> 2х1000, 1х500, 3х20.
  Будьте обережні з "жадібним алгоритмом"! Видані купюри також мають бути “вилучені” з банкомату.
  Тобто якщо до операції в банкоматі було 5х1000, 5х500, 5х20 - має стати 3х1000, 4х500, 2х20.
- як і раніше, поповнення балансу користувача не впливає на кількість купюр. Їх кількість може змінювати лише інкасатор.
- обов’язкова реалізація таких дій (назви можете використовувати свої):
При запускі
Вхід
Реєстрація (з перевіркою валідності/складності введених даних)
Вихід
Для користувача
Баланс
Поповнення
Зняття
Історія транзакцій
Вихід на стартове меню
Для інкасатора
Наявні купюри/баланс тощо
Зміна кількості купюр
Повна історія операцій по банкомату (дії всіх користувачів та інкасаторів)
Вихід на стартове меню
'''
import sqlite3
import datetime
from i_want import i_want_to_get


main_menu = {1: 'Ввійти',
             2: 'Зареєструватись',
             3: 'Вихід'
            }
menu_admin = {1: 'Переглянути баланс банкомата',
              2: 'Змінити кількість кюпюр',
              3: 'Історія транзакцій банкомата',
              4: 'До попереднього меню'
              }
menu_user = {1: 'Переглянути баланс',
             2: 'Поповнити баланс ',
             3: 'Зняти кошти',
             4: 'Історія транзакцій',
             5: 'До попереднього меню'
             }
menu_user_admin = {1: 'Адміністратор', 2: 'Користувач', 3: 'Вихід в головне меню'}
menu_change_coins = {1: 'Додати купюри', 2: 'Забрати купюри', 3: 'В попереднє меню'}
coins = {'10': 0, '20': 0, '50': 0, '100': 0, '200': 0, '500': 0, '1000': 0}

def my_decorator(function):
    def wrapper(*args, **kwargs):
        print()
        print('-' * 35)
        result = function(*args, **kwargs)
        print('-' * 35)
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


@my_decorator
def show_user_transaction_history(user_name):
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT date, trans FROM user_trans WHERE user = '{user_name}'")
        print(f'Історія транзакцій користувача {user_name}')
        for row in cursor.fetchall():
            print(f'| {row[0]} | {row[1].rjust(8)} |')


@my_decorator
def show_bank_transaction_history():
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute("SELECT user from users")
        print('Історія транзакцій банкомата')
        rows = cursor.fetchall()
        for row in rows:
            print('-' * 34)
            print(f"Користувач: {row[0]}")
            print('-' * 34)
            cursor.execute(f"SELECT date, trans FROM user_trans WHERE user = '{row[0]}'")
            for row1 in cursor.fetchall():
                print(f'| {row1[0]} | {row1[1].rjust(8)}|')
            print('-' * 34)


@my_decorator
def show_bank_balance():
    result = get_bank_balance()
    print(f'Баланс банкомата дорівнює: {result}')


def add_coins():
    sum_of_coins = 0
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT coin, coin_count FROM coins')
        for current_coin in cursor.fetchall():
            while True:
                current_count = input(f'Скільки купюр номіналом {current_coin[0]} додаєте? ')
                if current_count.isdigit():
                    current_count = int(current_count)
                    break
                else:
                    print('Кількість повинна бути числом')
                    print('Повторіть ввод')
            sum_of_coins += current_coin[0] * current_count
            coins_count_now = current_coin[1]
            cursor.execute(f'''UPDATE coins SET coin_count = {current_count + coins_count_now} 
                               WHERE coin = {current_coin[0]}''')
        con.commit()
        show_bank_balance()
        append_transaction('admin', f'+{sum_of_coins}')


def get_coins():
    sum_of_coins = 0
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        cursor.execute(f'SELECT coin, coin_count FROM coins')
        for current_coin in cursor.fetchall():
            while True:
                while True:
                    current_count = input(f'Скільки купюр номіналом {current_coin[0]} забираєте? ')
                    if current_count.isdigit():
                        current_count = int(current_count)
                        break
                    else:
                        print('Кількість повинна бути числом')
                        print('Повторіть ввод')
                if current_count < current_coin[1]:
                    break
                else:
                    print('Ви намагаєтесь знати більше кюпюр ніж є в банкоматі')
                    print(f'Наразі їх номіналу {current_coin[0]} є {current_coin[1]}')
                    print('Повторіть ввод')

            sum_of_coins += current_coin[0] * current_count
            coins_count_now = current_coin[1]
            cursor.execute(f'''UPDATE coins SET coin_count = {coins_count_now-current_count} 
                                   WHERE coin = {current_coin[0]}''')
        con.commit()
        show_bank_balance()
        append_transaction('admin', f'- {sum_of_coins}')
        

def change_num_coins():
    while True:
        output_menu(menu_change_coins)
        choice_menu = get_choice(menu_change_coins)
        if choice_menu == 1:
            add_coins()
        elif choice_menu == 2:
            get_coins()
        elif choice_menu == 3:
            break



def get_bank_balance():
    with sqlite3.connect('bankomat.db') as con:
        cursor = con.cursor()
        for row in cursor.execute(f'SELECT * FROM coins'):
            print(row[1], 'кюпюр номінала ', row[0])
        cursor.execute(f'SELECT * FROM coins')
        result = sum(coin * coin_count for coin, coin_count in cursor.fetchall())
    return result


def get_money(user_name):
    dict_of_notes = {}
    current_balance = show_balance(user_name)
    attemp = 1
    while True and attemp <= 3:
        while True:
            sum_money = input('Яку суму бажаєте зняти? ')
            if sum_money.isdigit() and 0 <= int(sum_money) <= current_balance:
                sum_money = int(sum_money)                
                break
            else:
                print('Ви намагаєтесь зняти суму, яка більше, ніж є у Вас на рахунку.')
                print('Введіть, будь ласка, іншу суму')
                
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            for row in cursor.execute(f'SELECT * FROM coins'):
                dict_of_notes[row[0]] = row[1]
        result = i_want_to_get(sum_money, dict_of_notes)
        if result:
            print(result)
            with sqlite3.connect('bankomat.db') as con:
                cursor = con.cursor()
                cursor.execute(f'SELECT * FROM coins')
                for current_coin in cursor.fetchall():
                    for key, val in result.items():
                        cursor.execute(f'''UPDATE coins SET coin_count = {current_coin[1]-val} 
                                               WHERE coin = {key}''')
                con.commit()     
            current_balance -= sum_money
            append_transaction(user_name, f'-{sum_money}')
            break
        else:
            print('Нажаль банкомат не може видати зазначену вами суму')
            print('Повторіть ввод')              
            print(f'У Вас ще {3 - attemp} спроби(a)')
            attemp += 1
    print_new_balance(user_name, str(current_balance))
    return


def user_validation():
    result = (False, '')
    attemp = 1
    while True and attemp <= 3:
        username = input("Введіть Ваше ім'я: ")
        password = input("Введіть Ваш пароль: ")
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()            
            cursor.execute("SELECT user, password FROM users ")
        if (username, password) in cursor.fetchall():
            result = (True, username)
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
    print('Логін і пароль повинні складатись із літер і цифр і мати довжину не меньше як 6 символів.')
    while True:
        while True:
            user_name = input('Логін: ')
            password = input('Пароль: ')
            if len(user_name) >= 6 and user_name.isalnum() and not user_name.isdigit() and not user_name.isalpha()\
               and len(password) >= 6 and password.isalnum() and not password.isdigit() and not password.isalpha():
                break
            else:
                print('Ваш логін і/або пароль не відповідають вимогам.')
                print('Повторіть ввод')
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT user FROM users WHERE user = "{user_name}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO users VALUES(?, ?, ?)', (user_name, password, 0))
                con.commit()
                break
            else:
                print('Користувач з таким логіном вже існує.')
                print('Повторіть ввод')
    return user_name


def do_admin_operations():
    while True:
        output_menu(menu_admin)
        admin_choice = get_choice(menu_admin)
        if admin_choice == 1:
            show_bank_balance()
        elif admin_choice == 2:
            change_num_coins()
        elif admin_choice == 3:
            show_bank_transaction_history()
        elif admin_choice == 4:
            break


def user_routine(user):
    while True:
        output_menu(menu_user)
        user_choice = get_choice(menu_user)
        if user_choice == 1:
            show_balance(user)
        elif user_choice == 2:
            add_balance(user)
        elif user_choice == 3:
            get_money(user)
        elif user_choice == 4:
            show_user_transaction_history(user)
        elif user_choice == 5:
            break
        
        
def admin_routine(user):
    while True:
        print('Будете продовжувати роботу як: ')
        output_menu(menu_user_admin)
        user_admin_choice = get_choice(menu_user_admin)
        if user_admin_choice == 1:
            do_admin_operations()
        if user_admin_choice == 2:
            user_routine(user)
        if user_admin_choice == 3:
            break

 
def start():
    while True:
        output_menu(main_menu)
        enter_choice = get_choice(main_menu)
        if enter_choice == 1:
            valid, user = user_validation()
            if valid and user != 'admin':
                user_routine(user)
            if valid and user == 'admin':
                admin_routine(user)
        elif enter_choice == 2:
            new_user = user_registration()
            user_routine(new_user)            
        elif enter_choice == 3:
            break



if __name__ == '__main__':
    start()
    print('Програма закінчила свою роботу')
