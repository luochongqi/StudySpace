#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/1 8:35 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_04_05.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE

# 字典推导式


list01 = ['LHY', 'HHUU', 'AS']
dic = {item: len(item) for item in list01}
for key, value in dic.items():
    print(f"{key}：{value}")