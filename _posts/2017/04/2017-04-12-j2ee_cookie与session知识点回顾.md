---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "J2EE_Cookie与Session知识点回顾"
date: "2017-04-12"
categories: 
  - "未分类"
---

**Cookie**

 **进行 session 跟踪而储存在用户本地终端上的数据（通常经过加密）.cookie是会话技术的一种，因为http协议是无状态的，每次都是基于一个请求和一个响应，每次请求和响应都跟上次没有关系，我们需要记录之前的对话，则需要cookie技术，它是属于客户端(浏览器)保存信息的技术。**

**Cookie基本用法**
   1.添加cookie到浏览器
      1>新建一个cookie(键值对)
          Cookie cookie = new Cookie("name", "tom");
      2>将cookie 添加到响应中
          response.addCookie(cookie);
   2.浏览器发送cookie到服务器,如何取
      1>获得所有浏览器发送的cookie
          Cookie[] cookies = request.getCookies();
      2>遍历并判断我们要找的cookie
          if(cookies!=null && cookies.length>0){
              for(Cookie c : cookies){
                 if(c.getName().equals("name")){
                      System.out.println("获得的cookie:"+c.getName()+":"+c.getValue());
                 }
        }
}

例子：

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/04/11.jpg" alt="screenshot" width="80%" height="auto">
</p>

BServlet接收遍历

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/04/21.jpg" alt="screenshot" width="80%" height="auto">
</p>

**Cookie原理：**

让浏览器记住键值对，是向响应头中添加一下头即可

                       set-Cookie:name=tom;

浏览器记住之后，向服务器发送键值对，是在请求头中添加下面的信息：

                       Cookie:name=tome

 **浏览器记录多久？**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/04/cookiee7949fe591bde591a8e69c9f.jpg" alt="screenshot" width="80%" height="auto">
</p>

例子：Google浏览器一般的Cookie持续时间是一年

但是，默认的回话期间有效，（关闭浏览器，cookie就被删除）(**有效时间-1**)

**细节1：**

1.有效时间的设置 ， 根据查看JDK1.6 <p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/04/setmax.jpg" alt="screenshot" width="80%" height="auto">
</p>

设置方法:
        1>设置一个正数，标示最大有效时间，单位是秒
              cookie.setMaxAge(60*60);
        2>设置为负数，负值意味着 cookie 不会被持久存储，将在 Web 浏览器退出时删除。
              cookie.setMaxAge(-1);
        3>标示cookie的有效时间为0，0 值会导致删除 cookie。这个操作可以作为删除cookie的方法

**细节2：**

浏览器在什么情况下发送cookie的路径

       cookie的默认路径就是发送cookie的servlet所在目录.
                         /Day09-cookie 
                        /Day09-cookie/abc/xxxServlet
       访问路径如果是cookie路径的子路径那么,浏览器就会把该cookie告诉服务器.

**细节3：**

cookie中的域
```
    想要以下三个 主机和主机下的项目能共享一个cookie.
                     www.baidu.com
                     music.baidu.com
                     map.baidu.com
    完成两步即可: 
        1.设置cookie的域为 ".baidu.com"
        2.设置cookie路径 为: "/" 
    以上就是跨主机访问cookie.不常用.
```

**Session简介：**

Session是服务器端保存会话信息的技术.

How to use it?
```        
1.获得session
        HttpSession session = request.getSession();
2.操作session  (CURD)
        // session.setAttribute(arg0, arg1)
        // session.getAttribute(arg0)
        // session.removeAttribute(arg0)
        // session.getAttributeNames()
```

**Session原理：**

和Cookie一样，session的http过程也是无状态的过程，则在服务器端会在内存中开辟一个空间(session)，并对Session对应给浏览器。

下次浏览器去访问服务器,会把sessionID交给服务器，服务器通过sessionID找到刚才开辟的空间。

以上就是session原理。
