#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/1 8:39 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_04_06.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE


list01 = ['LHY', 'HHUU', 'AS']
list02 = ['111', '112', '113']

dic = {list01[i]: list02[i] for i in range(len(list01))}
for key, value in dic.items():
    print(f"{key}：{value}")

dic = {value: key for key, value in dic.items()}
for key, value in dic.items():
    print(f"{key}：{value}")