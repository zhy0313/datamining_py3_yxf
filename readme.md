data-mining-py3 : 多站非官方API库 with Python3 & 练手代码
=========================================================

|Author| |Build| |DocumentationStatus| |PypiVersion| |License| |PypiDownloadStatus|

通知
----

由于知乎前端老是改阿改的，每次我都要更新弄的我好烦的说……

所以我开发了一个新的项目\ `Zhihu-OAuth <https://github.com/7sDream/zhihu-oauth>`__。

这个新项目用了一些黑科技手段，反正应该是更加稳定和快速了！**而且还支持 Python 2 哟！**
稳定我倒是没测，但是这里有一个
`速度对比 <https://github.com/7sDream/zhihu-oauth/blob/master/compare.md>`__。

如果你是准备新开一个项目的话，我强烈建议你看看我的新项目~

如果你已经用 Zhihu-py3 写了一些代码的话，我最近会写一个从 Zhihu-py3 转到 Zhihu-OAuth
的简易指南，你也可以关注一下哟。

毕竟嘛，有更好的方案的话，为什么不试试呢？

关系结构
--------

非py文件：
\docs\*::使用帮助文档
\example\*::例子
\resources\*::资源文件
\LICENSE::许可证
\README.rst::安装前必读


py文件（不考虑各__init__.py）：
\setup.py::安装文件，安装成功后就无用了

\data-mining-py3-gui.py::图形界面，依赖PyQt5，提供各test*子模块的入口（直接通过系统调用，与子模块只建立名字联系），可以不使用此入口，直接在命令行进入子模块
\data-mining-py3-cli.py::命令行界面，无依赖，菜单式交互进入各子模块

    \test
        #test.py::临时性测试
        #cross_game.py::井字游戏
        #...
    #\test_zhihu\test_zhihu.py
        \zhihu::知乎相关代码，不能直接执行
                zhihu_rule.py::知乎相关的登录、筛选等静态规则
                zhihu_client.py::模拟客户端登录
                zhihu_spider.py::爬取网页
                zhihu_filter.py::筛选网页内容
        \common::公共代码，不能直接执行
                common.py::此目录下的公共代码
                save.py::把筛选出的有用信息保存到文件或数据库
                analize.py::分析数据
                show.py::通过图形界面展示数据分析的结果并输出到表单
    #\test_douban\test_douban.py
        \douban::豆瓣相关代码，不能直接执行
        \common::公共代码，不能直接执行
                common.py::此目录下的公共代码
                save.py::把筛选出的有用信息保存到文件或数据库
                analize.py::分析数据
                show.py::通过图形界面展示数据分析的结果并输出到表单
    #\test_baidu_tieba\test_baidu_tieba.py
        \baidu_tieba::百度贴吧相关代码，不能直接执行
        \common::公共代码，不能直接执行
                common.py::此目录下的公共代码
                save.py::把筛选出的有用信息保存到文件或数据库
                analize.py::分析数据
                show.py::通过图形界面展示数据分析的结果并输出到表单


功能
----

由于知乎没有公开API，加上受到\ `zhihu-python <https://github.com/egrcc/zhihu-python>`__\ 项目的启发，在Python3下重新写了一个知乎的数据解析模块。

提供的功能一句话概括为，用户提供知乎的网址构用于建对应类的对象，可以获取到某些需要的数据。

简单例子：

..  code:: python

    from zhihu import ZhihuClient

    Cookies_File = 'cookies.json'

    client = ZhihuClient(Cookies_File)

    url = 'http://www.zhihu.com/question/24825703'
    question = client.question(url)

    print(question.title)
    print(question.answer_num)
    print(question.follower_num)
    print(question.topics)

    for answer in question.answers:
        print(answer.author.name, answer.upvote_num)

这段代码的输出为：

::

    关系亲密的人之间要说「谢谢」吗？
    627
    4322
    ['心理学', '恋爱', '社会', '礼仪', '亲密关系']
    龙晓航 50
    小不点儿 198
    芝士就是力量 89
    欧阳忆希 425
    ...

另外还有\ ``Author（用户）``\ 、\ ``Answer（答案）``\ 、\ ``Collection（收藏夹）``\ 、\ ``Column（专栏）``\ 、\ ``Post（文章）``\ 、\ ``Topic（话题）``\ 等类可以使用，\ ``Answer``,\ ``Post``\ 类提供了\ ``save``\ 方法能将答案或文章保存为HTML或Markdown格式，具体请看文档，或者\ ``zhihu-test.py``\ 。

安装
----

