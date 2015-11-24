
#  Windows下开发环境搭建-裸机版本


> 作者：nieyong

IDE开发工具Keil v5.10下载地址：Crazepony百度云网盘[Keil-uVision5-MDK5-12.zip](http://pan.baidu.com/s/1sjr24qD)（5.2及以后版本）。

IDE开发工具Keil v4.10下载地址：Crazepony百度云网盘[Keil-uVision4-MDK4-12.zip](http://pan.baidu.com/s/1ntNqLdv)。

飞控源代码下载地址：Github项目[crazepony-firmware-none](https://github.com/Crazepony/crazepony-firmware-none/releases)。

CP2102驱动及ISP烧录工具下载地址：Crazepony百度云网盘[开发工具](http://pan.baidu.com/s/1eQ1kfPw#path=%252F)

## 环境配置说明
裸机版本是指没有使用RTOS的主控固件版本，由于没有使用RTOS，程序代码显得更加简单明了，开发环境配置简单，非常适合初学者使用。

裸机版本的代码使用Keil进行开发编译，下面介绍编译环境的搭建和编译过程。在crazepony 5.1版本及以前，使用keil 4.10进行开发。但是由于其不支持utf-8编码，所以从5.1版本之后都会使用keil 5.10版本进行开发。

## Keil 4的安装和破解
由于主控使用的是ARM Cortex-M3内核的STM32，所以必须使用带有ARM编译工具链的Keil 4。网络上很多只有几十兆大小的的Keil 4可能只支持C51开发。Crazepony百度云网盘提供带有ARM编译工具链的Keil 4安装文件下载，带有破解注册机和破解说明文档。用户自行下载安装，可以看到该Keil版本为v4.10。

![](/assets/img/keil-version.jpg)

该安装文件在Windows XP，32位系统上测试通过。已知存在的问题： 

* 不支持utf-8编码。utf-8编码的中文在Keil 4下面会显示为乱码，所以这部分固件代码没有使用utf-8编码。没有找到能够配置支持utf-8的地方，很可能是Keil版本比较老，或者破解导致无法支持utf-8编码。

## Keil 5的安装和破解（推荐）
最新crazepony版本都使用keil 5.10进行开发调试，并且文件使用utf-8编码。crazepony百度云盘提供keil 5.10安装文件下载。并且可以注册破解。

Keil 5的安装文件是Keil 4的几倍，很多组件与模板都需要分开来安装，安装稍微比较麻烦。在安装完主程序之后，会弹出Pack Installer的对话框，用于被开发芯片对应模板的安装。crazepony使用的STM32F103T8主控芯片，所以从右边选择STM32F1 Series，在左侧点击安装。

![](/assets/img/keil-5-installer.png)

## 源代码下载
主控固件裸机版本，裸机指没有使用实时操作系统RTOS。由于没有使用RTOS，所以代码更加简单明了，适合初学者使用。

Crazepony项目是开源的，所有代码都托管在Github的[Crazepony项目](https://github.com/Crazepony)下。裸机源代码放置在[crazepony-firmware-none](https://github.com/Crazepony/crazepony-firmware-none)下，命名中的none表示不使用RTOS。

可以直接使用git获得源代码，也可以从[crazepony-firmware-none release](https://github.com/Crazepony/crazepony-firmware-none/releases)下载各个版本的裸机源代码。

![](/assets/img/git-download.png)

## 源代码导入和编译
在源代码中，有三个文件为Keil工程文件。

~~~
Crazepony.uvopt
Crazepony.uvproj
Crazepony.dep
~~~

以Keil 5为例，点击Project栏目下Open project，打开代码解压所在文件夹选中Crazepony.uvproj，此时已将代码项目工程所有文件导入Keil 5，如图所示：

![](/assets/img/keil-build.jpg)

点击左上角的编译按钮，编译整个项目，在工程下生成Output目录，目录中Crazepony.hex就是可以烧写到STM32的固件。

STM32固件的调试和烧入可以使用J-Link或者ST-Link等调试器进行开发，详见[J-Link的使用及常见问题](./jlink-debug.html)。Crazepony也支持USB口烧入，即采用ISP下载，操作简单。只需要安装cp2102驱动程序，使用一根Mini USB数据线连接电脑。详见[固件烧写](./flash-firmware.html)，烧录界面如图所示:

![](/assets/img/shaolu.png)

