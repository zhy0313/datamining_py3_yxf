#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        模拟客户端。内部维护了自己专用的网络会话，可用cookies自动登录或账号密码验证码手动登录。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os
import re
import time
import getpass
import random

# module
import common.selenium as _selenium
import zhihu.src.base as base

# 加载浏览器引擎
browser = _selenium.load_driver('chrome', load_image=False)
# 定义cookies文件名
Cookies_file = browser.name + '_cookies.json'


def check_login():
    if os.path.isfile(Cookies_file):
        print("cookies file found.")
        browser.get(base.Zhihu_URL)
        time.sleep(1)
        browser.delete_all_cookies()
        # print('加载cookies前：'+str(browser.get_cookies()))
        with open(Cookies_file) as f:  # 读取保存为标准json格式的文件
            cookies_str = f.read().replace('"', '\\"')  # 把有意义的双引号转义，防止丢失
            cookie_obj = eval(cookies_str)  # 直接执行eval建立对象
            for cookie in cookie_obj:  # 成功解析json为对象
                name = cookie['name']
                value = cookie['value']
                browser.add_cookie({'name': name, 'value': value})  # 将每一条json格式的cookies加载到浏览器。此后只要浏览器不关，就能一直维护cookies
            f.close()
        # print('加载cookies后：'+str(browser.get_cookies()))
    else:
        print("cookies file not found, please login...")
        login()


def login():
    browser.get(base.Zhihu_Login)
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys('18861824721')  # 输入用户名
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys('hcmw252513zh2')  # 输入密码
    browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()  # 点击登录按钮
    time.sleep(1)
    browser.get_screenshot_as_file('登录页面.png')
    try:
        capcha = input('请输入你看到的验证码：')
        browser.find_element_by_xpath('//*[@id="captcha"]').send_keys(capcha)  # 输入验证码
        browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()  # 再次点击登录按钮
    except:
        if browser.name == 'phantomjs':
            input("貌似是中文验证码？phantomjs没办法了")
        else:
            input("貌似是中文验证码？只能到浏览器界面自己去点击并登录了。记得登录完成回来Enter一下")
    time.sleep(6)
    browser.get_screenshot_as_file('screenshot.png')
    cookies = browser.get_cookies()  # 标准json格式
    with open(Cookies_file, 'w') as f:
        f.write(str(cookies))
        f.close()
    check_login()


def logout():
    if os.path.exists(Cookies_file):
        os.remove(Cookies_file)  # 只要删除记录登录信息的cookies即可


def start_client():
    pass


def exit_client():  # 保存cookies并退出
    cookies = browser.get_cookies()  # 标准json格式
    with open(Cookies_file, 'w') as f:
        f.write(str(cookies))
        f.close()
    browser.quit()


# class Client:
#     def __init__(self, cookies):
#         """
#         客户端类
#         """
#         #self._session = requests.Session()
#         session.headers.update(base.Default_Header)
#         ua = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#         #ua = {'User-Agent': random.choice(base.UA_Pool)}  # 随机UA
#         #session.headers.update(ua)
#         if os.path.isfile(cookies):
#             print("cookies file found.")
#             assert isinstance(cookies, str)
#             self.login_with_cookies(cookies)
#         else:
#             print("cookies file not found, please login...")
#             self.login_in_terminal(cookies)
#             #self.login_with_cookies(cookies)
#
#     @staticmethod
#     def get_captcha():
#         """
#         获取验证码数据。
#         """
#         print(str(dict(session.cookies)))
#         params = {
#             'r': str(int(time.time() * 1000)),
#             'type': 'login',
#         }
#         r = session.get(base.Captcha_URL, params=params)
#         with open('captcha.png', 'wb') as f:
#             f.write(r.content)
#             f.close()
#         print(u'请到 %s 目录找到captcha.png手动输入' % os.path.abspath('captcha.png'))
#         print("Please input the captcha:")
#         captcha = input()
#         return captcha
#
#     @staticmethod
#     def login_with_cookies(cookies):
#         """
#         带cookie登录，并在登录后更新cookie
#         """
#         if os.path.isfile(cookies):
#             with open(cookies) as f:
#                 cookie = f.read()
#                 cookies_dict = json.load(cookie)
#                 session.cookies.update(cookies_dict)  # 将cookies文件读取到内存，供以后测试用
#
#     def login_in_terminal(self, cookies):  # 网络抓包防止网站故意刷新，只能用firefox浏览器
#         print('====== zhihu login =====')
#         session.get(base.Zhihu_URL)  # 给session获取初始cookies
#         account = input('account: ')
#         password = getpass.getpass('password: ')
#         post_data = {
#             'password': password,
#             #'remember_me': 'true',
#             #'captcha': self.get_captcha()
#         }
#         if re.match(base.re_phone_num_pattern, account):
#             login_url = base.Zhihu_Login_Phone
#             phone_num = {'phone_num': account}
#             post_data.update(phone_num)
#         else:
#             login_url = base.Zhihu_Login_Email
#             email = {'email': account}
#             post_data.update(email)
#         print('====== logging.... =====')
#         print(str(post_data))
#         r = session.post(login_url, data=post_data)
#         j = r.json()
#         code = int(j['r'])
#         message = j['msg']
#         cookies_str = json.dumps(session.cookies.get_dict()) if code == 0 else ''
#         with open(cookies, 'w', encoding='utf-8') as f:
#             f.write(cookies_str)
#         if code == 0:
#             print('login successfully,{0}'.format(message))
#         else:
#             print('login failed, reason: {0}'.format(message))
