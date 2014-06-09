---
layout: wiki
title: STM32开发环境搭建-linux
---

# {{ page.title }}

Crazepony飞控主板使用STM32作为主控制器，下面主要介绍如何在ubuntu系统下进行STM32固件的开发/编译/下载。

对STM32处理器代码的开发需要在ubuntu系统下搭建arm嵌入式开发的交叉编译工具链。测试的系统为ubuntu 14.04。

## 交叉编译工具链安装方法一
STM32处理器使用gcc-arm-none-eabi-交叉编译链。使用wget下载交叉编译工具链到本地，并且解压缩到`~/bin/`目录下。

```
wget https://launchpad.net/gcc-arm-embedded/4.7/4.7-2013-q1-update/+download/gcc-arm-none-eabi-4_7-2013q1-20130313-linux.tar.bz2
mkdir ~/bin
tar xjf gcc-arm-none-eabi-4_7-2013q1-20130313-linux.tar.bz2 -C ~/bin
```

修改~/.bashrc文件，将交叉编译工具链的路径添加到当前用户的默认搜索路径下。并且使用source命令使其马上生效。

```
echo -e "\nPATH=\$PATH:$HOME/bin/gcc-arm-none-eabi-4_7-2013q1/bin" >> ~/.bashrc
source ~/.bashrc
```

可以使用type命令检测交叉编译工具是否安装成功。例如检测其`arm-none-eabi-gcc`命令，可以看到其在刚才安装的~/bin目录下检测到。

```
type arm-none-eabi-gcc
arm-none-eabi-gcc 是 /home/ny/bin/gcc-arm-none-eabi-4_7-2013q1/bin/arm-none-eabi-gcc
```

## 交叉编译工具链安装方法二
方法一需要手动下载gcc-arm-none-eabi-工具链压缩包，解压缩，然后手动配置工具链的地址系统默认路径下。该方法适合几乎所有的Linux系统，例如fedora/ubuntu/debian等。对于ubuntu用户，可以直接使用apt包管理工具进行安装。

* 由于gcc-arm-none-eabi-没有包含在ubuntu默认支持的包内，需要添加一个支持gcc-arm-none-eabi-的源：

```
sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded
```

* 更新添加的源：

```
sudo apt-get update
```

* 安装gcc-arm-none-eabi-工具链

```
sudo apt-get install gcc-arm-none-eabi
```

使用type命令检查是否安装成功，如果出现下面的提示，那么就说明安装成功，可以使用。

```
$ type arm-none-eabi-gcc
arm-none-eabi-gcc 是 /usr/bin/arm-none-eabi-gcc
```

## arm-none-eabi说明
arm相关的交叉编译工具链由很多，例如arm-linux-eabi，arm-none-eabi。STM32处理器使用的是arm-none-eabi。

```
arm-none-eabi和arm-linux-eabi等的区别：
arm-linux-eabi 用于编译arm linux内核代码。
arm-none-eabi 不指名操作系统，可以是linux, 也可以是vxworks等，arm-none-eabi 不包含 __linux__ 等特定宏，所以往往编译linux 内核的时候通不过，不支持那些跟操作系统关系密切的函数，比如fork(2)，使用的是newlib这个专用于嵌入式系统的C库。
arm-none-linux-eabi 用于Linux的，使用Glibc。
```

## 硬件开发工具
Crazyflie电路原理图使用的KiCad，KiCad以一个开源的EDA工具，并且跨平台，在windows和linux下都能够使用。

KiCad的home page：[http://www.kicad-pcb.org/](http://www.kicad-pcb.org)。在ubuntu下的安装：

```
sudo apt-get install kicad
```
