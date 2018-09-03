# -*- coding: utf-8 -*-

# Scrapy settings for zhaopin_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'zhaopin_project'

SPIDER_MODULES = ['zhaopin_project.spiders']
NEWSPIDER_MODULE = 'zhaopin_project.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'zhaopin_project (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
  #拉钩 'Cookie': 'JSESSIONID=ABAAABAAAGGABCB67CE69574088FABB85AE5201A724183B; user_trace_token=20180830160353-f943a2a8-c31d-4e5c-8ff5-4c0cd30c4dd6; _ga=GA1.2.88218204.1535616236; _gid=GA1.2.567678452.1535616236; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535616236; LGUID=20180830160355-3dd5f7f5-ac2b-11e8-b30a-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_navigation; LGSID=20180830190003-d8a88d82-ac43-11e8-be13-525400f775ce; X_HTTP_TOKEN=702ce4a93df2357b487672d838a8328d; SEARCH_ID=26fc099f411c428eb01049b5d82ebc4a; _gat=1; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1535628770; LGRID=20180830193248-6c20275a-ac48-11e8-b30a-5254005c3644',
  #拉钩 'Referer' :'https://www.baidu.com/link?url=K8nQuAoO_0wL-QyZVTOebhqFgd9jtTCeXZbdz_p5kRi&wd=&eqid=896ff90a0000d304000000055b87d627'
  # 'Cookie': 'sts_deviceid=1658b40c4a6202-0be622fb801055-9393265-1049088-1658b40c4a7157; sts_sg=1; sts_sid=1658b40dcee31d-0478ede1068878-9393265-1049088-1658b40dcefa7f; zp_src_url=https%3A%2F%2Fwww.google.co.kr%2F; dywea=95841923.3417988215127260000.1535639609.1535639609.1535639609.1; dywec=95841923; dywez=95841923.1535639609.1.1.dywecsr=google.co.kr|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utma=269921210.206463636.1535639611.1535639611.1535639611.1; __utmc=269921210; __utmz=269921210.1535639611.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; stayTimeCookie=1535639612451; referrerUrl=https%3A//www.zhaopin.com/; ZP_OLD_FLAG=false; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1535639753; LastCity=%E5%85%A8%E5%9B%BD; LastCity%5Fid=489; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; adfbid=0; adfbid2=0; dyweb=95841923.4.10.1535639609; __utmb=269921210.4.10.1535639611; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%229a58527e-3a91-415b-ace5-fd41f210121d-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=5; GUID=89525d5a750d4303acec5ea35f96b4c1; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1535639915',
  # 'Referer': 'https://www.google.co.kr/'
  #前程无忧 Referer: https://www.baidu.com/link?url=GcsSWxjYOi_yUtw6-F6f8N1l2olz6o2Mho68aXWlOdS&wd=&eqid=e538351e00021335000000055b88b9e1
   # 'Cookie': 'partner=www_baidu_com; 51job=cenglish%3D0%26%7C%26; guid=15356871462648190079; slife=lastvisit%3D010000%26%7C%26; nsearch=jobarea%3D%26%7C%26ord_field%3D%26%7C%26recentSearch0%3D%26%7C%26recentSearch1%3D%26%7C%26recentSearch2%3D%26%7C%26recentSearch3%3D%26%7C%26recentSearch4%3D%26%7C%26collapse_expansion%3D; search=jobarea%7E%60000000%7C%21ord_field%7E%600%7C%21recentSearch0%7E%601%A1%FB%A1%FA000000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1535688009%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21recentSearch1%7E%601%A1%FB%A1%FA010000%2C00%A1%FB%A1%FA000000%A1%FB%A1%FA0000%A1%FB%A1%FA00%A1%FB%A1%FA9%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA99%A1%FB%A1%FA%A1%FB%A1%FA2%A1%FB%A1%FA%A1%FB%A1%FA-1%A1%FB%A1%FA1535687985%A1%FB%A1%FA0%A1%FB%A1%FA%A1%FB%A1%FA%7C%21collapse_expansion%7E%601%7C%21'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'zhaopin_project.middlewares.ZhaopinProjectSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'zhaopin_project.middlewares.ZhaopinProjectDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'zhaopin_project.pipelines.ZhaopinProjectPipeline': 300,
   'zhaopin_project.pipelines.StorerMysqlScrapyPipeline': 300,
   'scrapy_redis.pipelines.RedisPipeline': 310
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379