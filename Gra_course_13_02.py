#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/12/19 15:49 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_12_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

x = np.linspace(0, 8 * np.pi, 1000)
sinx = np.sin(x)
cosx = np.cos(x/2) / 2

plt.figure('Fill', facecolor='lightgray')
plt.title('Fill', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.grid(linestyle=':')
plt.plot(x, sinx, color='dodgerblue', label='sin(x)')
plt.plot(x, cosx, color='orangered', label='cos(x/2)/2')

plt.fill_between(x, sinx, cosx, sinx < conx, color='dodgerblue', alpha=0.5)
plt.fill_between(x, sinx, cosx, sinx > conx, color='orangered', alpha=0.5)

plt.legend()
plt.show()
