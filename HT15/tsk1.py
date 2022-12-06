'''
1. Викорисовуючи requests/BeautifulSoup, заходите на ось цей сайт "https://www.expireddomains.net/domain-lists/",
   вибираєте будь-яку на ваш вибір доменну зону і парсите список  доменів з усіма відповідними колонками - доменів
   там буде десятки тисяч (звичайно ураховуючи пагінацію). Всі отримані значення зберегти в CSV файл.
'''
import csv

import requests
from bs4 import BeautifulSoup as bs

FILE_FIELDS = ['domain', 'bl', 'domainpop', 'abirth', 'aentries', 'dmoz', 'statuscom', 'statusnet', 'statusorg',
               'statusde', 'statustld_registered', 'related_cnobi', 'price']
BASE_URL = 'https://www.expireddomains.net/dan-buy-now-com-domains/'
user_agent = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0\
                 Safari/537.36 OPR/92.0.0.0'
}
result = []


def parse_first_page(BASE_URL):
    page = requests.get(BASE_URL, headers=user_agent).content
    page_soup = bs(page, 'lxml')
    domains = page_soup.select('.base1 tbody tr')
    for domain in domains:
        result.append(tuple(domain.text.split('\n')[1:-1]))
    return result


def parse_next_pages(BASE_URL):
    for page_number in range(2, 11):
        home_page = BASE_URL + f'?start={25 * (page_number - 1)}#listing'
        print(f'Parse page # {page_number}')
        result.extend(parse_first_page(home_page))
    return result


def write_info_to_csv(result):
    with open('domains.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(FILE_FIELDS)
        writer.writerows(result)


if __name__ == "__main__":
    parse_first_page(BASE_URL)
    parse_next_pages(BASE_URL)
    write_info_to_csv(result)
