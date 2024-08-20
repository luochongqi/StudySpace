#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/3/28 21:53 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : KNN.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
# 导入所需库
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

matplotlib.use('TkAgg')

# 加载鸢尾花数据集
iris = load_iris()
X = iris.data
y = iris.target

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 定义KNN分类器
k_values = [1, 3, 5, 7, 9]
train_accuracy = []
test_accuracy = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)

    # 计算训练集和测试集准确率
    train_accuracy.append(accuracy_score(y_train, knn.predict(X_train)))
    test_accuracy.append(accuracy_score(y_test, knn.predict(X_test)))

# 绘制准确率曲线
plt.figure(figsize=(10, 6))
plt.plot(k_values, train_accuracy, label='Train Accuracy')
plt.plot(k_values, test_accuracy, label='Test Accuracy')
plt.title('KNN Algorithm Analysis')
plt.xlabel('Number of Neighbors (k)')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
