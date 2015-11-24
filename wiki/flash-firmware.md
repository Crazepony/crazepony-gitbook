
#  USB固件烧写


> 作者：nieyong

编译好STM32的代码，得到hex格式的固件文件，如何烧写到主控中？

Crazepony将SWD调试接口预留出来，可以使用J-Link或者ST-Link等调试器进行开发，详见[J-Link的使用及常见问题](./jlink-debug.html)。Crazepony也支持USB口烧入，即采用ISP下载，操作简单。只需要安装cp2102驱动程序，使用一根Mini USB数据线连接电脑。这里就详细介绍使用USB固件烧写流程。

首先从crazepony的百度云盘中下载开发工具，点击[这里](http://pan.baidu.com/s/1eQ1kfPw)。解压压缩文件得到3个文件夹。

## 安装cp2102驱动
cp2102是Crazepony上使用的USB转串口芯片。cp2102和STM32芯片以串口相连，和电脑PC以USB接口相连，这是Crazepony能够接上USB线对飞控/遥控器进行固件烧写编程和调试信息打印的原因。

首先要把cp2102的驱动在电脑PC上装好，这样电脑作为Host才能够识别到cp2102。这个驱动在32位windows xp系统/64位 windows 7系统下都测试通过。

![](/assets/img/cp2102.jpg)

安装成功之后，在我的电脑->设备管理->端口（COM和LPT），就可以看到Crazepony对应的串口号，例如下图为COM3。看到该串口中有关于CP210x的描述。

![](/assets/img/param-assistant-3.png)

## 烧入hex文件
打开ISP下载器，载入需要下载的hex文件，具体如下图所示。

![](/assets/img/download-1.jpg)

在硬件设计上，直接使用CP2102复位STM32并且引导进入串口升级固件的ISP下载模式。CP2102使用RTS高电平复位STM32芯片，然后使用DTR将STM32的Boot0引脚拉低，STM32进入串口升级固件的ISP下载模式。所以在ISP下载器上，必须选择左下角的“RTS的高电平复位，DTR高电平进Bootloader”。


## 查看打印信息

连上USB线，打开串口助手，波特率设置为115200，查看串口打印信息。默认每隔1秒打印一次传感器数据信息。

> Crazepony默认出厂固件串口打印信息和上位机数据都关闭。USB串口打印和USB上位机同时只能够使用一个，不能够同时使用。原因是串口上的上位机数据在串口助手上看到的是乱码。要使用串口打印信息，请开启`SysConfig.h`中的`DEBUG_UART`宏。要使用上位机查看信息，请关闭`SysConfig.h`中的`DEBUG_UART`宏，并开启`main.c`中的`CommPCUploadHandle()`函数。

![](/assets/img/uart-info.jpg)
