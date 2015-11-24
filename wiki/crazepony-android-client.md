
#  Crazepony Android APP开发和配置


> 作者：nieyong

Crazepony的Android客户端源代码也是托管在github的crazepony项目下，点击[这里](https://github.com/Crazepony/crazepony-android-client-none)查看。可以直接下载zip压缩包，也可以通过git clone到本地。

~~~
git clone git@github.com:Crazepony/crazepony-android-client-none.git
~~~

> Crazepony Android APP在5.0版本使用ADT Bundle进行开发。5.1版本以及以后版本使用Android Studio进行开发。

## ADT Bundle开发环境搭建
Crazepony 5.0版本的Android APPP开发环境使用Google Android提供的一站式开发包[ADT Bundle](http://developer.android.com/sdk/index.html)。ADT Bundle提供了Android APP开发所需的所有工具，包括Eclipse IDE，ADT (Android Developer Tools) 插件，java库等等。

> 下载地址：[http://developer.android.com/sdk/index.html](http://developer.android.com/sdk/index.html)。该下载地址现在已经不再提供ADT Bundle下载。

下载解压缩到任意目录，就可以使用，无需安装。

## Android Studio开发环境搭建

Google已经提供Android集成开发环境Android Studio，不再推荐使用原来集成Eclipse IDE，ADT，Java库等ADT Bundle。所以Crazepony 5.1版本以及以后版本使用Android Studio进行开发。

> Android Studio官网下载地址：[http://developer.android.com/sdk/index.html](http://developer.android.com/sdk/index.html)。

在中国国内提供百度云盘下载。

>百度云盘下载地址：[点击下载](http://pan.baidu.com/s/1nttCBB7)， 提供了Android Studio及对应的JDK下载。

首先安装下载的jdk-7u67-windows-i586.exe，然后再安装Android Studio开发环境。

## 配置说明

Crazepony的Android客户端默认编译的Android SDK API版本为15（对应Android 4.0.3），支持的Android版本为4.0.0或以上。

![](/assets/img/Android-SDK-Manager.png)

![](/assets/img/Properties-for-CrazyflieControll.png)

