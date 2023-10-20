#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/18 8:50 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_02_03.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
# 通过使用split()和map()函数实现多个同类型数据的输入
name, gender, age, record = map(str, input("请依次输入姓名、性别、年龄和成绩：").split())
age = int(age)
record = float(record)
print("我的姓名是：%s，年龄是：%d，性别是：%s，成绩是：%.1f。" % (name, age, gender, record))
print(f"我的姓名是：{name}，年龄是：{gender}，性别是：{age}，成绩是：{record}。")
