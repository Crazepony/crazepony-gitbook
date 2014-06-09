---
layout: wiki
title: Windows下开发环境搭建-裸机版本
---

# {{ page.title }}

IDE开发工具Keil v4.10下载地址：Crazepony百度云网盘[Keil-uVision4-MDK4-12.zip](http://pan.baidu.com/s/1ntNqLdv)。

裸机飞控源代码下载地址：Github项目[crazepony-firmware-none](https://github.com/Crazepony/crazepony-firmware-none/releases)。

## 环境配置说明
裸机版本是指没有使用RTOS的主控固件版本。源代码对应github上的地址为。由于没有使用RTOS，所以代码更加简单明了，适合初学者使用。

裸机版本的代码使用Keil 4进行开发编译，下面介绍编译环境的搭建和编译过程。

## Keil 4的安装和破解
由于主控使用的是ARM Cortex-M3内核的STM32，所以必须使用带有ARM编译工具链的Keil 4。网络上很多只有几十兆大小的的Keil 4可能只支持C51开发。Crazepony百度云网盘提供带有ARM编译工具链的Keil 4安装文件下载，带有破解注册机和破解说明文档。用户自行下载安装，可以看到该Keil版本为v4.10。

![](/assets/img/keil-version.jpg)

该安装文件在Windows XP，32位系统上测试通过。已知存在的问题： 

* 不支持utf-8编码。utf-8编码的中文在Keil 4下面会显示为乱码，所以这部分固件代码没有使用utf-8编码。没有找到能够配置支持utf-8的地方，很可能是Keil版本比较老，或者破解导致无法支持utf-8编码。

## 源代码下载
主控固件裸机版本，裸机指没有使用实时操作系统RTOS。由于没有使用RTOS，所以代码更加简单明了，适合初学者使用。

Crazepony项目是开源的，所有代码都托管在Github的[Crazepony项目](https://github.com/Crazepony)下。裸机源代码放置在[crazepony-firmware-none](https://github.com/Crazepony/crazepony-firmware-none)下，命名中的none表示不使用RTOS。

可以直接使用git获得源代码，也可以从[crazepony-firmware-none release](https://github.com/Crazepony/crazepony-firmware-none/releases)下载各个版本的裸机源代码。

![](/assets/img/git-download.png)

## 源代码导入和编译
在源代码中，有三个文件为Keil工程文件。

```
IMU_AHRS.uvopt
IMU_AHRS.uvproj
IMU_AHRS_IMU_AHRS.dep
```
使用上面安装的Keil 4打开文件`IMU_AHRS.uvproj`，就能够导入整个工程。如下图所示。

![](/assets/img/keil-build.jpg)

点击左上角的编译按钮，编译整个项目，在工程下生成Output目录，目录中aircraft.hex就是可以烧写到STM32的固件。参考另外一篇文章《主控固件烧写》将固件写入STM32中。
