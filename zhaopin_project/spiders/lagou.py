# -*- coding: utf-8 -*-
import scrapy
import re
from w3lib.html import remove_tags
from zhaopin_project.items import lagouProjectItem
from scrapy_redis.spiders import RedisSpider


class LagouSpider(RedisSpider):
    name = 'lagou'
    allowed_domains = ['lagou.com']
    # start_urls = ['http://lagou.com/']
    redis_key = 'daoun:lagou'

    def parse(self, response):
        div_list = response.xpath('//div[@id="sidebar"]/div/div')
        for div in div_list:
            list = div.xpath('./div[2]/dl')
            for a in list:
                lists = a.xpath('./dd/a/@href')
                for href in lists:
                    url = href.extract()
                    print(url)
                    yield scrapy.Request(url=url, callback=self.info_list)

    def info_list(self, response):
        li_list = response.xpath('//ul[@class="item_con_list"]/li')
        for li in li_list:
            href = li.xpath('./div/div/div/a/@href').extract_first()
            print(href)
            yield scrapy.Request(url=href, callback=self.infos,dont_filter=True)
            # yield
        url = response.xpath('//*[@id="s_position_list"]/div[2]/div/a[6]/@href').extract_first()
        # print(url)
        try:
            yield scrapy.Request(url=url, callback=self.info_list)
        except Exception as e:
            print(e)

    def infos(self,response):
        item = lagouProjectItem()
        # print('~'*30)
        titles = response.xpath('//div[@class="position-content-l"]')
        title = titles.xpath('./div/span/text()').extract_first()
        pirce = titles.xpath('./dd/p/span[1]/text()').extract_first()
        city = titles.xpath('./dd/p/span[2]/text()').extract_first()
        jingyan = titles.xpath('./dd/p/span[3]/text()').extract_first()
        xueli = titles.xpath('./dd/p/span[4]/text()').extract_first()
        quanzhi = titles.xpath('./dd/p/span[5]/text()').extract_first()
        # context = response.xpath('//dd[@class="job_bt"]/text()')
        req = re.compile(r'class="job_bt">(.*?)</dd>',re.S)
        context = remove_tags(req.search(response.text).group(1))

        item['title'] = title
        item['pirce'] = pirce
        item['city'] = city
        item['jingyan'] = jingyan
        item['xueli'] = xueli
        item['quanzhi'] = quanzhi
        item['context'] = context
        yield item
        # print(title,pirce)
        # print('2')