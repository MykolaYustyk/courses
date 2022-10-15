'''
3. На основі попередньої функції (скопіюйте кусок коду) створити наступний скрипт:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і
      надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
'''

class NameLengthException(Exception):
    pass


class PasswordException(Exception):
    pass


class StatusException(Exception):
    pass


def name_password_validation(username, password, online_status = 'offline'):
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


list_of_users = [ ['user1', 'password1', 'online'],
                  ['us', 'password2', 'online'],
                  ['user3', 'psw', 'online'],
                  ['user4', 'password4', ''],
                  ['user5aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaapopo11111123333', 'password', 'online']   
                ]
status = ''

for current_user in list_of_users:
    try:
        name, password, online_status = current_user
        if name_password_validation(name, password, online_status):
            status = 'Ok'
            
    except (NameLengthException, PasswordException, StatusException) as exc:
        status = exc
    finally:
        print(f'Name: {name}\n Password: {password}\n Online status: {online_status}')
        print('-' * 20)
        print(f'Status: {status}') 
        print()
           