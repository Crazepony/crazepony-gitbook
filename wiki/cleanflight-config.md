
#  Cleanflight的配置



## 开发环境搭建

下面介绍在Linux下（以Ubuntu为例），cleanflight交叉编译链的安装。

~~~
$ git clone git@github.com:cleanflight/cleanflight.git
~~~


交叉编译链的安装

~~~
$ sudo apt-get remove binutils-arm-none-eabi gcc-arm-none-eabi
$ sudo add-apt-repository ppa:terry.guo/gcc-arm-embedded
$ sudo apt-get update
~~~

Ubuntu 14.10:

~~~
$ sudo apt-get install gcc-arm-none-eabi=4.9.3.2014q4-0utopic12
~~~

Ubuntu 14.04:

~~~
$ sudo apt-get install gcc-arm-none-eabi=4.9.3.2014q4-0trusty12
~~~

Ubuntu 12.04:

~~~
$ sudo apt-get install gcc-arm-none-eabi=4.9.3.2014q4-0precise12
~~~

如果安装失败，请使用第二种方法，直接下载对应版本gcc-arm-none-eabi在ubuntu下的[安装包](http://ppa.launchpad.net/terry.guo/gcc-arm-embedded/ubuntu/pool/main/g/gcc-arm-none-eabi)。

安装下载的4-8-2014q2版的编译链：

~~~
$ sudo dpkg -i gcc-arm-none-eabi_4-8-2014q2-0saucy9_amd64.deb
~~~

##编译cleanflight固件

~~~
$ make TARGET='Flight Control Type Name'
例如：$ make TARGET=NAZE
~~~

cleanflight支持的飞控类型可以[点击查找](https://github.com/cleanflight/cleanflight/tree/master/docs)。

编译成功会生成相应的hex文件

~~~
arm-none-eabi-size ./obj/main/cleanflight_NAZE.elf 
   text    data     bss     dec     hex filename
    115396      264   12940  128600   1f658 ./obj/main/cleanflight_NAZE.elf
arm-none-eabi-objcopy -O ihex --set-start 0x8000000 obj/main/cleanflight_NAZE.elf obj/cleanflight_NAZE.hex
~~~

在obj文件夹下，就可以看到hex可烧写固件。


