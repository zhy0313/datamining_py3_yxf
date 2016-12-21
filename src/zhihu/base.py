#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取知乎需要的静态规则信息。
        站点特征信息。
        By Yanxingfei(1139),2016.08.10
"""

import re

# 不包含cookie的请求头的内容
Default_Header = {
    'Host':'www.zhihu.com',
    'Connection':'keep-alive',
    'Cache-Control': 'max-age=0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Referer': 'https://www.zhihu.com/',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8'
}


# 知乎主站登录相关链接
Zhihu_URL = 'https://www.zhihu.com' # 域名
Zhihu_Login = 'https://www.zhihu.com/#login'  # 登录地址
Captcha_URL = Zhihu_URL + '/captcha.gif' # 验证码地址
Column_Url = 'http://zhuanlan.zhihu.com' # 专栏地址
Get_Me_Info_Url = Column_Url + '/api/me' # 我的个人信息页

# 网址解析
re_group_url = re.compile(r'')
re_topic_url = re.compile(r'')
re_author_url = re.compile(r'')

# 知乎网站内容模型
Zhihu_Model = {
    'Me': {  # 个人信息
        'Activity': {

        }
    },
    'People': {  # 知乎用户

    },
    'Question': {  # 问题

    },
    'Answer': {  # 回答

    },
    'Topic': {  # 话题

    }
}
