import scrapy


class RozetkaScraperSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua']
    start_urls = ['http://rozetka.com.ua/ua/']
    current_category = 'notebooks/c80004/'
    category, category_id = current_category.split('/')[0:2]

    def parse(self, response):
        pass