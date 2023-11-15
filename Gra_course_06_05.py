#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/15 8:14 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_06_05.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import math


class Diagram:
    def __init__(self):
        pass

    def calc_area(self, diagram, **kwargs):
        if not isinstance(diagram, Diagram):
            print("输入的不是图形")
            return
        print(f"{diagram} {diagram.area()}")


class Circle(Diagram):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "该圆形的面积是："

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Diagram):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return "该矩形的面积是："

    def area(self):
        return self.length * self.width


class Triangle(Diagram):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def __str__(self):
        return "该三角形的面积是："

    def area(self):
        return 0.5 * self.base * self.height


d01 = Diagram()
d01.calc_area(Circle(10))
d01.calc_area(Rectangle(10, 20))
d01.calc_area(Triangle(10, 20))
