
## 2.4G遥控器NRF24L01
Crazepony机身上2.4G射频芯片NRF24L01和主控STM32使用SPI总线连接在一起。

Crazepony遥控器上，我们使用了市面上标准排插接口的NRF24L01模块。


## 手机APP通信协议
Crazepony APP和飞控之间通信协议使用了MWC飞控协议（MSP，Multiwii Serial Protocol），详见[MSP协议格式](http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol)。

MWC协议规定了飞控和上位机（或者手机APP）信息交流的基本格式。

MWC具体实现，可以查看Crazepony的Android APP[源代码](https://github.com/Crazepony/crazepony-android-client-none)中的`Protocol.java`文件。
