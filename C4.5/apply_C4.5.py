# -*- coding: utf-8 -*-
__author__ = 'fff_zrx'

import numpy as np
import pandas as pd
import json


def transdata(data):
    '''
    导入数据并处理
    :param datafile:
    :return:
    '''
    data.columns = ['petal_wid', 'petal_len', 'sepal_len', 'sepal_wid', 'sepal_len1', 'sepal_len2', 'sepal_wid1']

    def trans(x, n1, n2):
        if x <= n1:
            s = 1
        elif (x > n1) & (x <= n2):
            s = 2
        else:
            s = 3
        return s

    data['sepal_len'] = data['sepal_len'].apply(lambda x: trans(x, 5.4, 6.1))
    data['sepal_len1'] = data['sepal_len1'].apply(lambda x: trans(x, 5.4, 6.1))
    data['sepal_len2'] = data['sepal_len2'].apply(lambda x: trans(x, 5.4, 6.1))
    data['sepal_wid'] = data['sepal_wid'].apply(lambda x: trans(x, 2.9, 3.3))
    data['sepal_wid1'] = data['sepal_wid1'].apply(lambda x: trans(x, 2.9, 3.3))
    data['petal_len'] = data['petal_len'].apply(lambda x: trans(x, 1.9, 4.7))
    data['petal_wid'] = data['petal_wid'].apply(lambda x: trans(x, 0.8, 1.7))
    data = data.iloc[:, :].values.tolist()
    return data[0]


def grabTree(tree_file, fea_file):
    '''
    读取决策树和特征属性
    :param filename:
    :return:
    '''
    mytree = json.load(open(tree_file, 'r+'))
    featLabels = json.load(open(fea_file, 'r+'))
    return mytree, featLabels


if __name__ == '__main__':
    # 读取决策树和特征属性
    tree_file = 'mytree'
    fea_file = 'featLabels'
    myTree, featLabels = grabTree(tree_file, fea_file)
    print("决策树特征属性为：", featLabels)
    print("决策树的字典形式为：", myTree)
    testvalue = [2, 2, 1, 1, 1, 1, 1]
    testvalue = [str(value) for value in testvalue]
    # 或者输入'花瓣宽度', '花瓣长度', '花萼长度', '花萼宽度', '花萼长度', '花萼长度', '花萼宽度',再离散化
    # testvalue=[]
    # testvalue=pd.DataFrame([testvalue])
    # testvalue=transdata(testvalue)
    for i in range(0, len(featLabels)):
        try:
            myTree = myTree[featLabels[i]][testvalue[i]]
        except:
            print("这个测试结果是：")
            print(myTree)
            break
