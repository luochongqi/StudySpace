#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2023/10/13 8:19 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : tesseractTest.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
import base64
import urllib
import requests


def main():
    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/webimage?access_token=24.bc1a51a9ac3b945519e34c8c62e0243b.2592000.1699750850.282335-40982437"

    # image 可以通过 get_file_content_as_base64("C:\fakepath\bttc_wall_test01.jpg",True) 方法获取
    image = get_file_content_as_base64("bttc_wall_test01.jpg", True)

    payload = 'image=' + f'{image}' + '&detect_language=true&detect_direction=true'

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_file_content_as_base64(path, urlencoded=False):
    """
    获取文件base64编码
    :param path: 文件路径
    :param urlencoded: 是否对结果进行urlencoded
    :return: base64编码信息
    """
    with open(path, "rb") as f:
        content = base64.b64encode(f.read()).decode("utf8")
        if urlencoded:
            content = urllib.parse.quote_plus(content)
    return content


if __name__ == '__main__':
    main()
