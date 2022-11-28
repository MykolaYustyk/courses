'''
1. Додайте до банкомату меню отримання поточного курсу валют за допомогою requests (можна використати відкрите API ПриватБанку)
'''

import requests

def get_course():
    responce = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
    euro, usd = responce.json()
    print('Поточний курс Євро: ')
    print('Покупка:', f"{float(euro['buy']):.2f}")
    print(f'Продаж: {float(euro["sale"]):.2f}')
    print(35 * '-')
    print('Поточний курс USD: ')
    print('Покупка:', f"{float(usd['buy']):.2f}")
    print(f'Продаж: {float(usd["sale"]):.2f}')

if __name__ == "__main__":
    get_course()
