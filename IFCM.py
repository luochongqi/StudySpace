#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/4/17 19:15 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : IFCM.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import matplotlib

matplotlib.use('TkAgg')

# 导入鸢尾花数据集
iris = datasets.load_iris()
X = iris.data
y = iris.target


class IFCM:
    def __init__(self, k, m=2, epsilon=0.01, max_iter=100):
        self.k = k
        self.m = m
        self.epsilon = epsilon
        self.max_iter = max_iter

    def initialize_membership(self, n_samples, n_clusters):
        membership = np.random.rand(n_samples, n_clusters)
        membership /= np.sum(membership, axis=1)[:, np.newaxis]
        return membership

    def update_membership(self, X, centroids):
        dist = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        membership = 1 / (dist ** (2 / (self.m - 1)))
        membership /= np.sum(membership, axis=1)[:, np.newaxis]
        return membership

    def fit(self, X):
        n_samples, n_features = X.shape
        # 初始化隶属度矩阵
        membership = self.initialize_membership(n_samples, self.k)

        # 初始化聚类中心
        kmeans = KMeans(n_clusters=self.k)
        kmeans.fit(X)
        centroids = kmeans.cluster_centers_

        for _ in range(self.max_iter):
            prev_centroids = centroids.copy()

            # 更新聚类中心
            centroids = np.dot(membership.T, X) / np.sum(membership, axis=0)[:, np.newaxis]

            # 更新隶属度矩阵
            membership = self.update_membership(X, centroids)

            # 判断是否收敛
            diff = np.linalg.norm(centroids - prev_centroids)
            if diff < self.epsilon:
                break

        self.centroids_ = centroids
        self.labels_ = np.argmax(membership, axis=1)
        self.membership_ = membership  # 保存隶属度矩阵


# 使用PCA进行降维可视化
def plot_clusters(X, labels):
    pca = PCA(n_components=2)
    X_pca = pca.fit_transform(X)
    plt.figure(figsize=(8, 6))
    plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=50)
    plt.title('IFCM Clustering')
    plt.xlabel('PCA Component 1')
    plt.ylabel('PCA Component 2')
    plt.colorbar(label='Cluster')
    plt.show()


# 创建IFCM模型并拟合数据
ifcm = IFCM(k=3)
ifcm.fit(X)

# 输出各样本的隶属度
np.set_printoptions(suppress=True)  # 禁用科学计数法
membership_percentage = (ifcm.membership_ * 100).round(2)
print("Membership matrix shape:", membership_percentage.shape)
print("Membership matrix (in percentage):")
print(membership_percentage)

# 聚类并可视化结果
plot_clusters(X, ifcm.labels_)
