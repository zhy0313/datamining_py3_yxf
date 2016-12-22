#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        安装
        By Yanxingfei(1139),2016.08.10

        python setup（暂停）.py bdist_wininst::编译成windows安装程序，安装到python模块库
        python setup（暂停）.py bdist_rpm::编译成linuxRPM包
"""

try:
    from setuptools import setup, find_packages  # 安装相关，直接python setup（暂停）.py install即可安装此包
except ImportError:
    from distutils.core import setup


setup(  # 执行安装需要的元信息
    name='datamining_py3_yxf',  # 模块名
    version='0.0.1',  # 版本号
    keywords=['zhihu', 'douban', 'spider', 'html'],  # 关键词
    description='Spider in python3, with help of bs4, lxml, requests and html2text.',  # 描述
    author='Yanxingfei',  # 作者
    author_email='hcmw_yym@163.com',  # 作者邮箱
    license='MIT',  # 许可证
    url='https://github.com/yanyaming/datamining_py3_yxf',  # 链接
    download_url='https://github.com/yanyaming/datamining_py3_yxf',  # 下载链接
    install_requires=[  # 依赖模块
        'setuptools',
        'beautifulsoup4',
        'requests',
        #'html2text'
    ]
)
