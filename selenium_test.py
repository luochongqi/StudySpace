#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/3/18 22:25 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : selenium_test.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

# Chrome测试版的路径
chrome_testing_path = r"D:\StudySoftware\StartItem\browser\chrome-win64\chrome.exe"

# Chromedriver的路径
chromedriver_path = r"D:\StudySoftware\StartItem\browser\chromedriver-win64\chromedriver.exe"

# cookies路径
cookies_path = r"C:\Users\LHY\AppData\Local\Google\Chrome for Testing\User Data"

# 设置Chrome选项
options = webdriver.ChromeOptions()
options.binary_location = chrome_testing_path
options.add_experimental_option('detach', True)
options.add_experimental_option('excludeSwitches', ['enable-automation'])  # 防止网站发现我们使用模拟器
options.add_experimental_option("prefs", {
    "download.default_directory": "./downloads",  # 可选，设置下载目录
    "profile.managed_default_content_settings.javascript.enabled": True,
    "profile.default_content_setting_values.notifications": 2,  # 可选，禁止通知
    "goog:loggingPrefs": {"browser": "ALL"}
})
options.add_argument("--user-data-dir=" + cookies_path)
# 设置日志记录级别
options.add_argument('--log-level=3')  # 对应INFO级别，可尝试改为'1'（DEBUG级别）

# 设置WebDriver服务
service = Service(chromedriver_path)

# 创建Chrome WebDriver实例
driver = webdriver.Chrome(service=service, options=options)

# 打开百度网站
# driver.get("https://www.baidu.com")

# 之后可以添加更多的操作，比如搜索、导航等

# 劫持文心一言页面
driver.get('https://yiyan.baidu.com/')
sleep(25)

console_logs = driver.get_log('browser')

# # 进行标签定位
# login_btn = driver.find_element(By.CLASS_NAME, '_knWAL_G')
# login_btn.click()

# question_input = driver.find_element(By.CLASS_NAME, 'yc-editor')
# qestion_input.send_keys('我想知道什么是固态硬盘和机械硬盘')
# sleep(3)

# # 使用京东搜索小米笔记本
# driver.get('https://m.jd.com/')
# sleep(1)
# # 进行标签定位
# search_input = driver.find_element(By.ID, 'msKeyWord')
# print('找到输入框')
#
# # 向搜索框中录入关键词
# search_input.send_keys("小米笔记本")
# print('输入完检索信息')
#
# # 点击搜索按钮
# btn = driver.find_element(By.ID, 'msSearchBtn')
# btn.click()
# print('点击了搜索按钮')
# sleep(2)
#
# # 执行js，让滚轮向下滚动
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# print('正在翻滚页面')
# sleep(2)
#
# page_text = driver.page_source
#
# print(page_text)
# sleep(20)

driver.quit()
