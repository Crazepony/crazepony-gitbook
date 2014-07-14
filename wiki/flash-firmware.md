
#  主控固件烧写


编译好STM32的代码，得到hex格式的固件文件，如何烧写到主控中？

首先从crazepony的百度云盘中下载开发工具，点击[这里](http://pan.baidu.com/s/1eQ1kfPw)。解压压缩文件得到3个文件夹。

## 安装cp2102驱动
cp2102是usb转串口芯片的名字。cp2102连接主控MCU STM32芯片和我们的电脑PC，这样就可以通过USB接口对STM32芯片进行烧写编程。所以首先要把cp2102的驱动装上。这个驱动在32位windows xp系统/64位 windows 7系统下都测试通过。

![](/assets/img/cp2102.jpg)

## 烧入hex文件
打开下载器，然后用这个下载器下载hex文件。如果无法烧入成功，可以重新插拔一下。

![](/assets/img/download.jpg)

下载成功的标注。

![](/assets/img/download-done.jpg)

## 查看打印信息

连上usb线，打开压缩包的里的串口助手，波特率115200，查看调试参数，确认hex烧入成功，并且正常运行。注意选择正确的串口。如果没有信息，可以按下复位键复位飞行器主控。

![](/assets/img/uart-info.jpg)
