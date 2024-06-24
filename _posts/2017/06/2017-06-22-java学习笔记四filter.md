---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Java学习笔记(四):Filter"
date: "2017-06-22"
categories: 
  - "java"
---

 **6.22 今天不学习新知识，写三篇博文，复习之前学过的知识。**

- **过滤器简介：**

1.对资源的访问进行筛选（拦截）。请求和响应的拦截。过滤器好比写字楼的保安 2.过滤器对请求和响应的拦截，从而实现一些特殊的功能

- API文档

_A filter is an object that performs filtering tasks on either the request to a resource (a servlet or static content), or on the response from a resource, or both._ _Filters perform filtering in the doFilter method. Every Filter has access to a FilterConfig object from which it can obtain its initialization parameters, a reference to the ServletContext which it can use, for example, to load resources needed for filtering tasks._

- **过滤器的编写步骤**

1.编写一个类，实现javax.servlet.Filter方法
```java
 1 package com.itheima;
 2 
 3 import java.io.IOException;
 4 
 5 import javax.servlet.Filter;
 6 import javax.servlet.FilterChain;
 7 import javax.servlet.FilterConfig;
 8 import javax.servlet.ServletException;
 9 import javax.servlet.ServletRequest;
10 import javax.servlet.ServletResponse;
11 
12 /**
13  * FilterDemo1
14  * @author zhengstars
15  * @email 514587169@qq.com
16  * @date Jun 22, 2017 9:20:40 AM
17  * @version 1.0
18  */
19 public class FilterDemo1 implements Filter{
20 
21 	public void init(FilterConfig filterConfig) throws ServletException {
22 		
23 	}
24 
25 	public void doFilter(ServletRequest request, ServletResponse response,
26 			FilterChain chain) throws IOException, ServletException {
27 		System.out.println("执行了");
28 		chain.doFilter(request, response);//放行
29 	}
30 
31 	public void destroy() {
32 		
33 	}
34 	
35 }
```
2.配置要过滤的资源
```xml
 1 <!--?xml  version="1.0" encoding="UTF-8"?-->
 2 <web-app version="2.5" 
 3 	xmlns="http://java.sun.com/xml/ns/javaee" 
 4 	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
 5 	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
 6 	http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">
 7  
 8   
 9  	FilterDemo1
10   	com.itheima.filter.FilterDemo1
11   
12   
13   	FilterDemo
14   	/*
15   	
16 
```

- **过滤器的执行过程和生命周期**

诞生：应用被加载时。配置好的过滤器就会被容器实例化，接着初始化。 活着：应用活着，他就活着。针对用户的每次访问过滤器拦截范围内的资源，容器都会调用 _doFilter(SerlvetRequest,ServletResponse.FilterChain);_ 死亡：应用被卸载时，就会销毁。调用_destory_方法。

- 执行过程

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/06/333.jpg" alt="screenshot" width="80%" height="auto">
</p>

- 串联过滤器

1、多个过滤器对某个资源进行过滤 2、过滤器过滤顺序 注意：xml里面filter-mapping标签出现的顺序就是过滤的顺序

- 过滤器案例
- 案例1：过滤器实现中文编码问题

