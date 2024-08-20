#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time    : 2024/5/13 9:33 //这里时创建该文件的时间
# @Author  : Luo HaoYe  //这里写自己的名字
# @File    : Net_Select.py  //文件名
# @ProjectName: StudySpace //项目名称
# @Software: PyCharm //IDE
class Model_Select:
    def __init__(self):
        self.model = None
        self.state = ''

    def set_model(self, model_instance, state_info):
        """
        设置类变量中的model和state。

        参数:
        - model_instance: 一个模型实例，如torch.nn.Module的实例。
        - state_info: 与模型状态相关的信息，这个可以根据实际需求灵活定义，例如模型的状态字典或是其他描述状态的信息。
        """
        self.model = model_instance
        self.state = state_info

    def get_model(self):
        """
        返回类变量中存储的模型。

        返回:
        - model: 当前设置的模型实例。
        """
        if self.model is not None:
            return self.model
        else:
            raise ValueError("Model has not been set yet.")

fold = 2
print(f"zuihaode moxing {fold}")

