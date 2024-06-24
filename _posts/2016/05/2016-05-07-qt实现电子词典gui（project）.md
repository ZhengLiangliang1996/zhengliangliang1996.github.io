---
toc:
  sidebar: true
giscus_comments: true
layout: post
title: "QT实现电子词典GUI（project）"
date: "2016-05-07"
categories: 
  - "qt"
---

 

**利用基本的C语言的I/O流和一些简单的语句写的QT版电子词典，源码包括可用gcc编译的版本和QT编译的版本。小项目地址:[Fork me onGithub!](https://github.com/charlieputh/Digital_Dictionary)**

以下是辞典的内容 dict.txt

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/05/2016-05-07_103714.png" alt="screenshot" width="80%" height="auto">
</p>

### 1.选定变量

不难发现，词典的内容基本都是一行英文，下面一行是Trans（翻译）。所以在查找的过程如果是需要用key代表英文，用content代表翻译。而且用指针进行定义，放在struct dict里面，因为作为指针更好进行再堆里面动态分配内存，因为在遍历字典dict.txt文件的时候可以知道大小，所以不能定义成char类型再栈里面一次性分配。

- **struct部分**

```c++
struct dict{
	char *key;                                               //words distribute(malloc)
	char *content;                                           //words in translation
};
```

- **基本流程**

1.打开dict.txt文件

2.用户输入单词

3.查找单词 并 打印翻译到屏幕(或者中译英)

4.清理内存

 

* * *

**1.打开dict.txt文件**

写成int open_dict(struct dict **p,const char * dict_filename) 函数

具体代码:
```c++
/*Open the dict and read the content in it*/
int open_dict(struct dict **p, const char *dict_filename){
	FILE *pfile = fopen(dict_filename, "r");                 //open it by READ only
	if (pfile == NULL)
		return 0;                                        //If open failed return 0

	*p = (struct dict *)malloc(sizeof(struct dict) * Max);   //Distribute The Memory
	memset(*p, 0, sizeof(struct dict)*Max);                  //Initial it to 0
	struct dict *pD = *p;                                    //pD point to the *p 

	char buf[1024] = { 0 };                                  //Cache
	size_t len = 0;                                          //long unsigned int 
	int i = 0;                                               //counting method
	while (!feof(pfile)){                                    //Read the file recursively 
		memset(buf, 0, sizeof(buf));
		fgets(buf, sizeof(buf), pfile);                  //read one line
		len = strlen(buf);                                  
		if (len > 0){
			pD[i].key = (char *)malloc(len);         //distribute the memory 
			memset(pD[i].key, 0, len);
			strcpy(pD[i].key, &buf[1]);              //copy it Notice [#a]
		}

		memset(buf, 0, sizeof(buf));
		fgets(buf, sizeof(buf), pfile);
		len = strlen(buf);
		if (len > 0){
			pD[i].content = (char *)malloc(len);
			memset(pD[i].content, 0, len);
			strcpy(pD[i].content, &buf[6]);
		}
		i++;
	}
```
代码解释:

1.第一个形参是二级指针，代表指向dict *类型的首地址的指针 第二个形参是const类型文件名 2.基本的文件I/O操作，以只读方式打开。if（pfile == NULL）异常处理。 3.动态分配内存，大小是dict.txt里面行数的一半(一个词条占两行) 4.经验学习:动态分配内存时候都要运用memset进行清零操作 void * memset( void *str , int chr , size_t len ) 5.处于安全和指向考虑，定义指向*p的指针 6.第一行读key 第二行读content. fgets(line by line) （注意strcpy里面 buf第一个读得key是从[1]开始 buf第二个读得content从[6]开始，因为dict.txt里面词条分布的缘故，可以看第一张图。）

 

**2.用户输入单词**

用户输入单词，只需要用while(1)进行循环输入，并且设定一个command-exit用于退出的操作。

代码:
```c++
char key[1024];
char content[1024];
while (1){                                         	//while(1) can input constantly
	memset(key, 0, sizeof(key));
	memset(content, 0, sizeof(content));
	scanf("%s", key);                              	//get word from the user
	if (strncmp(key, "command-exit", 12) == 0)     	//make an exit command
			break;
        //...About the search
}
```
**3.查找单词 并 打印翻译到屏幕(或者中译英)**

在函数int search_dict(const struct dict *p, int size, const char *key, char *content)实现。

传入结构*p用户遍历查找，char *key是用户输入的，size是刚刚打开dict.txt返回的词条数字。

代码:
```c++
/*Search for the content according to the key*/
int search_dict(const struct dict *p, int size, const char *key, char *content){
	int i = 0;
	for (i = 0; i < size; i++){
		if ((p[i].key == NULL) || (p[i].content == NULL))
			continue;
		if (strncmp(p[i].key, key, strlen(key)) == 0)
		{
			strcpy(content, p[i].content);
			return 1;                            //find the word ,return 1
		}
	}
	return 0;                                            //if not ,return 0
}
```
一个一个进行对比。找到则返回复制到content里面，利用*共用内存关系直接返回。

**4.清理内存**

要对刚刚分配词条数的struct dict*p进行释放内存。十分简单。

代码:
```c++
void free_dict(struct dict *p, int size)
{
	int i = 0;
	for (i = 0; i < size; i++)                       //Free the memory recursively
	{
		if (p[i].key)
			free(p[i].key);
		if (p[i].content)
			free(p[i].content);
	}
	free(p);                                         //free p
}
```
完整的代码加上了clock函数来进行计算所需要的秒数。 [源代码](https://github.com/charlieputh/Digital_Dictionary/blob/master/test0.c)

运行:

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/05/2016-05-07_113649.png" alt="screenshot" width="80%" height="auto">
</p>

 


 

* * *

* * *

将上述代码改为QT版:

先制作Design界面：

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/05/2016-05-07_114248.png" alt="screenshot" width="80%" height="auto">
</p>

然后添加槽，对代码进行一些编码和文件名写死的修改，就可以啦

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/05/2016-05-07_114429.png" alt="screenshot" width="80%" height="auto">
</p>

<p align="center">
  <img src="https://zhengliangliang.files.wordpress.com/2016/05/2016-05-07_114510.png" alt="screenshot" width="80%" height="auto">
</p>

项目地址：[Fork me on github!](https://github.com/charlieputh/Digital_Dictionary-Qt)
