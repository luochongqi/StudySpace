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

values = [33, 17, 21, 29, 11]

spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript', 'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered', 'limegreen', 'violet', 'gold']
plt.figure('Pie', facecolor='lightgray')
plt.title('Pie', fontsize=20)
plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, explode=spaces)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
