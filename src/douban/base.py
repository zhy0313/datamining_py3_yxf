#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取豆瓣需要的规则信息
        By Yanxingfei(1139),2016.08.10
"""

import re
import os

Headers = {
    'Referer': 'https://www.douban.com/explore/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/50.0.2661.102 Safari/537.36',
    'Host': 'www.douban.com'
    }

Douban_URL = 'https://www.douban.com/'

re_group_url = re.compile(r'')
re_topic_url = re.compile(r'')
re_author_url = re.compile(r'')

