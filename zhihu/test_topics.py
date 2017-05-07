#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        遍历话题树。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import time
import threading
import queue
import os
import re
import random

# module
import common.db as db
import common.beautifulsoup as beautifulsoup
import zhihu.base as base
import zhihu.client as client

DATABASE = db.SqlServer('127.0.0.1', '1433', 'sa', '201212', 'zhihu')  # 数据库连接
TOPIC_QUEUE = queue.Queue()  # 话题url队列，保存所有从页面解析获取到的话题url，通过此队列获取每个话题详情。用于多线程任务队列
TOPIC_LIST = []  # 暂存话题url列表。用于跟踪运行状态
LOCK = threading.Lock()  # 线程互斥锁。用于同时只能有一个线程工作的操作


def load_topic_queue():  # 话题id
    if os.path.isfile('url_list_to_do.txt'):
        with open('url_list_to_do.txt') as f:
            urls = f.read().split('\n')
            for i in urls:
                TOPIC_QUEUE.put(i)
                TOPIC_LIST.append(i)
    else:
        soup = beautifulsoup.load_soup(open("完整话题结构-depth4.html", encoding="utf-8"))
        topics = soup.find_all('a', attrs={'name': 'topic'})
        for i in topics:
            url = i['data-token']
            TOPIC_QUEUE.put(url)
            TOPIC_LIST.append(url)
    print("队列内的话题总数：{0}".format(len(TOPIC_LIST)))


def save_topic_queue():
    if TOPIC_QUEUE.empty():
        os.remove('url_list_to_do.txt')
    else:
        print("执行暂存任务...")
        with open('url_list_to_do.txt', 'w') as f:
            url_list = ''
            for item in TOPIC_LIST:
                url_list += item
                url_list += '\n'
            f.write(url_list)
            f.close()
    return


class ThreadTopics(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self._name = name

    def run(self):
        while not TOPIC_QUEUE.empty():
            print("ThreadTopics-" + str(self._name))
            time.sleep(random.randint(1,5))
            try:
                item = TOPIC_QUEUE.get(timeout=5)
                TOPIC_LIST.remove(item)
                print("item:" + item)
            except:
                print("ThreadTopics-" + str(self._name) + "读取队列失败。")
                continue
            try:
                session = client.Client(use_selenium=False).requests_session()  # 程序卡死不动的原因：网络请求卡住。所以全部都要设置timeout
                r = session.get('https://www.zhihu.com/topic/{0}'.format(item) + '/top-answers', timeout=5)
                time.sleep(5)
                with open('topics/' + item + '.html', 'wb') as f:
                    f.write(r.content)
                LOCK.acquire()
                DATABASE.check_item('topics', item)
                DATABASE.commit()
                # soup = beautifulsoup.load_soup(r.text)
                # self.get_data(item, soup)
                if len(TOPIC_LIST) % 100 == 90:
                    print("当前任务数量：" + str(len(TOPIC_LIST)))
                    save_topic_queue()  # 检测到剩余任务的尾数为90，即每100次保存一次
                LOCK.release()
                continue
            except:
                print("ThreadTopics-" + str(self._name) + "线程请求网页失败。")
                TOPIC_QUEUE.put(item)  # 请求失败，则重新把刚才的url添加进去
                TOPIC_LIST.append(item)
                continue

    def get_data(self, item, soup):
        id = item
        url = 'https://www.zhihu.com/topic/{0}'.format(item) + '/top-answers'
        name = soup.select('#zh-topic-title > h1').text
        details = soup.select('#zh-topic-desc > div.zm-editable-content').text
        parent_node_list = []
        parent_node = soup.select('#zh-topic-side-parents-list > div > div').find_all('a')
        for node in parent_node:
            parent_node_list.append(
                {"parent_node_id": node['data-token'], "url": "https://www.zhihu.com/topic/{0}/top-answers".format(node['data-token'])}
            )
        top_answers_list = []
        top_answers = soup.find_all('div', attrs={'itemprop': 'question'})
        for i in top_answers:
            top_answers_list.append(
                {
                    "question_id": i.find('link', attrs={'itemprop': 'url'}).split('/')[1],
                    "question_url": "https://www.zhihu.com/question/{0}".format(i.find('link', attrs={'itemprop': 'url'})),
                    "title": i.find('a', attrs={'data-za-element-name': 'Title'}).text
                }
            )
        question_num = soup.select('#zh-topic-top-page-list > meta:nth-child(1)')['content']
        follower_num = soup.select('#zh-topic-side-head > div > a > strong').text


def test_topics():
    threads = []
    load_topic_queue()
    for i in range(5):
        time.sleep(5)
        thread = ThreadTopics(i)
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()
    save_topic_queue()
    print("多进程遍历爬取话题树，所有子进程执行完成。")
