from urllib.parse import urljoin

import scrapy


class PetMarketSpider(scrapy.Spider):
    name = "petmarket"
    custom_settings = {
        'CLOSESPIDER_PAGECOUNT': 0,
        'CLOSESPIDER_ITEMCOUNT': 20
    }
    start_urls = [
        'https://petmarket.ua/zootovary-dlja-sobak/suhoj-korm-dlja-sobak/royal-canin-korm-dlja-sobak/dlja-schenkov/'
    ]
    allowed_domains = [
        'petmarket.ua'
    ]

    def parse(self, response):
        for product in response.xpath('//li[@class="catalog-grid__item"]'):
            yield {
                'link': urljoin(response.url, product.xpath('.//a[@title]/@href').get()),
                'price': product.xpath('.//div[@class="catalogCard-price"]/text()').get(),
                'img': urljoin(response.url, product.xpath('.//img[@class="catalogCard-img"]/@src').get()),
                'name': product.xpath('.//a[@title]/@title').get()
            }
