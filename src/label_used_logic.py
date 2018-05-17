# -*- coding: utf-8 -*-
"""
Created on 2018/5/16

@author: Simba
"""


import get_device
import config as CONFIG


# 标记被使用的逻辑设备，并生成新的文件，并返回逻辑设备列表
def label_logic():
    useLogicList = get_device.getDeviceList(CONFIG.DEVICE_NUM, CONFIG.LOGIC_SOURCE_FILE, CONFIG.LOGIC_DES_FILE)
    return useLogicList


if __name__ == '__main__':
    label_logic()