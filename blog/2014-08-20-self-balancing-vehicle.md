#  Crazepony自平衡小车
> 作者： nieyong

离上次参加makeblock周末马拉松比赛已经快一个月了。一直想介绍我们Craze团队的作品**基于Crazepony自平衡小车**，却迟迟没有动笔。很多人在问为什么主页上关于自平衡小车的链接是空的，大家都等不及了。Crazepony平台不仅仅是一个四轴飞行器，而且还能够很简单的实现自平衡小车。

首先上图。我们使用了makeblock提供的机械构件，包括车轮，电机，以及一些金属连接构件。这里不得不赞一下makeblock的产品，全部是铝合金材质，非常高达上。而且特有的内嵌螺纹槽，给DIY提供了非常大的灵活性。基本上在任何地方都可以上螺丝进行连接。

![](/assets/img/vehicle-1.jpg)

![](/assets/img/vehicle-4.jpg)

电机驱动电路也使用makeblock提供的[Me Motor Driver](http://www.makeblock.cc/me-motor-driver-v2-0/)模块。Me系列模块本来是为降低makeblock电子部分门槛而开发的，使用了RJ-25连接头。这和Crazepony飞控板是不匹配的，所以我们不得不做飞线处理。

![](/assets/img/vehicle-2.jpg)

最上面就是Crazepony飞控板，使用原来四路电机输出PWM中的两路控制连接到电机驱动模块。

![](/assets/img/vehicle-3.jpg)

![](/assets/img/vehicle-5.jpg)

只需要稍稍修改飞控代码（主要是PID参数），我们的自平衡小车就能够站立起来了。在比赛中使用的这个方案是开环控制，没有小车运动速度的反馈作闭环控制，所以我们的自平衡小车并不能够行走自如。我们让它在一个定做的“拳击擂台”里冲撞。它的对手只有一个，那就是它自己，别让自己倒下啦。

最后放上Crazepony在拳击擂台里跌跌撞撞的视频。


<p>
<embed src="http://player.youku.com/player.php/sid/XNzYwNTA2NjUy/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>
</p>
