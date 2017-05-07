#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        知乎模拟客户端。内部维护了自己专用的网络会话，可用cookies自动登录或账号密码验证码手动登录。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os
import time
import getpass
import random

# module
import common.data as data
import common.selenium as selenium
import common.requests as requests
import zhihu.base as base


class Client:
    def __init__(self, use_selenium=True):
        self._selenium_browser = None
        self._requests_session = requests.Session()
        self._requests_session.update(header={'host': 'www.zhihu.com', 'referer': 'https://www.zhihu.com'})
        self._requests_session.set_proxy()
        self._requests_cookies_file = '../../common/data/requests_' + base.Domain + '_cookies.txt'
        if use_selenium:
            self._selenium_browser = selenium.load_browser('chrome', load_image=True)
            self._selenium_cookies_file = '../../common/data/' + self._selenium_browser.name + '_' + base.Domain + '_cookies.txt'
            if os.path.isfile(self._selenium_cookies_file):
                self._selenium_browser.get(base.Zhihu_URL)
                time.sleep(1)
                self._selenium_browser.delete_all_cookies()
                # print('加载cookies前：'+str(browser.get_cookies()))
                with open(self._selenium_cookies_file) as f:  # 读取保存为标准json格式的文件
                    cookies_str = f.read().replace('"', '\\"')  # 把有意义的双引号转义，防止丢失
                    cookie_obj = data.single_quote_json_str_to_python_obj(cookies_str)
                    for cookie in cookie_obj:  # 成功解析json为对象
                        name = cookie['name']
                        value = cookie['value']
                        self._selenium_browser.add_cookie(
                            {'name': name, 'value': value})  # 将每一条json格式的cookies加载到浏览器。此后只要浏览器不关，就能一直维护cookies
                    f.close()
                    # print('加载cookies后：'+str(browser.get_cookies()))
            else:
                print("cookies file not found, please login...")
                self._selenium_browser.get(base.Zhihu_Login)
                time.sleep(1)
                self._selenium_browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[1]/input').send_keys('18861824721')  # 输入用户名
                self._selenium_browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/form/div[1]/div[2]/input').send_keys('hcmw252513zh2')  # 输入密码
                self._selenium_browser.find_element_by_xpath(
                    '/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()  # 点击登录按钮
                time.sleep(1)
                self._selenium_browser.get_screenshot_as_file('登录页面.png')
                try:
                    capcha = input('请输入你看到的验证码：')
                    self._selenium_browser.find_element_by_xpath('//*[@id="captcha"]').send_keys(capcha)  # 输入验证码
                    self._selenium_browser.find_element_by_xpath(
                        '/html/body/div[1]/div/div[2]/div[2]/form/div[2]/button').click()  # 再次点击登录按钮
                except:
                    if self._selenium_browser.name == 'phantomjs':
                        input("貌似是中文验证码？phantomjs没办法了")
                    else:
                        input("貌似是中文验证码？只能到浏览器界面自己去点击并登录了。记得登录完成回来Enter一下")
                time.sleep(6)
                self._selenium_browser.get_screenshot_as_file('screenshot.png')
                cookies = self._selenium_browser.get_cookies()  # 标准json格式
                with open(self._selenium_cookies_file, 'w') as f:
                    f.write(str(cookies))
                    f.close()
                self._selenium_browser.get(base.Zhihu_URL)
                time.sleep(1)
                self._selenium_browser.delete_all_cookies()
                with open(self._selenium_cookies_file) as f:
                    cookies_str = f.read().replace('"', '\\"')
                    cookie_obj = data.single_quote_json_str_to_python_obj(cookies_str)
                    for cookie in cookie_obj:
                        name = cookie['name']
                        value = cookie['value']
                        self._selenium_browser.add_cookie(
                            {'name': name, 'value': value})
                    f.close()

    def requests_session(self):
        return self._requests_session

    def selenium_browser(self):
        return self._selenium_browser

    def quit_browser(self):  # 保存cookies并退出
        if self._selenium_browser:
            cookies = self._selenium_browser.get_cookies()  # 标准json格式
            with open(self._selenium_cookies_file, 'w') as f:
                f.write(str(cookies))
                f.close()
            self._selenium_browser.quit()
        else:
            print('没有启动selenium，不需要关闭。')
