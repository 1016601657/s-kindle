#-*- coding: utf-8 -*-
__author__ = 'LJS'
import scrapy
import time
import re
from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from mysubscrption.items import MysubscrptionItem

class Zhihu(CrawlSpider):
    name = 'zhihu'
    start_urls = ['http://daily.zhihu.com/']
    def parse(self, response):
        item = MysubscrptionItem()
        url = 'http://daily.zhihu.com'
        select = Selector(response)
        ribao = select.xpath('//div[@class="box"]')
        for eachRibao in ribao:
            s_url = eachRibao.xpath('a/@href').extract()
            for s in s_url:
                web_url = url+s_url[0]
                yield Request(web_url,callback=self.parse2)
    def parse2(self,response):
        filename = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'.txt'
        item = MysubscrptionItem()
        select = Selector(response)
        ribao = select.xpath('//div[@class="content"]')
        dr = re.compile(r'<[^>]+>',re.S)
        dd = dr.sub('',ribao)
        print(dd)
        item['title'] = ''
        item['content'] = ''
        item['date'] = ''
        item['geqian'] = ''
        # with open(filename,'wb') as f:
        #     f.write(response.body)

