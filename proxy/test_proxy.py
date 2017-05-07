#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Note:
        爬取并维护免费代理ip地址库。
        By Yanxingfei(1139),2016.08.10
"""

# build-in
import os
import sys
import timeit
import threading
import queue
import time
from urllib import request

sys.path.append(os.getcwd())  # 添加工程根目录(datamining_py3_yxf)到path环境变量

# module
import common.data as data
import common.beautifulsoup as beautifulsoup
import proxy.base as base
import proxy.client as client


Common_Data_Dir = '../../common/data/'


def test_kuaidaili(session):
    json_obj = []
    abroad_ip_url_http = "http://www.kuaidaili.com/free/outha/"
    for i in range(1, 20):  # 循环爬取多个页面
        try:
            r1 = session.get(abroad_ip_url_http + str(i) + "/")
            print(abroad_ip_url_http + str(i) + "/")
            time.sleep(10)
            with open('kuaidaili_{0}.html'.format(str(i)), 'wb') as f:
                f.write(r1.content)
                f.close()
            soup1 = beautifulsoup.load_soup(r1.content)
            table = soup1.select('#list > table > tbody > tr')  # 以tr为item的列表
            print(len(table))
            for tr in table:  # 每个页面的表格中的多个ip信息
                td = tr.find_all('td')
                json_obj.append({"url": "http://{0}:{1}".format(td[0].text, td[1].text), "type": "{0}".format(td[3].text)})  # 每个表格有子表格，分别记录不同信息
        except:
            continue
    for i in json_obj:  # 测试是否可用，不可用则删除
        time.sleep(5)
        try:
            r = session.get("http://httpbin.org/ip", proxies=i["url"])
            print(r.text + "ok")
        except:
            json_obj.remove(i)
            continue
    with open(Common_Data_Dir + 'proxy_abroad_http.txt', 'w') as f:
        json = data.python_obj_to_json_str(json_obj)
        f.write(json)
        f.close()


def test_nianshao(session):
    json_obj = []
    abroad_ip_url_https = "http://www.nianshao.me/?stype=2"
    for i in range(1, 20):  # 循环爬取多个页面
        try:
            r1 = session.get(abroad_ip_url_https + "&page=" + str(i))
            print(abroad_ip_url_https + "&page=" + str(i))
            time.sleep(10)
            with open('nianshao_{0}.html'.format(str(i)), 'wb') as f:
                f.write(r1.content)
                f.close()
            soup1 = beautifulsoup.load_soup(r1.content)
            table = soup1.select('#main > div > div > table > tbody > tr')  # 以tr为item的列表
            print(len(table))
            for tr in table:  # 每个页面的表格中的多个ip信息
                td = tr.find_all('td')
                json_obj.append({"url": "http://{0}:{1}".format(td[0].text, td[1].text), "type": "{0}".format(td[4].text)})  # 每个表格有子表格，分别记录不同信息
        except:
            continue
    for i in json_obj:
        time.sleep(5)
        try:
            r = session.get("http://httpbin.org/ip", proxies=i["url"])
            print(r.text + "ok")
        except:
            json_obj.remove(i)
            continue
    with open(Common_Data_Dir + 'proxy_abroad_https.txt', 'w') as f:
        json = data.python_obj_to_json_str(json_obj)
        f.write(json)
        f.close()


def test_xicidaili(session):
    json_obj_http = []
    json_obj_https = []
    china_url_http = "http://www.xicidaili.com/wt/"
    china_url_https = "http://www.xicidaili.com/wn/"
    for i in range(1, 20):  # 循环爬取多个页面
        try:
            r1 = session.get(china_url_http + "/" + str(i))
            print(china_url_http + "/" + str(i))
            time.sleep(10)
            with open('xicidaili1_{0}.html'.format(str(i)), 'wb') as f:
                f.write(r1.content)
                f.close()
            soup1 = beautifulsoup.load_soup(r1.content)
            table = soup1.select('#ip_list > tbody > tr')  # 以tr为item的列表
            print(len(table))
            for tr in table:  # 每个页面的表格中的多个ip信息
                if tr.find_all('td'):
                    td = tr.find_all('td')
                    json_obj_http.append({"url": "http://{0}:{1}".format(td[1].text, td[2].text), "type": "{0}".format(td[5].text)})  # 每个表格有子表格，分别记录不同信息
        except:
            continue
    for i in json_obj_http:
        time.sleep(5)
        try:
            r = session.get("http://httpbin.org/ip", proxies=i["url"])
            print(r.text + "ok")
        except:
            json_obj_http.remove(i)
            continue
    with open(Common_Data_Dir + 'proxy_china_http.txt', 'w') as f:
        json = data.python_obj_to_json_str(json_obj_http)
        f.write(json)
        f.close()
    for i in range(1, 20):  # 循环爬取多个页面
        try:
            r1 = session.get(china_url_https + "/" + str(i))
            print(china_url_https + "/" + str(i))
            time.sleep(10)
            with open('xicidaili2_{0}.html'.format(str(i)), 'wb') as f:
                f.write(r1.content)
                f.close()
            soup1 = beautifulsoup.load_soup(r1.content)
            table = soup1.select('#ip_list > tbody > tr')  # 以tr为item的列表
            print(len(table))
            for tr in table:  # 每个页面的表格中的多个ip信息
                if tr.find_all('td'):
                    td = tr.find_all('td')
                    json_obj_https.append({"url": "http://{0}:{1}".format(td[1].text, td[2].text), "type": "{0}".format(td[5].text)})  # 每个表格有子表格，分别记录不同信息
        except:
            continue
    for i in json_obj_https:
        time.sleep(5)
        try:
            r = session.get("http://httpbin.org/ip", proxies=i["url"])
            print(r.text + "ok")
        except:
            json_obj_https.remove(i)
            continue
    with open(Common_Data_Dir + 'proxy_china_https.txt', 'w') as f:
        json = data.python_obj_to_json_str(json_obj_https)
        f.write(json)
        f.close()


def test():
    session = client.Client().get_session()
    test_kuaidaili(session)  # 爬取国外代理http
    # test_nianshao(session)  # 爬取国外代理https
    # test_xicidaili(session)  # 爬取国内代理


def main():
    print("===== init directory =====")
    BASE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')  # 基础路径为data目录
    print("Base dir: ", BASE_DIR)
    os.chdir(BASE_DIR)  # 进入基础路径
    print("===== test start =====")
    try:  # 调用test()进入测试，直到测试完成
        time = timeit.timeit('test()', setup='from __main__ import test', number=1)
        print('===== test passed =====')
        print('time used: {0} s'.format(time))  # 计时
    except Exception as e:
        print('===== test failed =====')
        raise e
    finally:
        print("Done")
    print("Done")


if __name__ == '__main__':
    main()
