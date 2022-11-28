'''
3. http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи: цитата, автор,
   інфа про автора тощо.
- збирається інформація з 10 сторінок сайту.
- зберігати зібрані дані у CSV файл
'''
import requests
from bs4 import BeautifulSoup as bs
import csv
BASE_URL ='https://quotes.toscrape.com'
FILE_FIELDS = ['Цитата', 'Автор', "Про автора"]
  
result = []
for current_page in range(1, 11): 
    print(f'Parse {current_page} page')   
    response = requests.get(f'{BASE_URL}/page/{current_page}/')    
    soup = bs(response.content, 'lxml')
    quotes = soup.select('.quote')
    for qvt in quotes:
        quote = qvt.find('span', class_='text').text
        author = qvt.find('small', class_='author').text
        author_discription = qvt.find('a').get('href')
        author_discription = BASE_URL + author_discription
        result.append((quote, author,author_discription))

with open('result.csv','w',newline='') as file:
    
    writer = csv.writer(file, delimiter=';')
    writer.writerow(FILE_FIELDS)
    writer.writerows(result)
