from scrapy.spiders import SitemapSpider


class WebstoreSitemapSpider(SitemapSpider):
    name = 'webstore'
    allowed_domains = ['chrome.google.com']
    sitemap_urls = ['https://chrome.google.com/webstore/sitemap']

    def parse(self, response):
        yield {'id': response.url.split('/')[-1],
               'name': response.css('h1.e-f-w::text').get(),
               'discription': response.css('div.C-b-p-j-Pb::text').get()
               }



