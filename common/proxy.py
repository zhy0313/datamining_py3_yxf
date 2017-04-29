#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取并维护免费代理ip地址库。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os
import timeit

# requirements
import requests
from bs4 import BeautifulSoup


def get_proxy_pool():
    pass


def get_proxy():
    pass


if __name__ == '__main__':
    print("===== init directory =====")
    Proxy_data_file = "proxy.json"
    BASE_DIR = os.path.dirname(os.path.realpath(__file__))  # 基础路径为当前目录
    print("Base dir: ", BASE_DIR)
    os.chdir(BASE_DIR)  # 进入基础路径

    print("===== init client =====")
    print("Done")

    print("===== test start =====")
    try:  # 调用test()进入测试，直到测试完成
        time = timeit.timeit('test()', setup='from __main__ import test', number=1)
        print('===== test passed =====')
        print('time used: {0} s'.format(time))  # 计时
    except Exception as e:
        print('===== test failed =====')
        raise e
        pass
    finally:
        print("Done")

    print("===== exit client =====")
    os.chdir(BASE_DIR)
    input("按Enter键退出")
    print("Done")
