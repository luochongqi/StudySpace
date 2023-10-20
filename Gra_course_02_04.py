#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/18 9:09 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_02_04.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = int(input("Enter a year: "))

if is_leap(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
'''

year = int(input("请输入年份："))
print(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))
