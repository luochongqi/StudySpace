#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/29 8:17 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_05.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.zadd('ranking', {'song1': 1, 'song2': 1, 'song3': 3, 'song4': 2})
r.zadd('ranking', {'song5': 3, 'song6': 1, 'song7': 3})
r.zadd('ranking', {'song8': 1, 'song9': 1, 'song10': 3})
r.zincrby('ranking', 50, 'song3')
r.zincrby('ranking', 60, 'song5')
r.zincrby('ranking', 80, 'song7')
result = r.zrange('ranking', 0, -1, withscores=True)
print(result)
rlist = r.zrevrange('ranking', 0, 2, withscores=True)
print(rlist)
i = 1
for r in rlist:
    print("第%d名：%s，播放量：%d" % (i, r[0].decode(), r[1]))
    i += 1
