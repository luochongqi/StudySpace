#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/29 8:17 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_05.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.sadd('myset01', 'tom', 'rose')
r.sadd('myset01', 'linda', 'rose', 'mike')
print(r.smembers('myset01'))
print(r.scard('myset01'))
print(r.sismember('myset01', 'mike'))
print(r.spop('myset01'))
print(r.spop('myset01'))
print(r.smembers('myset01'))
r.srem('myset01', 'linda')
print(r.smembers('myset01'))
r.sadd('myset02', 'a', 'b')
r.sadd('myset03', 'c', 'b')
r.sadd('myset04', 'c', 'b', 'd')
print(r.sunion('myset02', 'myset03', 'myset04'))
print(r.sinter('myset02', 'myset03', 'myset04'))
