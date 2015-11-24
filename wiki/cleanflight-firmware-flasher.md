
## naze32 Cleanflight固件两种烧写方法

naze32刷Cleanflight固件我们需要做一些前期工作，安装串口驱动工具及官网更新的最新版本固件。下载链接如下：

<a href="http://pan.baidu.com/s/1eQ1kfPw" class="btn btn-lg btn-outline" role="button" target="_blank" >串口工具（cpl2102）</a>

<a href="github.com/cleanflight/cleanflight/releases" class="btn btn-lg btn-outline" role="button" target="_blank" >cleanflight固件</a>


###固件烧写
* 本地固件烧写比较简单，但需要模友提前在以上提供固件下载链接下载固件。打开cleanflight，不要建立naze32与PC之间的通信，进入Firmware flasher点击Load Firmware[Local]进入本地固件烧写，点击后会打开一个文件夹，选中通过固件下载链接下载所需固件，点击Flash Firmware即可完成本地烧写。烧写过程可以不使用翻墙软件。如下图所示：

![](/assets/img/naze32firmware.png) 


###在线烧写

* 在线烧写。模友可以获悉更新的最新固件，亦不用下载最新版本。烧写步骤按下图标号所示一步一步进行进行，标号2选择固件选择NAZE固件，点击在线获取可以看到关于此版本的说明性信息。在点击Load Firmware[Online]时因网速或其他问题可能窗口弹出固件信息需要一段时间，请大家耐心等待。点击Flash Firmware进度条变色会走动，完成更新固件后会提示Programming：SUCCESSFUL。这里提醒大家，无论是固件烧写还是在线烧写，请不要建立naze32与PC之间的通信。

![](/assets/img/naze-firmware0.png)  

![](/assets/img/naze-firmware2.png)  

## naze32重写Bootloader方法

若naze32本地固件烧写或者是在线烧写提示Bootloader错误，无法写入固件时我们应该怎么办？若自己在配置或者因接线导致naze32 FMU引脚烧掉，重新更换stm32因没有Bootloader无法完成第一次固件烧写，我们应该怎么解决？下面笔者为大家介绍怎样去解决怎样写入Bootloader的方法。

* 一、下载烧写工具。已通过百度网盘为大家提供烧写工具链接，工具中我附带了一个1.9.0版本的cleanfligh-naze32固件。

* 二、烧写前准备。烧写步骤。USB上电前，用镊子短接naze32飞控板的Boot引脚；USB上电后，点击所下载文件中STMicroelectronics flash loader应用进入烧写界面，查看设备管理器COM是否与烧写界面COM口一致，波特率设置为115200，其他默认即可。

* 三、按照默认选项一直next，直到出现如下界面。首先要选择我们要写入的文件，也就是在工具中附带的1.9.0版本cleanfligh-naze32固件，根据自己的情况选择是否要擦除资料。若更换新的STM32请选择no erase，next即开始写入。

![](/assets/img/firmware-flash-loader.png)  

## CC3D cleanflight固件烧写

## CC3D重写Bootloader方法
