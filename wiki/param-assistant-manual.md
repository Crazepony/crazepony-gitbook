
#  Crazepony上位机使用手册


>作者：nieyong

Crazepony四轴飞行器提供一个Windows PC端上位机软件，用于查看姿态数据，调节PID等操作。该上位机使用C#编写，源代码暂时没有开源。下面介绍上位机的配置和使用。

首先，从[百度云盘](http://pan.baidu.com/s/1gdf9bKf)下载最新的上位机，得到的文件如下，点击其中的可执行文件，打开上位机软件。

![](/assets/img/param-assistant-1.png)

将Crazepony四轴使用usb线连接到电脑，并且安装usb转串口驱动（关于如何安装该驱动，参考[《固件烧写》](/wiki/flash-firmware.html)中的安装cp2102驱动部分）。我的电脑->设备管理->端口（COM和LPT），就可以看到Crazepony对应的串口号，例如下图为COM3。Crazepony是使用CP210x芯片实现的USB转串口功能，所以会看到该串口中有关于CP210x的描述。

![](/assets/img/param-assistant-3.png)

接下来是在上位机中选择Crazepony串口。步骤如下图所示。如果提示串口已经被打开，可以在左上角的串口操作中选择关闭串口，再进行操作。如果串口正常连接并且打开，那么上位机就可以接收Crazepony的数据，晃动一下Crazepony会发现左上角的视图在变化。

![](/assets/img/param-assistant-4.png)

查看/修改PID参数。点击右边的参数设置，可以配置Crazepony的PID参数。

todo

监视姿态信息。电机右边的曲线控制，可以监视Crazepony的实时姿态信息。

![](/assets/img/param-assistant-5.png)

## 蓝牙无线调参

除了使用usb线连接上位机之外，还可以使用蓝牙无线连接上位机，这样可以省去连接线的束缚。

* 需要电脑有蓝牙设备
* 开飞机电源，打开电脑蓝牙设备查找，找到一个叫crazepony的设备配对连接，配对码为*1234*
* 打开电脑设备管理器，查看蓝牙透传串口号
* 打开上位机，选择刚刚看到的串口号，波特率115200，确认连接。
