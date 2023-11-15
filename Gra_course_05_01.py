#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/7 15:36 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_05_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Student:
    """
    学生类
    """

    def __init__(self, name='', sex='', age=0, grade=0):
        self.name = name
        self.sex = sex
        self.age = age
        self.grade = grade

    def print_self(self):
        print(self.name, self.sex, self.age, self.grade)


def search_name(stu_list, name):
    temp_stu = Student()
    for item in stu_list:
        if name == item.name:
            return item
    return temp_stu


def search_sex(stu_list, sex):
    temp_stu_list = []
    for item in stu_list:
        if sex == item.sex:
            temp_stu_list.append(item)
    return temp_stu_list


def search_age_grade(stu_list):
    temp_stu_list = []
    for item in stu_list:
        if item.age > 20 and item.grade > 60:
            temp_stu_list.append(item)
    return temp_stu_list


list_str = [
    Student("ZS", "男", 25, 59),
    Student("LS", "女", 28, 88),
    Student("Ww", "男", 40, 96),
    Student("Zi", "女", 18, 75)
]

temp01 = search_name(list_str, "ZS")
temp01.print_self()

temp02_s = search_sex(list_str, "男")
for item in temp02_s:
    item.print_self()

temp03_s = search_age_grade(list_str)
for item in temp03_s:
    item.print_self()

