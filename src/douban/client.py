#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        取得访问权限
        By Yanxingfei(1139),2016.08.10
"""

from urllib import request


class Client:
    # 取得访问权限
    def douban_client(self):
        pass

#开启debug模式
#？？？
class Debug:
    def httpdebug(self):
        httpHandler=request.HTTPHandler(debuglevel=1)
        httpsHandler=request.HTTPSHandler(debuglevel=1)
        opener=request.build_opener(httpHandler,httpsHandler)
        request.install_opener(opener)
