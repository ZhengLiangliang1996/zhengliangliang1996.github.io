---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "STL之Vector用法"
date: "2015-11-22"
categories: 
  - "datastructure"
---

心酸，今天花烧了，39度多，躺在被窝里面也要写程序。听说发烧的时候写代码思路会比较清晰。

------------

正文

- **Vector介绍**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2015/11/2015-11-22_212712.png" alt="screenshot" width="80%" height="auto">
</p>

Vector实际上也是一个数组，但是可以自动扩展，伸缩性比较好。Vector是C++标准模板库中的部分内容，它是一个多功能的，能够操作多种数据结构和算法的模板类和函数库。vector之所以被认为是一个容器，是因为它能够像容器一样存放各种类型的对象，简单地说，vector是一个能够存放任意类型的动态数组，能够增加和压缩数据。

- **Vector的一般接口和用法**

为了可以使用vector，必须在你的头文件中包含下面的代码：

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="528"><span lang="EN-US">#</span><span lang="EN-US">include</span><span lang="EN-US"> &lt;vector&gt;</span></td></tr></tbody></table>

 

vector属于std命名域的，因此需要通过命名限定，如下完成你的代码：

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="528"><span lang="EN-US">using</span><span lang="EN-US"> std::vector;</span><div></div><span lang="EN-US">vector&lt;</span><span lang="EN-US">int</span><span lang="EN-US">&gt; vInts;</span></td></tr></tbody></table>

 

或者连在一起，使用全名：

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="528"><span lang="EN-US">std::vector&lt;</span><span lang="EN-US">int</span><span lang="EN-US">&gt; vInts;</span></td></tr></tbody></table>

 

建议使用全局的命名域方式：

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="528"><span lang="EN-US">using</span> <span lang="EN-US">namespace</span><span lang="EN-US"> std;</span></td></tr></tbody></table>

 

**Vector的一些成员函数:**

**Vector****成员函数**

