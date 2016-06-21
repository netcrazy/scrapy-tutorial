#-*- coding: utf-8 -*-
import scrapy.cmdline
import sys

def masterqna():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'masterqna', '-o', '../masterqna.json'])

def jobkorea():
    scrapy.cmdline.execute(argv=['scrapy', 'crawl', 'jobkorea', '-o', '../jobkorea.json'])
    
#TODO cmd말구     
    
#C:/Python> python main.py처럼 직접수행시 if문 다음문장이 수행되게 하고, 그 외 이파일을 모듈로 불러쓸때는 수행되지 않게 한다.
if  __name__ =='__main__':
    
    args = " {masterqna|okjsp|jobkorea}"
    
    if len(sys.argv) != 2:
        print "usage : " + sys.argv[0] + args
        exit()
    
    if sys.argv[1] == 'masterqna':
        masterqna()
    elif sys.argv[1] == 'jobkorea':
        jobkorea()        