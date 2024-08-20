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

apples = np.array([30, 12, 25, 36, 14, 21, 31, 22, 33, 19, 25, 34])
oranges = np.array([21, 32, 14, 16, 18, 24, 25, 26, 32, 30, 20, 28])

plt.figure('Bar', facecolor='lightgray')
plt.title('Bar Chart', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Volume', fontsize=14)
plt.grid(linestyle=':', axis='y')
plt.tick_params(labelsize=10)
x = np.arange(12)
plt.xticks(x, ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

plt.bar(x - 0.2, apples, 0.4, color='dodgerblue', label='Apples')
plt.bar(x + 0.2, oranges, 0.4, color='orangered', label='Oranges')

plt.legend()
plt.show()
