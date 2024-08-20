#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/29 8:17 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_05.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.zadd('mobile_day1', {'huawei': 5000, 'oppo': 4000, 'iphone': 3800})
r.zadd('mobile_day2', {'huawei': 8000, 'oppo': 4300, 'iphone': 3200})
r.zadd('mobile_day3', {'huawei': 6000, 'oppo': 4500, 'iphone': 3100})
r.zunionstore('mobile_all', ('mobile_day1', 'mobile_day2', 'mobile_day3'), aggregate='max')
rlist = r.zrevrange('mobile_all', 0, -1, withscores=True)
i = 1
for r in rlist:
    print("第%d名：%s，销售量：%d" % (i, r[0].decode(), r[1]))
    i += 1

