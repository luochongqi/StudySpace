#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/20 9:43 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Spyder_Taobao_Goods.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
# CrowTaobaoPrice.py
import codecs
import requests


def get_html_text(url):
    try:
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败" + str(r.status_code)


def main():
    goods = '包'
    url = 'http://search.dangdang.com/?key='
    print(get_html_text(url + goods))


main()
