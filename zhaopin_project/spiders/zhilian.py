# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from w3lib.html import remove_tags
from zhaopin_project.items import ZhilianProjectItem
from scrapy_redis.spiders import RedisSpider
# scrapy.Spider
class ZhilianSpider(RedisSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    # start_urls = ['https://jobs.zhaopin.com/']
    # 设置redis键值
    redis_key = 'daoun:zhilian'

    base_url = 'https://jobs.zhaopin.com/'

    def parse(self, response):
        all_list = response.xpath('//div[@class="content-list"]')
        # print(all_list)
        for all_data in all_list:
            href_list = all_data.xpath('./div[2]/a/@href').extract()
            # print(href_list)
            for href in href_list:
                hrefs = parse.urljoin(self.base_url, href)
                # print(hrefs)
                # 返回列表页的url
                html = scrapy.Request(url=hrefs, callback=self.data_list_page)
                yield html


    def data_list_page(self,response):
        # print('近函数')
        div_list = response.xpath('//ul[@class="search_list"]/li/div')
        # print(div_list)
        for div in div_list[2:]:
            info_href = div.xpath('./span/a/@href').extract_first()
            # print(info_href)
            if 'cc' not in info_href:
                yield scrapy.Request(url=info_href, callback=self.data_info,meta={'url':info_href})
        # 分页函数 找下一页 然后调用其本身
        next_join = response.xpath('//span[@class="search_page_next"]/a/@href')
        next = parse.urljoin(self.base_url, next_join)
        yield scrapy.Request(url=next, callback=self.data_list_page)


    def data_info(self, response):
        # 找到数据 存储到item里
        item = ZhilianProjectItem()
        title = response.xpath('//h1/text()').extract_first()
        money = response.xpath('//ul[@class="terminal-ul clearfix"]/li[1]/strong/text()').extract_first()
        # city = response.xpath('//ul[@class="terminal-ul clearfix"]/li[2]/strong/text()').extract_first()
        city = response.xpath('//div[@class="tab-cont-box"]//h2/text()').extract_first()
        dates = response.xpath('//span[@id="span4freshdate"]/text()').extract_first()
        gongzuo = response.xpath('//ul[@class="terminal-ul clearfix"]/li[4]/strong/text()').extract_first()
        jingyan = response.xpath('//ul[@class="terminal-ul clearfix"]/li[5]/strong/text()').extract_first()
        xueli = response.xpath('//ul[@class="terminal-ul clearfix"]/li[6]/strong/text()').extract_first()
        context = ', '.join(response.xpath('//div[@class="terminalpage-main clearfix"]/div/div/p/text()').extract()[:]).replace(', ','\n').strip()
        item['title'] = title
        item['money'] = money
        item['city'] = city
        item['dates'] = dates
        item['gongzuo'] = gongzuo
        item['jingyan'] = jingyan
        item['xueli'] = xueli
        item['context'] = context
        # print(title,money,dates,gongzuo,jingyan,xueli,city,context)
        yield item
