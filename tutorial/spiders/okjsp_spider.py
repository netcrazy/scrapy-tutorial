#-*- coding: utf-8 -*-
"""
Created on 2014. 11. 24.
@author: ikchoi
"""

import scrapy
import datetime

from scrapy.selector import HtmlXPathSelector
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "okjsp"
    allowed_domains = ["okjsp.net"]
    start_urls = [
        "http://www.okjsp.net/bbs?act=LIST&bbs=ajaxqna&keyfield=content&keyword=&pg=0"
    ]


    def parse(self, response):
        for sel in response.xpath('//tr[@class="body"]'):
            url = "http://www.okjsp.net" + str(sel.xpath('td[@class="subject"]/div/a/@href').extract()[0])
            yield scrapy.Request(url, callback=self.parse_detail)
            

    def parse_detail(self, response):
        item = DmozItem()
        item['title'] = response.xpath('//*[@class="subject"]/text()').extract()[0].strip()
        item['link'] = response.url
        item['date'] = str(datetime.datetime.now())
        item['desc'] = response.xpath('//*[@id="centent"]').extract()[0]
        return item
    
    
    
    