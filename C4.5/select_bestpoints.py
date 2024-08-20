# -*- coding: utf-8 -*-
__author__ = 'fff_zrx'
import pandas as pd


def calculate_gini(data,fea,n1,n2):
    '''
    对连续变量fea根据n1,n2分成3类，计算Gini Index
    :param data: dataframe
    :param fea: 连续变量
    :param n1: 分界点1
    :param n2: 分界点2
    :return:
    '''

    s=data.shape[0]
    def trans(x):
        if x<=n1:
            s=1
        elif (x>n1)&(x<=n2):
            s=2
        else:
            s=3
        return s
    data['fealabel']=data[fea].apply(lambda x : trans(x))
    #数据集1中gini指数
    temp=data[data['fealabel']==1].groupby(['label']).agg({fea:'count'})
    temp=temp[fea].tolist()
    s1=sum(temp)
    temp=[pow(value/s1,2) for value in temp]
    result1=1-sum(temp)
    #数据集2中gini指数
    temp=data[data['fealabel']==2].groupby(['label']).agg({fea:'count'})
    temp=temp[fea].tolist()
    s2=sum(temp)
    temp=[ pow(value/s2,2) for value in temp]
    result2=1-sum(temp)
    #数据集3中gini指数
    temp=data[data['fealabel']==3].groupby(['label']).agg({fea:'count'})
    temp=temp[fea].tolist()
    s3=sum(temp)
    temp=[ pow(value/s3,2) for value in temp]
    result3=1-sum(temp)
    result=(s1/s)*result1+(s2/s)*result2+(s3/s)*result3
    return result


if __name__=='__main__':
    data = pd.read_table('./iris.txt',sep=',',header=None)
    data.columns=['sepal_len','sepal_wid','petal_len','petal_wid','label']
    data['sepal_len']=data['sepal_len'].astype(float)
    fealist=['sepal_len','sepal_wid','petal_len','petal_wid']
    fea=fealist[3]  #选定特征列
    data1=data.sort_values(by=[fea])
    data1=data1[fea].tolist()
    n_list=[]
    for i in range(0,len(data1)-1):
        n=(data1[i]+data1[i+1])*0.5
        n_list.append(n)
    final_list=[]
    [final_list.append(i) for i in n_list if not i in final_list]
    print(final_list)
    bestgini=0.68
    for i in range(0,len(final_list)):
        for j in range(i+1,len(final_list)):
            n1=final_list[i]
            n2=final_list[j]
            gini=calculate_gini(data,fea,n1,n2)
            print("n1,n2:",n1,n2)
            print('gini:',gini)
            print("-----------------")
            if gini<bestgini:
                bestgini=gini
                bestn=[n1,n2]
    print('------result------')
    print('对于特征%s：'%fea)
    print('最优分界点为：',bestn)
    print('基尼指数为：',bestgini)
