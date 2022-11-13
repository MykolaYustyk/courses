'''
 Банкомат 4.0: переробіть программу з функціонального підходу програмування на використання класів.
 Додайте шанс 10% отримати бонус на баланс при створенні нового користувача.
'''
import sqlite3
import datetime
import math

start_menu_list = ['Вхід', 'Реєстрація', 'Вихід']
user_menu_list = ['Переглянути баланс', 'Поповнити баланс ', 'Зняти кошти', 'Історія транзакцій', 'До головного меню']
admin_menu_list = ['Переглянути баланс банкомата','Змінити кількість кюпюр','Історія транзакцій банкомата']

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
        attemp = 1
        while True and attemp <= 3:
            sum_money = input('Яку суму бажаєте зняти? ')
            if sum_money.isdigit() and (0 <= int(sum_money) <= current_balance or sum_money <= get_bank_balance()):
                sum_money = int(sum_money)
                current_balance -= sum_money
                self.append_transaction(f'-{sum_money}')
                break
            else:
                print('Ви намагаєтесь зняти суму, яка більше, ніж є у Вас на рахунку або більше ніж є в банкоматі')
                print('Введіть, будь ласка, іншу суму')
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


def user_routine(current_user):
    while True:
        user_menu.show()
        choice = user_menu.get_choice()
        if choice == 1:
            current_user.show_balance()
        elif choice == 2:
            current_user.add_balance()
        elif choice == 3:
            get_money(user)
        elif choice == 4:
            current_user.show_user_transaction_history()
        elif choice == 5:
            break


def admin_routine(user):
    while True:
        admin_menu.show()
        choice = admin_menu.get_choice()
        if choice == 1:
            do_admin_operations()
        elif choice == 2:
            user_routine(user)
        elif choice == 3:
            print()
        elif choice == 7:

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
                admin_routine(current_user)
        elif choice == 2:
            print('User registration')
        elif choice == 3:
            break
    

if __name__ == "__main__":
    start()
print('Програма закінчила свою роботу. ')