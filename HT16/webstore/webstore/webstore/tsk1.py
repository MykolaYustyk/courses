from spiders.webstore import WebstoreSitemapSpider
from scrapy.crawler import CrawlerProcess


def main():
    c = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'webstore_app.csv',
    })
    c.crawl(WebstoreSitemapSpider)
    c.start()


if __name__ == '__main__':
    main()
