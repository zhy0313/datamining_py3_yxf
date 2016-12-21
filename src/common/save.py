#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        把筛选出来的有用信息存入数据库，结构化存储。
        By Yanxingfei(1139),2016.08.10
"""

import sqlite3


class Save:
    @staticmethod
    def save(self, _content):
        print('已保存')


class Sqlite:
    def __init__(self, db):
        self.db = db
        conn = sqlite3.connect(self.db)
        c = conn.cursor()

    def query(self):
        pass
