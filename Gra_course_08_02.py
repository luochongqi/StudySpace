#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/28 15:36 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_02.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis
import time
import random

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
for i in range(1, 10):
    url = 'index-' + i + '.html'
    r.lpush('localohost:url', url)
    time.sleep(random.randint(3, 5))
