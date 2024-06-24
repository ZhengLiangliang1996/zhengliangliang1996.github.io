---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "Bug：解决 nginx 502 Bad GateWay"
date: "2017-02-23"
categories: 
  - "未分类"
---

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/02/15094716_nehh.png" alt="screenshot" width="80%" height="auto">
</p>

**重新更换了一台笔记本，需要重新进行搭建Laravel的环境，但是搭建完virtualbox和vagrant之后，用nginx进行了站点映射的配置，但是打开界面显示的是。502 bad Gateway/Nginx 1.8.0.**

**我的nginx里的配置如下：**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/02/1.png" alt="screenshot" width="80%" height="auto">
</p>

**配置核对了，location所显示是9000端口，配置没有问题。于是查看日志文件。错误显示如下：**

**在网上找了许多502 bad gateway的解决办法，都是修改配置文件，但是我的配置文件并没有问题的。于是在栈溢上边问，找到类似的问题是php5没有启动，于是查看控制php5-fpm的端口**

 1 netstat -ntpl

**发现并没有启动php5-fpm的9000端口，则进行restart  netstat -an未发现监听9000端口。**

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/02/2.png" alt="screenshot" width="80%" height="auto">
</p>

**发现仍然无果****，怀疑是php5端口的问题。**

**查看/var/log/php5-fpm.log一切正常。**

**随后查看/etc/php5/fpm/pool.d/www.conf，发现listen = /var/run/php5-fpm.sock**

**将listen设置为9000,即改成listen=9000 如图<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/02/3.png" alt="screenshot" width="80%" height="auto">
</p>**

**重启php5-fpm与nginx后，恢复。进行项目git clone 再 migrate和seeder就看到原来的考试系统了<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2017/02/qqe59bbee7898720170223221246.png" alt="screenshot" width="80%" height="auto">
</p>**

**后续又可以大干一场了呢！**

**小结：php5的配置改成了sock，修改成监听127.0.0.1:9000即可.**

charlie
