#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取网页
        By Yanxingfei(1139),2016.08.10
"""

# python自带
# 网络请求，编解码
from urllib import request, parse


class Spider:
    # 爬取网页

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def get(self, _url):
        # 请求网页到缓存
        try:
            _page = request.urlopen(_url, timeout=10)
        except IOError:
            req = request.Request(_url, Spider.headers)
            _page = request.urlopen(req, timeout=10)
        return _page

    def post(self, _url):
        pass

    def login(self, _url, _username, _password):
        values = {
            'act': 'login',
            'user': _username,
            'pwd': _password}
        data = parse.urlencode(values)
        req = request.Request(_url, data, Spider.headers)
        _page = request.urlopen(req, timeout=10)
        return _page

    def use_cookie(self):
        pass
