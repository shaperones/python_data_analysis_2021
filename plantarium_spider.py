from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scraping.items import ScrapingItemLoader, ScrapingItem


class Taxonomy(CrawlSpider):
    name = "Taxonomy"
    start_urls = ["https://www.plantarium.ru/page/samples/taxon/44760.html"]

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths=['//div[@class="found-item-lat-name"]/a/@href'],
            allow_domains='plantarium.ru',
            allow='https://www.plantarium.ru/page/samples/taxon/\d+.html'
        ),
            callback='parse_item'
        )
    )

    def parse_item(self, response):
        selector = Selector(response)
        l = ScrapingItemLoader(ScrapingItem(), selector)
        l.add_value('url', response.url)
        l.add_
