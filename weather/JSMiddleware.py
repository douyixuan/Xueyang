from selenium import webdriver
from scrapy.http import HtmlResponse

import time
from selenium.webdriver import Chrome

from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.firefox.options import Options

from selenium.webdriver.support import expected_conditions as expected

from selenium.webdriver.support.wait import WebDriverWait


class PhantomJSMiddleware(object):


    def process_request(cls, request, spider):

        if spider.name == "angel":
            print
            "PhantomJS is starting..."
            #driver = webdriver.PhantomJS()  # 指定使用的浏览器
            driver = webdriver.Chrome()
            driver.get(request.url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
            time.sleep(3)

            body = driver.page_source
            print("访问" + request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return


class ChromeMiddleware(object):

    def process_request(cls, request, spider):

        #if spider.name == "angel":
        if spider.name == "devil":

            options = webdriver.ChromeOptions()
            # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
            options.add_argument('headless')

            # 创建chrome无界面对象
            driver = webdriver.Chrome(chrome_options=options)

            driver.get(request.url)
            time.sleep(1)
            js = "var q=document.documentElement.scrollTop=10000"
            driver.execute_script(js)  # 可执行js，模仿用户操作。此处为将页面拉至最底端。
            driver.implicitly_wait(3)
            #WebDriverWait(driver, 5, 0.5).until(driver.find_element_by_class_name('tr'))
            body = driver.page_source
            print("访问" + request.url)
            return HtmlResponse(driver.current_url, body=body, encoding='utf-8', request=request)
        else:
            return