<table border="1" cellspacing="1" cellpadding="0"><tbody><tr><td width="33%">函数</td><td width="66%">表述</td></tr><tr><td width="33%"><span lang="EN-US">c.assign(beg,end)</span><div></div><span lang="EN-US">c.assign(n,elem)</span></td><td width="66%">将<span lang="EN-US">[beg; end)</span>区间中的数据赋值给<span lang="EN-US">c</span>。<div></div>将<span lang="EN-US">n</span>个<span lang="EN-US">elem</span>的拷贝赋值给<span lang="EN-US">c</span>。</td></tr><tr><td width="33%"><span lang="EN-US">c.at(idx)</span></td><td width="66%">传回索引<span lang="EN-US">idx</span>所指的数据，如果<span lang="EN-US">idx</span>越界，抛出<span lang="EN-US">out_of_range</span>。</td></tr><tr><td width="33%"><span lang="EN-US">c.back()</span></td><td width="66%">传回最后一个数据，不检查这个数据是否存在。</td></tr><tr><td width="33%"><span lang="EN-US">c.begin()</span></td><td width="66%">传回迭代器重的可一个数据。</td></tr><tr><td width="33%"><span lang="EN-US">c.capacity()</span></td><td width="66%">返回容器中数据个数。</td></tr><tr><td width="33%"><span lang="EN-US">c.clear()</span></td><td width="66%">移除容器中所有数据。</td></tr><tr><td width="33%"><span lang="EN-US">c.empty()</span></td><td width="66%">判断容器是否为空。</td></tr><tr><td width="33%"><span lang="EN-US">c.end()</span></td><td width="66%">指向迭代器中的最后一个数据地址。</td></tr><tr><td width="33%"><span lang="EN-US">c.erase(pos)</span><div></div><span lang="EN-US">c.erase(beg,end)</span></td><td width="66%">删除<span lang="EN-US">pos</span>位置的数据，传回下一个数据的位置。<div></div>删除<span lang="EN-US">[beg,end)</span>区间的数据，传回下一个数据的位置。</td></tr><tr><td width="33%"><span lang="EN-US">c.front()</span></td><td width="66%">传回第一个数据。</td></tr><tr><td width="33%"><span lang="EN-US">get_allocator</span></td><td width="66%">使用构造函数返回一个拷贝。</td></tr><tr><td width="33%"><span lang="EN-US">c.insert(pos,elem)</span><div></div><span lang="EN-US">c.insert(pos,n,elem)</span><div></div><span lang="EN-US">c.insert(pos,beg,end)</span></td><td width="66%">在<span lang="EN-US">pos</span>位置插入一个<span lang="EN-US">elem</span>拷贝，传回新数据位置。<div></div>在<span lang="EN-US">pos</span>位置插入<span lang="EN-US">n</span>个<span lang="EN-US">elem</span>数据。无返回值。<div></div>在<span lang="EN-US">pos</span>位置插入在<span lang="EN-US">[beg,end)</span>区间的数据。无返回值。</td></tr><tr><td width="33%"><span lang="EN-US">c.max_size()</span></td><td width="66%">返回容器中最大数据的数量。</td></tr><tr><td width="33%"><span lang="EN-US">c.pop_back()</span></td><td width="66%">删除最后一个数据。</td></tr><tr><td width="33%"><span lang="EN-US">c.push_back(elem)</span></td><td width="66%">在尾部加入一个数据。</td></tr><tr><td width="33%"><span lang="EN-US">c.rbegin()</span></td><td width="66%">传回一个逆向队列的第一个数据。</td></tr><tr><td width="33%"><span lang="EN-US">c.rend()</span></td><td width="66%">传回一个逆向队列的最后一个数据的下一个位置。</td></tr><tr><td width="33%"><span lang="EN-US">c.resize(num)</span></td><td width="66%">重新指定队列的长度。</td></tr><tr><td width="33%"><span lang="EN-US">c.reserve()</span></td><td width="66%">保留适当的容量。</td></tr><tr><td width="33%"><span lang="EN-US">c.size()</span></td><td width="66%">返回容器中实际数据的个数。</td></tr><tr><td width="33%"><span lang="EN-US">c1.swap(c2)</span><div></div><span lang="EN-US">swap(c1,c2)</span></td><td width="66%">将<span lang="EN-US">c1</span>和<span lang="EN-US">c2</span>元素互换。<div></div>同上操作。</td></tr><tr><td width="33%"><span lang="EN-US">vector&lt;Elem&gt; c</span><div></div><span lang="EN-US">vector &lt;Elem&gt; c1(c2)</span><div></div><span lang="EN-US">vector &lt;Elem&gt; c(n)</span><div></div><span lang="EN-US">vector &lt;Elem&gt; c(n, elem)</span><div></div><span lang="EN-US">vector &lt;Elem&gt; c(beg,end)</span><div></div><span lang="EN-US">c.~ vector &lt;Elem&gt;()</span></td><td width="66%">创建一个空的<span lang="EN-US">vector</span>。<div></div>复制一个<span lang="EN-US">vector</span>。<div></div>创建一个<span lang="EN-US">vector</span>，含有<span lang="EN-US">n</span>个数据，数据均已缺省构造产生。<div></div>创建一个含有<span lang="EN-US">n</span>个<span lang="EN-US">elem</span>拷贝的<span lang="EN-US">vector</span>。<div></div>创建一个以<span lang="EN-US">[beg;end)</span>区间的<span lang="EN-US">vector</span>。<div></div>销毁所有数据，释放内存。</td></tr></tbody></table>

**Vector****操作**

<table border="1" cellspacing="1" cellpadding="0"><tbody><tr><td width="32%"><p align="left">函数</p></td><td width="66%"><p align="left">描述</p></td></tr><tr><td width="32%"><span lang="EN-US">operator</span><span lang="EN-US">[]</span></td><td width="66%">返回容器中指定位置的一个引用。</td></tr></tbody></table>

- **创建一个Vector**

#include <iostream>
#include <vector>

using namespace std;

