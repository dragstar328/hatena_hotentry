# -*- coding: utf-8 -*-
import scrapy
from hatena_hotentry.items import HatenaHotentryItem

class HotentrySpider(scrapy.Spider):
    name = "Hotentry"
    allowed_domains = ["feeds.feedburner.com"]
    start_urls = ['http://feeds.feedburner.com/hatena/b/hotentry']

    def parse(self, response):
        item = HatenaHotentryItem()
        response.selector.remove_namespaces()
        
        item['title'] =response.xpath('//item/title/text()').extract()
        item['link'] =response.xpath('//item/link/text()').extract()
        
        yield item
