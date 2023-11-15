#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/14 15:55 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_06_04.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Person:
    def __init__(self, name):
        self.name = name

    def go_to(self, vehicle, str_pos):
        if not isinstance(vehicle, Vehicle):
            print("vehicle is not a Vehicle")
            return
        vehicle.transport(str_pos)


class Vehicle:
    def transport(self, str_pos):
        raise NotImplementedError()


class Car(Vehicle):
    def transport(self, str_pos):
        print("car is transporting to %s" % str_pos)


class Airport(Vehicle):
    def transport(self, str_pos):
        print("airport is transporting to %s" % str_pos)


p01 = Person("老张")
p01.go_to(Car(), "东北")
p01.go_to(Airport(), "东北")
p01.go_to("sssss", "东北")
