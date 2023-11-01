#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/31 16:11 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_04_03.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
dic01 = {1: '第一季度有1,2,3月',
         2: '第二季度有4,5,6月',
         3: '第三季度有7,8,9月',
         4: '第四季度有10,11,12月'
         }
season = int(input("输入你想要获得的季度信息："))
if dic01.get(season) is not None:
    print(dic01[season])
else:
    print("输入有误")
