#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/3/29 12:55 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : PCM.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import numpy as np
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')


# 定义PCM（可能性C均值）聚类算法类
class PCM:
    def __init__(self, n_clusters=3, max_iter=100, m=2, error=1e-6):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.m = m
        self.error = error

    def fit(self, X):
        n_samples, n_features = X.shape
        u = np.random.rand(n_samples, self.n_clusters)
        u /= np.sum(u, axis=1)[:, None]
        centroids = np.random.rand(self.n_clusters, n_features)

        for _ in range(self.max_iter):
            prev_u = u.copy()

            # 计算隶属度矩阵
            d = np.zeros((n_samples, self.n_clusters))
            for i in range(n_samples):
                for j in range(self.n_clusters):
                    d[i, j] = np.linalg.norm(X[i] - centroids[j])

            for i in range(n_samples):
                for j in range(self.n_clusters):
                    den = 0.0
                    for k in range(self.n_clusters):
                        den += (d[i, j] / d[i, k]) ** (2 / (self.m - 1))
                    u[i, j] = 1 / den

            # 更新聚类中心
            for j in range(self.n_clusters):
                num = 0.0
                den = 0.0
                for i in range(n_samples):
                    num += (u[i, j] ** self.m) * X[i]
                    den += u[i, j] ** self.m
                centroids[j] = num / den

            if np.linalg.norm(u - prev_u) < self.error:
                break

        self.centroids_ = centroids
        self.u_ = u

    def predict(self, X):
        n_samples, _ = X.shape
        d = np.zeros((n_samples, self.n_clusters))
        for i in range(n_samples):
            for j in range(self.n_clusters):
                d[i, j] = np.linalg.norm(X[i] - self.centroids_[j])
        return np.argmin(d, axis=1)


# 加载鸢尾花数据集并进行预处理
iris = datasets.load_iris()
X = iris.data[:, :2]  # 只取前两个特征用于可视化
y = iris.target

# 数据标准化
scaler = StandardScaler()
X = scaler.fit_transform(X)

# 划分训练集与测试集，这里仅使用训练集进行聚类和可视化
X_train, _, _, _ = train_test_split(X, y, test_size=0.5, random_state=42)  # 不划分测试集，全部数据用于训练聚类模型

# 创建PCM实例并拟合数据
pcm = PCM(n_clusters=3)
pcm.fit(X_train)

# 可视化聚类结果
colors = ['r', 'g', 'b']
for i in range(3):
    cluster_points = X_train[pcm.predict(X_train) == i]
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[i], label=f'Cluster {i + 1}')

plt.scatter(pcm.centroids_[:, 0], pcm.centroids_[:, 1], c='black', marker='x', label='Centroids')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Possibilistic C-means Clustering of Iris Data (First Two Features)')
plt.legend()
plt.show()
