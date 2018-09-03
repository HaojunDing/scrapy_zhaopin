# -*- coding: utf-8 -*-
import scrapy
import re
from w3lib.html import remove_tags
from zhaopin_project.items import QianchengProjectItem
from scrapy_redis.spiders import RedisSpider

# scrapy.Spider
class QianchengSpider(RedisSpider):
    name = 'qiancheng'
    allowed_domains = ['51job.com']
    # start_urls = ['https://search.51job.com/list/000000,000000,0000,00,9,99,%2B,2,4.html']
    redis_key = 'daoun:qiancheng'
    # lpush daoun:qiancheng https://search.51job.com/list/000000,000000,0000,00,9,99,%2B,2,4.html

    def parse(self, response):
        html = response.text
        a_req = re.compile(r'<a target="_blank" title=".*?href="(.*?)" onmousedown=')
        href_list = a_req.findall(html)
        for href in href_list:
            # print(href)
            yield scrapy.Request(url=href, callback=self.data_info)

        next = re.compile(r'</a></li><li class="bk"><a href="(.*?)">')
        next_href = next.search(html).group(1)
        # print(next_href)
        href_page = next_href.split('?')[0]

        print(href_page)
        yield scrapy.Request(url=href_page, callback=self.parse)

    def data_info(self,response):
        item = QianchengProjectItem()
        html = response.text
        req = re.compile(r'<h1 title="(.*?)"')
        title = req.search(html).group(1)
        yaoqiu_req = re.compile(r'"msg ltype" title="(.*?)"')
        yaoqiu = yaoqiu_req.search(html).group(1).replace('&nbsp;', '')
        context_req = re.compile('ss="bmsg job_msg inbox">(.*?)</div>',re.S)
        context = ','.join(remove_tags(context_req.search(html).group(1)).split()).replace('&nbsp;','')
        city_req = re.compile(r'bmsg inbox">.*?</span>(.*?)</p>',re.S)
        city = city_req.search(html).group(1)
        pirce_res = re.compile(r'</h1>.*?<strong>(.*?)</',re.S)
        pirce = pirce_res.findall(html)[0]

        item['title'] = title
        item['yaoqiu'] = yaoqiu
        item['pirce'] = pirce
        item['city'] = city
        item['context'] = context
        yield item
        # print(pirce)
        #
        # print(title)
        # print(yaoqiu)
        # print(city)
        # print(context)
        # # print('1231')
        # pass
