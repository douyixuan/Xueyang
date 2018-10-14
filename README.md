# 300 Cities' weather records in 2017

> Cause I received a help from Xueyang, so I gave birth to this spider.
## configuration
### 路径修改

需要修改的文件:
> 用记事本或者其他工具打开修改
Xueyang/weather/spiders/devil.py
```
代码：
        with open('/Users/mengxiangyu/Downloads/workspace/Xueyang/weather/cities.txt', 'r') as f:
                cities = f.read().split(' ')
文件cities.txt的路径需要修改

代码：
        city_path = '/Users/mengxiangyu/Downloads/weather/'
文件输出路径需要修改，你要存在哪里，就写一个路径
代码：
        start_urls.append('https://www.aqistudy.cn/historydata/daydata.php?city=' + city +
                    '&month=2017' + month)
修改2016只需把改2017替换
```

### 环境还差一个chrome浏览器
http://chromedriver.chromium.org/downloads
下载之后路径需要配置一下，要不然找不到
参考文章：
https://www.jianshu.com/p/5ea69cd6c3f5
windows 系统环境变量配置，即PATH
https://jingyan.baidu.com/article/8ebacdf02d3c2949f65cd5d0.html


### 运行命令
```
>>>cd （Xueyang-master那个文件夹的路径）
>>>scrapy crawl angel

```
### 到此结束，下面不需要看了！！！











### 使用说明
```
1.下载代码

2.安装python环境（安装则忽略）


3.安装python virtualenv环境（命令行）
参考网站：
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000
pip3 install virtualenv

安装后启动虚拟环境
cd （virtualenv的路径）/bin
source activate


4.安装selenium
pip3 install selenium

5.安装phantomJS
pip3 install phantomjs

6.修改cities.txt, 放入需要的城市
保存

7.运行：（在虚拟环境下）
scrapy crawl angel
```


### ！！！！！一定要小心编码，文件编码


### python + selenium + phantomJS
- 3.7
- 3.14.1
- 2.1.1


### 文件持久化格式
- CSV
- UTF-8，no bom

### bug
- Only one document for saving data
- crash at the middle of process
- no parallel process
- csv change code
