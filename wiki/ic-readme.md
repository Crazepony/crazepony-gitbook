
#  Crazepony器件总览及选型说明


> 作者：nieyong

我们暂时不提供桨叶/空心杯电机/电池等易损耗配件的购买。Craze团队整理了部分淘宝上的购买地址及注意事项，大家可以自行购买。

## 电机 & 桨叶

720有刷空心杯电机，中心轴直径1mm。淘宝购买地址：[地址1](http://item.taobao.com/item.htm?ut_sk=1.U5nfk/5pPyADAHT9gIoKBhWX_21380790_1416310719.Copy.ShareSceneItemDetail&id=41176268103)。

![](/assets/img/motor-720.jpg)

直径为75mm桨叶，桨叶中心孔直径为1mm，正好配中心轴直径为1mm的720电机。淘宝购买地址：[地址1](http://item.taobao.com/item.htm?spm=a230r.1.0.0.ZZNieR&id=35723782642&ns=1&abbucket=7#detail)。

![](/assets/img/prop-75.png)

## 电池
Crazepony飞机电池为650mAh，3.7V，25C航模电池。大家也可以选择350mAh电池，购买[地址](http://detail.1688.com/offer/1234287135.html)（建议自己上淘宝上寻找，这个链接是阿里巴巴链接，需要批量拿货）。

购买时需要注意电池接口。

## 2.4G无线射频
Crazepony机身上使用2.4G无线射频收发芯片nRF24L01。

![](/assets/img/nRF24L01-ic.jpg)

遥控器上使用2.4G无线射频模块，根据遥控距离的不同，有下面两种可以选择。

加功率放大（PA）的鞭状天线，最大发送功率20dBm，可以遥控距离100米。购买[地址](http://detail.tmall.com/item.htm?spm=a230r.1.14.1.6SuQ2w&id=40504364189&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=13)。

![](/assets/img/rm-ctrl-8.jpg)

不加PA的发射模块，最大发射功率0dBm，可以遥控距离20米。购买[地址](http://detail.tmall.com/item.htm?spm=a230r.1.14.1.qbCmu0&id=41587731684&ad_id=&am_id=&cm_id=140105335569ed55e27b&pm_id=&abbucket=13)。

![](/assets/img/rm-ctrl-7.jpg)

## 主控MCU（单片机）
主控为STM32的F10系列，STM32F103T8U6，ARM Cotex-M3内核，72MHz主频，128KB存储空间，BGA封装。

![](/assets/img/stm32-ic.jpg)
![](/assets/img/stm32-ic-back.jpg)

## 电机驱动
SI2302，N沟道增强型MOS，导通电阻82mΩ，2.2v低GS电压。

## 陀螺仪加速度计
MPU6050，三轴陀螺仪+三轴加速度计，自带DMP四元数输出，内部温度补偿。

![](/assets/img/mpu-6050-ic.jpg)

## 气压计
MS5611，10cm精度气压计。

![](/assets/img/ms5611.jpg)

## 电子罗盘（磁力计）
HMC5883L，电子罗盘。

![](/assets/img/HMC5883L-ic.jpg)

## 蓝牙透传模块
HM-06

淘宝购买[地址](http://item.taobao.com/item.htm?spm=a230r.1.14.1.xYrzTD&id=17278839073&ns=1&_u=j1omdar17efa#detail)，仅此一家。

## USB转串口芯片
cp2102，USB转串口芯片，用于固件下载，参数调试。

## 锂电池充电管理
LT4054，锂电充电管理芯片。


## 摇杆电位器
淘宝购买[地址](http://item.taobao.com/item.htm?spm=a1z09.2.9.163.18Dk2I&id=38490983640&_u=m205fe4p579e)。

我们对油门摇杆的要求是推左右自动回中，推上下不回，可停留在另意位置。根据这个要求，我们只找到了这种**拆机**的摇杆物料。

5.1版本即以后，油门摇杆使用自动回中的电位器，不再使用上面的拆机摇杆，所有摇杆都是新物料。

## 陶瓷天线
飞机上2.4G使用了陶瓷天线，型号为：rainsun An9520-245。
