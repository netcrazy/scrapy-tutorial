#-*- coding: utf-8 -*-
"""
Created on 2015. 01. 13.
@author: ikchoi
"""

import scrapy
import datetime

from tutorial.items import JobItem

#기본 4000까지 크롤링함..
class DmozSpider(scrapy.Spider):
    name = "jobkorea"
    allowed_domains = ["jobkorea.co.kr"]
    start_urls = [

        "http://www.jobkorea.co.kr/List_GI/GI_Part_List.asp?Part_No=35300&page=1"
    ]

    def parse(self, response):
        
        items = []
        for sel in response.xpath('//div[@class="lgiSec lgiTplList lgiListNormal"]/table/tbody/tr'):

            item = JobItem()
            #기업명
            item['author'] = sel.xpath('td[@class="tplTitle"]/a/text()').extract()[0]
            #(기업명)제목
            item['title'] = sel.xpath('td[@class="tplTitle "]/div/a/@title').extract()[0]
            #링크
            item['link'] = "http://www.jobkorea.co.kr" + str(sel.select('td[@class="tplTitle "]/div/a/@href').extract()[0])
            item['date'] = str(datetime.datetime.now())
            #직무분야 \n 지역 \n 경력
            item['desc'] = sel.xpath('td[@class="tplTitle "]/div/p/text()').extract()[0] + '\n' + sel.select('td[@class="tplTitle "]/div/div/text()').extract()[0] + '\n' + sel.select('td[not(@*)]/text()').extract()[0] + '\n' + sel.select('td[not(@*)]/span/text()').extract()[0]
            
            items.append(item)
            
        return items
            
    
    
    
    
    