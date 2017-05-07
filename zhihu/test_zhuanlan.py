#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        随机访问获取一定数量的专栏号，分析。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import time
import queue
import threading
import os
import re

# module
import common.db as db
import common.beautifulsoup as beautifulsoup
import zhihu.base as base
import zhihu.client as client

DATABASE = db.SqlServer('127.0.0.1', '1433', 'sa', '201212', 'zhihu')  # 数据库连接
ZHUANLAN_QUEUE = queue.Queue()  # 话题url队列，保存所有从页面解析获取到的话题url，通过此队列获取每个话题详情
LOCK = threading.Lock()  # 线程互斥锁，用于同时只能有一个线程工作的操作
COUNT = 0  # 全局访问量统计


def count(num):
    global COUNT
    COUNT += num


class ThreadZhuanlan(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self._name = name

    def run(self):
        while True:
            print("ThreadZhuanlan-" + str(self._name))
            time.sleep(5)
            item = ZHUANLAN_QUEUE.get()
            session = client.Client(use_selenium=False).requests_session()
            try:
                r = session.get(item)
                time.sleep(5)
                with open('zhuanlan/' + item + '.html', 'wb') as f:
                    f.write(r.content)
                time.sleep(5)
                DATABASE.check_item('zhuanlan', item)
                DATABASE.commit()
                # soup = beautifulsoup.load_soup(r.text)
                # self.get_data(item, soup)
            except:
                print("ThreadZhuanlan-" + str(self._name) + "线程请求网页失败。")
            ZHUANLAN_QUEUE.task_done()

    def get_data(self, item, soup):
        pass


def test_zhuanlan():
    threads = []
    for i in range(1000):  # 访问1000次
        ZHUANLAN_QUEUE.put('https://zhuanlan.zhihu.com/')
    for i in range(5):  # requests不断访问，每一次推荐的专栏号都不一样。
        thread = ThreadZhuanlan(i)
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()
    print("多线程遍历爬取话题树，所有子线程执行完成。")
