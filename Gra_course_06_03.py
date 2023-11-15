#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/14 15:16 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_06_03.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Person:
    def __init__(self, name, money=0):
        self.name = name
        self.total_money = money


class Bank:
    def __init__(self, name, money):
        self.name = name
        self.total_money = money

    def draw_money(self, person, value):
        if self.total_money >= value:
            self.total_money -= value
            person.total_money += value
            print(person.name + " 取走了" + str(value) + "元")
        else:
            print("余额不足")


p01 = Person("小明", 100)


