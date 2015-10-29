#coding:utf-8
__author__ = 'LJS'
import scrapy

from scrapy.spiders import CrawlSpider
from scrapy.http import Request
from scrapy.selector import Selector
from mysubscrption.items import MysubscrptionItem

class Zhihu(CrawlSpider):
    name = 'zhihu'
    start_urls = ['http://daily.zhihu.com/']

    url = 'http://daily.zhihu.com/story/7352098'

    def parse(self,response):
        Day = response.body
        # item = MysubscrptionItem()
        # selector = Selector(response)
        # Day = selector.xpath('//div[@class=container-fixed-width]')
        yield Day
        # print Day
