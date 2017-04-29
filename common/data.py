#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        封装数据处理代码。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import json


def str_to_json(json_str):
    # json_obj = json.loads(json.dumps(json_str))  # json解析有单双引号的问题，用这个式子可以解决。但最终输出并没有变化
    json_obj = eval(json_str)  # 未知错误，json.loads()不能解析标准json格式？只能读取字符串，无法解析为对象。只能用eval形成对象
    return json_obj  # dict or list


def json_to_str(json_object):
    pass


def json_to_dict(json_object):
    pass


def dict_to_json(dict_object):
    pass
