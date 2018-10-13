from selenium import webdriver

# 创建chrome参数对象
options = webdriver.ChromeOptions()

# 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
options.add_argument('headless')

# 创建chrome无界面对象
driver = webdriver.Chrome(chrome_options=options)

# 访问烯牛数据
url = "http://www.xiniudata.com/project/event/lib/invest"
driver.get(url)

# 等待，让js有时间渲染
driver.implicitly_wait(3)

#打印内容
# print(driver.page_source)

# 解析内容
print(driver.find_element_by_css_selector(".table-body").text)

# 关闭窗口和浏览器
driver.close()
driver.quit()