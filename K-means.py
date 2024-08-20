#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/3/28 21:26 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : K-means.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib


# 加载鸢尾花数据集
from sklearn.datasets import load_iris

matplotlib.use('TkAgg')

iris = load_iris()
data = iris.data  # 特征数据
target = iris.target  # 目标标签


# 1. 初始化K个中心点
def initialize_centroids(data, k):
    centers = data[np.random.choice(range(len(data)), k, replace=False)]
    return centers


# 2. 计算每个样本与中心点的欧式距离
def compute_distances(data, centers):
    dists = np.linalg.norm(data[:, :, np.newaxis] - centers.T, axis=1)
    return dists


# 3. 将每个样本分配到距离最近的簇
def assign_clusters(data, centers):
    distances = compute_distances(data, centers)
    labels = np.argmin(distances, axis=1)
    return labels


# 4. 更新簇的中心点
def update_centers(data, labels, k):
    new_centers = np.array([data[labels == i].mean(axis=0) for i in range(k)])
    return new_centers


# 5. 迭代直至簇中心不再改变或小于指定阈值
def kmeans(data, k, max_iters=100, tol=1e-4):
    centers = initialize_centroids(data, k)
    for _ in range(max_iters):
        labels = assign_clusters(data, centers)
        new_centers = update_centers(data, labels, k)
        if np.linalg.norm(new_centers - centers) < tol:
            break
        centers = new_centers
    return labels, centers


# 调用K-means算法
k = 3  # 假设你想分成3个簇
labels, centers = kmeans(data, k)

# 打印簇的标签和中心点
print("Cluster labels:", labels)
print("Cluster centers:", centers)

# 绘制K-means聚类结果
fig, ax = plt.subplots(figsize=(8, 6))

# 只取前两个特征进行可视化（可根据实际数据调整）
visualize_features = [0, 1]
data_subset = data[:, visualize_features]

# 绘制散点图
for i in range(k):
    cluster_data = data_subset[labels == i]
    ax.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f"Cluster {i + 1}")

# 绘制簇中心点
ax.scatter(centers[:, visualize_features[0]], centers[:, visualize_features[1]], marker="X", color="black", s=100,
           label="Centers")

# 设置图例
ax.legend()

# 设置坐标轴标签
ax.set_xlabel(iris.feature_names[visualize_features[0]])
ax.set_ylabel(iris.feature_names[visualize_features[1]])

plt.title("K-means Clustering on Iris Dataset")
plt.show()
