#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        知乎数据分析主程序。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os  # 系统命令
import sys  # python设置
import shutil  # 高级文件操作
import timeit  # 计时相关
from datetime import datetime  # 日期时间
import threading  # 多线程
import time  # 时间相关

sys.path.append(os.getcwd())  # 添加工程根目录(datamining_py3_yxf)到path环境变量

# module
import zhihu.base as base
import zhihu.shower as shower
import zhihu.test_question as test_question
import zhihu.test_topics as test_topics
import zhihu.test_people as test_people
import zhihu.test_zhuanlan as test_zhuanlan


def test():
    # test_question.test_question("https://www.zhihu.com/question/21373902")
    test_topics.test_topics()
    # test_zhuanlan()
    # test_people()


def main():
    print("===== init directory =====")
    BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')  # 基础路径为data目录
    print("Base dir: ", BASE_DIR)
    os.chdir(BASE_DIR)  # 进入基础路径
    print("Done")
    print("===== test start =====")
    try:  # 调用test()进入测试，直到测试完成
        time = timeit.timeit('test()', setup='from __main__ import test', number=1)
        print('===== test passed =====')
        print('time used: {0} s'.format(time))  # 计时
    except Exception as e:
        print('===== test failed =====')
        raise e
    finally:
        print("Done")


if __name__ == '__main__':
    main()
