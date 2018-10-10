# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 日期	AQI	质量等级	PM2.5	PM10	SO2	CO	NO2	O3_8h
    city = scrapy.Field()
    date = scrapy.Field()
    AQI = scrapy.Field()
    quality = scrapy.Field()
    PM2p5 = scrapy.Field()
    PM10 = scrapy.Field()
    SO2 = scrapy.Field()
    CO = scrapy.Field()
    NO2 = scrapy.Field()
    O3_8h = scrapy.Field()
    pass
