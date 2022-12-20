import scrapy


class WebstoreSitemapSpider(scrapy.Spider):
    name = 'webstore_sitemap'
    allowed_domains = ['chrome.google.com']
    start_urls = ['http://chrome.google.com/']

    def parse(self, response):
        pass
