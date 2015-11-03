#-*-coding:utf-8-*-
author__ = 'LJS'
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
    numArr = ['第一章','第二章','第三章','第四章','第五章','第六章','第七章','第八章','第九章','第十章']
    def parse(self, response):
        item = MysubscrptionItem()
        url = 'http://daily.zhihu.com'
        select = Selector(response)
        ribao = select.xpath('//div[@class="box"]')
        num = 0
        for eachRibao in ribao:
            s_url = eachRibao.xpath('a/@href').extract()
            for s in s_url:
                if num == 8:
		   exit()
		web_url = url+s_url[0]
                yield Request(web_url,meta={'num':num},callback=self.parse2)
                num = num + 1

    def parse2(self,response):
        filename = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+'.txt'
        item = MysubscrptionItem()
        zhang = response.meta['num']
        select = Selector(response)
		#作者
        author = select.xpath('//span[@class="author"]/text()').extract()
        #bio 个签
        bio = select.xpath('//span[@class="bio"]/text()').extract()
        #标题
        title = select.xpath('//h1[@class="headline-title"]/text()').extract()
        # filename = title[0]
        ribao = select.xpath('//div[@class="content"]/p/text()').extract()
        for x in ribao:
            with open(filename,'ab') as f:
            	f.write(self.numArr[zhang])
            	f.write("\n")
            	f.write(title[0].encode('utf-8'))
            	f.write("\n")
            	f.write(author[0].encode('utf-8'))
            	f.write("\n")
            	f.write(bio[0].encode('utf-8'))
            	f.write("\n")
                f.write(x.encode('utf-8'))
        # item['title'] = ''
        # item['content'] = ''
        # item['date'] = ''
        # item['geqian'] = ''

