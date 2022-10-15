'''
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну
     цифру;
   - якесь власне додаткове правило :)
   Якщо якийсь із параметрів не відповідає вимогам - породити виключення із відповідним текстом.

'''

class NameLengthException(Exception):
    pass


class PasswordException(Exception):
    pass


class StatusException(Exception):
    pass


def name_password_validation(username, password, online_status):
    result = False
    if not(3 <= len(username) <= 50):
        raise NameLengthException('Iм\'я повинно бути не меншим за 3 символа і не більшим за 50')                              
    if not (len(password) >= 8 and password.isalnum() and not password.isdigit() and not password.isalpha()):
        raise PasswordException('Пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру')
    if online_status != 'online':
        raise StatusException('Користувач не онлайн')
    else:
        result = True
    return result

user_name = input('Input your name: ')
user_pass = input('Input password: ')
user_status = input('Status: ').lower()

try:
    rez = name_password_validation(user_name, user_pass, user_status) 
    print(f'Результат: {rez}')
except (NameLengthException, PasswordException, StatusException ) as exc:
    print(f'Помилка: {exc}')
finally:
    print(f'Програма завершила свою роботу.')       