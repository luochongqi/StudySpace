#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/4/17 21:23 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : IFCM_true.py  //文件名
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

    def fit(self, X, prev_centroids=None, prev_membership=None):
        n_samples, n_features = X.shape

        if prev_membership is None:
            # 初始化隶属度矩阵
            membership = self.initialize_membership(n_samples, self.k)
        else:
            # 使用上一次的隶属度矩阵
            membership = prev_membership

        if prev_centroids is None:
            # 初始化聚类中心
            kmeans = KMeans(n_clusters=self.k)
            kmeans.fit(X)
            centroids = kmeans.cluster_centers_
        else:
            # 使用上一次的聚类中心
            centroids = prev_centroids

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

        return centroids, membership


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


# 生成模拟数据流
def generate_data_stream(n_samples, n_features, batch_size=10):
    for _ in range(n_samples // batch_size):
        X_batch = np.random.rand(batch_size, n_features)
        yield X_batch


# 聚类并可视化结果
ifcm = IFCM(k=3)

prev_centroids = None
prev_membership = None

for X_batch in generate_data_stream(n_samples=150, n_features=4, batch_size=10):
    centroids, membership = ifcm.fit(X_batch, prev_centroids, prev_membership)
    prev_centroids = centroids
    prev_membership = membership

    # 输出聚类结果
    labels = np.argmax(membership, axis=1)
    print("Cluster labels:")
    print(labels)

# 最终可视化结果
X = np.random.rand(150, 4)  # 生成150个样本用于最终的可视化
centroids, membership = ifcm.fit(X, prev_centroids, prev_membership)
plot_clusters(X, np.argmax(membership, axis=1))
