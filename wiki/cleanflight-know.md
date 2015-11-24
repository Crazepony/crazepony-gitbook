
## Cleanflight介绍

Cleanflight可以在多转子的飞机被用来和固定翼飞机，它支持多种的形状和电机数量，不限quadcopters，hexacopters，octocopters，tricopters和飞机。 Cleanflight是开源的飞控软件,源代码在GitHub上，你可以自由修改，并提交改进。

## Baseflight介绍

Baseflight有自己的跨平台的Chrome应用配置设置和刷新新固件。它可以Chrome Web Store中[下载]( https://chrome.google.com/webstore/detail/baseflight-configurator/mppkgnedeapfejgfimkdoninnofofigk?hl=en)。


## cleanflight GUI安装

需要Chrome浏览器（或者chromium）的版本大于38，我们首先需要翻墙在Chrome浏览器应用商店中搜索关键字cleanflight，搜索结果会出现cleanflight configurator（Baseflight configurator也在搜索结果中出现），将其添加到应用中会自动下载安装Cleanflight上位机。经常使用谷歌浏览器的模友基本都购买了谷歌年费，没有购买年费的我为大家推荐自由门翻墙软件，当然也可以下载最新的host文件，我们只有翻墙后进入谷歌应用中搜索cleanflight，否则Chrome浏览器应用商店你将无法使用。

![](../assets/img/cleanflight_003.jpg)

在ubuntu环境下，除了按照以上方法安装Cleanflight上位机，需要开启chrome应用访问串口的权限。

<a href="http://pan.baidu.com/s/1kTGLXrx" class="btn btn-lg btn-outline" role="button" target="_blank" >自由门翻墙软件</a>

## naze32介绍
naze32兼容mwc所有的软件，同时兼容Cleanflight，性能稳定，是模友玩转穿越机的不错选择。

naze32配置

* 32位处理器3.3v/72mhz（STM32F103CB）
* 陀螺仪+加速度计（MPU6050）
* 三轴磁强计（HMC5883L）
* 压力传感器（ms5611）
* 灵活的输出，支持各种类型的飞机有四、六、三、双、 Y4、Y6 、八轴（默认是quad-x）
* 支持8通道输入，RC输入支持标准的接收机PWM、PPM接收机
* 支持电池电压监测功能
* 16兆自带的SPI Flash
* 安装和配置车载MicroUSB
* 支持LED灯带，支持超声波、GPS
* 支持命令输入

## CC3D介绍

OpenPilot是一个开源的自动驾驶平台，为小型无人机，它能够飞multirotors，直升机和固定翼飞机，是模友玩穿越机最青睐的飞控。

cc3d配置

* 32位处理器3.3v/72mhz（STM32F103CB）
* 陀螺仪+加速度计（MPU6000）
* 灵活的输出，支持各种类型的飞机有固定翼、四轴六轴及车类（默认是quad-x）
* 支持6通道输入，RC输入支持标准的接收机PWM
* 支持外部拓展接口
* 支持cleanflight固件
