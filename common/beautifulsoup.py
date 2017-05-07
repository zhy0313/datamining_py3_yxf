#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        封装与第三方库bs4相关的代码。
        网页dom结构解析。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os

# requirements
from bs4 import BeautifulSoup


def load_soup(html_doc, parser="html5lib"):
    soup = BeautifulSoup(html_doc, parser)
    return soup
