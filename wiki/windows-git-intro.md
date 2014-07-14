
#  windows下github的配置

git for Windows下载地址[http://msysgit.github.io/](http://msysgit.github.io/);

之后我们能看到有GitBash和GitGUI两个程序，打开GitBash

为了生成一个sshkey输入 ssh-keygen -t rsa


![](/assets/img/ssh-keygen.jpg)

去生成路径下可以看到以下两个文件：

![](/assets/img/id-rsa.jpg)

打开id_rsa.pub把里面的内容全部复制出来。

打开GitHub点击右上角的小扳手，在SSHKEY里添加刚才复制的内容。提交就OK!

看到多了一个SSHKEYS。名字可以随便写。。

![](/assets/img/rsa-github.png)

下一步把GitHub上的源码Clone到本地：

输入git clone git@github.com:Crazepony/crazepony.github.io.git

连敲几个回车

![](/assets/img/git-clone.jpg)

内容有点多，耐心等待一会。。。

进入crazepony的目录:cd crazepony.github.io

也可以使用git gui来管理我们的版本库：

![](/assets/img/git-gui.jpg)
