#  Carmack平方根函数经典案例
> 作者： nieyong

> 编者注：在Crazepony飞控代码姿态解算融合中，有一个只有短短不到十行的函数，求解平方根的倒数。该函数是著名的Carmack平方根求解算法，拥有极高的运算效率，堪称经典。本文就介绍该函数背后的故事，由Craze团队-nieyong整理编辑。

首先粘贴Crazepony飞控代码`IMUSO3.c`文件中的该函数，求一个浮点数的平方根的倒数。

~~~
static float invSqrt(float number) 
{
    volatile long i;
    volatile float x, y;
    volatile const float f = 1.5F;

    x = number * 0.5F;
    y = number;
    i = * (( long * ) &y);
    i = 0x5f375a86 - ( i >> 1 );
    y = * (( float * ) &i);
    y = y * ( f - ( x * y * y ) );
    return y;
}
~~~

Quake-III Arena（雷神之锤3）是90年代的经典游戏之一。该系列的游戏不但画面和内容不错，而且即使计算机配置低，也能极其流畅地运行。这要归功于它3D引擎的开发者约翰-卡马克（John Carmack）。事实上早在90年代初DOS时代，只要能在PC上搞个小动画都能让人惊叹一番的时候，John Carmack就推出了石破天惊的Castle Wolfstein, 然后再接再励，doom, doom-II, Quake...每次都把3D技术推到极致。他的3D引擎代码极度高效，几乎是在压榨PC机的每条运算指令。当初微软的Direct3D也得听取他的意见，修改了不少API。

最近，Quake的开发商ID SOFTWARE遵守GPL协议，公开了Quake-III的原代码，让世人有幸目睹Carmack传奇的3D引擎的原码。

我们知道，越底层的函数，调用越频繁。3D引擎归根到底还是数学运算。那么找到最底层的数学运算函数（在`game/code/q_math.c`），必然是精心编写的。里面有很多有趣的函数，很多都令人惊奇。在`game/code/q_math.c`里发现了这样一段代码。它的作用是将一个数开平方并取倒，经测试这段代码比`(float)(1.0/sqrt(x))`快4倍。

~~~
float Q_rsqrt(float number)
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y = number;
	i = * ( long * ) &y;   // evil floating point bit level hacking
	i = 0x5f3759df - ( i >> 1 ); // what the fuck?
	y = * ( float * ) &i;
	y = y * ( threehalfs - ( x2 * y * y ) ); // 1st iteration
	// y   = y * ( threehalfs - ( x2 * y * y ) ); // 2nd iteration, this can be removed

	#ifndef Q3_VM
	#ifdef __linux__
		 assert( !isnan(y) ); // bk010122 - FPE?
	#endif
	#endif
	return y;
}  
~~~

函数返回平方根的倒数，即`1/sqrt(x)`，这个函数在图像处理中比标准函数`sqrt(x)`更有用。 

注意到这个函数只用了一次叠代。编译，实验，这个函数不仅工作的很好，而且比标准的`sqrt()`函数快4倍！要知道，编译器自带的函数，可是经过严格仔细的汇编优化的啊！这个简洁的函数，最核心，也是最让人费解的，就是标注了“what the fuck?”的一句 

> i = 0x5f3759df - ( i >> 1 );

再加上`y = y * ( threehalfs - ( x2 * y * y ) );`，两句话就完成了开方运算！而且注意到，核心那句是定点移位运算，速度极快！特别在很多没有乘法指令的RISC结构CPU上，这样做是极其高效的。

算法的原理其实不复杂,就是牛顿迭代法,用`x-f(x)/f'(x)`来不断的逼近`f(x)=a`的根。

一般的求平方根都是这么循环迭代算的，但是卡马克真正牛B的地方是他选择了一个神秘的常数0x5f3759df来计算那个猜测值，就是加注释的那一行，那一行算出的值非常接近1/sqrt(n)，这样我们只需要2次牛顿迭代就可以达到我们所需要的精度。好吧如果这个还不算厉害，接着看。

普渡大学的数学家Chris Lomont看了以后觉得有趣，决定要研究一下卡马克弄出来的这个猜测值有什么奥秘。Lomont也是个牛人，在精心研究之后从理论上也推导出一个最佳猜测值，和卡马克的数字非常接近, 0x5f37642f。Lomont计算出结果以后非常满意，于是拿自己计算出的最佳猜测值和卡马克的神秘数字做比赛，看看谁的数字能够更快更精确的求得平方根。结果是卡马克赢了...谁也不知道卡马克是怎么找到这个数字的。

最后Lomont怒了，采用暴力方法一个数字一个数字试过来，终于找到一个比卡马克数字要好上那么一丁点的数字，虽然实际上这两个数字所产生的结果非常近似，这个暴力得出的数字是0x5f375a86。Crazepony飞控代码中，就是使用的这个值。

> Lomont为此写下一篇论文，"Fast Inverse Square Root"。论文下载地址：http://www.math.purdue.edu/~clomont/Math/Papers/2003/InvSqrt.pdf或者http://www.matrix67.com/data/InvSqrt.pdf。参考<IEEE Standard 754 for Binary Floating-Point Arithmetic><FAST INVERSE SQUARE ROOT>

大家可以尝试在PC机、51、AVR、430、ARM、上面编译并实验，惊讶一下它的工作效率。 

有则新闻，大意是说Ryszard Sommefeldt很久以前看到这段code，他一看之下惊为天人，想要拜见这位前辈高人，但是一路追寻下去却一直找不到人。在大家追寻的过程中，有人提到一份叫做MIT HACKMEM的文件，这是1970年代的MIT强者们做的一些笔记 (hack memo)，大部份是algorithm，有些 code 是PDP-10 asm写的，另外有少数是C code (有人整理了一份列表)。

这个函数之所以重要，是因为求平方根倒数这个动作在3D运算（向量运算的部份）里面常常会用到，如果你用最原始的sqrt()然后再倒数的话，速度比上面的这个版本大概慢了四倍吧。当然，在飞控多旋翼的姿态解算中，同样涉及到很多向量运算，需要求平方根倒数，所以我们Crazepony选用了这样一个经典的函数。**数学，算法是软件的根基，无论是对于游戏3D引擎还是无人机多旋翼飞控，都是相通的。Carmack平方根函数就是很好的证明。**



