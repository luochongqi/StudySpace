#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/28 15:36 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_03.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
while True:
    url = r.brpop('localhost:url', 6)
    print(url)
    if url:
        print("正在抓取中：" + url.decode())
    else:
        print("抓取结束")
        break
