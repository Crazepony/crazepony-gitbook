
#  Jekyll的安装和使用


这个站点使用了github提供的jekyll工具生成html静态网页。所以在本地进行调试时，最好在本地安装jekyll工具，模拟在github生成网页的效果。详细可以参考Github Help中的[Using Jekyll with Pages](https://help.github.com/articles/using-jekyll-with-pages)。

## ubuntu下安装jekyll
在ubuntu中使用下面的命令安装jekyll：

~~~
//jekyll是用ruby写的，所以需要先安装ruby开发环境
$ sudo apt-get install ruby
$ sudo apt-get install ruby-dev
$ sudo gem install rdoc

//安装jekyll
$ sudo gem install jekyll
~~~

在本地调试crazepony网站效果：

~~~
//进入站点源码目录，开启jekyll服务
$ cd crazepony.github.io
$ jekyll serve

~~~

开启jekyll服务之后，在站点源代码下，会生成一个名为_site的目录，该目录下就是jekyll生成的站点静态网页。并且jekyll在本地开启了一个简单的http服务，在浏览器中输入`http://localhost:4000/`，就能够看到站点的效果。

## windows下安装jekyll
windows下安装jekyll会遇到很多奇奇怪怪的问题，所以可能没法成功，一定要有耐心。下面是在笔者的windows 7,64位系统上配置成功的过程。

Ruby和Ruby DevKit下载地址[http://rubyinstaller.org/downloads/](http://rubyinstaller.org/downloads/)。下载ruby 1.9.3版本以及对应的开发包DevKit，ruby 2.0会遇到很多兼容上的错误，不要使用。

![](/assets/img/ruby.png)

![](/assets/img/ruby-devkit.png)

* 安装上面下载的Ruby和Ruby DevKit；
* 打开Ruby DevKit安装目录下的shell，输入下面的命令安装jekyll；

~~~
$ cd c:
$ cd RubyDevKit193 //进入Ruby DevKit的安装目录
$ ruby dk.rb init
$ ruby dk.rb install
$ gem install jekyll
~~~


如果出现安装错误尝试降低jekyll的安装版本,执行以下命令
~~~
$ gem install jekyll -v 1.5.0
~~~


Portable Python下载地址[http://portablepython.com/](http://portablepython.com/)。下载python 2.7版本并且安装。

![](/assets/img/python.png)

至此，在windows下的终端cmd中应该存在jekyll命令。切换到源码路径下，使用`jekyll serve`命令就能够开启jekyll的服务，和ubuntu下的使用是一样的。

## jekyll的相关配置

本站点使用到的jekyll功能或者配置。

* [jekyll配置代码高亮](http://jekyllrb.com/docs/templates/#code-snippet-highlighting)
* [内嵌gist代码](http://jekyllrb.com/docs/templates/#gist)

[Poople](http://getpoole.com/)是一个jekyll模板站点，有很不错适合个人博客的模板提供。Crazepony的博客站点使用的[BeiYuu](http://beiyuu.com/)的模板，最原始就应该是来自Poople中的Hyde模板。
