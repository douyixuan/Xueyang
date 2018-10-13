# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
from selenium import webdriver
import io
import sys


class WeatherSpider(scrapy.Spider):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    name = "angel"
    #scrapy shell 'https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month=2017-01'
    #start_urls=['https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month=2017-01']

    start_urls = []
    cities = []

    with open('/Users/mengxiangyu/Downloads/workspace/Xueyang/weather/cities.txt', 'r') as f:
        cities = f.read().split(' ')
        f.close()
    #https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month=201703
    for city in cities:
        for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            start_urls.append('https://www.aqistudy.cn/historydata/daydata.php?city=' + city +
                    '&month=2017' + month)
   # print(start_urls)



    def parse(self, response):

        #response=response.replace(encoding="ansi")
        html = response.body
        #print(html)
        #logging.info(u'----------使用splash爬取网首页异步加载内容-----------')
        title = response.xpath('//h2[@id="title"]/text()').extract()
        #path = 'file:/Users/mengxiangyu/Downloads/weather' + title + '.csv'
        #f = open(path)
        print(title)
        # /html/body/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[1]
        for info in response.xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr'):

            item = WeatherItem()
            #print(item)
            #date  AQI	质量等级	PM2.5	PM10	SO2	CO	NO2	O3_8h
            #/html/body/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[1]
            item['city'] = title
            item['date'] = info.xpath('td[1]/text()').extract()
            item['AQI'] = info.xpath('td[2]/text()').extract()
            item['quality'] = info.xpath('td[3]/span/text()').extract()
            # /html/body/div[3]/div[1]/div[1]/table/tbody/tr[3]/td[4]
            item['PM2p5'] = info.xpath('td[4]/text()').extract()
            item['PM10'] = info.xpath('td[5]/text()').extract()
            item['SO2'] = info.xpath('td[6]/text()').extract()
            item['CO'] = info.xpath('td[7]/text()').extract()
            item['NO2'] = info.xpath('td[8]/text()').extract()
            item['O3_8h'] = info.xpath('td[9]/text()').extract()

            yield item

            # 翻页
            #next_page = response.xpath('//span[@class="next"]/a/@href')
            #if next_page:
            #    url = response.urljoin(next_page[0].extract())
            #    yield scrapy.Request(url, self.parse)

