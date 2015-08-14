#-*- coding: utf-8 -*-
'''
Created on 2014. 11. 25.

@author: ikchoi
'''
import datetime
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
 
body = '<html><body><span>한글</span></body></html>'
 
c = Selector(text=body).xpath('//span/text()').extract()[0]
 
 
a = '\u0047'
print a.decode('unicode-escape')
  
b = '\uc548\ub4dc\ub85c\uc774\ub4dc \uae30\uae30 \uc5f0\uacb0 \ubb38\uc81c\uc785\ub2c8\ub2e4'
print b.decode('unicode-escape') 
  
print c


now = datetime.datetime.now()
print now