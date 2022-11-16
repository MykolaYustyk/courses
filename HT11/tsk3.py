'''
 Банкомат 4.0: переробіть программу з функціонального підходу програмування на використання класів.
 Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.
'''
import sqlite3
import datetime
from i_want import i_want_to_get

start_menu_list = ['Вхід', 'Реєстрація', 'Вихід']
user_menu_list = ['Переглянути баланс', 'Поповнити баланс ', 'Зняти кошти', 'Історія транзакцій', 'До головного меню']
admin_menu_list = ['Переглянути баланс банкомата', 'Змінити кількість кюпюр', 'Історія транзакцій банкомата']
change_coins_menu_list = ['Додати купюри', 'Забрати купюри', 'В попереднє меню']


def my_decorator(function):
    def wrapper(*args, **kwargs):
        print()
        print('-' * 35)
        result = function(*args, **kwargs)
        print('-' * 35)
        return result

    return wrapper


class User:
    balance = 0
    first_time = False

    def __init__(self, name, password):
        self.name = name
        self.password = password

    @my_decorator
    def show_balance(self):
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT ballance FROM users WHERE user = '{self.name}' ")
            result = cursor.fetchone()[0]
            print(f'Ваш баланс дорівнює {result}')
        return result

    @my_decorator
    def print_new_balance(self, current_balance):

        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            cursor.execute(f"UPDATE users SET ballance = {current_balance} WHERE user = '{self.name}'")
            con.commit()
        print(f'Ваш новий баланc становить {current_balance}')

    def append_transaction(self, change_balance):
        now = datetime.datetime.now()
        now = now.strftime(" %d.%m.%Y %X")
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            cursor.execute(f"INSERT INTO user_trans VALUES(?, ?, ?)", (self.name, now, change_balance))
            con.commit()

    def add_balance(self):
        current_balance = self.show_balance()
        attemp = 1
        while True and attemp <= 3:
            add_money = input('На яку суму бажаєте поповнити свій баланс? ')
            if add_money.isdigit():
                add_money = int(add_money)
                if add_money % 10 != 0:
                    print(f'Вам повертається {add_money % 10}')
                    add_money = add_money - (add_money % 10)
                current_balance += int(add_money)
                if self.first_time:
                    current_balance *= 1.1
                    print('Вам як новому користувачеві нараховано бонус на перший внесок')
                    self.first_time = False
                self.append_transaction(f'+{add_money}')
                break
            else:
                print("Ви намагаєтесь поповнити баланс неприйнятними даними ")
                print('Введіть, будь ласка, іншу суму')
                print(f'У Вас ще {3 - attemp} спроби(a)')
                attemp += 1
        self.print_new_balance(current_balance)
        return

    def get_money(self):
        current_balance = self.show_balance()
        dict_of_notes = {}
        attemp = 1
        while True and attemp <= 3:
            while True:
                sum_money = input('Яку суму бажаєте зняти? ')
                if sum_money.isdigit() and (0 <= int(sum_money) <= current_balance or int(sum_money) < self.get_bank_balance()):
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
                            cursor.execute(f'''UPDATE coins SET coin_count = {current_coin[1] - val} 
                                                       WHERE coin = {key}''')
                    con.commit()
                current_balance -= sum_money
                self.append_transaction(f'-{sum_money}')
                break
            else:
                print('Нажаль банкомат не може видати зазначену вами суму')
                print('Повторіть ввод')
                print(f'У Вас ще {3 - attemp} спроби(a)')
                attemp += 1
        self.print_new_balance(str(current_balance))
        return

    @my_decorator
    def show_user_transaction_history(self):
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            cursor.execute(f"SELECT date, trans FROM user_trans WHERE user = '{self.name}'")
            print(f'Історія транзакцій користувача {self.name}')
            for row in cursor.fetchall():
                print(f'| {row[0]} | {row[1].rjust(8)} |')

    @staticmethod
    def get_bank_balance():
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            for row in cursor.execute(f'SELECT * FROM coins'):
                print(row[1], 'кюпюр номінала ', row[0])
            cursor.execute(f'SELECT * FROM coins')
            result = sum(coin * coin_count for coin, coin_count in cursor.fetchall())
        return result

    @my_decorator
    def show_bank_balance(self):
        result = self.get_bank_balance()
        print(f'Баланс банкомата дорівнює: {result}')


