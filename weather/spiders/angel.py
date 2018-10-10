# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem
from selenium import webdriver

class WeatherSpider(scrapy.Spider):
    name = "angel"
    #scrapy shell 'https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month=2017-01'
    #start_urls=['https://www.aqistudy.cn/historydata/daydata.php?city=%E5%8C%97%E4%BA%AC&month=2017-01']
    start_urls = []
    cities = []
    with open('/Users/mengxiangyu/Downloads/workspace/Xueyang/weather/cities.txt', 'r') as f:
        cities = f.read().split(' ')

    for city in cities:
        for month in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
            start_urls.append('https://www.aqistudy.cn/historydata/daydata.php?city=' + city +
                    '&month=2017-' + month)
   # print(start_urls)



    def parse(self, response):

        response=response.replace(encoding="ansi")
        html = response.body
        #print(html)
        # item['title'] = info.xpath('h2[@id="title"]/text()').extract()
        #logging.info(u'----------使用splash爬取京东网首页异步加载内容-----------')
        title = response.xpath('//h2[@id="title"]/text()').extract()
        #path = 'file:/Users/mengxiangyu/Downloads/weather' + title + '.csv'
        #f = open(path)
        print(title)
        # /html/body/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[1]
        for info in response.xpath('/html/body/div[3]/div[1]/div[1]/table/tbody/tr'):
            item = WeatherItem()

            #date  AQI	质量等级	PM2.5	PM10	SO2	CO	NO2	O3_8h
            #/html/body/div[3]/div[1]/div[1]/table/tbody/tr[2]/td[1]
            item['city'] = title
            item['date'] = info.select('td[1]/text()').extract()
            item['AQI'] = info.select('td[2]/text()').extract()
            item['quality'] = info.select('td[3]/span/text()').extract()
            item['PM2p5'] = info.select('td[4]/text()').extract()
            item['PM10'] = info.select('td[5]/text()').extract()
            item['SO2'] = info.select('td[6]/text()').extract()
            item['CO'] = info.select('td[7]/text()').extract()
            item['NO2'] = info.select('td[8]/text()').extract()
            item['O3_8h'] = info.select('td[9]/text()').extract()

            yield item

            # 翻页
            #next_page = response.xpath('//span[@class="next"]/a/@href')
            #if next_page:
            #    url = response.urljoin(next_page[0].extract())
            #    yield scrapy.Request(url, self.parse)

