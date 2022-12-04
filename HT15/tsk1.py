'''

1. Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт "https://www.expireddomains.net/domain-lists/"\
   (з ним будьте обережні), вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів з усіма відповідними
   колонками - доменів там буде десятки тисяч (звичайно ураховуючи пагінацію). Всі отримані значення зберегти в CSV файл.
'''
import requests
from bs4 import BeautifulSoup as bs

BASE_URL = 'https://www.expireddomains.net/namecheap-auction-domains/'
responce = requests.get(BASE_URL, timeout=(10, 0.1))
soup = bs(responce.content, 'lxml')
print(soup)
    
