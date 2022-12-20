import scrapy


class RozetkaSpider(scrapy.Spider):
    name = 'rozetka'
    allowed_domains = ['rozetka.com.ua']
    start_urls = ['http://rozetka.com.ua/notebooks/c80004/']

    def get_count_of_pages(self, response):
        return int(response.css('.pagination__link::text').getall()[-1])

    def parse(self, response):
        for item in response.css('div.goods-tile'):
            yield{
                'good_id': item.css('.goods-tile__inner::attr(data-goods-id)').get(),
                'title': item.css('.goods-tile__title::text').get(),
                'rating': item.css('svg::attr(aria-label)').get(),
                'price': int(item.css('.goods-tile__price-value::text').get().replace(u'\xa0','').strip())
            }
        for page in range(2, self.get_count_of_pages(response)):
            current_page = f'{self.start_urls[0]}page={page}/'
            yield response.follow(current_page, callback=self.parse)

