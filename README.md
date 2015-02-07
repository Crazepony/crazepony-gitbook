Crazepony四轴飞行器书籍
========

这是配套Crazepony四轴飞行器项目的书籍。使用了[GitBook](https://www.gitbook.com/)管理和发布。

书籍的内容来自Crazepony网站[百科wiki](http://www.crazepony.com/wiki.html)，这里只进行了整理和发布，给大家提供在线查看的[Web版本](http://www.crazepony.com/book/)以及可供下载的[PDF版本]()。

Web版本书籍调试命令：

> gitbook serve ./

在浏览器下输入[http://0.0.0.0:4000](http://0.0.0.0:4000)就可以查看修改效果。

Web版本书籍生成命令：

> gitbook build ./ --output=./outputFolder

在Crazepony网站的[Book目录](http://www.crazepony.com/book/)下的就是使用该命令生成的静态Web版本书籍。

书籍内容来自Crazepony网站wiki，我们会定期将wiki的更新同步到书籍中来。虽然网站wiki和gitbook书籍都是使用markdown语言写成，但是还是有部分头文件不相同。我们专门写了一个python脚本批量将网站wiki的md文件转化为适合gitbook的文件。进入./wiki目录，运行：

> ./deleteline.py

2015-2-7 ，第一次发布，0.1版本。


