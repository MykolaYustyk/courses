'''
1. Створіть функцію, всередині якої будуть записано СПИСОК із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - 
   необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
    якщо введено правильну пару ім'я/пароль - вертається True;
    якщо введено неправильну пару ім'я/пароль:
        якщо silent == True - функція повертає False
        якщо silent == False - породжується виключення LoginException (його також треба створити =))

'''
class LoginExeption(Exception):
    pass


def validation(user_name, user_password, silent = False):
    users_list = [('user1', '1234'),
                  ('user2', 'qwer'),
                  ('user3', 'asdf'),
                  ('user4', 'zxvc'),
                  ('user5', '1q2w')       
                 ]
    
    if (user_name, user_password) in users_list:
        result = True
    else:
        if silent == True:
            result = False
        else:
            raise LoginExeption('Something wrong !!! ')
    return result    
 
        
username = input('What your name?: ')
password = input('Input your password: ')
silent = bool(input('Silent: ').title())

try:
    print(f'Result is {validation(username, password, silent)}')
except LoginExeption as exc:
    print(exc)
finally:
    print('Stop'.center(8,'_'))
    