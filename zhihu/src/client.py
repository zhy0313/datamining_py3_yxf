#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        模拟客户端。内部维护了自己专用的网络会话，可用cookies自动登录或账号密码验证码手动登录。
        模拟客户端登录动作。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os
import re
import time
import json
import getpass

# requirements
import requests  # 更好的第三方网络库

# module
import zhihu.src.base as base

# 建立全局会话
session = requests.Session()


class Client:
    def __init__(self, ua, cookies):
        """
        客户端类
        """
        #self._session = requests.Session()
        session.headers.update(base.Default_Header)
        session.headers.update(ua)
        print(str(session.headers))
        if os.path.isfile(cookies):
            print("cookies file found.")
            assert isinstance(cookies, str)
            self.login_with_cookies(cookies)
        else:
            print("cookies file not found, please login...")
            self.login_in_terminal(cookies)

    @staticmethod
    def get_captcha():
        """
        获取验证码数据。
        """
        session.get(base.Zhihu_URL)  # 给session获取初始cookies
        print(str(dict(session.cookies)))
        params = {
            'r': str(int(time.time() * 1000)),
            'type': 'login',
        }
        r = session.get(base.Captcha_URL, params=params)
        with open('captcha.png', 'wb') as f:
            f.write(r.content)
            f.close()
        print(u'请到 %s 目录找到captcha.png手动输入' % os.path.abspath('captcha.png'))
        print("Please input the captcha:")
        captcha = input()
        return captcha

    @staticmethod
    def login_with_cookies(cookies):
        """
        带cookie登录，并在登录后更新cookie
        """
        if os.path.isfile(cookies):
            with open(cookies) as f:
                cookies = f.read()
        cookies_dict = json.loads(cookies)
        session.cookies.update(cookies_dict)  # 将cookies文件读取到内存，供以后测试用

    def login_in_terminal(self, cookies):  # 网络抓包防止网站故意刷新，只能用firefox浏览器
        print('====== zhihu login =====')
        account = input('account: ')
        password = getpass.getpass('password: ')
        post_data = {
            'password': password,
            'remember_me': 'true',
            'captcha': self.get_captcha()
        }
        if re.match(base.re_phone_num_pattern, account):
            login_url = base.Zhihu_Login_Phone
            phone_num = {'phone_num': account}
            post_data.update(phone_num)
        else:
            login_url = base.Zhihu_Login_Email
            email = {'email': account}
            post_data.update(email)
        print('====== logging.... =====')
        print(str(post_data))
        r = session.post(login_url, data=post_data)
        j = r.json()
        code = int(j['r'])
        message = j['msg']
        cookies_str = json.dumps(session.cookies.get_dict()) if code == 0 else ''
        with open(cookies, 'w', encoding='utf-8') as f:
            f.write(cookies_str)
        if code == 0:
            print('login successfully')
        else:
            print('login failed, reason: {0}'.format(message))
