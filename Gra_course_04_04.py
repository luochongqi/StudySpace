#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/1 8:21 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_04_04.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
s_input = input("请输入一串英文字母：")
l_input = list(s_input)
dic = {}
for i in l_input:
    if i not in dic.keys():
        dic[i] = 1
    else:
        dic[i] += 1

sorted(dic)
for key, value in dic.items():
    print(f"{key}：{value}")
