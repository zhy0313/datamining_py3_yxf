#!/bin/python
# -*- coding: utf-8 -*-

"""
    Note:
        提取网页内容。
        模拟浏览器对网页的解析，筛选出有用信息。
        By Yanxingfei(1139),2016.08.10
"""

# 额外安装
# 网页解析
from bs4 import BeautifulSoup


class Filter:
    def title(self, _page):
        #'html.parser'是python标准解析库，'html5lib'是额外安装的
        soup=BeautifulSoup(_page,'html5lib')
        #有些元素无法显示是因为js动态加载（动态网页）
        #筛选元素
        title=soup.select("body > div.box.body > div.body_left > div.body_top > h1")
        print(title)
        return title

    def user_info(self, _page):
        pass

    def all_url(self, _page):
        pass
