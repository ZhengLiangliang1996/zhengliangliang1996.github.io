---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Web_Crawler爬top100电影信息"
date: "2018-04-08"
categories: 
  - "python"
tags: 
  - "爬虫"
---

早上看到一个公众微信号发了个爬猫眼top100的电影信息 大致看了一下 把源码修改了将数据存储到MongoDB里面，方便之后更新到jupyter上进行数据可视化分析:

==============================

``` python
 1 import requests 
 2 import pymongo
 3 import re
 4 from requests.exceptions import RequestException
 5 from multiprocessing import Pool
 ```

只需要这5个库，按顺序分别用来进行请求界面，连接MongoDB, 使用re的pattern方法，请求异常，多进程与池

建立数据库 webCrawler_CatEYE.p

 1 client = pymongo.MongoClient('localhost',27017)
 2 cateye = client['cateye']
 3 content = cateye['content']

webCrawler_CatEYE.py
```python
 1 
 2 def get_one_page(url):
 3    try:
 4        res = requests.get(url,headers = headers)
 5        if res.status_code == 200:
 6            return res.text
 7        return None
 8    except RequestException:
 9        return None
10 
11 # Building the page compiler
12 def parse_one_page(html):
13         pattern = re.compile('<dd>.*?board-index.*?>(d+)</i>.*?data-src="(.*?)".*?name"><a'
14                              + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
15                              + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
16         items = re.findall(pattern, html)
17         for item in items:
18             yield {
19                 'index': item[0],
20                 'image': item[1],
21                 'title': item[2],
22                 'actor': item[3].strip()[3:],
23                 'time': item[4].strip()[5:],
24                 'score': item[5] + item[6]
25             }
26 
27 # Stoing the data from pages (Into mongoDB)
28 def write_to_mongoDB(item):
29     #content.insert_one({'index': item[0], 'image': item[1], 'title': item[2], 'actor': item[3].strip()[3:], 'time':item[4].strip()[5:],'score':item[5] + item[6]})
30     content.insert_one(item)
31 
32 # Main function
33 def main(offset):
34     url = 'http://maoyan.com/board/4?offset=' + str(offset)
35     html = get_one_page(url)
36     for item in parse_one_page(html):
37         print(item)
38         write_to_mongoDB(item)
39 
40 
41 if __name__ == '__main__':
42     p = Pool()
43     p.map(main,[i*10 for i in range(10)])
44 
```
 

稍微解释一下 第一个函数请求一个页面 用requests.get，然后进行try一下

然后对界面进行解析，我们比较常用的是BeautifulSoup来解析，这里我们使用re中的pattern来进行匹配。然后用yield数据结构进行存储。前面建立好数据库，到了后面直接用表的一个Insert_one方法进行插入，顺爽丝滑

主程序 每个界面访问完就打印出来 写进数据库

然后用多进程进行，POOL函数会自动判别你的系统是多少核的，不需要自己去查然后再写上去，这很方便，然后map起来，就大功告成

 

运行结果

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/04/e59bbee789871.png" alt="screenshot" width="80%" height="auto">
</p>

数据库

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2018/04/e59bbee7898711.png" alt="screenshot" width="80%" height="auto">
</p>

之后想看看根据类别爬1000部电影，然后可视化数据出来，画一些fancy的图，就这样。

 

btw，粗略看了下，这100部我都看过
