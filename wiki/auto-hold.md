
#  自主悬停&高度融合


自主悬停是Crazepony玩家问得最多的问题，也是技术难度最高的问题。

首先我们明确什么是自主悬停？下面是一位资深航模玩家对于自主悬停的解释。

> 飞行器能够悬停在某个位置，在发生了偏离之后能够自动校正并且回到原来悬停的位置，并且能够在该位置保持足够长的时间，至少2分钟以上，那么我们认为该飞行器是能够自主悬停的。

飞行器在空中是一个三维坐标(x,y,z)位置，涉及到两个维度的悬停。第一是在水平面上(x,y)，飞行器不能够左右或者前后漂移。第二是在垂直方向上（又叫Z轴维度），飞行器不能够发生掉高等现象。针对这两个不同的维度，有不同的技术进行解决。

在水平面上，为了确定飞行器的位置，一般使用GPS进行定位，室内一般使用光流进行定位（室内没有GPS信号）。

在垂直方向上，一般使用气压计进行定高，室内等条件下可以使用超声波模块。

## 能否只用6维数据实现悬停

能否只使用3维加速度和3维陀螺仪这6个维度的数据实现自主悬停？而不再使用气压计和GPS等。现在就我了解，是很难实现。因为只使用这个6维数据，无法知道飞行器在空中的绝对坐标，只能够由6维数据获得相对偏移。没有绝对坐标，就无法对位置实现**闭环控制**。

当然，我们看到很多只是用了MPU6050的玩具四轴，也能够实现一定程度的悬停，但是那并不是真正意义上的自主悬停。

## 水平面的定位

