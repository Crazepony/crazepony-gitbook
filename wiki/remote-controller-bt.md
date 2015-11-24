
#  手机APP蓝牙遥控


为了能够使用智能手机，平板电脑等设备遥控，Crazepony上配置了蓝牙遥控的模块。使用我们专门为Crazepony开发的APP，就能够通过手机进行遥控。

* 传统蓝牙2.1版本已经不再生产
* Android手机需要系统在Android 4.3及以上，才能够支持BLE
* 暂时不支持手机体感控制

Crazepony支持传统蓝牙2.1和蓝牙4.0 BLE两种模式。我们使用了济南华茂科技有限公司的蓝牙透传模块HM-06（蓝牙2.1）和HM-11（蓝牙4.0 BLE）。这两块模块的大小，引脚定义都是完全一致的，所以可以互换（飞控固件和APP不能够兼容）。

**现在传统蓝牙2.1（HM-06模块）已经不再生产。**

## 蓝牙2.1通信

蓝牙2.1透传模块是传统的蓝牙串口模块，现在该产品（HM-06模块）已经停产，Crazepony已经全部使用最新蓝牙4.0 BLE透传模块。

蓝牙2.1通信带宽大，连接复杂，而且时间长。配对的时候需要使用PIN码：1234

## 蓝牙4.0 BLE通信

蓝牙BLE技术（bluetooth Low Energy）是在蓝牙4.0中引入的一个全新的2.4G通信协议，原则上它和传统的蓝牙协议（蓝牙2.1）并没有技术迭代上的关系。它有功耗低，连接方便等特点，非常适合对功耗要求高的可穿戴式设备。

我们使用的是基于TI BLE方案CC2541的蓝牙透传模块，由[济南华茂科技有限公司](http://www.jnhuamao.cn)研发生产。

![](/assets/img/hm-11.jpg)

使用该模块进行Crazepony开发的时候，最应该注意的就是带宽问题。BLE技术本身的带宽就比较小，大数据量可能会导致模块死机。下面有我们在开发中遇到的实际案例。

更多关于[BLE技术笔记](http://nieyong.github.io/wiki_ble/)。

## BLE对应的APP

**需要手机系统Android 4.3及以上才能够支持BLE。**

BLE是无法在手机系统的蓝牙设置中搜寻到的，必须配备BLE相关APP。我们提供了支持BLE的Android APP Crazepony_5.2_ble.apk[下载](http://pan.baidu.com/s/1qW9kZtq)。

![](/assets/img/ble-app-1.jpg)

蓝牙4.0 BLE连接时，无需配对，无需PIN码。

![](/assets/img/ble-app-2.jpg)

iphone手机的APP我们即将推出。

## 由printf引起的血案

使用BLE透传模块进行Crazepony开发的时候，最应该注意的就是带宽问题。BLE技术本身的带宽就比较小，大数据量可能会导致模块死机。

另外，比较特殊的一点是，Crazepony的串口使用是比较特殊的。STM32的串口1（UART1）同时连接CP2102（USB转串口芯片，用于和PC通信）和HM-11（BLE蓝牙透传模块，用于和手机通信），这个设计本来是不合串口使用规范的。会导致原来用于输出导PC的串口调试信息（printf函数输出）会同时被BLE模块接收到。

我们测试发现在启动过程中BLE蓝牙模块会概率性的出现死机现象，后来查询发现是启动信息中有大量printf输出。修改之后就不再出现该问题。

详见Github提交[616542bcd](https://github.com/Crazepony/crazepony-firmware-none/commit/616542bcd2a5b0c7f058092878e8a75ccbce23bb?diff=unified)。

![](/assets/img/ble-crash.png)
