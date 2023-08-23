#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/8/22 23:02 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Spider_test01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import requests
from bs4 import BeautifulSoup

r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo, "html.parser")
print(soup.prettify())

