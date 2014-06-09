---
layout: wiki
title: 源代码的文件编码和文件格式
---

# {{ page.title }}

文件编码
=============
原则上所有源代码默认使用utf-8编码。

网站源码文件必须使用utf-8编码。如果使用其它的编码，例如中文中常见的gdb格式，会导致中文乱码，或者网页无法生成的问题。

文件编码常识

Windows操作系统默认文件编码是gbk，又叫做gb2312或者cp936。cp936是微软发布的用在文件系统中的编码方式，而gb2313是中国国家标准，又叫做ANSI格式编码。例如在notepad++编辑器上gb2312编码的文件就显示为ANSI格式编码；使用Linux下的file命令，则显示为ISO-8859；在Vim下使用`set fenc?`命令查看，则显示为fileencoding=euc-cn。其实这三种都是表示gb2313编码。

Linux操作系统默认文件编码是utf-8，一般用系统宏$LANG表示。

```
$ echo $LANG
zh_CN.UTF-8
```

下面几个crazepony固件代码文件，就是使用的Windows下的默认编码gb2313。为了在某些工具下（例如gitk工具）中文不显示为乱码，我们要求所有的文件都使用utf-8编码。但是由于我们现在使用的Keil 4不支持utf-8编码，所以utf-8编码的中文在Keil 4下面会显示为乱码，所以这部分固件代码没有使用utf-8编码。

```
$ file User_Src/*
User_Src/main.c:           ISO-8859 C++ program text
User_Src/Sys_Fun.c:        ISO-8859 C program text
User_Src/Sys_Fun.h:        ISO-8859 C program text
……
```



行结束符问题
=============
在Linux/Windows/Mac下，行结束符不一样。这样在多个平台之间进行协作开发时，在checkin和checkout之后，会有很多行结束符不统一引起的问题。

添加.gitattribute文件，可以解决行结束符在多个平台下不一致的问题。

现在使用的.gitattribute配置为：

* 代码库中都为LF，也就是checkin的时候，会把所有文件的行结束符转化为LF；
* 工作路径下为所在OS的行结束符，也就是在checkout的时候，git回自动根据当前的OS将文件的行结束符做转化；
* 对于图片，jar库，和so文件等二进制文件，不进行上面的转化；
