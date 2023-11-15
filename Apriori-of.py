#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/5 16:18 //
# @Author  : Luo HaoYe  //罗浩业
# @File    : Apriori-of.py  //Apriori算法-正式版
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import sys
import copy


def is_single(_set):
    """
    如果集合的长度是1，返回字符串；如果集合的长度>1，返回元组
    :param _set: 集合
    :return:
    """
    if len(_set) == 1:
        ls = list(_set)
        return str(ls[0])
    else:
        ts = tuple(_set)
        ts = sorted(ts)
        return tuple(ts)


def xj_max_len(_data):
    """
    获取项集最大可能的项集数
    :param _data: 原始数据
    :return:
    """
    _max = 0
    for T in _data:
        if len(T) > _max:
            _max = len(T)
    return _max


def dic_to_list(_dic):
    """
    将频繁项集字典转换为频繁项集列表
    :param _dic: 频繁项集字典
    :return:
    """
    return list(map(list, _dic.keys()))


def sort_dic(_dic):
    """
    字典排序函数，根据键值排序
    :param _dic: 原始字典
    :return: 排好序的字典
    """
    process_dic = {}
    sorted_keys = sorted(_dic.keys())
    for key in sorted_keys:
        process_dic[key] = _dic[key]
    return process_dic


def ret_fre(_data, _support):
    """
    生成频繁项集字典
    :param _data:
    :param _support:
    :return: 返回频繁项集字典
    """
    fre_dic = {}
    for key, value in _data.items():
        if value >= _support:
            fre_dic[key] = value
    fre_dic = sort_dic(fre_dic)
    return fre_dic


def initialize(_data, _support):
    """
    初始化，生成频繁一项集字典
    :param _data: 原始数据
    :param _support: 支持度阈值
    :return: 频繁一项集字典
    """
    support_dic = {}
    for T in data:
        for t in T:
            if t in support_dic:
                support_dic[t] += 1
            elif t not in support_dic:
                support_dic[t] = 1
    support_dic = ret_fre(support_dic, _support)
    support_dic = sort_dic(support_dic)
    return support_dic


def join(_data, _num):
    """
    连接操作，升项操作，从_num频繁项集升为_num+1项集
    :param _data: 第_num频繁项集列表
    :param _num: 表示是第_num频繁项集
    :return: 返回第_num+1项集列表
    """
    process_data = []
    i = 0
    for T in _data:
        for t in _data:
            if T == t:
                continue
            T_p = T.pop()
            t_p = t.pop()
            if T == t:
                T_bak = []
                T_bak.extend(t)
                T_bak.append(T_p)
                T_bak.append(t_p)
                process_data.append(T_bak)
                process_data[i].sort()
                i += 1
            T.append(T_p)
            t.append(t_p)
    return process_data, _num + 1


def middle_get_fre(_xj, _data, _support):
    """
    获得非第1项集的频繁项集字典
    :param _xj: 项集
    :param _data: 原始数据
    :param _support: 支持度阈值
    :return:
    """
    process_dic = {}
    for T in _xj:
        process_dic[tuple(T)] = 0  # list不能作为hash值使用，所以转换为元组
        for t in _data:
            T_s = set(T)
            t_s = set(t)
            if T_s <= t_s:
                process_dic[tuple(T)] += 1
    process_dic = ret_fre(process_dic, _support)
    process_dic = sort_dic(process_dic)
    return process_dic


def get_rules(_total_req, _confidence):
    """
    挖掘规则
    :param _total_req: 所有的频繁项集
    :param _confidence: 置信度阈值
    :return:
    """
    rules = []
    tr_set = [set(item) for item in _total_req.keys()]
    for T in tr_set:
        for t in tr_set:
            if T == t:
                continue
            if T >= t:
                _conf = _total_req[is_single(T)] / _total_req[is_single(t)]
                if _conf > _confidence:
                    rules.append((is_single(t), is_single(T), _conf))
    return rules


def apriori(_data, _min_sup, _min_conf):
    """
    关联规则：Apriori算法
    :param _data: 原始数据
    :param _min_sup: 支持度阈值
    :param _min_conf: 置信度阈值
    :return:
    """
    try:
        _max_len = xj_max_len(_data)
        total_req = {}
        result_req = initialize(data, _min_sup)
        total_req.update(result_req)
        num = 1
        # 获取高维的频繁项集
        while num <= _max_len:
            xj, num = join(dic_to_list(result_req), num)
            if not xj:
                break
            result_req = middle_get_fre(xj, data, _min_sup)
            total_req.update(result_req)
        print(f"频繁项集：{total_req}")
        total_rules = get_rules(total_req, confidence)
        print(f"关联规则：{total_rules}")
    except:
        return False
    return True


data = [['A', 'C', 'D'], ['B', 'C', 'E'], ['A', 'B', 'C', 'E'], ['B', 'E']]
support = 2
confidence = 0.5

if apriori(data, support, confidence):
    print("关联规则Apriori算法运行成功")
# print(apriori(data, support, confidence))
# one_req = initialize(data, 2)
# xj, num = join(dic_to_list(one_req), 1)
# two_req = middle_get_fre(xj, data, 2)
# print(list(map(list, two_req.keys())))
# tt = ('A', )
# lt = list(tt)
# print(type(lt[0]))