写一个jsp进行显示：
```

 1 <%@ page language="java" import="java.util.*" pageEncoding="UTF-8"%>
 2 
 3 <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
 4 <html>
 5  <head>
 6    <title>title</title>
 7    
 8 	<meta http-equiv="pragma" content="no-cache">
 9 	<meta http-equiv="cache-control" content="no-cache">
10 	<meta http-equiv="expires" content="0">
11 	<!--
12 	<link rel="stylesheet" type="text/css" href="styles.css">
13 	-->
14 
15   </head>
16   
17   <body>
18   	<%--
19   	${pageContext.request.contextPath}
20   	pageContext.getRequest().getContextPath();返回/day19_01_example
21   	 --%>
22     <form action="${pageContext.request.contextPath}/servlet/ServletDemo1" method="post">
23     	<input type="text" name="name"/><input type="submit" value="保存"/>
24     </form>
25   </body>
26 </html>
```
Servlet
```java
 1 package com.itheima.servlet;
 2 
 3 import java.io.IOException;
 4 
 5 import javax.servlet.ServletException;
 6 import javax.servlet.http.HttpServlet;
 7 import javax.servlet.http.HttpServletRequest;
 8 import javax.servlet.http.HttpServletResponse;
 9 
10 public class ServletDemo1 extends HttpServlet {
11 
12 	public void doGet(HttpServletRequest request, HttpServletResponse response)
13 			throws ServletException, IOException {
14 		response.getWriter().write("你好");
15 		response.getWriter().write(request.getParameter("name"));
16 	}
17 
18 	public void doPost(HttpServletRequest request, HttpServletResponse response)
19 			throws ServletException, IOException {
20 		doGet(request, response);
21 	}
22 
23 }
```
Servlet进行了中文输出，在filter中要进行编码修改:
```
 1 package com.itheima.filter;
 2 
 3 import java.io.IOException;
 4 
 5 import javax.servlet.Filter;
 6 import javax.servlet.FilterChain;
 7 import javax.servlet.FilterConfig;
 8 import javax.servlet.ServletException;
 9 import javax.servlet.ServletRequest;
10 import javax.servlet.ServletResponse;
11 
12 public class SetCharacterEncodingFilter implements Filter {
13 
14 	private FilterConfig filterConfig;
15 
16 	public void init(FilterConfig filterConfig) throws ServletException {
17 		this.filterConfig = filterConfig;
18 	}
19 
20 	public void doFilter(ServletRequest request, ServletResponse response,
21 			FilterChain chain) throws IOException, ServletException {
22 		//读取指定的参数
23 		String encoding = filterConfig.getInitParameter("encoding");
24 		if(encoding==null){
25 			//没有配置参数，给一个默认值
26 			encoding = "UTF-8";
27 		}
28 		
29 		request.setCharacterEncoding(encoding);
30 		response.setCharacterEncoding(encoding);
31 		response.setContentType("text/html;charset="+encoding);
32 		chain.doFilter(request, response);
33 	}
34 
35 	public void destroy() {
36 
37 	}
38 
39 }
```
- 案例2:动态资源的缓存设置 如Servlet和JSP就算是动态资源

在filter中编码时候，注意调用的setHeader是HttpServletRequest的对象的方法，所以要对原先的ServletRequest的对象进行对象名修改。然后进行强制转换。分别控制缓存时间，无缓存控制。
```
 1 package com.itheima.filter;
 2 
 3 import java.io.IOException;
 4 
 5 import javax.servlet.Filter;
 6 import javax.servlet.FilterChain;
 7 import javax.servlet.FilterConfig;
 8 import javax.servlet.ServletException;
 9 import javax.servlet.ServletRequest;
10 import javax.servlet.ServletResponse;
11 import javax.servlet.http.HttpServletRequest;
12 import javax.servlet.http.HttpServletResponse;
13 //控制动态资源不要缓存
14 public class NoCacheFilter implements Filter {
15 
16 	public void init(FilterConfig filterConfig) throws ServletException {
17 
18 	}
19 
20 	public void doFilter(ServletRequest req, ServletResponse resp,
21 			FilterChain chain) throws IOException, ServletException {
22 		
23 		HttpServletRequest request;
24 		HttpServletResponse response;
25 		try{
26 			request = (HttpServletRequest)req;
27 			response = (HttpServletResponse)resp;
28 		}catch(Exception e){
29 			throw new RuntimeException("non-http request or response");
30 		}
31 		
32 		response.setHeader("Expires", "-1");//控制缓存时间。只要比当前时间小即可
33 		response.setHeader("Cache-Control", "no-cache");//HTTP1.1
34 		response.setHeader("Pragma", "no-cache");//HTTP1.0
35 		
36 		chain.doFilter(request, response);
37 	}
38 
39 	public void destroy() {
40 		
41 	}
42 
43 }
```
- 案例三：静态资源的缓存控制 如html js css

首先在xml中注册，并且设定每个标签的时间
```xml
 1 <!--?xml  version="1.0" encoding="UTF-8"?-->
 2 <web-app version="2.5" 
 3 	xmlns="http://java.sun.com/xml/ns/javaee" 
 4 	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
 5 	xsi:schemaLocation="http://java.sun.com/xml/ns/javaee 
 6 	http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd">
 7  
 8  
 9  	SetCharacterEncodingFilter
10   	com.itheima.filter.SetCharacterEncodingFilter
11   	
12   
13   
14   	SetCharacterEncodingFilter
15   	/*
16   
17   
18   
19   	NoCacheFilter
20   	com.itheima.filter.NoCacheFilter
21   
22   
23   	NoCacheFilter
24   	*.jsp
25   
26    
27   	NoCacheFilter
28   	/servlet/*
29   
30   
31   
32   	NeedCacheFilter
33   	com.itheima.filter.NeedCacheFilter
34   	
35   		html
36   		60
37   	
38   	
39   		js
40   		120
41   	
42   	
43   		css
44   		180
45   	
46   
47   
48   	NeedCacheFilter
49   	*.html
50   
51   
52   	NeedCacheFilter
53   	*.js
54   
55   
56   	NeedCacheFilter
57   	*.css
58   
59   
60     ServletDemo1
61     com.itheima.servlet.ServletDemo1
62   
63   
64     ServletDemo2
65     com.itheima.servlet.ServletDemo2
66   
67 
68 
69   
70     ServletDemo1
71     /servlet/ServletDemo1
72   
73   
74     ServletDemo2
75     /servlet/ServletDemo2
76   	
77   
78     index.jsp
79   
80 
```
在filter中，要先得到FilterConfig，因为要得到xml中各参数设置的时间 ，并且要获取用户访问的资源后缀，判断是js，html还是css，最后做出响应的缓存设置时间。

