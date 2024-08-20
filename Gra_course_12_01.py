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
        movie_dict = {}
        dd_list = parse_html.xpath('//dl[@class="board_wrapper"]/dd')
        for dd in dd_list:
            movie_dict['name'] = dd.xpath('./a/@title')[0].strip()
            movie_dict['star'] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            movie_dict['time'] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            print(movie_dict)

    def main(self):
        for offset in range(0, 31, 10):
            url = self.url.format(offset)
            print(url)
            self.get_page(url)
            time.sleep(random.randint(1, 3))


if __name__ == '__main__':
    start = time.time()
    spider = MoaoYan_Spider()
    spider.main()
    end = time.time()
