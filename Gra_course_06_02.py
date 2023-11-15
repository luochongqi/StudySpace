#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/14 15:06 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_06_02.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Person:
    def __init__(self, name, age, gender):
        self.name = name

    def driving(self, vehicle, place):
        print(self.name + " is driving " + vehicle + " to " + place)


class Vehicle:
    def __init__(self, name):
        self.name = name

    def travel(self, place):
        print(self.name + " is traveling to " + place)


class Place:
    def __init__(self, name):
        self.name = name

    def visit(self):
        print(self.name + " is visited")



