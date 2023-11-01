#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/25 8:11 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Python_random_number.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import random

random_number = random.randrange(1, 100)
n = 0
while n < 5:
    n += 1
    num = int(input("请输入猜测的数字："))
    if num > random_number:
        print("大了")
    elif num < random_number:
        print("小了")
    else:
        print("对了")
        break
else:
    print(f"你已经没有机会了，正确答案是：{random_number}")
