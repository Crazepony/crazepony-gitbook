
#  开源四轴飞行器


> 作者：nieyong

## APM & 3D Robotics
3D Robotics公司旗下的飞控有3款，分别是ArduPilot（简称APM），PX4和Pihawk。

APM是比较古老的版本，处理核心使用的是Arduino，16位mega系列单片机，开发环境为arduino-IDE，基于Arduino这点和MWC飞控是一样的。功能上依然很强大，地面站使用apm-planner和mission-planner。最新版本为APM 2.6，开源。

PX4是apm的升级版，使用了很流行的stm32f407单片机，处理速度上了一个大台阶，摆脱了arduino的瓶颈，走向了发烧级的道路。不过PX4实际上是由两部分组成的，PX4FMU和PX4IO板。

![](/assets/img/px4.png)

后来又推出了Pixhawk飞控，其实就是把PX4FMU和PX4IO板结合在了一起，更高的集成度。

![](/assets/img/pixhawk.jpg)

其背后的商业公司是3D Robotics。3D Robotics创始人是克里斯·安德森（Chris Anderson），前《连线》主编，著有《长尾理论》，《创客：新工业革命》等畅销书。创客运动的积极倡导者和领袖级人物。有关克里斯·安德森和他的无人机，可以参看《开源杂志》上的报道[《变革推动者.克里斯安德森的无人机梦想腾飞》](http://obook.cc/openbook8/maker/changers.html).

围绕着3DR公司的产品，形成了一个活跃的无人机爱好者社区，无人机飞控功能很强大，能飞固定翼、旋翼、直升机等。旗下网站也有好几个ardupilot.com、diydrones.com、3drobotics.com，很是混杂，很多资料和文档看的眼花缭乱。

据业内人士透露，diydrones是现在最活跃的四轴飞行器，无人机论坛，日活跃用户有2万多（2014-6，这个数据是否真实没有验证过）。所以把这个放在第一位介绍给大家。

* 3DR官网： [http://3drobotics.com/](http://3drobotics.com/)。这个网站简单来说就是3dr卖飞控的官方旗舰店，我还以为开发者的一些东西也在上面，，好浪费感情。
* apm飞控的官网：[http://copter.ardupilot.com](http://copter.ardupilot.com) 。见名知意，基于arduino的飞控，肯定是apm的官网了，一些开发者资料在[http://dev.ardupilot.com](http://dev.ardupilot.com)。 
* pixhawk飞控的官网：[https://pixhawk.org](https://pixhawk.org/) 。 PIX4和Pixhawk的资料都在上面，此外上述代码都托管在GitHub上。
* diydones论坛：[http://diydrones.com](http://diydrones.com) 。这个是3dr旗下的交流论坛，你可以在这里找到很多国外的飞控爱好者。

![](/assets/img/3d-robotics.png)

本节内容部分来自Wellmakers博客[3D Robotics相关介绍](http://wellmakers.com/?p=221)。

## MWC & MultiWii
MWC是MultiWii Copter的缩写，是最为经典的开源的多轴飞行器固件。此固件的原创作者是法国的Alex，他为了打造自己的Y3飞行器（一个三轴飞行器），在开源硬件平台Arduino的基础上开发了最初的MWC固件。几年来经过许多高手的参与及共同努力，开发进度越来越快，已经基本成熟，支持三轴，四轴，六轴等多种飞行器。其最大的特点是，**其硬件是基于Arduino平台。**这为很多熟悉开源硬件平台Arduino的玩家入门提供方便。

下图为Alex最早使用MWC的Y3飞行器。

![](/assets/img/mwc.jpg)

根据使用Arduino开发板的不同，MWC飞控有两种版本。

* Atmega328P 版本，32K的Flash，Atmel公司8位AVR单片机内核
* Atmega2560 版本，256K的Flash，Atmel公司8位AVR单片机内核

> AVR单片机内核就是AVR内核，和51内核是不一样的，它的汇编指令与51单片机汇编指令是完全不一样的。AVR内核是美国ATMEL公司研发的。ATMEL公司有三大系列MCU，一种是老式的以8051内核的单片机，第二种是目前大量使用的以AVR内核的AVR单片机。第三种是目前高端的以ARM内核的微处理器。

所以我们可以使用Arduino Pro Mini/Arduino Mega等开发板配合传感器开发板来搭建自己的四轴飞行器。当然，需要有数字电路和编程的底子，不过如果悟性好，看看文档也能搞起来。主要难点在于调试，很难把它调得很稳，需要很大的耐心。

* MultiWii官网：[http://www.multiwii.com/](http://www.multiwii.com/)
* MultiWii官方在Google Code上的代码库：[http://code.google.com/p/multiwii/](http://code.google.com/p/multiwii/)
* MultiWii官方在Github上的代码库：[https://github.com/multiwii](https://github.com/multiwii)

> 正是由于MWC使用的是8位单片机做的主控芯片，在后来的发展中受到了性能的限制。很多玩家就把MWC飞控代码移植到32位处理器上（例如STM32），形成了[BaseFlight](https://github.com/multiwii/baseflight)飞控代码，后来从BaseFlight项目又分出来（fork）了CleanFlight飞控项目。

## CC3D & OpenPilot
![](/assets/img/openpilot-logo.png)

OpenPilot社区主要提供下面两个版本的飞控硬件平台：

* OpenPilot CopterControl Platform（又叫CC3D平台）。使用STM32F1作为主控，没有气压计，价格便宜，功能稳定，已经被大量使用和接受。
* OpenPilot Revolution Platform（还在开发中，未发布，2015-5-2）。使用STM32F4作为主控。

![](/assets/img/cc3d.png)

配合上面两个飞控硬件平台，OpenPilot还提供一个功能强大，支持跨平台（Windows，Mac OS，Linux）的[地面站](https://www.openpilot.org/product/openpilot-gcs/)（包含上位机功能）。

![](/assets/img/openpilot-gcs.png)

CC3D是现在OpenPilot现在提供的唯一大量使用的飞控。由于其飞控固件稳定，配置简单，价格便宜，而且有强大的地面站上位机支持，所以非常受欢迎。**穿越机QAV250就是使用的CC3D作为默认飞控**，crazepony团队会花很多精力来研究这个飞控，以便给大家提供更好的技术支持。

> OpenPilot本身提供的飞控固件已经非常稳定。但是很多穿越机的玩家会把CleanFlight飞控固件烧入到CC3D飞控平台上，以获得更好的飞行体验。更多内容，请看CleanFlight飞控固件部分。

* OpenPilot官网：[www.openpilot.org](http://www.openpilot.org)
* OpenPilot Wiki：[https://wiki.openpilot.org](https://wiki.openpilot.org)

## Cleanflight
在前面谈到MWC和CC3D飞控的时候，都有谈到Cleanflight，那么到底什么是Cleanflight呢？在crazepony的wiki中为什么要详细单独介绍它呢？

正如在MWC介绍中提到的，由于MWC使用的是8位单片机做的主控芯片，在后来的发展中受到了性能的限制。很多玩家就把MWC飞控代码移植到32位处理器上（例如STM32），形成了[BaseFlight](https://github.com/multiwii/baseflight)飞控代码，后来从BaseFlight项目又分出来（fork）了CleanFlight飞控项目。Cleanflight其实只是一个基于MWC的飞控代码，它现在已经支持了下面这些飞控硬件平台：

* AlienWii32
* Naze32
* CC3D
* CJMCU
* CheBuzzF3
* Olimexino
* Sparky

上面的硬件飞控平台，除了CC3D比较有名之外，Naze32算是一个后起之秀。但是他们都有一个特点，基本上都是基于STM32主控MCU，内核为32位ARM Contex-M。那么crazepony的wiki中为什么要详细介绍这个飞控呢，有下面几点：

* crazepony也是使用的STM32作为主控MCU，而且硬件选型和Naze32完全一样，很有借鉴意义
* CC3D和Naze32飞控都可以刷Cleanflight的飞控，用于研究CrazeFPV H250穿越机
* Naze32作为后起之秀，有超越CC3D的趋势，在国外穿越机玩家中非常流行

Naze32的正面图，和CC3D最大的区别是它有加入气压计MS5611：

![](/assets/img/naze32.jpg)

下面是Cleanflight的官网和代码库。

* Cleanflight官网：[http://cleanflight.com/](http://cleanflight.com/)
* Cleanflight官方在Github上的代码库：[https://github.com/cleanflight](https://github.com/cleanflight)

cleanflight飞控几个大的特点：
* 飞控代码基于MWC，稳定简洁；
* 为现在的32位处理器而开发，删除了原来为了支持8位处理器而存在的冗余代码。
* 加入了很多好玩的功能。例如支持LED灯带，支持OLED，支持超声波传感器
* 使用了先进的代码开发管理，代码结构清晰，冗余性强，测试充分
* 支持多个硬件平台，例如CC3D，Naze32等


## MikroKopter
在2006年10月24号，Holger Buss和Ingo Busker创造了MK，一个伟大的Mikrokopter四轴社区。 在2007年中，Mikrokopter便像一个“ 空中的钉子”，像一只鸟一样，稳步的停留在空中。这对于开源四轴飞行器是一个很大的里程碑。

MikroKopter来自德国。毫无疑问，MikroKopter这个名字来源于德语，对应的英文应该是MicroCopter。其英文官网地址是[http://www.mikrokopter.de/en/home](http://www.mikrokopter.de/en/home)。

作者在SVN上共享了代码。

![](/assets/img/mikrokopter.png)

## KK飞控
最经典的多轴飞控，价格十分便宜，很多人就是用它学会飞四轴的。主要问题是没有自稳，更不用说什么定高、GPS之类的高级功能了。因为没有自稳，新手练习起来就比较困难，不过对于从直升机转过来的玩家来说就是小case了。支持3轴、四轴、6轴、V22的飞行模式；

[http://www.kkmulticopter.com/](http://www.kkmulticopter.com/)

## Paparazzi

![](/assets/img/penguin.gif)

这是国外一个开源的固定翼，多轴飞行器项目。一个做固定翼的朋友购买了它的组件。github上的资料，wiki等都挺全面的。项目不仅仅只包括飞控板的软硬件，包括从稳压电源和GPS到卡尔曼滤波代码, 而是一个强大和不断扩大的地面空中软硬件群，包括数传电台，天线和一个高度进化的用户友好的地面控制软件界面。

[http://wiki.paparazziuav.org/wiki/Main_Page](http://wiki.paparazziuav.org/wiki/Main_Page)

[https://github.com/paparazzi/](https://github.com/paparazzi/)


## open drone（国内）
![](/assets/img/open-drone.png)

[http://www.open-drone.org/](http://www.open-drone.org/)

[https://github.com/opendrone](https://github.com/opendrone)

open drone是由北京的LUG和创客组建的一个项目。但是没有看到其产品。很可能还是一个比较松散的组织，没有以公司盈利的团队形式存在。

## erlerobot

这是一个使用Linux系统的开源四轴飞行器项目。他们的口号是：Building the next generation of educational drones。

[http://erlerobot.com/](http://erlerobot.com/)

[https://github.com/erlerobot](https://github.com/erlerobot)

有比较齐全的wiki，并且使用gitbook形式提供四轴飞行器开发的电子书。

[https://github.com/erlerobot/wiki/wiki](https://github.com/erlerobot/wiki/wiki)

[http://erlerobot.github.io/erle_gitbook/en/](http://erlerobot.github.io/erle_gitbook/en/)