new 1.java
```java
 1 package com.itheima.filter;
 2 
 3 import java.io.IOException;
 4 
 5 import javax.servlet.Filter;
 6 import javax.servlet.FilterChain;
 7 import javax.servlet.FilterConfig;
 8 import javax.servlet.ServletException;
 9 import javax.servlet.ServletRequest;
10 import javax.servlet.ServletResponse;
11 import javax.servlet.http.HttpServletRequest;
12 import javax.servlet.http.HttpServletResponse;
13 //控制静态资源的缓存时间
14 public class NeedCacheFilter implements Filter {
15 
16 	private FilterConfig filterConfig;
17 
18 	public void init(FilterConfig filterConfig) throws ServletException {
19 		this.filterConfig = filterConfig;
20 	}
21 
22 	public void doFilter(ServletRequest req, ServletResponse resp,
23 			FilterChain chain) throws IOException, ServletException {
24 		HttpServletRequest request;
25 		HttpServletResponse response;
26 		try{
27 			request = (HttpServletRequest)req;
28 			response = (HttpServletResponse)resp;
29 		}catch(Exception e){
30 			throw new RuntimeException("non-http request or response");
31 		}
32 		
33 		long time = 0;//缓存的时间.单位是毫秒
34 		
35 		//知道用户访问的是html|css|js   截取uri的后缀  /day19_01_example/1.html
36 		String uri = request.getRequestURI();//    /day19_01_example/1.html
37 		String extensitionName = uri.substring(uri.lastIndexOf(".")+1);// html
38 		
39 		
40 		
41 		//获取对应的参数：设置缓存的时间
42 		if("html".equals(extensitionName)){
43 			time = Long.parseLong(filterConfig.getInitParameter("html"))*60*1000;
44 		}
45 		if("css".equals(extensitionName)){
46 			time = Long.parseLong(filterConfig.getInitParameter("css"))*60*1000;
47 		}
48 		if("js".equals(extensitionName)){
49 			time = Long.parseLong(filterConfig.getInitParameter("js"))*60*1000;
50 		}
51 		
52 		response.setDateHeader("Expires", System.currentTimeMillis()+time);
53 		chain.doFilter(request, response);
54 	}
55 
56 	public void destroy() {
57 
58 	}
59 
60 }
```
- **案例四:用户自定义登录**

顺便复习一下java中的mvc层(个人感觉用了php的Laravel框架学习java的mvc命名不是很习惯)

domain主控制层，是用户与数据库交互的核心中转站，控制用户数据收集，控制请求转向

User.java
```java
 1 package com.itheima.domain;
 2 
 3 import java.io.Serializable;
 4 /*
 5 create database day19;
 6 use day19;
 7 create table users(
 8 	id int primary key,
 9 	username varchar(100) not null unique,
10 	password varchar(100) not null,
11 	nickname varchar(100) not null
12 );
13  */
14 public class User implements Serializable {
15 	private int id;
16 	private String username;//唯一，不能为空
17 	private String password;//不能为空。加密：MD5 | SHA 
18 	private String nickname;//昵称
19 	public int getId() {
20 		return id;
21 	}
22 	public void setId(int id) {
23 		this.id = id;
24 	}
25 	public String getUsername() {
26 		return username;
27 	}
28 	public void setUsername(String username) {
29 		this.username = username;
30 	}
31 	public String getPassword() {
32 		return password;
33 	}
34 	public void setPassword(String password) {
35 		this.password = password;
36 	}
37 	public String getNickname() {
38 		return nickname;
39 	}
40 	public void setNickname(String nickname) {
41 		this.nickname = nickname;
42 	}
43 	
44 }
```
dao是持久层，读写数据库。只负责ＣＲＵＤ，不管业务逻辑

