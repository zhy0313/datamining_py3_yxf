#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        封装通用正则表达式规则。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import re


# 匹配数据格式
re_int_number_pattern = re.compile(r'^-?[1-9]\d*$')  # 匹配整数
re_number_in_string_pattern = re.compile(r'(?<=/)\d+(?=/)')  # 匹配字符串中的数字
re_positive_int_number_pattern = re.compile(r'^[1-9]\d*$')  # 匹配正整数
re_float_number_pattern = re.compile(r'^-?[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')  # 匹配浮点数
re_chinese_character_pattern = re.compile(r'[\u4e00-\u9fa5]')  # 匹配中文字符
re_number_in_double_quotes_pattern = re.compile(r'\"\d\"')  # 匹配双引号中的数字


# 匹配特定信息
re_url_pattern = re.compile(r'[a-zA-z]+://[^\s]*')  # 匹配url网址
re_phone_num_pattern = re.compile(r'^1\d{10}$')  # 匹配手机号
re_email_pattern = re.compile(  # 匹配email地址
    "[\w!#$%&'*+/=?^_`{|}~-]+(?:\.[\w!#$%&'*+/=?^_`{|}~-]+)*@(?:[\w](?:[\w-]*[\w])?\.)+[\w](?:[\w-]*[\w])?"
)
re_standard_date_pattern = re.compile(  # 匹配标准格式日期：yyyy-mm-dd
    r'([0-9]{3}[1-9]|[0-9]{2}[1-9][0-9]{1}|[0-9]{1}[1-9][0-9]{2}|[1-9][0-9]{3})-(((0[13578]|1[02])-(0[1-9]|[12][0-9]|3[01]))|((0[469]|11)-(0[1-9]|[12][0-9]|30))|(02-(0[1-9]|[1][0-9]|2[0-8])))'
)
re_html_notes_pattern = re.compile(r'<[!?]?[^>]+-->')  # 匹配html注释
re_ipv4_pattern = re.compile(r'(\d{1,3}\.){3}\d')  # 匹配ipv4地址
re_mac_pattern = re.compile(r'([A-Fa-f0-9]{2}\:){5}[A-Fa-f0-9]')  # 匹配mac地址
