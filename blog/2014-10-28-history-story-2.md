#  内部资料-Crazepony第二版改进部分
> 作者： nieyong

> 我们将陆续公布Crazepony内部邮件和讨论资料，和大家一起见证Crazepony的发展和成长。这里的第二版即从Crazepony-II 1.1版本到Crazepony-II 2.1版本的修改。有关Crazepony版本历史，详见[这里](/history.html)。

下面是该部分讨论资料在evernote笔记中的存档截图。

![](/assets/img/post-12-12.png)

下面是对该部分资料整理之后。现在看来，有不少已经体现在我们的Crazepony上，例如双曲线板型，Micro USB接口实现充电，下载，调试等。但是还有一些至今没有能够实现，例如更好的电机固定方式。整理的内容完全保持愿意，只对错别字等错误进行了修改。

=================

* 将位于四个展翼上的电子元器件都退回到主板，为以后使用定制支架做准备，并且留出固定外壳的孔，参考crazyfile的设计
* 确定PCB的颜色，形状。目标是科技感，高大上。建议使用黑色，形状最好圆润一点，参考crazyfile设计

![](/assets/img/post-12-0.png)
![](/assets/img/post-12-1.png)

* 电机的固定方式

* BT模块的添加需要注意的问题，是否可以选用陶瓷天线，解决天线部分pcb面积大的问题

* 所有接口都使用micro usb，包括充电/调参/固件升级

* LED的指示灯尽量简洁明了

* 防撞圈安装孔大小，使用何种防撞圈？

* BT和2.4G是否需要做一个拨码开关切换

* 电池，是用接插件插呢，还是直接焊上去

* 可以学习phantom的，在机头部分用红色条纹标记出来，这样就分的清楚机头机尾
![](/assets/img/post-12-2.png)

* 把roll/pitch/yaw/thrust等几个飞行器姿态标示出来
![](/assets/img/post-12-4.jpg)


## 电机固定问题
在撞击的时候，基本上都是桨叶或者4个支架首先收到冲击。所以最重要的就是马达和支架的连接。绝大部分都是使用使用pcb作为四轴的支架。现在使用了电机底座，但是和pcb的连接处太细小。从下面几点考虑：
* 增加pcb的厚度，现在的应该是1.2mm厚的。在保证质量不太重的情况下，增加到1.6mm或者1.8mm；
* 增宽pcb支架的宽度；（王婆四轴和水中游鱼四轴就是这样做的）
![](/assets/img/post-12-5.png)

* 选择大口电机底座；下面是crazyfile的电机底座，值得推荐。
![](/assets/img/post-12-6.png)



四轴飞行器脚架 716空心杯马达座 安装座 四翼电机架 0716。http://item.taobao.com/item.htm?id=37094709800&qq-pf-to=pcqq.group
![](/assets/img/post-12-7.png)

使用该底座，很多人提到摔断脚的问题：http://item.taobao.com/item.htm?spm=2013.1.0.0.d1d5xN&scm=1007.10011.531.0&id=36862276460&pvid=f32c2e96-a4ca-4f54-b6d0-a5e862c46370
![](/assets/img/post-12-8.jpg)
![](/assets/img/post-12-9.jpg)



## 连接器
USB接口：使用micro USB接口，不要使用mini USB接口。因为micro USB接口是现在手机的标配，不是每个人都有mini USB线。前面为b型mini USB接口（我们现在使用的），后面为b型micro USB接口；
USB接口需要实现的功能：固件的烧写功能；参数调节功能；充电功能；

![](/assets/img/post-12-10.png)
![](/assets/img/post-12-11.png)

按键：飞行器复位按键的位置和开关放到同一个位置，方便在打开电源开关之后按复位键；
开关：开关选用更好的物料；
JLINK接口：不要再用该接口，客户需要另外购买JLINK烧写器；


