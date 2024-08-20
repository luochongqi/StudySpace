# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 17:52:46 2023

@author: LHY
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier

# 导入数据集
# 西瓜数据
#X 瓜蒂：脱落（0）、未脱落（1）
#X 形状：圆（0）、尖（1）
#X 颜色：深绿（0）、浅绿（1）、青色（2）
#y 状态：生（0）、熟（1）
X_train = np.array([[0, 0, 0], [1, 1, 1],
                    [1, 0, 1], [0, 1, 2],
                    [0, 0, 1], [1, 1, 2],
                    [0, 1, 0], [1, 0, 2],
                    [0, 1, 0], [1, 0, 0]])
y_train = np.array([1, 0, 0, 1, 1, 0, 1, 1, 0, 1])

# ID3分类树，信息增益特征选择
dtree = DecisionTreeClassifier(criterion='entropy')
# 训练
dtree.fit(X_train, y_train)
# 测试
X_test = np.array([[0, 0, 2]])
pred_y = dtree.predict(X_test)
print(pred_y)

# 决策树可视化
import graphviz
from sklearn.tree import export_graphviz
dot_data = export_graphviz(dtree,
                           feature_names=['Gua Di', 'Xing Zhuang', 'Yan Se'],
                           filled=True,
                           rounded=True
                           )
graph = graphviz.Source(dot_data)
graph.view()
