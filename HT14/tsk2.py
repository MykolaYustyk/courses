'''
2. Створіть програму для отримання курсу валют за певний період.
- отримати від користувача дату (це може бути як один день так і інтервал - початкова і кінцева дати, продумайте механізм
  реалізації) і назву валюти
- вивести курс по відношенню до гривні на момент вказаної дати (або за кожен день у вказаному інтервалі)
- не забудьте перевірку на валідність введених даних
'''

import requests
from datetime import datetime, timedelta

list_of_valutes = ('USD', "GBP", 'CAD', "PLZ", 'SEK', "XAU")

first_date = input('Введіть першу дату в форматі дд.мм.рррр:')
second_date = input('Введіть другу дату в форматі дд.мм.рррр:')
while True:
  current_currency = input('Введіть назву валюти ')
  if current_currency.upper() in list_of_valutes:
    current_currency = current_currency.upper()
    break
  else:
    print(f'Помилка. Введіть іншу валюту. Банк обслуговує наступні валюти {list_of_valutes}')
print(35 * '-')
first_date_as_date = datetime.strptime(first_date, "%d.%m.%Y")
second_date_as_date = datetime.strptime(second_date, "%d.%m.%Y")
dif = (second_date_as_date - first_date_as_date).days
for day in range(dif+1):
    current_date = first_date_as_date + timedelta(days = day)
    current_date = datetime.strftime(current_date, '%d.%m.%Y')
    response = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?date={current_date}')
    print(f'{current_date}')
    for dict_val in response.json()["exchangeRate"]:
      if dict_val['currency'] == current_currency:
        print(f"{dict_val['currency']} Продаж: {dict_val['saleRate']:.2f} Покупка: {dict_val['purchaseRate']:.2f}")
    print(35 * '-')