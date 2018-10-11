# 300 Cities' weather records in 2017

> Cause I received a help from Xueyang, so I gave birth to this spider.




## configuration
### Path
```
需要修改的地方:
1.Xueyang/weather/spiders/angel.py

with open('/Users/mengxiangyu/Downloads/workspace/Xueyang/weather/cities.txt', 'r') as f:
        cities = f.read().split(' ')
cities.txt的路径需要修改

2.Xueyang/weather/settings.py
最下面靠上一点
FEED_URI = u'file:/Users/mengxiangyu/Downloads/weather.csv'  #将抓取的数据存放到文件中。
(从/Users开始，换成你的目录：   E：/a/b/..)

```
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
## Instruction

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
