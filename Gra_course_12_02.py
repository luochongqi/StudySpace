#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/12/19 15:49 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_12_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import requests
from lxml import etree
import time
import random


class MaoYan_Spider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36',
        }
        self.url = 'https://www.maoyan.com/board/4?&offset={}'

    def get_page(self, url):
        headers = self.headers
        html = requests.get(url=url, headers=headers).content.decode('utf-8')
        self.parse_page(html)

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        house_dict = {}
        dd_list = parse_html.xpath("//ul[@class='sellListContent']/li[@class='clear LOGCLICKDATA'] | //ul[@class='sellListContent']/li[@class='clear LOGVIEWDATA LOGCLICKDATA']")
        for dd in dd_list:
            house_dict['region'] = dd.xpath(".//a[@data-el='region']/text()")
            house_dict['totalPrice'] = dd.xpath(".//div[@class='totalPrice']/span//text()")
            house_dict['unitPrice'] = dd.xpath(".//div[@class='unitPrice']/span//text()")
            print(house_dict)

    def main(self):
        self.get_page(url)


if __name__ == '__main__':
    start = time.time()
    spider = MoaoYan_Spider()
    spider.main()
    end = time.time()
