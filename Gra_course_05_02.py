#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/8 9:15 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_05_02.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Enemy:
    def __init__(self, name):
        self.name = name
        self.__hp = 0
        self.__atk = 0
        self.__atk_speed = 0

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if not isinstance(value, int):
            raise TypeError('hp must be an integer')
        if value < 0:
            raise ValueError('hp must be greater than 0')
        self.__hp = value

    @property
    def atk(self):
        return self.__atk

    @atk.setter
    def atk(self, value):
        if not isinstance(value, int):
            raise TypeError('atk must be an integer')
        if value < 0:
            raise ValueError('atk must be greater than 0')
        self.__atk = value

    @property
    def atk_speed(self):
        return self.__atk_speed

    @atk_speed.setter
    def atk_speed(self, value):
        if not isinstance(value, int):
            raise TypeError('atk_speed must be an integer')
        if value < 0:
            raise ValueError('atk_speed must be greater than 0')
        self.__atk_speed = value


enemy1 = Enemy('goblin')
print(enemy1.hp, enemy1.atk, enemy1.atk_speed)
enemy1.hp = 100
enemy1.atk = 10
enemy1.atk_speed = 10
print(enemy1.hp, enemy1.atk, enemy1.atk_speed)