室外使用GPS进行水平定位，室内一般使用光流技术（optical flow）。光流传感器其实就是一个摄像头，安装在飞行器上垂直拍摄地面。光流技术就是要对拍摄到的画面进行视觉处理，以此知道相对于地面坐标位置。APM飞控中关于光流传感器的[介绍](http://copter.ardupilot.cn/wiki/optical-flow-sensor/)。

![](/assets/img/optical-flow-sensor.jpg)
![](/assets/img/optical-flow-sensor-2.jpg)

## 垂直方向定位

在垂直方向上，使用高精度气压计（如MS5611）进行定位。在飞行器处于较低高度时，可以使用超声波进行高度定位。

## Crazepony的自动悬停

飞行器要想实现真正意义的自主悬停需要有自稳和空中绝对坐标。Crazepony有一个高精度气压计MS5611，所以可以实现Z轴的自主悬停。在水平方向上，crazepony没有绝对坐标，无法实现悬停。

在Z轴自主悬停上，Crazepony有一个高精度气压计MS5611，通过气压传感器采集的大气压值计算出来，将气压传感器采集值进行校正后，再通过温度二阶补偿，得到准确的大气压值，最后经过气压转换高度公式就可以得到一个相对于起飞地点的绝对高度（参考[气压计MS5611](./ms5611.html)）。

MS5611气压计的精度为10CM，因此需要融合加速度计互补滤波得到比较合适的高度值，Z轴速度值和加速度值。用高度作外环，速度作内环形成高度双环PID控制器，调节输出油门实现Z轴的自主悬停。高度融合在文件`Altitude.c`中实现，高度双环PID控制在`Control.c`文件中的`CtrlAlti()`函数中实现。

高度双环PID控制总体流程。

![](/assets/img/gdpid.png)

代码实现在`Control.c`文件中的`CtrlAlti()`函数中。

~~~
……
// pid and feedforward control . in ned frame
posZErr= -(altSp - alt);
posZVelSp = posZErr * alt_PID.P + spZMoveRate * ALT_FEED_FORWARD;
//consider landing mode
if(altCtrlMode==LANDING)
    posZVelSp = LAND_SPEED;

velZ=nav.vz;	
velZErr = posZVelSp - velZ;
valZErrD = (spZMoveRate - velZ) * alt_PID.P - (velZ - velZPrev) / dt;	//spZMoveRate is from manual stick vel control
velZPrev=velZ;

thrustZSp= velZErr * alt_vel_PID.P + valZErrD * alt_vel_PID.D + thrustZInt;	//in ned frame. thrustZInt contains hover thrust
……
~~~

在水平方向上，由于Crazepony没有绝对坐标，使用3维加速度和3维陀螺仪这6个维度的数据进行双环PID控制形成一个自稳系统，可实现短时间定点脱控悬停，但是受误差影响产生偏离，没有水平绝对坐标就无法回到原来的位置，所以Crazepony是无法实现正真意义上自动悬停的。

## Z轴悬停-悬停油门基准值

在Z轴悬停代码中，定义了一个悬停油门基准值`HOVER_THRU`，该值决定着飞行器脱控悬停的时候需要的油门大小。对悬停起到至关重要的作用。 在版本[9bf1e83f](https://github.com/Crazepony/crazepony-firmware-none/commit/9bf1e83f78c5f238e65faac1f0ac2cba1527cc29)之后，该宏定义由函数`estimateHoverThru()`代替，根据当前电池电压大小，输出对应的油门悬停基准值，能够彻底解决充满电之后第一次飞行直接往上冲的问题。

油门基准值的选取对悬停是至关重要的。例如，我们换了一批扭力更大的电机，那么在飞行器重量不变的情况下，使用原来的基准值就会出现脱控之后一直往上飞的情况。这个时候，我们就需要将该值改小，以此适应这批次扭力大的电机。

悬停油门基准值将会直接影响Z轴悬停，**选取不当或者系统参数发生变化时，就会出现往上飞或者掉高的问题**。这里的系统参数发生变化，包括电池电力变化，飞机重量改变，电机扭力变化等。如果使用固定值，在电池充满电之后，会出现起飞之后往上冲的问题。所以在版本[9bf1e83f](https://github.com/Crazepony/crazepony-firmware-none/commit/9bf1e83f78c5f238e65faac1f0ac2cba1527cc29)之后，该悬停油门基准值由函数`estimateHoverThru()`输出。根据电池电压不同，使用不同的油门基准值。

~~~
float estimateHoverThru(void){
	float hoverHru = 0.55f;
	
	//电池电压检测
	Battery.BatteryAD  = GetBatteryAD();
	Battery.BatteryVal = Battery.Bat_K * (Battery.BatteryAD/4096.0) * Battery.ADRef;//实际电压 值计算
	
	if(Battery.BatteryVal > 4.05){
		hoverHru = -0.35f;
	}else if(Battery.BatteryVal > 3.90){
		hoverHru = -0.40f;
	}else if(Battery.BatteryVal > 3.80){
		hoverHru = -0.45f;
	}else if(Battery.BatteryVal > 3.70){
		hoverHru = -0.50f;
	}else{
		hoverHru = -0.55f;
	}

	return hoverHru;
}
~~~

## Z轴悬停-最小油门值
根据机重和动力系统的输出，我们还为Crazepony设定了一个最小的油门输出值`THR_MIN`，这样能够限制最大的下降速度。可以避免下降速度过快，机身失去平衡。

限定最小的油门输出值`THR_MIN`本来是为了解决下降过快的问题，有时候也会带来副作用。例如充电后第一次飞行，由于动力输出强劲，如果这个最小油门输出值设置得过大，那么即使将摇杆油门拉到了最低，飞机也会一直往上冲。在版本[7ee226a](https://github.com/Crazepony/crazepony-firmware-none/commit/7ee226a181f03e50f1d0b4a09fb3faf534ccd0a9)之后，该宏被修改为函数`estimateMinThru()`，将输出和当前电池电压挂钩，能够解决**往上冲下拉油门时无法受控的问题**。

~~~
float estimateMinThru(void){
	float minThru = -0.55f;
	
	//电池电压检测
	Battery.BatteryAD  = GetBatteryAD();
	Battery.BatteryVal = Battery.Bat_K * (Battery.BatteryAD/4096.0) * Battery.ADRef;//实际电压 值计算
	
	if(Battery.BatteryVal > 4.05){
		minThru = -0.30f;
	}else if(Battery.BatteryVal > 3.90){
		minThru = -0.40f;
	}else{
		minThru = -0.55f;
	}
	
	return minThru;
}
~~~
