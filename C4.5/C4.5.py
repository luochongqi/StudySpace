#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/3/31 20:56 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : C4.5.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE

from math import log
import operator
import pandas as pd
import treePlotter
import json
import matplotlib

matplotlib.use('TKAgg')


def dataentropy(data, feat=-1):
    '''
    计算数据的熵(entropy)
    :param data:
    :param feat:
    :return:
    '''
    lendata = len(data)  # 数据条数
    labelCounts = {}  # 数据中不同类别的条数
    for featVec in data:
        category = featVec[feat]  # 默认取每行数据的最后一个作为类别
        if category not in labelCounts.keys():
            labelCounts[category] = 0
        labelCounts[category] += 1  # 统计有多少个类以及每个类的数量
    entropy = 0
    for key in labelCounts:
        prob = float(labelCounts[key]) / lendata  # 计算单个类的熵值
        entropy -= prob * log(prob, 2)  # 累加每个类的熵值
    return entropy


def splitData(data, i, value):
    '''
    按某个特征value分类后的数据
    :param data:
    :param i:
    :param value:
    :return:
    '''
    splitData = []
    for featVec in data:
        if featVec[i] == value:
            rfv = featVec[:i]
            rfv.extend(featVec[i + 1:])
            splitData.append(rfv)
    return splitData


def BestSplit(data):
    '''
    根据信息增益率选择最优分类特征
    '''
    num_fea = len(data[0]) - 1  # 计算特征数量
    baseEnt = dataentropy(data, -1)  # 计算初始熵
    bestGainRate = 0
    bestFeat = -1
    for i in range(num_fea):
        featList = [rowdata[i] for rowdata in data]
        uniqueVals = set(featList)
        newEnt = 0
        for value in uniqueVals:
            subData = splitData(data, i, value)  # 获取按照特征value分类后的数据
            prob = len(subData) / float(len(data))
            newEnt += prob * dataentropy(subData, -1)  # 按特征分类后计算得到的熵
        info = baseEnt - newEnt  # 即信息增益
        splitinfo = dataentropy(data, i)  # 按某特征计算熵值，也即是splitonfo
        if splitinfo == 0:  # 若某特征值都相同，即splitonfo为0，对分类无意义则跳过该特征
            break
        GainRate = info / splitinfo  # 计算信息增益率
        if (GainRate > bestGainRate):
            bestGainRate = GainRate
            bestFeat = i  # 返回最佳分类特征
    return bestFeat


def majorityCnt(classList):
    '''
    按分类后类别数量排序，取数量较大的
    '''
    c_count = {}
    for i in classList:
        if i not in c_count.keys():
            c_count[i] = 0
        c_count[i] += 1
    ClassCount = sorted(c_count.items(), key=operator.itemgetter(1), reverse=True)  # 按照统计量降序排序
    return ClassCount[0][0]


def createTree(data, labels, featLabels):
    '''
    建立决策树
    '''
    classList = [rowdata[-1] for rowdata in data]  # 取每一行的最后一列，分类结果（1/0）
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(data[0]) == 1 or len(labels) == 0:
        return majorityCnt(classList)
    bestFeat = BestSplit(data)  # 根据信息增益选择最优特征
    if bestFeat == -1:
        return majorityCnt(classList)
    bestLab = labels[bestFeat]
    featLabels.append(bestLab)
    myTree = {bestLab: {}}  # 分类结果以字典形式保存
    del (labels[bestFeat])
    featValues = [rowdata[bestFeat] for rowdata in data]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestLab][value] = createTree(splitData(data, bestFeat, value), subLabels, featLabels)
    return myTree


def storeTree(inputTree, filename):
    '''
    保存决策树
    :param inputTree:
    :param filename:
    :return:
    '''
    json.dump(inputTree, open(filename, 'w+'))


def importdata(datafile):
    '''
    导入数据并处理
    :param datafile:
    :return:
    '''
    data = pd.read_table(datafile, sep=',', header=None)
    data.columns = ['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'label']

    def trans(x, n1, n2):
        if x <= n1:
            s = 1
        elif (x > n1) & (x <= n2):
            s = 2
        else:
            s = 3
        return s

    data['sepal_len'] = data['sepal_len'].apply(lambda x: trans(x, 5.4, 6.1))
    data['sepal_wid'] = data['sepal_wid'].apply(lambda x: trans(x, 2.9, 3.3))
    data['petal_len'] = data['petal_len'].apply(lambda x: trans(x, 1.9, 4.7))
    data['petal_wid'] = data['petal_wid'].apply(lambda x: trans(x, 0.8, 1.7))
    data = data.iloc[:, :].values.tolist()
    labels = ["花萼长度", "花萼宽度", "花瓣长度", "花瓣宽度"]
    return data, labels


if __name__ == '__main__':
    datafile = r'./iris.txt'  # 文件路径
    data, labels = importdata(datafile)  # 导入数据
    featLabels = []
    mytree = createTree(data, labels, featLabels)
    print(mytree)  # 输出决策树模型结果
    # 保存决策树和特征属性名
    storeTree(mytree, 'mytree')
    # 保存特征列表
    json.dump(featLabels, open('featLabels', 'w+'))
    # 可视化决策树
    treePlotter.createPlot(mytree)
