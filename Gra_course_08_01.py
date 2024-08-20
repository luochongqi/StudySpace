#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/28 15:22 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.lpush('tedu:python', 'socket', 'pythonweb')
r.rpush('tedu:python', 'spiderman')
r.rpop('tedu:python')
r.lpop('tedu:python')
r.rpush('tedu:python', 'a', 'b', 'c')
index_2 = r.lindex('tedu:python', 2)
print(index_2)
print(index_2.decode())
r.lrem('tedu:python', 1, index_2.decode())
r.ltrim('tedu:python', 0, 1)
