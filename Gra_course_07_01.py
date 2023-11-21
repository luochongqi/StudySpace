#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/11/21 15:05 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Gra_course_07_01.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import xlwings as xw
import time
import sys
import os
import threading
import traceback
from tqdm import tqdm
import keyboard
import pywintypes
from win32com.client import DispatchEx
from xlwings._xlwindows import COMRetryObjectWrapper

# 全局数据，全部为空
app = None
wb = None
sht1 = None  # sheet0，源数据sheet
sht2 = None  # sheet1，输出数据sheet
filename = ''

# 输出文字样式变量
head_color_font_green = '\033[1;32;40m'  # 绿色高亮
head_color_font_red = '\033[1;33;40m'  # 红色高亮
tail_color_font = '\033[0m'


# 获得正确运行的excel程序
def get_excel_app():
    try:
        in_app = xw.App(visible=False, add_book=False)  # 默认使用
        return in_app
    except pywintypes.com_error:
        try:
            _xl = COMRetryObjectWrapper(DispatchEx("ket.Application"))
            impl = xw._xlwindows.App(visible=False, add_book=False, xl=_xl)
            in_app = xw.App(visible=False, add_book=False, impl=impl)
            return in_app
        except pywintypes.com_error:
            return None


# 提示消息的输出函数
def message(statement):
    print(head_color_font_red + statement + tail_color_font)


# 程序正常退出函数
def procedure_exit(statement, error):
    message(statement)
    time.sleep(5)
    if error == 1:
        app.kill()
    sys.exit()


# 数据输出函数
def output_data(data_list):
    for data in data_list:
        print(data)


# 写入新的数据
def write_data(row_num):
    global sht2
    if sht2 is None:
        sht2 = wb.sheets.add(name='已处理', after=sht1)
    sht2.range('A1').value = ['内蒙古高校名单']  # 写标题
    sht2.range('A1:G1').merge()  # 合并单元格
    title_rng = sht2.range('A1:G1')  # 获取标题区域
    title_rng.api.HorizontalAlignment = -4108  # 水平居中
    title_rng.api.VerticalAlignment = -4108  # 垂直居中
    title_rng.row_height = 25  # 设置行高
    sht2['A1:G1'].font.bold = True  # 设置标题字体为粗体
    sht2['A1:G1'].font.color = (0, 0, 255)  # 设置标题字体为蓝色
    sht1.range('A1:G1').copy(sht2.range('A2:G2'))  # 复制抬头
    filter_string = f'C2:C{row_num}'
    filter_rng = sht1.range(filter_string)
    count = 0
    bit = 2
    start = 2
    for v in filter_rng.value:
        if v == '内蒙古':
            count += 1
            s_copy_string = f'A{bit}:G{bit}'
            d_copy_string = f'A{start + count}:G{start + count}'
            sht1.range(s_copy_string).copy(sht2.range(d_copy_string))
        bit += 1


# 打开文件函数
def open_file():
    # 申明全局变量
    global app, wb, filename, sht1, sht2

    # 打开excel程序，默认设置：程序可见，只打开不新建工作簿，屏幕更新关闭
    app = get_excel_app()
    if not app:
        procedure_exit(f"打开excel的程序遇到问题，程序即将退出！", APP_ERROR)
    app.display_alerts = False
    app.screen_updating = False

    # 获取sheet1
    print("导入文件要求如下：")
    print("1、文件为excel文件，后缀名为.xls；")
    print("2、excel文件必须和该程序处于同一个目录下，且需要输入完整的文件名（例如：xxx.xlsx；注意：不用带路径）；\n\n")
    while True:
        filename = input("请输入需要处理的完整文件名：").strip()
        f_split_list = filename.split('.')
        if len(f_split_list) < 2 or f_split_list[1] != 'xls':
            message(f"文件名后缀发生错误，请检查！")
            press_key = input(f"\n输入'q'退出程序！输入其他任意信息程序继续！\n")
            if press_key == 'q':
                procedure_exit(f'即将退出程序！', APP_ERROR)
            else:
                continue
        elif not os.path.exists(filename):
            message(f"该文件不存在！")
            press_key = input(f"\n输入'q'退出程序！输入其他任意信息程序继续！\n")
            if press_key == 'q':
                procedure_exit(f'即将退出程序！', APP_ERROR)
            else:
                continue
        else:
            break

    wb = app.books.open(filename)
    sht1 = xw.sheets.active
    rng = sht1.range('A1').expand('table')
    row_num = rng.rows.count
    output_data(rng.value)
    write_data(row_num)


# 关闭文件函数
def close_file(f_name):
    # 使源sheet为active的
    sht1.activate()
    # 保存
    wb.save('(已处理)' + f_name)
    # 退出excel
    app.kill()


open_file()
close_file(filename)
