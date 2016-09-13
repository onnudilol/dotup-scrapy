import scrapy
from dotup_scrapy.items import DotupItem
import re


class DotupSpider(scrapy.Spider):
    name = 'dotup'
    start_urls = ['http://dotup.org']
    # This regex extracts the filename from URLs
    id_re = re.compile(r'([0-9]+).[a-z0-9]{1,4}')

    def parse(self, response):
        for href in response.selector.xpath('/html/body/div/a/@href | //font[@size="-2"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_files)

    def parse_files(self, response):
        for sel in response.selector.xpath('//table[@summary="upinfo"]/tr[position()>1]'):
            url = response.urljoin(sel.xpath('td/a/@href').extract()[0][1:-5])

            item = DotupItem()
            item['id'] = int(self.id_re.search(url).group(1))
            item['url'] = url
            item['original'] = sel.xpath('td[6]/text()').extract()[0]

            yield item
