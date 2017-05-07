data-mining-py3 : 网站数据爬取、分析、展示
=========================================================

设想
----

毕设：  
要点——解耦合、分模块、各个爬虫分开互不相干  

1.维护已登录cookies，browser_domain_cookies.txt——common\data\*cookies.txt
可选2.requests代理ip池——common\data\proxy.txt
3.requests+bs4解析主要用来持续大量爬/selenium+自身解析主要用来单页面动态操作
可选4.postgresql数据库(db.py)——可以存储json数据，运行、连接python、导出数据
5.多线程爬取——爬虫的运行入口，出错不退出主进程，只退出线程。
6.爬的内容——	
    1.遍历知乎话题树（先用selenium点击找出全部话题，然后用requests每一个都点进去看），（话题名称、链接、描述、父话题、精华问题、热门问题、关注度），分析话题分领域关注热度
    2.用selenium只通过点击找到1000专栏，（专栏链接、名称、描述、关注度）
    3.搜狗微信公众号和知乎热点话题之间的关注点区别，分析这两个社群的不同
    4.以我为起点，从我的关注对象开始广度遍历（设定活跃条件），一直遍历1万用户，分析其（行业、教育、活跃度、地区）

代码结构
--------

周边文件：  
\.gitignore::git配置文件  
\README.md::安装前必读  
\ghostdriver.log::浏览器日志可忽略  
\requirements.txt::python第三方库依赖配置文件  
\start_on_windows.bat::windows系统环境运行脚本  
\start_on_linux.sh::linux系统环境运行脚本   
\setup.py::安装文件，安装成功后就无用了。可读取依赖配置文件自动安装依赖  
\data-mining-py3-cli.py::命令行界面，无依赖，菜单式交互进入各子模块，直接调用  
\test  
    test.py::临时性测试  
    ...  

核心文件：  
\common::  
    \data::  
    data.py::  
    db.py::  
    bs4.py::  
    requests.py::  
    selenium.py::  
\zhihu::  
    \data::爬虫临时数据或文件，登录页面截图、待分析完整页面代码等  
    base.py::主站相关代码，不可直接运行  
    client.py::客户端相关代码，不可直接运行  
    saver.py::数据库交互相关代码，不可直接运行  
    shower.py::数据分析展示相关代码，不可直接运行  
    spider.py::爬虫相关代码，不可直接运行  
    test_domain.py::各个爬虫多线程加载脚本  
    test_*.py::独立的各子爬虫运行脚本  

功能
----

