#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/12/19 15:49 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_12_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

n = 300
x = np.random.normal(175, 5, n)
y = np.random.normal(65, 10, n)
plt.figure('Persons', facecolor='lightgray')
plt.title('Persons', fontsize=16)
plt.xlabel('Height', fontsize=14)
plt.ylabel('Weight', fontsize=14)
d = (x - 175) ** 2 + (y - 65) ** 2
plt.scatter(x, y, marker='o', s=60, c=d, cmap='jet', label='Persons')
plt.legend()
plt.show()
