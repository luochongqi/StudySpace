#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/31 14:47 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_04_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
names = []
while True:
    name = input("请输入学生姓名：")
    if name.lower() == 'esc':
        print("程序即将退出")
        break
    if name not in names:
        print("加入成功")
        names.append(name)
    else:
        print("名字重复，加入失败")

for n in names:
    print(n)


