#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        模拟客户端。内部维护了自己专用的网络会话，可用cookies自动登录或账号密码验证码手动登录。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os
import time
import getpass
import random

# module
import common.selenium as selenium
import common.requests as requests
import proxy.base as base


class Client:
    def __init__(self):
        self._requests_session = requests.Session()
        self._requests_session.update()

    def get_session(self):
        return self._requests_session
