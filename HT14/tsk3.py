'''
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор,
   інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
'''
import requests
from bs4 import BeautifulSoup as bs
import csv

BASE_URL = 'https://quotes.toscrape.com'
FILE_FIELDS = ['Quote', 'Author', "Birth date", 'Birth place', 'Tags']


def get_author_info(link):
    response = requests.get(link)
    soup = bs(response.content, 'lxml')
    date_of_born = soup.find('span', class_='author-born-date').text
    born_location = soup.find('span', class_='author-born-location').text
    return [date_of_born, born_location]


def get_tags(qvt):
    result = []
    tags = qvt.select('.tag')
    for tag in tags:
        result.append(tag.text)
    return ', '.join(result)


def get_info_from_quote(qvt):
    result = []
    quote = qvt.find('span', class_='text').text.strip('”').strip('“')
    author = qvt.find('small', class_='author').text
    author_information_link = qvt.find('a').get('href')
    author_information_link = BASE_URL + author_information_link
    author_info = get_author_info(author_information_link)
    tags = get_tags(qvt)
    result.append((quote, author, *author_info, tags))
    return result


def get_info_from_pages(soup):
    result = []
    quotes = soup.select('.quote')
    for qvt in quotes:
        result.append(get_info_from_quote(qvt))
    return result


def site_parser():
    result = []
    for current_page in range(1, 11):
        print(f'Parse {current_page} page')
        response = requests.get(f'{BASE_URL}/page/{current_page}/')
        soup = bs(response.content, 'lxml')
        result.append(get_info_from_pages(soup))


def write_info_to_csv(result):
    with open('result.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(FILE_FIELDS)
        writer.writerows(result)


if __name__ == '__main__':
    site_parser()
