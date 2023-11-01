#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/25 8:37 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : function_chr_study.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
while True:
    uni_str = input("请输入你想要转换的Unicode码：")
    if uni_str == ' ':
        print("程序已结束")
        break
    uni_int = int(uni_str)
    if uni_int == 160:
        print("程序已结束")
        break
    uni_to_str = chr(uni_int)
    print(uni_to_str)

