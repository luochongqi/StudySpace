#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/14 14:31 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_06_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Person:
    def __init__(self):
        self.__name = ""
        self.__total_money = 0
        self.__skills = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, str_name):
        self.__name = str_name

    @property
    def skills(self):
        return self.__skills[:]

    @skills.setter
    def skills(self, str_skills):
        self.__skills.append(str_skills)

    @property
    def total_money(self):
        return self.__total_money

    def teach(self, person_another, str_skills):
        person_another.skills = str_skills
        print(self.name + " 教 " + person_another.name + " " + str_skills)

    def work(self, money):
        self.__total_money += money
        print(self.name + " 工作挣了 " + str(self.__total_money) + " 元 ")


zs = Person()
ls = Person()
zs.name = "张三"
ls.name = "李四"
zs.teach(ls, "Python")
ls.teach(zs, "游戏")
print(zs.skills)
zs.work(8000)
ls.work(10000)
zs.work(3000)