..  class:: bold

   本项目依赖于\ `requests <https://pypi.python.org/pypi/requests/2.7.0>`__\ 、\ `BeautifulSoup4 <http://www.crummy.com/software/BeautifulSoup>`__\ 、\ `html2text <https://github.com/aaronsw/html2text>`__

已将项目发布到pypi，请使用下列命令安装

..  code:: bash

    (sudo) pip(3) install (--upgrade) zhihu-py3

希望开启lxml的话请使用：

..  code:: bash

    (sudo) pip(3) install (--upgrade) zhihu-py3[lxml]


因为lxml解析html效率高而且容错率强，在知乎使用\ ``<br>``\ 时，自带的html.parser会将其转换成\ ``<br>...</br>``\ ，而lxml则转换为\ ``<br/>``\ ，更为标准且美观，所以推荐使用第二个命令。

不安装lxml也能使用本模块，此时会自动使用html.parser作为解析器。

PS 若在安装lxml时出错，请安装libxml和libxslt后重试：

..  code:: bash

    sudo apt-get install libxml2 libxml2-dev libxslt1.1 libxslt1-dev

准备工作
--------

第一次使用推荐运行以下代码生成 cookies 文件：

..  code:: python

    from zhihu import ZhihuClient

    ZhihuClient().create_cookies('cookies.json')

运行结果

::

    ====== zhihu login =====
    email: <your-email>
    password: <your-password>
    please check captcha.gif for captcha
    captcha: <captcha-code>
    ====== logging.... =====
    login successfully
    cookies file created.

运行成功后会在目录下生成\ ``cookies.json``\ 文件。

以下示例皆以登录成功为前提。

建议在正式使用之前运行\ ``zhihu-test.py``\ 测试一下。

用法实例
--------

为了精简 Readme，本部分移动至文档内。

请看文档的「用法示例」部分。

登录方法综述
---------------------------------------------

为了精简 Readme，本部分移动至文档内。

请看文档的「登录方法综述」部分。

文档
----

终于搞定了文档这个磨人的小妖精，可惜 Sphinx 还是不会用 T^T
先随意弄成这样吧：

`Master版文档 <http://zhihu-py3.readthedocs.org/zh_CN/latest>`__

`Dev版文档 <http://zhihu-py3.readthedocs.org/zh_CN/dev>`__

其他
----

**有问题请开Issue，几个小时后无回应可加最后面的QQ群询问。**

友链：

-  \ `zhihurss <https://github.com/SimplyY/zhihu-rss>`__\ ：一个基于 zhihu-py3 做的跨平台知乎 rss(any user) 的客户端。


TODO List
---------

- [x] 增加获取用户关注者，用户追随者
- [x] 增加获取答案点赞用户功能
- [x] 获取用户头像地址
- [x] 打包为标准Python模块
- [x] 重构代码，增加\ ``ZhihuClient``\ 类，使类可以自定义cookies文件
- [x] 收藏夹关注者，问题关注者等等
- [x] ``ZhihuClient``\ 增加各种用户操作（比如给某答案点赞）
- [ ] Unittest （因为知乎可能会变，所以这个有点难
- [x] 增加获取用户关注专栏数和关注专栏的功能
- [x] 增加获取用户关注话题数和关注话题的功能
- [x] 评论类也要慢慢提上议程了吧

联系我
------

Github：\ `@7sDream <https://github.com/7sDream>`__

知乎：\ `@7sDream <http://www.zhihu.com/people/7sdream>`__

新浪微博：\ `@Dilover <http://weibo.com/didilover>`__

邮箱：\ `给我发邮件 <mailto:xixihaha.xiha@qq.com>`__

编程交流群：478786205

.. |Author| image:: https://img.shields.io/badge/Author-7sDream-blue.svg
   :target: https://github.com/7sDream
.. |DocumentationStatus| image:: https://readthedocs.org/projects/zhihu-py3/badge/?version=latest
   :target: https://readthedocs.org/projects/zhihu-py3/?badge=latest
.. |PypiVersion| image:: https://img.shields.io/pypi/v/zhihu-py3.svg
   :target: https://pypi.python.org/pypi/zhihu-py3
.. |PypiDownloadStatus| image:: https://img.shields.io/pypi/dd/zhihu-py3.svg
   :target: https://pypi.python.org/pypi/zhihu-py3
.. |License| image:: https://img.shields.io/pypi/l/zhihu-py3.svg
   :target: https://github.com/7sDream/zhihu-py3/blob/master/LICENSE
.. |Build| image:: https://travis-ci.org/7sDream/zhihu-py3.svg?branch=dev
   :target: https://travis-ci.org/7sDream/zhihu-py3
