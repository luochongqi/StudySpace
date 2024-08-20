#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/22 9:42 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_07_02.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
print(r.keys('*'))
