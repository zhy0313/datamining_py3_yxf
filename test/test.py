#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        测试
        By Yanxingfei(1139),2016.08.10
"""


print('===============start test=================')
import time
import math
import random
import os
import sys
import json
import re
import common.db as db
database = db.SqlServer('127.0.0.1', '1433', 'sa', '201212', 'zhihu')
id = "21373902"
title = "\'""ansivurnv""\'"
url = "\'""https://www.baidu.com/""\'"
# database.check_item("topics",id)
# database.update("topics","","id={0}".format(id))
database.query("insert into topics(id) values(1234)",False)
print('================end test==================')
