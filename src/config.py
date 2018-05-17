# -*- coding: utf-8 -*-
"""
Created on 2018/5/16

@author: Simba
"""


# 使用的设备数量
DEVICE_NUM = 100

# 物理设备源文件
DEVICE_SOURCE_FILE = r"D:\device.txt"
# 物理设备目的文件
DEVICE_DES_FILE = r"F:\output\device.txt"

# 逻辑设备源文件
LOGIC_SOURCE_FILE = r"D:\logic.txt"
# 逻辑设备目的文件
LOGIC_DES_FILE = r"F:\output\logic.txt"

# 设备组添加设备参数
ADD_LOGIC_TO_GROUP = {
    "url": "http://140.143.217.34:9876/api/devicegroup/device/add",
    "payload": {
        "LogicDeviceID":"",
        "GroupID":"1fcf7bed-41ef-4dd4-a9ad-2b500e9b3178"
    },
    "headers": {
        'Content-Type': "application/json",
        'access_key': "AK-StressTest",
        'secret_key': "SK-StressTest",
        'authkey': "dp-auth-v0",
        'Cache-Control': "no-cache"
    }
}

# 设备组添加设备错误文件
ADD_LOGIC_TO_GROUP_ERRFILE = r"F:\output\addlogictogroup.txt"

# 设备绑定错误文件
DEVICE_BUND_ERRFILE = r"F:\output\bunderrfile.txt"

# 绑定设备参数
BUND_LOGIC_DEVICE = {
    "url": "http://140.143.217.34:9876/api/device/bind",
    "payload": {
        "DeviceType": "nemo",
        "LogicDeviceID": "",
        "DeviceID": "",
        "DeviceName": "",
        "Comment": "StressTest"
    },
    "headers": {
        'Content-Type': "application/json",
        'secret_key': "SK-StressTest",
        'access_key': "AK-StressTest",
        'authkey': "dp-auth-v0",
        'Cache-Control': "no-cache"
    }
}