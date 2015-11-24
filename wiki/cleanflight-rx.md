
#  接收机


> 作者：nieyong

文档地址[Rx.md](https://github.com/Crazepony/cleanflight/blob/master/docs/Rx.md)，下面是翻译文章。

A receiver is used to receive radio control signals from your transmitter and convert them into signals that the flight controller can understand.

接收机是用来接收遥控发射机的无线控制信号，并且把他们转化为飞控能够理解的信号格式。

There are 3 basic types of receivers:

现在常用有3种类型的接收机：

1. Parallel PWM Receivers
2. PPM Receivers
3. Serial Receivers

1. 并行PWM接收机
2. PPM接收机
3. 串行接收机

> 注：类型是由接收机输出给飞控的信号格式来划分的。

## Parallel PWM Receivers

## 并行PWM接收机

8 channel support, 1 channel per input pin.  On some platforms using parallel input will disable the use of serial ports
and SoftSerial making it hard to use telemetry or GPS features.

cleanflight飞控支持最多8个通道的并行PWM接收机，每个通道有一根输入信号线。在有些硬件平台上，使用并行接收机会使得串行端口和软串行无法使用，无法使用GPS功能。

## PPM Receivers

## PPM接收机

PPM is sometimes known as PPM SUM or CPPM.

PPM有时候也叫做PPM SUM或者CPPM。

12 channels via a single input pin, not as accurate or jitter free as methods that use serial communications, but readily available.

12个通道数据由一根信号线输入，虽然在精确度，防抖性方面没有串行输入那么优异，但是仍然不失为非常可行的接收机模式。

These receivers are reported working:

下面这些PPM接收在cleanflight飞控下测试是可行的：

FrSky D4R-II
http://www.frsky-rc.com/product/pro.php?pro_id=24

[FrSky D4R-II](http://www.frsky-rc.com/product/pro.php?pro_id=24)

Graupner GR24
http://www.graupner.de/en/products/33512/product.aspx

[Graupner GR24](http://www.graupner.de/en/products/33512/product.aspx)

R615X Spektrum/JR DSM2/DSMX Compatible 6Ch 2.4GHz Receiver w/CPPM
http://orangerx.com/2014/05/20/r615x-spektrumjr-dsm2dsmx-compatible-6ch-2-4ghz-receiver-wcppm-2/

R615X Spektrum/JR DSM2/DSMX兼容6通道接收机。[例如](http://orangerx.com/2014/05/20/r615x-spektrumjr-dsm2dsmx-compatible-6ch-2-4ghz-receiver-wcppm-2/)

FrSky D8R-XP 8ch telemetry receiver, or CPPM and RSSI enabled receiver
http://www.frsky-rc.com/product/pro.php?pro_id=21

FrSky D8R-XP 8通道接收机，或者CPPM和RSSI功能开启的接收机，[例如]( http://www.frsky-rc.com/product/pro.php?pro_id=21)

## Serial Receivers

## 串行接收机

### Spektrum

### Spektrum

8 channels via serial currently supported.

现在支持8通道串行Spektrum接收机。

These receivers are reported working:

下面这些接收机在cleanflight下测试可用：

Lemon Rx DSMX Compatible PPM 8-Channel Receiver + Lemon DSMX Compatible Satellite with Failsafe
http://www.lemon-rx.com/shop/index.php?route=product/product&product_id=118


### S.BUS

16 channels via serial currently supported.  See the Serial chapter in the documentation for a configuration example.

现在支持16通道的串行S.BUS接收机。配置案例查看《串行数据》章节。

* In most cases you will need an inverter between the receiver output and the flight controller hardware.  
* Softserial ports cannot be used with SBUS because it runs at too high of a bitrate (1Mbps).  Refer to the chapter specific to your board to determine which port(s) may be used.
* You will need to configure the channel mapping in the GUI (Receiver tab) or CLI (`map` command).

* 在大部分情况下在接收机和飞控直接需要一个信号转换器。
* 软件串行端口不能够和SBUS接收器连接，因为该端口速率太高（1Mbps）。请查看硬件平台决定使用哪个端口。
* 需要在cleanflight GUI中（Receiver栏）或者命令行下（`map`命令）配置通道映射。

These receivers are reported working:

下面这些接收机在cleanflight下测试可以使用：

FrSky X4RSB 3/16ch Telemetry Receiver
http://www.frsky-rc.com/product/pro.php?pro_id=135

FrSky X4RSB 3/16ch 接收机。[详见](http://www.frsky-rc.com/product/pro.php?pro_id=135)

FrSky X8R 8/16ch Telemetry Receiver
http://www.frsky-rc.com/product/pro.php?pro_id=105

FrSky X8R 8/16ch 接收机。[详见](http://www.frsky-rc.com/product/pro.php?pro_id=105)

Futaba R2008SB 2.4GHz S-FHSS
http://www.futaba-rc.com/systems/futk8100-8j/

Futaba R2008SB 2.4GHz S-FHSS接收机。[详见](http://www.futaba-rc.com/systems/futk8100-8j/)

#### OpenTX S.BUS configuration

#### OpenTX S.BUS配置

If using OpenTX set the transmitter module to D16 mode and select CH1-16 on the transmitter before binding to allow reception
of 16 channels. 

OpenTX 2.09, which is shipped on some Taranis X9D Plus transmitters, has a bug - [issue:1701](https://github.com/opentx/opentx/issues/1701).
The bug prevents use of all 16 channels.  Upgrade to the latest OpenTX version to allow correct reception of all 16 channels,
without the fix you are limited to 8 channels regardless of the CH1-16/D16 settings.


### XBUS

The firmware currently supports the MODE B version of the XBus protocol.
Make sure to set your TX to use "MODE B" for XBUS in the TX menus!
See here for info on JR's XBUS protocol: http://www.jrpropo.com/english/propo/XBus/

These receivers are reported working:

XG14 14ch DMSS System w/RG731BX XBus Receiver
http://www.jramericas.com/233794/JRP00631/

There exist a remote receiver made for small BNF-models like the Align T-Rex 150 helicopter. The code also supports using the Align DMSS RJ01 receiver directly with the cleanflight software.
To use this receiver you must power it with 3V from the hardware, and then connect the serial line as other serial RX receivers.
In order for this receiver to work, you need to specify the XBUS_MODE_B_RJ01 for serialrx_provider. Note that you need to set your radio mode for XBUS "MODE B" also for this receiver to work.
Receiver name: Align DMSS RJ01 (HER15001)

### SUMD

16 channels via serial currently supported.

These receivers are reported working:

GR-24 receiver HoTT
http://www.graupner.de/en/products/33512/product.aspx

Graupner receiver GR-12SH+ HoTT
http://www.graupner.de/en/products/870ade17-ace8-427f-943b-657040579906/33565/product.aspx

### SUMH

8 channels via serial currently supported.

SUMH is a legacy Graupner protocol.  Graupner have issued a firmware updates for many recivers that lets them use SUMD instead.

## MultiWii serial protocol (MSP)

Allows you to use MSP commands as the RC input.  Only 8 channel support to maintain compatibility with MSP.
 
## Configuration

There are 3 features that control receiver mode:

```
RX_PPM
RX_SERIAL
RX_PARALLEL_PWM
RX_MSP
```

Only one receiver feature can be enabled at a time.

### Serial RX

See the Serial chapter for some some RX configuration examples.

To setup spectrum on the Naze32 or clones in the GUI:
1. Start on the "Ports" tab make sure that UART2 has serial RX.  If not set the checkbox, save and reboot.
2. Move to the "Configuration" page and in the upper lefthand corner choose Serial RX as the receiver type.
3. Below that choose the type of serial receiver that you are using.  Save and reboot.

Using CLI:
For Serial RX enable `RX_SERIAL` and set the `serialrx_provider` CLI setting as follows.

| Serial RX Provider | Value |
| SPEKTRUM1024       | 0     |
| SPEKTRUM2048       | 1     |
| SBUS               | 2     |
| SUMD               | 3     |
| SUMH               | 4     |
| XBUS_MODE_B        | 5     |
| XBUS_MODE_B_RJ01   | 6     |

### PPM/PWM input filtering.

Hardware input filtering can be enabled if you are experiencing interference on the signal sent via your PWM/PPM RX.

Use the `input_filtering_mode` CLI setting to select a mode.

| Value | Meaning   |
| 0     | Disabled  |
| 1     | Enabled   |