UserDaoImpl:
```java
 1 package com.itheima.dao.impl;
 2 
 3 import java.sql.SQLException;
 4 
 5 import org.apache.commons.dbutils.QueryRunner;
 6 import org.apache.commons.dbutils.handlers.BeanHandler;
 7 
 8 import com.itheima.dao.UserDao;
 9 import com.itheima.domain.User;
10 import com.itheima.util.DBCPUtil;
11 
12 public class UserDaoImpl implements UserDao {
13 	private QueryRunner qr = new QueryRunner(DBCPUtil.getDataSource());
14 	public User find(String username, String password) {
15 		try {
16 			return qr.query("select * from users where username=? and password=?", new BeanHandler<User>(User.class), username,password);
17 		} catch (SQLException e) {
18 			throw new RuntimeException(e);
19 		}
20 	}
21 }
```
service是[业务逻辑层](https://www.baidu.com/s?wd=%E4%B8%9A%E5%8A%A1%E9%80%BB%E8%BE%91%E5%B1%82&tn=44039180_cpr&fenlei=mv6quAkxTZn0IZRqIHckPjm4nH00T1YdP1cYPWD4nyf4m104mHf0IAYqnWm3PW64rj0d0AP8IA3qPjfsn1bkrjKxmLKz0ZNzUjdCIZwsrBtEXh9GuA7EQhF9pywdQhPEUiqkIyN1IA-EUBt1nHnznW01Pjc)，处理数据逻辑，验证数据

完成用户登录逻辑，错误的用户名或密码则返回null
```java
 1 package com.itheima.service.impl;
 2 
 3 import com.itheima.dao.UserDao;
 4 import com.itheima.dao.impl.UserDaoImpl;
 5 import com.itheima.domain.User;
 6 import com.itheima.service.BusinessService;
 7 
 8 public class BusinessServiceImpl implements BusinessService {
 9 	private UserDao dao = new UserDaoImpl();
10 	public User login(String username, String password) {
11 		return dao.find(username,password);
12 	}
13 
14 }
```
之后是Filter层，对登录的用户的查看session是否选择了记住，如果选择，就直接进入登录后的界面。只管没有登录的，获取cookie来进行得到用户名和密码，进行登录，放入HttpSession中进行登录。
```java
 1 package com.itheima.filter;
 2 
 3 import java.io.IOException;
 4 
 5 import javax.servlet.Filter;
 6 import javax.servlet.FilterChain;
 7 import javax.servlet.FilterConfig;
 8 import javax.servlet.ServletException;
 9 import javax.servlet.ServletRequest;
10 import javax.servlet.ServletResponse;
11 import javax.servlet.http.Cookie;
12 import javax.servlet.http.HttpServletRequest;
13 import javax.servlet.http.HttpServletResponse;
14 import javax.servlet.http.HttpSession;
15 
16 import com.itheima.domain.User;
17 import com.itheima.service.BusinessService;
18 import com.itheima.service.impl.BusinessServiceImpl;
19 import com.itheima.util.SecurityUtil;
20 
21 public class AutoLoginFilter implements Filter {
22 	private BusinessService s = new BusinessServiceImpl();
23 	public void init(FilterConfig filterConfig) throws ServletException {
24 
25 	}
26 
27 	public void doFilter(ServletRequest req, ServletResponse res,
28 			FilterChain chain) throws IOException, ServletException {
29 		HttpServletRequest request;
30 		HttpServletResponse response;
31 
32 		try {
33 			request = (HttpServletRequest) req;
34 			response = (HttpServletResponse) res;
35 		} catch (ClassCastException e) {
36 			throw new ServletException("non-HTTP request or response");
37 		}
38 		
39 		//判断是否登录：
40 		HttpSession session = request.getSession();
41 		User sessionUser = (User)session.getAttribute("user");
42 			//只管：没有登录的
43 		if(sessionUser==null){
44 				//获取loginInfo的cookie
45 			Cookie loginInfoCookie = null;
46 			Cookie cs[] = request.getCookies();
47 			for(int i=0;cs!=null&&i<cs.length;i++){
48 				if("loginInfo".equals(cs[i].getName())){
49 					loginInfoCookie = cs[i];
50 					break;
51 				}
52 			}
53 			if(loginInfoCookie!=null){
54 				//截取用户名（base64）和密码（md5）
55 				String value = loginInfoCookie.getValue();// 1tzQocT+_ICy5YqxZB1uWSwcVLSNLcA==
56 				//再次向数据库验证
57 				String username = SecurityUtil.base64decode(value.split("_")[0]);
58 				String password = value.split("_")[1];
59 				User user = s.login(username, password);
60 				//对：把user放到HttpSession中。完成自动登录
61 				if(user!=null){
62 					session.setAttribute("user", user);//自动登录
63 				}
64 			}
65 		}
66 		//不管登录还是没有登录：都必须放行
67 		chain.doFilter(request, response);
68 	}
69 
70 	public void destroy() {
71 
72 	}
73 
74 }
```
