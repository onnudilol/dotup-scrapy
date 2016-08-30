from dotup_scrapy.spiders.dotup import DotupSpider


class DotupLightSpider(DotupSpider):
    name = 'dotup_light'
    start_urls = ['http://light.dotup.org']
