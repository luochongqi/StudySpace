#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/29 8:17 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_05.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.hset('userinfo', 'username', 'zhangsheng001')
r.hset('userinfo', 'username', 'zhangsheng002')
print(r.hget('userinfo', 'username'))
r.hset('userinfo', 'password', '12346')
r.hset('userinfo', 'gender', 'f')
r.hset('userinfo', 'height', '178')
all_data = r.hgetall('userinfo')
print(all_data)
r.hdel('userinfo', 'height')
all_data = r.hgetall('userinfo')
print(all_data)
key_names = r.hkeys('userinfo')
print(key_names)
key_values = r.hvals('userinfo')
print(key_values)
