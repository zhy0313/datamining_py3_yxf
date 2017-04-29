#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        封装与第三方库selenium相关的代码。
        By Yanxingfei(1139),2016.08.10
"""

# requirements
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


"""
    Doc:
        建立selenium-phantomjs浏览器引擎：
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["User-Agent"] = ("yourUA")
            browser = webDriver.PhantomJS(desired_capabilities=dcap)
            browser.close()
        维护cookies：
            browser.get(domain_url)
            browser.delete_all_cookies()
            browser.add_cookie({'name': name, 'value': value})
            browser.get(your_url)
        选择窗口、页面元素：
            switch_to：切换
                switch_to.window()：切换到页面窗口
                switch_to.alert()：切换到alert对话框
                switch_to.frame()：切换到框架
                switch_to.active_element()：切换到活跃区域
            find_element_by_xpath()：xpath选择器
            find_element_by_css_selector()：css选择器
            find_element_by_id()：id选择器
            find_element_by_tag_name()：标签选择器
            find_element_by_class_name()：class选择器
        模拟操作：
            get_screenshot_as_file()：给网页截图
            send_keys()：给input输入框输入内容
            clear()：清空input输入框
            click()：鼠标左键单击
            doubleClick()：鼠标左键双击
            contextClick()：鼠标右键单击
            accept()：alert确定
            dismiss()：alert取消
            getText()：获取内容
            submit()：提交页面
            dragAndDrop(source,target)：鼠标拖拽
"""


def load_driver(driver, load_image=True):
    if driver == 'chrome':
        if load_image:
            browser = webdriver.Chrome()
            return browser
        else:
            prefs = {  # 设置不显示图片
                'profile.default_content_setting_values': {
                    'images': 2
                }
            }
            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', prefs)
            browser = webdriver.Chrome(chrome_options=options)
            return browser
    elif driver == 'phantomjs':
        dcap = dict(DesiredCapabilities.PHANTOMJS)  # 需要修改UA伪装成别的浏览器，因为很多网站限制PhantomJS访问
        dcap["UserAgent"] = (
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        )
        # dcap["phantomjs.page.settings.userAgent"] = (
        # "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"
        # )
        browser = webdriver.PhantomJS(desired_capabilities=dcap)
        return browser
    elif driver == 'firefox':
        browser = webdriver.Firefox()
        return browser
    else:
        print("Warning! You have set an invalid web driver!")


