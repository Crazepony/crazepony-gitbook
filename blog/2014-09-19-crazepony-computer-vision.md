#  CrazePony与计算机视觉
> 作者： Ziv.Lin

大家好,我是CrazePony的视觉攻城狮,Ziv.Lin,我擅长的部分是计算机视觉和嵌入式编程,非常荣幸地能够加入CrazePony团队~

众所周知,一个飞行器想要做到悬停的话，必须引入一个位置环进行反馈，也就是说需要获知无人机的空间绝对坐标，目前的无人机普遍采用GPS（Global Position System）以获得其位置，但是GPS信号存在容易受干扰（甚至是欺骗，伊朗截获美国的RQ170就是采用GPS欺骗的方法）、在室内没有信号等无法克服的弊端，如今，业界正在寻求一种解决方案，以克服GPS的这些先天性的缺点，也就是我今天想要说的计算机视觉( ^_^ )

对于类似CrazePony这些微型飞行器来说，载重相当有限，不大可能机载GPS系统（因为如果想要获得较低的定位误差,必须使用介电陶瓷的天线，其重量较重）,想要实现悬停等动作,比较可行的方法就是引入视觉定位系统,如下图所示.

![](/assets/img/post-8-1.png)

CrazePonzy的计算机视觉定位我打算分为三步走:

第一步:就是实现四轴飞行器的视觉跟踪,现在已经初步完成~

![](/assets/img/post-8-5.png)

这个视觉定位系统视频已经上传至CrazePony的首页（也附加在本文最后），这个是基于OpenCV库开发的一个定位系统,其算法流程图如下所示:

![](/assets/img/post-8-2.png)

第二步:就是实现飞行器的航线飞行,现在,我们团队正在努力实现中

第三部:把所有的计算机视觉移植到手机平台去,现在我们已经实现OpenCV库在Android上面的移植了,相信总有一天,你可以使用你的手机飞CrazePony了

![](/assets/img/post-8-3.png)

![](/assets/img/post-8-4.png)

最后附上Crazepony视觉定位系统的优酷视频。

<p>
<embed src="http://player.youku.com/player.php/sid/XNzc1NjI4NTEy/v.swf" allowFullScreen="true" quality="high" width="480" height="400" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash"></embed>
</p>
