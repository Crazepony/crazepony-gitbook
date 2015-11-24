
## naze32飞控
naze32是日本人基于Multiwii二次开发一款简单的飞控，为小型室内或者中等尺寸的室外多轴飞行器设计。市场上现在主要分为6DOF和10DOF版本，两个版本区别在于有没有气压计以及电子罗盘。6DOF主控板没有气压计及电子罗盘，10DOF飞控带有气压计及电子罗盘。对比图片如下：

![](/assets/img/naze-surface1.png)

![](/assets/img/naze-surface2.png)

## naze32在cleanflight环境下的配置

**友情提示：下述配置naze32刷cleanflight固件以10DOF为例，naze32配置操作之前请卸桨叶**

naze32带10DOF，气压计可以辅助H250在空中实现定高，对于新手来说比cc3d表现更稳定。但是经过几次的cc3d与naze32的试飞情况比较，在穿越模式中cc3d反应更快、表现更暴力，naze32的稳定性更高，对于新手而言操控起来感觉很舒服。下面就针对于naze32刷cleanflight固件简要讲述如何配置。

* 一、建立naze32与主机之间的通信。点击sutep，连接后可以通过上位机参看当前H250姿态，点击calibrate Acceleromenter 水平放置H250校准加速度计；点击calibrate Magnetometer，你有30秒的时间校准电子罗盘，建议大家360度顺逆时针转动H250，尽量保证每一个方位都可以转动到。

![](/assets/img/naze-config-1.png)

* 二、配置H250.根据自己的H250配置情况，在configuration选项中整体配置H250，包括遥控器的配置，电机电调配置，模式配置，是否外挂GPS、超声波等外设。这里值得注意的是当naze32作为六轴主控时因端口资源占用不支持外设超声波。naze32外接不同资源，因stm32接口复用并不是所有模式端口通用，模友要根据自己的外设情况对应不同外设配置正确接线。例如接入GPS时，GPS占用3、4通道，若采用pwm接收机1、2通道还是原来的对应的通道输出，其他通道输出端往后平移，请详见naze32不同模式对应的接口方法。**多啰嗦一句，每一次设置后请保存你的设置**

![](/assets/img/naze-config-3.png)

![](/assets/img/naze-config-5.png)

![](/assets/img/naze-config-4.png)

* 三、接收设备配置。接收配置主要为配置遥控器，设定遥控曲线参数。这里需要注意，若使用PWM接收机且配置了GPS，你需要在port配置中打开usart2，配置波特率为38400，勾选GPS，在configuration中 Received mode先选择PPM，使能GPS并保存当前数据。重新配置接收机的信号输入，并保存配置。

![](/assets/img/naze-config-6.png)
 

* 四、配置电机。在configuration中有关于电机电调的配置选项，包括解锁后电机是否怠速转动，油门的最小量、最大值及中间值的设定，在motor中我们所需要的任务主要是查看电机的正反转是否与实际指定方向一致，组建启动全部电机查看转速是否保持一致。

![](/assets/img/naze-config-7.png)

* 五、飞行模式设置。飞行模式一般主要设置解锁方式、自稳模式切换、开关气压计定高、GPS定点返航、OSD设置及超声波定高等，一定要注意不要配置冲突，根据自己的遥控通道合理配置。

![](/assets/img/naze-config-8.png)

* 六、PID参数整定。上位机自配PID可以满足飞行需求，建议大家根据自己的机型及飞行需求进一步对参数进行整定，使我们的机机性能更佳。PID通俗理解请参考文档廖老师的博客[PID通俗理解](http://blog.gkong.com/liaochangchu_117560.ashx)

![](/assets/img/naze-config-9.png)

* 七、GPS信息读取。GPS接收卫星信号室外比较好，若没有使用OSD功能，我们在室外飞行无法从机身直接读取信息，有利于模友通过上位机查看GPS界面直观读出GPS信息。

![](/assets/img/naze-config-10.png)

* 八、数传或遥控调参。在adjustment配置中，可实现远程调整参数，通过数传或者遥控通道实现。一般地数传标识有433或者915，这表示数传的频率为433MHz或915MHz，其中有USB接口端可以连接PC或者是支持OTG功能的手机。

![](/assets/img/naze-config-11.png)

* 九、灯带的配置。为了正确指示出H250机头的方向，一般我们都会为H250机尾及机臂装上灯带有利于我们辨别方向。灯带建议使用I2C接口灯带，匹配naze32预留I2C指示灯接口，配置界面以右下角第一个方格开始，自右往左依次排列，模友可以根据自己的喜好配置不同的指示颜色。具体操作在1中按顺序设置灯带排列效果，选项2中匹配不同指示的功能，3区域选择颜色。

![](/assets/img/naze-config-12.png)

* 十、cmd命令界面，以上所有配置均可使用cmd命令匹配。注：以上各分项配置没有具体顺序!!

![](/assets/img/naze-config-13.png)


## CC3D在cleanflight环境下的配置

todo

