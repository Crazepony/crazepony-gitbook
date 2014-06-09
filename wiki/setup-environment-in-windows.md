---
layout: wiki
title: Windows下开发环境搭建
---

# {{ page.title }}

## 环境配置说明
目前采用Keil+gcc+jlink是最好的编译与调试方法。Keil内部有自己的编译工具链，但是Keil自带的编译器不支持目前代码的许多语法，所以建议使用gcc工具链。等代码稳定未来可以直接移植到Keil自带的编译器上。

## 安装arm-none-eabi gcc工具链
arm-2013.11-24-arm-none-eabi的[下载地址](http://url.cn/Q47CUQ)

* 为了后面配置的方便，在其中的"Next"菜单中选择 “添加参数到环境变量” (菜单提示的是英文)
* 路径请注意中间不要有空格。比如我的根路径是：D:\MentorGraphics\Sourcery_CodeBench_Lite_for_ARM_EABI

## 使用Keil4
若Keil4能配置成功，选择Keil4将是最方便的办法。安装Keil4并配置gcc的方法：

* 打开工程
* 点击菜单 Project->Manage->Component,Envrenment,Book。选择Folders/Entensions，选择勾中gcc
* 把路径设置为工具链的根目录，比如我的环境设置为：D:\MentorGraphics\Sourcery_CodeBench_Lite_for_ARM_EABI
* 如图所示：

![keil gcc配置方法](http://jannson.github.io/images/keil_gnu.jpg)

## 使用Keil5
若Keil4通过以上配置，编译工程的时候提示找不到gcc或认不出来编译文件的名字，那么请安装Keil5。Keil5的安装文件是Keil4的几倍，很多组件与模板都需要分开来安装，安装稍微比较麻烦。

* 下载并安装：[mdk510.exe](http://url.cn/RpNDSG)
* 下载并安装：[mdkcm510.exe](http://url.cn/OnByyf)
* 下载并安装：[Keil.ARMCortex_D...0.0.1.pack Cortex相关模板文件](http://url.cn/OzaCAP)
* 下载并安装：[Keil.STM32F1xx_D...1.0.4.pack STM32F1xx相关模板](http://url.cn/PHqblw)
* 下载[破解程序](http://url.cn/R2Pxw1)
打开keil5-->FILE-->Lisence Managerment 用破解程序生成序列号并输入到keil5里。破解成功。
* 下载：http://url.cn/O3oSQL 解压并替换keil5根目录开始的C:\Keil_v5\ARM\Segger压缩包里的两个文件，以进行jlink调试：
* 配置gcc如同Keil的方法。
* 注意jlink的驱动：win7 x64与win7/winxp x86可能不一样（TODO提供链接下载）

## 使用原生态的make编译
使用原生态的make编译也很方便，并且也可以通过keil来下载并调试

* 安装arm-none-eabi工具链
修改工具链根目录下的cs-make.exe为make.exe，cs-rm.exe为rm.exe
* 安装python2.7并把其加入到环境变量
* 下载MyGit，并得到Git的windows版工具
* 下载crazyflie的默认python-client代码，与此版本代码在同一级目录
* 打开MyGit，cd到项目代码目录并：
`make`

