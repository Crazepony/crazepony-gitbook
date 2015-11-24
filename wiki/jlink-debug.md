
#  J-Link的使用及常见问题


> 作者：nieyong

crazepony除了可以使用usb接口下载程序之外，还将swd接口预留到了板外。可以使用J-Link，ST-Link等工具进行代码的烧写/在线调试等。下面介绍J-Link的配置和常见问题。

## J-Link与Crazepony的接线
一般我们买到的J-Link如下所示，是一个20针的排线口。对于SWD接口，我们只需要使用3根线就可以。J-Link和Crazepony的连接如图如下，使用彩虹排线连接就可以。（Crazepony的SWD接口排阵默认未焊接）

* 1所指排针与飞控的VCC相连（如果飞机自己供电，可以不连接）
* 2所指排阵与飞控的GND相连
* 3所指排阵并飞控的DIO相连
* 4所指排阵并与飞控的CLK相连

![](/assets/img/jlink-7.4.jpg)

J-Link与Crazepony相连示意图。Crazepony遥控器的连接也是同理。

![](/assets/img/jlink-8.jpg)

## J-Link的配置和使用
使用keil打开crazepony工程文件，点击Options for Target 'Crazepony'，选择Debug部分，下拉选择J-Link/J-Trace Cortex.

![](/assets/img/jlink-9.png)

然后点击设置，配置如下。

![](/assets/img/jlink-1.png)

在选择了SW接口之后，将飞控开关打到on，点击Auto Alk，如果连接正确，就会扫描到开发板上的SW接口。

## J-Link固件烧写

在插拔的过程中，J-Link经常会出现固件丢失无法使用的情况，这时需要重刷J-Link调试器的固件。或者从keil 4切换导Keil 5的时候，需要升级J-Link调试器固件。

下面以J-Link V8型号调试其为例说明如何重刷J-Link的固件。

安装AT91-ISP，安装完成后在桌面上将有两图标。

![](/assets/img/jlink-2.jpg)

擦除芯片，进入编程模式。J-Link面板上有两对接口，其中A为擦除，B为编程接口。

![](/assets/img/jlink-3.jpg)

擦除芯片过程，将J-Link连接到电脑，短接A两孔约5秒钟，断开，然后拔掉J-Link与电脑的连接。如果重新连接电脑，led灭掉，在设备管理中找不到任何相关设备，则表示擦除成功。

擦除成功后，要进入编程模式。进入编程模式的过程，短接B两孔，连接接J-Link到电脑，至少约10秒钟，拔掉USB线，断开B处短接。再次插上电脑，在设备管理中有未知设备出现，则表示进入编程模式成功。

![](/assets/img/jlink-3.png)

如果已经安装了AT91-ISP，并且其驱动运转正常，那么可以J-Link被识别为一个USB转串口设备，表示进入编程模式成功。我们测试有些电脑安装之后驱动会不正确，请换一台电脑重试。只有驱动正常，入下图所示，才可以烧入固件。

![](/assets/img/jlink-4.png)

双击SAM-PROG v2.4, 运行烧录软件如下。

![](/assets/img/jlink-5.jpg)

将J-Link通过USB线与PC机连接。此时，SAM-PROG v2.4软件中的Write Flash
按钮将变为有效。注意，先打开SAM-PROG v2.4，再连接J-LINK与PC机。 

点击Write Flash按钮，烧录固件，待烧录完成后，Active Connection：将变为 1。 

如果遇到问题是write flash一直都是灰色的，那么可能是AT91-ISP驱动未正常运行，无法J-Link识别为USB转串口设备。换台电脑就可以。

至此,J-LINK的固件已经更新完毕，正常情况下，连接电脑与J-LINK时，JLINK的指示灯将闪烁。如果J-Link驱动安装正确，那么LED最后常绿。 

## Keil 5下面J-Link失效的问题

在Keil 5下面，老版本的J-Link可能无法使用，出现下面的提示。这个时候需要升级J-Link固件。参考文档[MDK5安装与JLINK问题解决方法(支持代码自动补全)](http://www.9mcu.com/9mcubbs/forum.php?mod=viewthread&tid=1050785)

![](/assets/img/jlink-5.png)




