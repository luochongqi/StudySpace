#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/28 16:01 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_08_04.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.setbit('user1', 1, 1)
r.setbit('user1', 4, 1)

r.setbit('user2', 99, 1)
r.setbit('user2', 199, 1)

for i in range(0, 365, 2):
    r.setbit('user3', i, 1)

for i in range(0, 365, 3):
    r.setbit('user4', i, 1)

user_list = r.keys('user*')
print(user_list)
active_user = []
noactive_user = []
for item in user_list:
    login_count = r.bitcount(item)
    if login_count >= 100:
        active_user.append((item, login_count))
    else:
        noactive_user.append((item, login_count))
print(active_user)
print(noactive_user)
for item in active_user:
    print("活跃的用户是： %s    活跃次数是：%s" % (item[0].decode(), item[1]))
for item in noactive_user:
    print("非活跃的用户是： %s    活跃次数是：%s" % (item[0].decode(), item[1]))
