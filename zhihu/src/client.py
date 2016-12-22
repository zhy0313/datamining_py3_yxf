#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        知乎模拟客户端类，内部维护了自己专用的网络会话，可用cookies自动登录或账号密码验证码手动登录。
        模拟客户端登录动作。
        By Yanxingfei(1139),2016.08.10
"""

import os
import re
import time
import requests  # 更好的第三方网络库
import zhihu.src.base as base


class Client:
    def __init__(self):
        """
        客户端类
        """
        self.Cookie_File = 'zhihu_cookie.txt'
        if os.path.isfile(self.Cookie_File):
            print("Cookies file found.")
            self.login_with_cookies()
        else:
            print("Cookies file not exist, please login...")
            self.login_in_terminal()

    # ===== login staff =====

    @staticmethod
    def get_captcha(cookie_first):
        """
        获取验证码数据。
        :return: 验证码图片数据。
        :rtype: bytes
        """
        params = {
            'r': str(int(time.time() * 1000)),
            'type': 'login',
        }
        r = requests.get(url=base.Captcha_URL, params=params, cookies=cookie_first, headers=base.Default_Header)
        with open('captcha.png', 'wb') as f:
            f.write(r.content)
            f.close()
        print(u'请到 %s 目录找到captcha.png手动输入' % os.path.abspath('captcha.png'))
        print("Please input the captcha:")
        captcha = input()
        return captcha

    def login_with_cookies(self):
        """
        带cookie登录，并在登录后更新cookie
        :return:
        """
        cookie_request = self.get_cookie()  # 从文件中读取cookie内容
        r = requests.get(url=base.Zhihu_URL, headers=base.Default_Header, cookies=cookie_request)  # 自定义header，带cookie请求
        cookie_response = dict(r.cookies)
        self.set_cookie(cookie_request, cookie_response)  # 把应答里的set-cookie重写到原cookie文件
        with open('zhihu.html', 'w', encoding='utf-8') as f:
            f.write(r.text)

    def login_in_terminal(self):  # 网络抓包防止网站故意刷新，只能用firefox浏览器
        r1 = requests.get(url=base.Zhihu_URL, headers=base.Default_Header)  # 初次访问建立初始cookie
        cookie_first = dict(r1.cookies)
        with open(self.Cookie_File, 'w', encoding='utf-8') as f:  # 把对象逐条写入文件
            for i in cookie_first:
                f.write(i)
                f.write('=')
                f.write(cookie_first[i])
                f.write('; ')
        with open(self.Cookie_File, 'rb+') as f:  # 在文件末尾去掉无效字符。文件指针只能在b二进制模式下使用
            f.read()
            f.seek(-2, 2)  # 定位到文件末尾倒数第二个字符
            f.truncate()  # 只保留指针位置之前的字符
            f.close()
        try:
            _xsrf = cookie_first['_xsrf']
        except:
            print(u'未知错误，cookie中的_xsrf项未找到')
            _xsrf = ''
        print("Please input your account:")
        account = input()
        print("Please input your password:")
        password = input()
        if re.match(base.re_phone_num_pattern, account):
            login_url = base.Zhihu_Login_Phone
            post_data = {
                '_xsrf': _xsrf,
                'password': password,
                'remember_me': 'true',
                'phone_num': account,
                'captcha': self.get_captcha(cookie_first)
            }
        else:
            login_url = base.Zhihu_Login_Email
            post_data = {
                '_xsrf': _xsrf,
                'password': password,
                'remember_me': 'true',
                'email': account,
                'captcha': self.get_captcha(cookie_first)
            }
        print(str(post_data))
        r2 = requests.post(url=login_url, cookies=cookie_first, data=post_data, headers=base.Data_Header)
        cookie_response = dict(r2.cookies)
        self.set_cookie(cookie_first, cookie_response)
        login_code = eval(r2.text)
        if login_code["r"] == 0:
            print(login_code['msg'])
            self.login_with_cookies()
        else:
            print(login_code)

    def get_cookie(self):
        cookies = {}
        with open(self.Cookie_File, 'r', encoding='utf-8') as f:  # 解析原cookie文件建立字典对象
            try:
                for line in f.read().split(';'):
                    name, value = line.strip().split('=', 1)  # 1代表只分割一次，即只从第一个等号处分割
                    cookies[name] = value
                return cookies
            except ValueError:
                return ''

    def set_cookie(self, cookie_request, cookie_response):
        cookie_request.update(cookie_response)  # 把新cookie对象更新到原cookie对象
        with open(self.Cookie_File, 'w', encoding='utf-8') as f:  # 重新把对象逐条写入文件
            for i in cookie_request:
                f.write(i)
                f.write('=')
                f.write(cookie_request[i])
                f.write('; ')
        with open(self.Cookie_File, 'rb+') as f:  # 在文件末尾去掉无效字符。文件指针只能在b二进制模式下使用
            f.read()
            f.seek(-2, 2)  # 定位到文件末尾倒数第二个字符
            f.truncate()  # 只保留指针位置之前的字符
            f.close()

    # ===== network staff =====

    # def set_proxy(self, proxy):
    #     """
    #     设置代理
    #     :param str proxy: 使用 "http://example.com:port" 的形式
    #     :return: 无
    #     :rtype: None
    #
    #     :说明:
    #         由于一个 :class:`.ZhihuClient` 对象和它创建出来的其他知乎对象共用
    #         一个cookie，所以调用这个方法也会将所有生成出的知乎类设置上代理。
    #     """
    #     self.cookie.proxies.update({'http': proxy})
    #
    # def set_proxy_pool(self, proxies, auth=None, https=True):
    #     """
    #     设置代理池
    #     :param proxies: proxy列表, 形如 ``["ip1:port1", "ip2:port2"]``
    #     :param auth: 如果代理需要验证身份, 通过这个参数提供, 比如
    #     :param https: 默认为 True, 传入 False 则不设置 https 代理
    #     .. code-block:: python
    #
    #           from urllib.requests.auth import HTTPProxyAuth
    #           auth = HTTPProxyAuth('laike9m', '123')
    #     :说明:
    #          每次 GET/POST 请求会随机选择列表中的代理
    #     """
    #     from random import choice
    #
    #     if https:
    #         self.proxies = [{'http': p, 'https': p} for p in proxies]
    #     else:
    #         self.proxies = [{'http': p} for p in proxies]
    #
    #     def get_with_random_proxy(url, **kwargs):
    #         proxy = choice(self.proxies)
    #         kwargs['proxies'] = proxy
    #         if auth:
    #             kwargs['auth'] = auth
    #         return self.cookie.original_get(url, **kwargs)
    #
    #     def post_with_random_proxy(url, *args, **kwargs):
    #         proxy = choice(self.proxies)
    #         kwargs['proxies'] = proxy
    #         if auth:
    #             kwargs['auth'] = auth
    #         return self.cookie.original_post(url, *args, **kwargs)
    #
    #     self.cookie.original_get = self.cookie.get
    #     self.cookie.get = get_with_random_proxy
    #     self.cookie.original_post = self.cookie.post
    #     self.cookie.post = post_with_random_proxy
    #
    # def remove_proxy_pool(self):
    #     """
    #     移除代理池
    #     """
    #     self.proxies = None
    #     self.cookie.get = self.cookie.original_get
    #     self.cookie.post = self.cookie.original_post
    #     del self.cookie.original_get
    #     del self.cookie.original_post
