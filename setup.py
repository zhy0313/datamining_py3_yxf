#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        安装
        By Yanxingfei(1139),2016.08.10

        python setup（暂停）.py bdist_wininst::编译成windows安装程序，安装到python模块库
        python setup（暂停）.py bdist_rpm::编译成linuxRPM包
"""
from __future__ import unicode_literals  # 引入py3的新特性用来兼容py2，如果运行环境是py3则忽略此行
import re  # 正则
import ast  # 修改代码
try:
    from setuptools import setup, find_packages  # 安装相关，直接python setup（暂停）.py install即可安装此包
except ImportError:
    from distutils.core import setup


def extract_version():
    with open('common/__init__.py', 'rb') as f_version:
        ast_tree = re.search(
            r'__version__ = (.*)',
            f_version.read().decode('utf-8')
        ).group(1)
        if ast_tree is None:
            raise RuntimeError('Cannot find version information')
        return str(ast.literal_eval(ast_tree))

with open('readme.md', 'rb') as f_readme:
    readme = f_readme.read().decode('utf-8')

version = extract_version()

setup(  # 执行安装需要的元信息，核心代码
    name='datamining_py3_yxf',  # 模块名
    version=version,  # 版本号
    keywords=['zhihu','douban', 'network', 'spider', 'html'],  # 关键词
    description='Zhihu & Douban & Baidu UNOFFICIAL API library in python3, '  # 描述
                'with help of bs4, lxml, requests and html2text.',
    long_description=readme,  # 长描述
    author='Yanxingfei',  # 作者
    author_email='hcmw_yym@163.com',  # 作者邮箱
    license='MIT',  # 许可证
    url='https://github.com/7sDream/zhihu-py3',  # 链接
    download_url='https://github.com/7sDream/zhihu-py3',  # 下载链接
    install_requires=[  # 依赖模块
        'setuptools',
        'beautifulsoup4',
        'requests',
        #'html2text'
    ],
    extras_require={
        'lxml': ['lxml']
    },
    packages=find_packages(),  # 模块内包含的包，可有多个
    classifiers=[
        'Development Status :: 0 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)