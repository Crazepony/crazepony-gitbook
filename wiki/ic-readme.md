
#  Crazepony器件总览及选型说明


## 主控MCU（单片机）
STM32f103T8U6，内核为ARM Cotex-M3，72MHz主频，AD/硬件I2C/硬件PWM。

![](/assets/img/stm32-ic.jpg)

## 电机驱动
SI2302，N沟道增强型MOS，导通电阻只有82mΩ，2.2v低GS电压。

## 陀螺仪加速度计
MPU6206，三轴陀螺仪+三轴加速度计，自带DMP四元数输出，内部温度补偿。

![](/assets/img/mpu-6050-ic.jpg)

## 电子罗盘（磁力计）
HMC5883L，电子罗盘。

![](/assets/img/HMC5883L-ic.jpg)

## 2.4G无线射频芯片
nRF24L01，2.4G无线射频收发芯片。

![](/assets/img/nRF24L01-ic.jpg)

## 蓝牙透传模块
HM-06

## USB转串口芯片
cp2102，USB转串口芯片，用于固件下载，参数调试。

## 锂电池充电管理
LT4054，锂电充电管理。

## 电机
716有刷空心杯电机。

## 桨叶
直径为45mm小桨，正反桨各一对。
