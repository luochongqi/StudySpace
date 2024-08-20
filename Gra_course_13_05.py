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

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, 1000), np.linspace(-3, 3, 1000))
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
plt.figure('Contour', facecolor='lightgray')
plt.title('Contour', fontsize=16)
plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.tick_params(labelsize=10)
cntr = plt.contour(x, y, z, 8, colors='black', linewidths=0.5)
plt.clabel(cntr, inline_spacing=1, fmt='%.1f', fontsize=10)
plt.contourf(x, y, z, 8, alpha=0.75, cmap='jet')

plt.show()
