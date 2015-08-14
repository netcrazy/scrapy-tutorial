#-*- coding: utf-8 -*-
'''
Created on 2014. 11. 24.

@author: ikchoi
'''

import scrapy
import datetime

from scrapy.selector import HtmlXPathSelector
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "masterqna"
    allowed_domains = ["masterqna.com"]
    start_urls = [
        "http://www.masterqna.com/android/questions?start=0",
        "http://www.masterqna.com/android/questions?start=20"
    ]

    def parse(self, response):
        for sel in response.xpath('//div[@class="qa-q-item-title"]'):
            url = "http://www.masterqna.com/android" + str(sel.xpath('a/@href').extract()[0])[1:]
            yield scrapy.Request(url, callback=self.parse_detail)
            

    def parse_detail(self, response):
        hxs = HtmlXPathSelector(response)
        item = DmozItem()
        item['title'] = response.xpath('//span[@class="entry-title"]/text()').extract()[0] #hxs. .xpath('//div[@class="qa-q-item-title"]/a/text()').extract()[0]
        item['link'] = response.url #"http://www.masterqna.com/android" + str(sel.xpath('//div[@class="qa-q-item-title"]/a/@href').extract()[0])[1:]
        
        item['date'] = str(datetime.datetime.now()) #str(self.get_datetime(  datetime.datetime.now()
                          #                   , sel.xpath('//span[@class="qa-q-item-when-data"]/text()').extract()[0])
                          # )
        
        item['desc'] = response.xpath('//div[@class="entry-content"]').extract()[0] #sel.xpath('text()').extract()
        return item


    def get_datetime(self, curdate, write_date):
        
        #rtn_date = ''

        #TODO... 날짜조작
        #try :
        #    tmp_date1 = write_date[-1].strip()
        #    
        #    if tmp_date1 == '분':
        #        rtn_date = write_date[:-1]
        #    elif tmp_date1 == '간':
        #        rtn_date = write_date[:-2]
        #    elif tmp_date1 == '일':
        #        rtn_date = write_date[:-1]
        #       
        #except :
        #    print '에러'
               
        
  
        
        return curdate
    
    
    
    
    