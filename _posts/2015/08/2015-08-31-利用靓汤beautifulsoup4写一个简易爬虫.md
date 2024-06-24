---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "利用靓汤BeautifulSoup4写一个简易爬虫"
date: "2015-08-31"
categories: 
  - "python"
coverImage: "h_large_esee_7a88000669c12f75.jpg"
---

###                               **     爬虫编写总结**

**首先，给大家一个我自己受害极深的结论：不要在家宅太久！不要再家宅太久！不要在家宅太久！重要的事情讲3遍，为什么这么说？在家里太容易消沉了，四面都是及其甜蜜蜜温暖的味道，每天你妈帮你安排地妥妥的，削弱了你好好学习成为人生赢家的野心，可能大部分像我一样自制力自我感觉良好，前期学习紧凑，每天的代码量也是不含糊。但是！（这才是重点！）慢慢的，你会发现你每天会莫名喜欢昏睡，没人故意打扰你，是因为家里太舒适了，被舒适同化了！说多了都是泪，剩下几天赶紧做假期收尾工作，计划备表整理好  :( 噢！对了，也不要在学校宅宿舍里头发霉~**

上星期入门了Python，一学这语言真是处处都是惊喜：定义变量可以没有类型直接进行计算;去除了烦人的括号，直接用缩进对齐真是太感叹自己学C时候的坐井观天；元组和字典完爆数组;IDE精简；安装包和运用模块十分简单；

但我仍然很敬畏C++,许多高度计算效率和基本的轮子都是C++造出来的。不过学了Python让我有了一点包二奶的感觉。

------------

正文：

这个简易的爬虫主要爬了一下豆瓣的影评，只爬了每篇文章的链接和作者。

我用的IDE是Pycharm 3.4.1

导入两个包  BeautifulSoup4 和  requests ,导入方法 进入 file->setting->ProjectInterpreter

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_184424.png" alt="screenshot" width="80%" height="auto">
</p>

右边有个绿色的加号＋，按了就可以搜索模块了 BeautifulSoup4 和 requests.

如果安装不了，就全部卸载安装到另一个目录下重新试一下。

**一.关于2个模块解析**

From 维基百科：

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_194956.png" alt="screenshot" width="80%" height="auto">
</p>

bf4 作为python的包可以解析HTML和XML文件，包括有格式错误的标记。它创建了一颗搜索树来爬网站或者文档

1.py具体使用方法

# anchor extraction from html document
from bs4 import BeautifulSoup 
import urllib2

webpage = urllib2.urlopen('http://en.wikipedia.org/wiki/Main_Page')
soup = BeautifulSoup(webpage)
for anchor in soup.find_all('a'):
    print(anchor.get('href', '/'))

1.导入包：from bs4 import BeautifulSoup

2.将网站打开传递给.text后缀的一个可读文件，才可以被靓汤作为对象爬，然后赋给soup

第二个包是requests

1.导入包 import requests

2.其实requests和urllib是很像的。 requests.get(url)的功能和urllib.open(url)十分相像，都是用来打开网站的。

具体方法：

>>> import requests
>>> r = requests.get('https:/ GITHUB.com/timeline.json')
>>> r.text
u'[{"repository":{"open_issues":0,"url":"https:/ GITHUB.com/.
..

**二 爬一系列页面**

我要访问的网站是豆瓣的热门影评页面：[点我](http://movie.douban.com/review/best/?start=0) .页面最后有个计数start变量第一个页面是start = 0,试着翻一下，可以发现start每次增加10，这时初始辨识某一个页面与另一个相似页面的区别，就是后面的变量值在发生变化，可以用一个自加行为产生访问页面。再用靓汤遍历，用soup.findAll来进行关键词的查找。
```python
import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    page = 10
    title = 0
    while page <= max_page:
        url = 'http://movie.douban.com/review/best/?start=' + str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in  soup.findAll('a',{'class':'j 
 a_unfolder'}):
            href = link.get('href')
            title += 1
            print(title)
            print(href)
            get_single_item_data(href)
        page += 10 
```
先祭上本部分代码

1. 后面的 str+（page）就是刚刚说到的页面变量参数，最后有一个 page +=10 就是一直在变化，为了能进行直接续网站而不是进行单纯的加法，将其强制转换成string类型。
2. 再到大函数来看，利用while来进行一一遍历，遍历的页面是传入函数的参数，由用户来决定要多少个页面，只要确定每个页面+10就可以了。
3. 在thenewboston上看这个教学视频的时候，觉得很麻烦，打开了网站要传送source_code,再传给plain_text觉得很麻烦，这是因为代码的可读性原因很重要，不过其实还是程序员的习惯因素决定的，可以直接打开就用beautifulsoup变成一个对象的。
4. 这里有个很有意思的事情，我的这里的BeautifulSoup不是单纯放进去plain_text就可以了，查看了文档说要在后面加上"html.parser"不知道大家的需不需要。

**遍历环节：**

我们首先要找到每个页面有链接的标题:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/faststoneeditor1.jpg" alt="screenshot" width="80%" height="auto">
</p>

按右键查找源代码

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_203422.png" alt="screenshot" width="80%" height="auto">
</p>

上面这一串，虽然后标题，有href链接，但是class部分是没有的，应该是被隐藏了，所以这里只能用下面这一串也含有标题链接href的代码，因为有class ,可以准确的找到

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_203528.png" alt="screenshot" width="80%" height="auto">
</p>

所以在遍历的时候  for link in soup.findAll('a',{'class':'j a_unfolder'})**:**

可以准确找到这个地方，记得for循环后面有冒号！

然后后面打印出来即可。

**三 爬标题连接里面的链接&信息**

写爬虫很像盗梦空间，可以有梦中梦，则就是爬链接里面的链接，其实码代码就是一个织梦过程。

原理类似，写代码就是不断的代码重用，因为要完成类似的过程。所以我们可以利用前面的爬虫模板，修改变量就可以实现。在这里，因为豆瓣网站改版了，很多代码更新，许多class都不知道死去哪里，所以这里不打算再爬连接，就爬里面的作者名

打开刚才第一个影评做示范：

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_204552.png" alt="screenshot" width="80%" height="auto">
</p>

作者是 黄香蕉 我们就查找这一部分的源代码，右键——》查看页面源代码  找到黄香蕉所在的位置

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_204741.png" alt="screenshot" width="80%" height="auto">
</p>

它在span里面，属性是property 属性名字是  v:reviewer

所以查找的时候  for link in soup.findAll('span',{'property':'v:reivewer'})

所以整一串代码是：
```python
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for item_name in soup.findAll('span',{'property':'v:reviewer'}):
        print(item_name.string)
```
呈现的效果

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/08/2015-08-31_205155.png" alt="screenshot" width="80%" height="auto">
</p>

虽然很简单，但是显示地十分漂亮整洁。

这里贴出来全部代码，供大家一同学习，如果有什么不妥或者知识性错误请反馈至137988166@qq.com

总代码：

```python
import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    page = 10
    title = 0
    while page <= max_page:
        url = 'http://movie.douban.com/review/best/?start=' +
        str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text,"html.parser")
        for link in  soup.findAll('a',{'class':'j 
 a_unfolder'}):
            href = link.get('href')
            title += 1
            print(title)
            print(href)
            get_single_item_data(href)
        page += 10

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    for item_name in soup.findAll('span',{'property':'v:
 reviewer'}):
        print(item_name.string)

trade_spider(40)
```
快开学咯，大家一起加油哇！

