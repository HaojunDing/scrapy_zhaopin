# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class lagouProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    pirce = scrapy.Field()
    city = scrapy.Field()
    jingyan = scrapy.Field()
    xueli = scrapy.Field()
    quanzhi = scrapy.Field()
    context = scrapy.Field()
    def store(self):
    # pass
        print('进到sql函数了')
        sql = 'insert into lagou (title, pirce, city, jingyan, xueli, quanzhi, context) values (%s, %s, %s, %s, %s, %s, %s)'
        print(sql)
        data = (self['title'], self['pirce'], self['city'], self['jingyan'], self['xueli'], self['quanzhi'], self['context'])
        return (sql, data)


class ZhilianProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    money = scrapy.Field()
    city = scrapy.Field()
    dates = scrapy.Field()
    gongzuo = scrapy.Field()
    jingyan = scrapy.Field()
    xueli = scrapy.Field()
    context = scrapy.Field()

    def store(self):
    # pass
        print('进到sql函数了')
        sql = 'insert into zhilian (title, money, city, dates, gongzuo, jingyan, xueli, context) values (%s, %s, %s, %s, %s, %s, %s, %s)'
        print(sql)
        data = (self['title'], self['money'], self['city'], self['dates'], self['gongzuo'], self['jingyan'], self['xueli'], self['context'])
        return (sql, data)

class QianchengProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    yaoqiu = scrapy.Field()
    city = scrapy.Field()
    context = scrapy.Field()
    pirce = scrapy.Field()
    def store(self):
    # pass
        print('进到sql函数了')
        sql = 'insert into qiancheng (title, yaoqiu, pirce, city, context) values (%s, %s, %s, %s, %s)'
        print(sql)
        data = (self['title'], self['yaoqiu'], self['pirce'], self['city'], self['context'])
        return (sql, data)