class Admin(User):

    def __init__(self):
        super().__init__('admin', 'admin')

    @staticmethod
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

    def coins_operations(self):
        while True:
            change_coins_menu.show()
            choice_menu = change_coins_menu.get_choice()
            if choice_menu == 1:
                self.add_coins()
            elif choice_menu == 2:
                self.get_coins()
            elif choice_menu == 3:
                break

    def add_coins(self):
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
            self.show_bank_balance()
            self.append_transaction(f'+{sum_of_coins}')

    def get_coins(self):
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
                cursor.execute(f'''UPDATE coins SET coin_count = {coins_count_now - current_count} 
                                           WHERE coin = {current_coin[0]}''')
            con.commit()
            self.show_bank_balance()
            self.append_transaction(f'- {sum_of_coins}')


class Menu:

    def __init__(self, list_menu):
        self.list_menu = list_menu

    @my_decorator
    def show(self):
        for i, val in enumerate(self.list_menu, 1):
            print(f'{i}. {val}')

    def get_choice(self):
        while True:
            current_choice = input('Ваш вибір: ')
            if current_choice.isdigit() and 1 <= int(current_choice) <= len(self.list_menu):
                break
            else:
                print(f'Вибір повинен бути в межах від 1 до {len(self.list_menu)}')
                print('Повторіть ввод.')

        return int(current_choice)


start_menu = Menu(start_menu_list)
user_menu = Menu(user_menu_list)
admin_menu = Menu(admin_menu_list + user_menu_list)
change_coins_menu = Menu(change_coins_menu_list)


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
            result = (True, username, password)
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
            if len(user_name) >= 6 and user_name.isalnum() and not user_name.isdigit() and not user_name.isalpha() \
                    and len(password) >= 6 and password.isalnum() and not password.isdigit() and not password.isalpha():
                new_user = User(user_name, password)
                break
            else:
                print('Ваш логін і/або пароль не відповідають вимогам.')
                print('Повторіть ввод')
        with sqlite3.connect('bankomat.db') as con:
            cursor = con.cursor()
            cursor.execute(f'SELECT user FROM users WHERE user = "{new_user.name}"')
            if cursor.fetchone() is None:
                cursor.execute(f'INSERT INTO users VALUES(?, ?, ?)', (new_user.name, new_user.password, 0))
                con.commit()
                break
            else:
                print('Користувач з таким логіном вже існує.')
                print('Повторіть ввод')
    return (new_user.name, new_user.password)


def user_routine(current_user):
    while True:
        user_menu.show()
        choice = user_menu.get_choice()
        if choice == 1:
            current_user.show_balance()
        elif choice == 2:
            current_user.add_balance()
        elif choice == 3:
            current_user.get_money()
        elif choice == 4:
            current_user.show_user_transaction_history()
        elif choice == 5:
            break


def admin_routine():
    while True:
        admin_menu.show()
        choice = admin_menu.get_choice()
        admin = Admin()
        if choice == 1:
            admin.show_bank_balance()
        elif choice == 2:
            admin.coins_operations()
        elif choice == 3:
            admin.show_bank_transaction_history()
        elif choice == 4:
            admin.show_balance()
        elif choice == 5:
            admin.add_balance()
        elif choice == 6:
            admin.get_money()
        elif choice == 7:
            admin.show_user_transaction_history()
        elif choice == 8:
            break


def start():
    while True:
        start_menu.show()
        choice = start_menu.get_choice()
        if choice == 1:
            valid, user, password = user_validation()
            current_user = User(user, password)
            if valid and user != 'admin':
                user_routine(current_user)
            if valid and user == 'admin':
                admin_routine()
        elif choice == 2:
            user, password = user_registration()
            current_user = User(user, password)
            current_user.first_time = True
            user_routine(current_user)
        elif choice == 3:
            break


if __name__ == "__main__":
    start()
print('Програма закінчила свою роботу. ')
