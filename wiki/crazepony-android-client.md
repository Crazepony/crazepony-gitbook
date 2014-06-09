---
layout: wiki
title: Crazepony Android客户端
---

# {{ page.title }}

Crazepony的Android客户端源代码也是托管在github的crazepony项目下，点击[这里](https://github.com/Crazepony/crazepony-android-client)查看。可以直接下载zip压缩包，也可以通过git clone到本地。

```
git clone git@github.com:Crazepony/crazepony-android-client.git

```

## Android开发环境搭建
Crazepony的Android客户端开发需要搭建Android APP开发环境。最简单的办法是使用Google Android提供的一站式开发包[ADT Bundle](http://developer.android.com/sdk/index.html)。ADT Bundle提供了Android APP开发所需的所有工具，包括Eclipse IDE，ADT (Android Developer Tools) 插件，java库等等。

> 下载地址：[http://developer.android.com/sdk/index.html](http://developer.android.com/sdk/index.html)


下载解压缩到任意目录，就可以使用，无需安装。

## 配置说明

Crazepony的Android客户端默认编译的Android SDK API版本为15（对应Android 4.0.3），支持的Android版本为4.0.0或以上。

![](/assets/img/Android-SDK-Manager.png)

![](/assets/img/Properties-for-CrazyflieControll.png)

## 关于通信

使用蓝牙和主控上的蓝牙透传模块通信，APP为主设备（master），主控上的蓝牙透传模块为从设备（slave）。具体协议参考《通信协议》一文。

APP发送操作命令的频率为20Hz，也就是说50ms发送一个操作命令包。

暂时没有添加《通信协议》中提到的Packet length字段和checksum字段。原因是我觉得他们如此有点儿混乱，和其它数据包的处理不一致。

下面为蓝牙透传模块接收到的数据截图：

![](/assets/img/uart-rc.png)
