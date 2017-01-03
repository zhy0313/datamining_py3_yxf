#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取网页。
        模拟浏览器浏览过程。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import re
import sys
import http.cookiejar as cookielib

# requirements
import requests
from bs4 import BeautifulSoup

# module
import zhihu.src.base as base
import zhihu.src.client as client


class Question:
    def __init__(self, url, title=None, session=None):
        if not re.match(base.re_question_url, url):
            raise ValueError("\"" + url + "\"" + " : it isn't a question url.")
        else:
            self._url = url
        if session is None:
            self._session = client.session
        if title is None:
            self._title = ''
        self._answer_num = ''
        self._follower_num = ''
        self._id = int(re.match(r'.*/(\d+)', self._url).group(1))
        self._author = ''
        self._creation_time = ''
        self._logs = None
        self._deleted = None
        self._html = self.get_content()
        self._soup = BeautifulSoup(self._html,'html5lib')

    def get_content(self):
        if self._url.endswith('/'):
            resp = self._session.get(self._url[:-1])
        else:
            resp = self._session.get(self._url)
        return resp.content

    @property
    def url(self):
        # always return url like https://www.zhihu.com/question/1234/
        url = re.match(base.re_question_url, self._url).group()
        return url if url.endswith('/') else url + '/'

    @property
    def id(self):
        """获取问题id（网址最后的部分）.

        :return: 问题id
        :rtype: int
        """
        return self._id

    @property
    def qid(self):
        """获取问题内部id（用不到就忽视吧）

        :return: 问题内部id
        :rtype: int
        """
        return int(self._soup.find('div', id='zh-question-detail')['data-resourceid'])

    @property
    def xsrf(self):
        """获取知乎的反xsrf参数（用不到就忽视吧~）

        :return: xsrf参数
        :rtype: str
        """
        return self._soup.find('input', attrs={'name': '_xsrf'})['value']

    @property
    def html(self):
        """获取页面源码.

        :return: 页面源码
        :rtype: str
        """
        return self._soup.prettify()

    @property
    def title(self):
        """获取问题标题.

        :return: 问题标题
        :rtype: str
        """
        return self._soup.find('h2', class_='zm-item-title').text.replace('\n', '')

    @property
    def details(self):
        """获取问题详细描述，目前实现方法只是直接获取文本，效果不满意……等更新.

        :return: 问题详细描述
        :rtype: str
        """
        return self._soup.find("div", id="zh-question-detail").div.text

    @property
    def answer_num(self):
        """获取问题答案数量.

        :return: 问题答案数量
        :rtype: int
        """
        answer_num_block = self._soup.find('h3', id='zh-question-answer-num')
        # 当0人回答或1回答时，都会找不到 answer_num_block，
        # 通过找答案的赞同数block来判断到底有没有答案。
        # （感谢知乎用户 段晓晨 提出此问题）
        if answer_num_block is None:
            if self._soup.find('span', class_='count') is not None:
                return 1
            else:
                return 0
        return int(answer_num_block['data-num'])

    @property
    def follower_num(self):
        """获取问题关注人数.

        :return: 问题关注人数
        :rtype: int
        """
        follower_num_block = self._soup.find('div', class_='zg-gray-normal')
        # 无人关注时 找不到对应block，直接返回0 （感谢知乎用户 段晓晨 提出此问题）
        if follower_num_block is None or follower_num_block.strong is None:
            return 0
        return int(follower_num_block.strong.text)

    @property
    def topics(self):
        """获取问题所属话题.

        :return: 问题所属话题
        :rtype: Topic.Iterable
        """
        for topic in self._soup.find_all('a', class_='zm-item-tag'):
            yield Topic(base.Zhihu_URL + topic['href'], topic.text.replace('\n', ''), session=self._session)

    def followers(self):
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
    def __init__(self, url, name=None, session=None):
        """创建话题类实例.

        :param url: 话题url
        :param name: 话题名称，可选
        :return: Topic
        """
        self.url = url
        self._name = name
        self._session = session
        self._id = int(base.re_topic_url.match(self.url).group(1))


class Anonymous:
    def __init__(self):
        self.name = "匿名用户"
        self.url = ''
