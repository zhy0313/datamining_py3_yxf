#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        获取问题下全部信息。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import time
import re

# module
import common.db as db
import zhihu.base as base
import zhihu.client as client
import zhihu.shower as shower


# 使用数据库连接
database = db.SqlServer('127.0.0.1', '1433', 'sa', '201212', 'zhihu')


# class Question:
#     def __init__(self, url):
#         if not re.match(base.re_question_url_pattern, url):
#             raise ValueError("\"" + url + "\"" + " : it isn't a question url.")
#         else:
#             self._url = url
#         self._title = ''
#         self._answer_num = ''
#         self._follower_num = ''
#         self._id = int(re.match(r'.*/(\d+)', self._url).group(1))
#         self._author = ''
#         self._creation_time = ''
#         self._logs = None
#         self._deleted = None
#         browser.get(url)
#         browser.get_screenshot_as_file('question.png')
#
#     @property
#     def url(self):
#         # always return url like https://www.zhihu.com/question/1234/
#         url = re.match(base.re_question_url_pattern, self._url).group()
#         return "\'" + url + "\'" if url.endswith('/') else "\'" + url + '/'+ "\'"
#
#     @property
#     def id(self):
#         # 获取问题id（网址最后的部分）.
#         return self._id
#
#     @property
#     def title(self):
#         # 获取问题标题.
#         try:
#             return "\'" + browser.find_element_by_css_selector(
#                 '#root > div > main > div > div:nth-child(1) > div.QuestionHeader > div.QuestionHeader-content > div.QuestionHeader-main > h1'
#             ).text + "\'"
#         except:
#             return "\'" + 'invalid title' + "\'"
#
#     @property
#     def details(self):
#         # 获取问题详细描述，目前实现方法只是直接获取文本，效果不满意……等更新.
#         try:
#             return "\'" + browser.find_element_by_css_selector(
#                 '#root > div > main > div > div:nth-child(1) > div.QuestionHeader > div.QuestionHeader-content > div.QuestionHeader-main > div.QuestionHeader-detail > div > div > span'
#             ).text + "\'"
#         except:
#             return "\'" + 'invalid details' + "\'"
#
#     @property
#     def answer_num(self):
#         # 获取问题答案数量.
#         str = browser.find_element_by_xpath(
#             '//*[@id="root"]/div/main/div/div[2]/div[1]/div/div[1]/div/div[1]/h4/span/text()'
#         )
#         num = re.match(regx.re_number_in_double_quotes_pattern, str)
#         return int(num)
#
#     @property
#     def follower_num(self):
#         # 获取问题关注人数.
#         num = browser.find_element_by_css_selector(
#             '#root > div > main > div > div:nth-child(1) > div.QuestionHeader > div.QuestionHeader-content > div.QuestionHeader-side > div > div > div > button > div.NumberBoard-value'
#         ).text
#         # 无人关注时 找不到对应block，直接返回0 （感谢知乎用户 段晓晨 提出此问题）
#         if num is None:
#             return 0
#         return int(num)
#
#     @property
#     def viewed_num(self):
#         # 获取问题浏览次数.
#         num = browser.find_element_by_css_selector(
#             '#root > div > main > div > div:nth-child(1) > div.QuestionHeader > div.QuestionHeader-content > div.QuestionHeader-side > div > div > div > div.NumberBoard-item > div.NumberBoard-value'
#         ).text
#         return int(num)
#
#     @property
#     def topics(self):
#         # 获取问题所属话题.
#         topics = browser.find_element_by_css_selector(
#             '#root > div > main > div > div:nth-child(1) > div.QuestionHeader > div.QuestionHeader-content > div.QuestionHeader-main > div.QuestionHeader-topics'
#         )
#         for topic in topics:
#             yield base.Zhihu_URL + topic.div.span.a['href'], topic.div.span.a.div.div.text
#
#     @property
#     def followers(self):
#         # 获取关注此问题的用户.问题: 要注意若执行过程中另外有人关注，可能造成重复获取到某些用户
#         # self._make_soup()
#         # followers_url = self.url + 'followers'
#         # for x in common_follower(followers_url, self.xsrf, self._session):
#         #     yield x
#         return
#
#     @property
#     def author(self):
#         return
#
#     @property
#     def answers(self):
#         return
#
#     @property
#     def creation_time(self):
#         # 问题创建时间
#         # logs = self._query_logs()
#         # time_string = logs[-1].find('div', class_='zm-item-meta').time[
#         #     'datetime']
#         # return datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
#         return
#
#     @property
#     def last_edit_time(self):
#         # 问题最后编辑时间
#         # data = {'_xsrf': self.xsrf, 'offset': '1'}
#         # res = self._session.post(self.url + 'log', data=data)
#         # _, content = res.json()['msg']
#         # soup = BeautifulSoup(content)
#         # time_string = soup.find_all('time')[0]['datetime']
#         # return datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")
#         return
#
#     @property
#     def top_answer(self):
#         return
#
#     def save(self):
#         database.check_item("question", self.id)
#         database.commit()
#         database.update(  # 对已有的id记录进行更新
#             "question",   # 表
#             "url={0}, title={1},details={2}".format(self.url, self.title, self.details),   # 要更新的字段
#             "id={0}".format(self.id)  # 根据id找到这条记录
#         )
#         database.commit()


def test_question(url):
    # 给出一个特定的问题
    # question = Question(url)
    # question.save()
    pass
