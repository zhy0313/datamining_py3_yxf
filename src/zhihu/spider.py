#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取网页。
        模拟浏览器浏览过程。
        By Yanxingfei(1139),2016.08.10
"""

import urllib.request, urllib.parse  # 网络请求，网址解析


class Spider:
    def get(self, _url):
        # 请求网页到缓存
        try:
            _page = urllib.request.urlopen(_url, timeout=10)
        except IOError:
            req = urllib.request.Request(_url, Spider.headers)
            _page = urllib.request.urlopen(req, timeout=10)
        return _page

    def post(self, _url):
        pass

    def login(self, _url, _username, _password):
        values = {
            'act': 'login',
            'user': _username,
            'pwd': _password}
        data = urllib.parse.urlencode(values)
        req = urllib.request.Request(_url, data, Spider.headers)
        _page = urllib.request.urlopen(req, timeout=10)
        return _page

    def use_cookie(self):
        pass


class _Anonymous:
    def __init__(self):
        self.name = "匿名用户"
        self.url = ''


ANONYMOUS = _Anonymous()


class Question:
    def __init__(self, url):
        self.url = url

    def title(self):
        pass

    def details(self):
        pass

    def answer_num(self):
        pass

    def follower_num(self):
        pass

    def followers(self):
        pass

    def topics(self):
        pass

    def people(self):
        pass

    def answers(self):
        pass

    def deleted(self):
        pass

    def creation_time(self):
        pass

    def last_edit_time(self):
        pass

    def top_answer(self):
        pass

    def refresh(self):
        pass

class Answer:
    pass


class People:
    pass


class Column:
    pass


class Commit:
    pass


class Me:
    pass


class Topic:
    pass