int main(){
	//创建一个int类型 数量为500的vector
	vector<int> people (500);
	//创建一个char类型 数量为500 且开始全部初始化为0的vector
	vector<char> name(500, char(0));
	//创建一个char的拷贝
	vector<char> nameFromAnother(name); 
	system("pause");
	return 0;
}

向vector中输入数据

#include <iostream>
#include <vector>

using namespace std;

int main(){
	
	//向vector中添加数据
        //vector添加数据的缺省方法是push_back() push_back表示将数据添加到
        //vector的尾部，并且按需要来分配内存
        //例如添加10个数据
	for (int i = 0; i < 10; i++){
		people.push_back(int(i));
	}
	system("pause");
	return 0;
}

获取vector中指定位置的数据:很多时候我们不必要知道vector里面有多少数据，vector里面的数据是动态分配的，使用push_back()的一系列分配空间常常决定于文件或一些数据源。如果你想知道vector存放了多少数据，你可以使用empty()。获取vector的大小，可以使用size()。例

int nSize = v.empty()?-1:static_cast<int>(v.size)

**访问vector中的数据:**

可以使用两种方法来访问vector 1.vector::at() 2.vector::operator[]

operator主要是为了和C语言兼容，他可以像C的数组一样操作，但是at()是进行了边界检查。，如果访问超过了vector的范围，将抛出一个例外。由于operator[]容易造成一些错误，所有我们很少用它，下面进行验证一下：

分析下面的代码：

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="528"><span lang="EN-US">vector&lt;</span><span lang="EN-US">int</span><span lang="EN-US">&gt; v;</span><div></div><span lang="EN-US">v.reserve(10);</span><div></div><span lang="EN-US">&nbsp;</span><span lang="EN-US">for</span><span lang="EN-US">(</span><span lang="EN-US">int</span><span lang="EN-US"> i=0; i&lt;7; i++)</span><div></div><span lang="EN-US">&nbsp;&nbsp;&nbsp; v.push_back(i);</span><div></div><span lang="EN-US">&nbsp;</span><span lang="EN-US">try</span><span lang="EN-US">{</span><div></div><span lang="EN-US">&nbsp;</span><span lang="EN-US">int</span><span lang="EN-US"> iVal1 = v[7];&nbsp; // not bounds checked - will not throw</span><div></div><span lang="EN-US">&nbsp;</span><span lang="EN-US">int</span><span lang="EN-US"> iVal2 = v.at(7); // bounds checked - will throw if out of range</span><div></div><span lang="EN-US">}</span><div></div><span lang="EN-US">catch</span><span lang="EN-US">(</span><span lang="EN-US">const</span><span lang="EN-US"> exception&amp; e)</span><span lang="EN-US">{</span><div></div><span lang="EN-US">&nbsp;cout &lt;&lt; e.what();</span><div></div><span lang="EN-US">}</span></td></tr></tbody></table>

 

我们使用reserve()分配了10个int型的空间，但并不没有初始化。

你可以在这个代码中尝试不同条件，观察它的结果，但是无论何时使用at()，都是正确的。

- **Vector的删除操作**

vector能够非常容易地添加数据，也能很方便地取出数据，同样vector提供了erase()，pop_back()，clear()来删除数据，当你删除数据的时候，你应该知道要删除尾部的数据，或者是删除所有数据，还是个别的数据。在考虑删除等操作之前让我们静下来考虑一下在STL中的一些应用。

**Remove_if()****算法**

现在我们考虑操作里面的数据。如果要使用remove_if()，我们需要在头文件中包含如下代码：：

<table border="0" cellspacing="0" cellpadding="0"><tbody><tr><td valign="top" width="528"><span lang="EN-US">#</span><span lang="EN-US">include</span><span lang="EN-US"> &lt;algorithm&gt;</span></td></tr></tbody></table>

 Remove_if()有三个参数：

1、 iterator _First：指向第一个数据的迭代指针。

2、 iterator _Last：指向最后一个数据的迭代指针。

3、 predicate _Pred：一个可以对迭代操作的条件函数。

 

真的太困的，先睡了，明天再写。2015年11月22日22:05:00

**Written By：Speak Now**
