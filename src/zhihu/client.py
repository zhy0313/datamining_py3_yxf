#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        知乎模拟客户端类，内部维护了自己专用的网络会话，可用cookies自动登录或账号密码验证码手动登录。
        模拟客户端登录动作。
        By Yanxingfei(1139),2016.08.10
"""

import os
import time
import requests  # 更好的第三方网络库
import src.zhihu.base as base


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
    def get_captcha():
        """
        获取验证码数据。
        :return: 验证码图片数据。
        :rtype: bytes
        """
        params = {
            'r': str(int(time.time() * 1000)),
            'type': 'login',
        }
        r = requests.get(url=base.Captcha_URL, params=params, headers=base.Default_Header)
        return r.content

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

    def login_in_terminal(self):  # 暂时不管
        r = requests.get(url=base.Zhihu_Login, headers=base.Default_Header)
        cookie_response = dict(r.cookies)
        print(str(cookie_response))
        with open(self.Cookie_File, 'w', encoding='utf-8') as f:
            for i in cookie_response:
                f.write(i)
                f.write('=')
                f.write(cookie_response[i])
                f.write('; ')

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
    #
    # # ===== getter staff ======
    #
    # def me(self):
    #     """
    #     获取使用特定 cookies 的 Me 实例
    #     :return: cookies对应的Me对象
    #     :rtype: Me
    #     """
    #     #from .me import Me
    #     headers = dict(base.Default_Header)
    #     headers['Host'] = 'zhuanlan.zhihu.com'
    #     res = self.cookie.get(base.Get_Me_Info_Url, headers=headers)
    #     json_data = res.json()
    #     url = json_data['profileUrl']
    #     name = json_data['name']
    #     motto = json_data['bio']
    #     photo = json_data['avatar']['template'].format(
    #         id=json_data['avatar']['id'], size='r')
    #     #return Me(url, name, motto, photo, cookie=self.cookie)
