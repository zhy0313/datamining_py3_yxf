#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        封装数据处理代码。
        主要处理cookies、json等数据。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import json


def single_quote_json_str_to_python_obj(str):  # 输入单引号为边界的类json字符串（内部可能还有双引号），返回单引号为边界的python字典or列表对象。
    json_obj = eval(str)  # 不能用内置函数解析。只能模拟执行。
    return json_obj  # dict or list


def json_str_to_python_obj(str):  # 输入完全正规的json字符串（键-值边界为双引号），返回单引号为边界的python字典or列表对象。
    json_obj = json.loads(str)
    return json_obj


def python_obj_to_json_str(obj):  # 输入边界为单引号的类json对象（python列表或字典），返回边界为双引号的json字符串且双引号加斜杠转义。
    json_str = json.dumps(obj)
    return json_str


def browser_cookies_to_dict(browser_cookies):
    pass


def iptext_to_python_dict(iptext):
    list = iptext.split('\n')
    json_list = []
    for i in list:
        json_list.append({"url": "{0}".format(i)})
    return json_list
