'''
2. Викорисовуючи Scrapy, написати скрипт, який буде приймати на вхід назву та ID категорії (у форматі назва/id/)
із сайту https://rozetka.com.ua і буде збирати всі товари із цієї категорії, збирати по ним всі можливі дані (бренд,
 категорія, модель, ціна, рейтинг тощо) і зберігати їх у CSV файл (наприклад, якщо передана категорія
  mobile-phones/c80003/, то файл буде називатися c80003_products.csv)
'''

import os

def main():
    current_category = 'notebooks/c80004/'
    category_name, category_id = current_category.split('/')[:2]
    os.system(f'scrapy crawl rozetka -o {category_id}_products.csv')

if __name__=='__main__':
    main()