---
layout: wiki
title: 通信部分介绍
---

# {{ page.title }}

通信协议指的是遥控端和主控之间交互数据的封装，是一种自行约定的数据封装格式。我们采用的是Crazyflie项目中定义的[CRTP协议](http://wiki.bitcraze.se/projects:crazyflie:firmware:comm_protocol)。

遥控端和主控之间数据的交互，物理层可以有下面几种方式：

* 单片2.4G无线射频收发芯片，通过SPI接口和MCU连接
* 蓝牙2.1透传模块，通过串口UART和MCU连接
* 蓝牙4.0低功耗BLE透传模块，通过串口UART和MCU连接

这几种不同的物理层通信方式在同一时刻只能够选择其中的一种。并且蓝牙2.1和蓝牙BLE根据安装的透传模块不一样进行选择。

![crazyflie task](/assets/img/crazyflie-task-comm.png)


## ESky Protocol

在上面示意图的的通信方式选择上，最左边为EskyLink，对应使用宏USE_ESKYLINK来开启是否选择该种链接方式。

```
# Make copter firmware to be used with the bootloader, CF controlled with eSky ET6i transmitter

$ make clean && make USE_ESKYLINK=1 CLOAD=1 all 
```

所谓的Esky Protocol，其实时ESky公司遥控器使用的通信协议。所以如果选用这种通信方式，那么可以使用ESky航模公司的遥控器进行控制。Crazyflie官网支持[ESKY ET6I Remote Control](http://wiki.bitcraze.se/projects:crazyflie:hacks:et6i)遥控器。

关于ESky公司的2.4G遥控器设备的通信协议，参考[ArduinoRCLib](http://sourceforge.net/projects/arduinorclib/)项目中的描述：

> The Esky 2.4 GHz equipment uses the Nordic NRF2401AG in both the transmitter and receiver. A compatible alternative to this chip is the NRF24L01+ (which is widely available).

ESky相关协议内容暂时不研究。

## 串口

使用串口作为物理层指的是蓝牙透传模块（包括蓝牙2.1或者蓝牙4.0 BLE模块）。串口配置为115200 8N1，收发异步。

一个可供主控解析的数据包格式，约定如下：

```
  7   6   5   4   3   2   1   0
  +---+---+---+---+---+---+---+---+
  |     Port      |  Res. | Chan. | 
  +---+---+---+---+---+---+---+---+
  |            DATA 0             |
  +---+---+---+---+---+---+---+---+
  :   :   :   :   :   :   :   :   :
  +---+---+---+---+---+---+---+---+
  |            DATA 31            |
  +---+---+---+---+---+---+---+---+
```
开始为一个字节的头，该字节中包括port字段，reserve字段，channel字段。紧跟着该自己，就是0-31个字节的数据，数据的长度是任意的。

头字节中的port字段用来区分该数据包的功能，常见的包括下面几个

* 0x0 : console
* 0x2 : parameter，表示后面的数据是系统的参数
* 0x3 : commander，*操作命令*，控制飞机的飞行，包括pitch/yaw/roll等
* ……

对于串口传输，在上面数据包的最前面需要加上两个字节0xaaaa的起始数据，在最后加上一个字节的checksum数据。格式如下：

```
  7   6   5   4   3   2   1   0
  +---+---+---+---+---+---+---+---+
  |             0xAA              |
  +---+---+---+---+---+---+---+---+
  |             0xAA              |
  +---+---+---+---+---+---+---+---+
  |      Port     |  Res  | Chan. |
  +---+---+---+---+---+---+---+---+
  |         Packet length         |
  +---+---+---+---+---+---+---+---+
  |            DATA 0             |
  +---+---+---+---+---+---+---+---+
  :   :   :   :   :   :   :   :   :
  +---+---+---+---+---+---+---+---+
  |            DATA 30            |
  +---+---+---+---+---+---+---+---+
  |            Cksum              |
  +---+---+---+---+---+---+---+---+

  +--------+--------+--------+--------+--------+--....--+--------+
  |  0xAA  |  0xAA  | Header | Length | Data0  | Packet | Cksum  |
  +--------+--------+--------+--------+--------+--....--+--------+
```
注意，紧跟在头后面的第一个data字节，表示后面数据的长度。


## 操作命令
操作命令是指用于控制飞行器起飞，前后左右运动的命令，英文commander。操控命令是遥控器最基本，也是最常用的命令。数据包头中port字段为0x3表示操作命令。[Crazyflie操作数据](http://wiki.bitcraze.se/projects:crazyflie:crtp:commander)格式约定如下。

```
+-------+-------+-------+-------+
| ROLL  | PITCH |  YAW  |THRUST |
+-------+-------+-------+-------+
0       4       8       12      14 bytes
```
操作数据一共14个字节，前12个字节分别表示Roll，Pitch，Yaw的值，每个值使用4个字节。后2个字节表示Thrust的值，使用2个字节。

所以，使用串口发送的一个操作命令示例如下：

```
0xaa 0xaa 0x30 0x0e 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x00 0x3e
```
