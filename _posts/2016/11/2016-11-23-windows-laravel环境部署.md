---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Windows Laravel环境部署"
date: "2016-11-23"
categories: 
  - "other"
  - "php"
---

#  **Windows上环境搭建**

-  Tool

 [**VirtualBox**](https://www.virtualbox.org/) :**开源虚拟机软件**

 **[Varant](https://www.vagrantup.com/downloads.html)** :**_Vagrant_是一个基于Ruby的工具，用于创建和部署虚拟化开发环境**

 **VPS**  :**FQ**

- **Homestead Install：(PS:安装vagrant需要vpn，国内镜像慢成狗)**

``` 
 1 mkdir vagrant_getting_started  
 2 cd vagrant_getting_started    
 3 vagrant init  laravel/homestead    
 4 vagrant box add laravel/homestead   
 5 vagrant up
 ```

**在以上的 vagrant box add laravel/homestead之中，会有如下的显示**
```
 1 ~  vagrant box add laravel/homestead
 2 ==> box: Loading metadata for box 'laravel/homestead'
 3    box: URL: https://atlas.hashicorp.com/laravel/homestead
 4 This box can work with multiple providers! The providers that it
 5 can work with are listed below. Please review the list and choose
 6 the provider you will be working with.
 7 
 8 1) virtualbox
 9 2) vmware_desktop
10 
11 Enter your choice: 1
```

**选择1**

**启动了虚拟机之后，虚拟机里面已经安装好了Laravel和Composer，这是比较方便的一个地方.【ps:开vpn！开vpn！开vpn！重要事情说3遍】**

- **edit Homestead**

**Homestead:**

**Laravel Homestead是一个官方的、预封装的Vagrant“箱子”，它提供给你一个奇妙的开发环境而不需要你在本机上安装PHP、HHVM、web服务器和其它的服务器软件。**

**完成了上面的步骤之后，就进行配置Homestead的映射地址**

**在所安装位置里**

``` homestead init```


<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/11/2016-11-23_222814.jpg" alt="screenshot" width="80%" height="auto">
</p>

**红色圈住的位置是映射地址 就用默认的不需要改变**

- **Mysql数据库的账号和密码是**
```
 1 user: homestead
 2 password: secret
```

- **配置nginx**

**Nginx是一款[轻量级](http://baike.baidu.com/subview/1318763/16205192.htm)的[Web](http://baike.baidu.com/subview/3912/15992867.htm) 服务器/[反向代理](http://baike.baidu.com/view/1165595.htm)服务器及[电子邮件](http://baike.baidu.com/view/1524.htm)（IMAP/POP3）代理服务器，并在一个BSD-like 协议下发行.**

**首先在nginx的配置文件夹中加入一个文件**

**vim /etc/nginx/sites-enable/伪站点** 

**例如**       **vim /etc/nginx/sites-enabled/dev.lucy.com.conf**
```javascript
 1 server {
 2  listen        80;
 3  server_name   dev.lucy.com;
 4  root          /vagrant_data/lucy/public;
 5  index         index.php index.html index.htm;
 6 
 7  location / {
 8    index  index.php index.html index.htm;
 9    try_files $uri @rewrite;
10   }
11 
12   location @rewrite {
13     rewrite ^ /index.php;
14   }
15 
16   location ~ .php$ {
17     fastcgi_pass 127.0.0.1:9000;
18     fastcgi_index index.php;
19     include fastcgi.conf;
20   }
21 access_log /vagrant_data/logs/lucy.access.log;
22  error_log /vagrant_data/logs/lucy.error.log;
23 }
```
**新建一个php项目在/vagrant_data目录下叫 lucy 命令行是** 

``` 
 1 $laravel new lucy
 2 //creaye log files without wirting anything
 3 $vim lucy.access.log
 4 $vim lucy.error.log
```

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/11/2016-11-23_231433.jpg" alt="screenshot" width="80%" height="auto">
</p> 

**在Homestead所在同级目录下有VagrantFile，可以配置只有本虚拟机可以访问和修改的私有地址。**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/11/2016-11-24_232226.png" alt="screenshot" width="80%" height="auto">
</p>

**然后去自己的windows下面的host文件下修改配置**

```192.168.33.11  dev.lucy.com```

**最后可以看到自己的美丽的界面**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/11/2016-11-24_2331351.png" alt="screenshot" width="80%" height="auto">
</p>
