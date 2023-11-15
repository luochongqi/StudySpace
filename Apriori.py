#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/5 11:26 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Apriori.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE

def load_data_set():
    """
    加载数据集
    返回：数据集列表
    """
    return [['A', 'B', 'C'],
            ['A', 'C'],
            ['A', 'D'],
            ['B', 'E', 'F']]


def create_C1(data_set):
    """
    创建候选1项集
    参数：数据集
    返回：候选1项集列表
    """
    C1 = []
    for transaction in data_set:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset, C1))


def scan_D(D, Ck, min_support):
    """
    扫描数据集，生成支持度大于等于min_support的候选项集
    参数：数据集D，候选项集Ck，最小支持度min_support
    返回：支持度大于等于min_support的候选项集列表
    """
    ss_cnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not can in ss_cnt:
                    ss_cnt[can] = 1
                else:
                    ss_cnt[can] += 1
    num_items = float(len(D))
    ret_list = []
    support_data = {}
    for key in ss_cnt:
        support = ss_cnt[key] / num_items
        if support >= min_support:
            ret_list.insert(0, key)
            support_data[key] = support
    return ret_list, support_data


def apriori_gen(Lk, k):
    """
    生成候选项集Ck
    参数：频繁k-1项集列表Lk，k值
    返回：候选项集Ck列表
    """
    ret_list = []
    len_Lk = len(Lk)
    for i in range(len_Lk):
        for j in range(i + 1, len_Lk):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                ret_list.append(Lk[i] | Lk[j])
    return ret_list


def apriori(data_set, min_support=0.5):
    """
    Apriori算法主函数
    参数：数据集，最小支持度min_support
    返回：频繁项集和支持度字典
    """
    C1 = create_C1(data_set)
    D = list(map(set, data_set))
    L1, support_data = scan_D(D, C1, min_support)
    L = [L1]
    k = 2
    while len(L[k - 2]) > 0:
        Ck = apriori_gen(L[k - 2], k)
        Lk, supK = scan_D(D, Ck, min_support)
        support_data.update(supK)
        L.append(Lk)
        k += 1
    return L, support_data


def generate_rules(L, support_data, min_confidence=0.7):
    """
    生成关联规则
    参数：频繁项集列表L，支持度字典support_data，最小置信度min_confidence
    返回：关联规则列表
    """
    big_rule_list = []
    sub_set_list = [item for item in support_data]
    for i in range(0, len(L)):
        for freq_set in L[i]:
            for sub_set in sub_set_list:
                if sub_set.issubset(freq_set) and freq_set - sub_set != set():
                    conf = support_data[freq_set] / support_data[sub_set]
                    big_rule_list.append((sub_set, freq_set - sub_set, conf))
    return big_rule_list


if __name__ == "__main__":
    data_set = load_data_set()
    L, support_data = apriori(data_set, min_support=0.5)
    rules = generate_rules(L, support_data, min_confidence=0.7)
    print("频繁项集：", L)
    print("支持度字典：", support_data)
    print("关联规则：", rules)
