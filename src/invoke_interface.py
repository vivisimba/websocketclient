# -*- coding: utf-8 -*-
"""
Created on 2018/5/16

@author: Simba
"""


import label_used_logic
import get_device
import config as CONFIG
import requests
import json
import pprint
import time


def standardDic(dic):
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dic)


# 设备组添加逻辑设备
def addLogicToGroup(logicIdList, addlogictogroupPath):
    errDic = {}
    num = 1
    for i in logicIdList:
        payloadDic = CONFIG.ADD_LOGIC_TO_GROUP["payload"]
        payloadDic["LogicDeviceID"] = i
        response = requests.request(
            "POST", CONFIG.ADD_LOGIC_TO_GROUP["url"],
            data=json.dumps(payloadDic),
            headers=CONFIG.ADD_LOGIC_TO_GROUP["headers"])
        resDic =  response.json()
        if resDic["Code"] != 1:
            errDic[i] = resDic
        else:
            print "Add %s to %s success. %d" % (i, payloadDic["GroupID"], num)
            num = num + 1
    with open(addlogictogroupPath, "w") as errFile:
        for k, v in errDic.items():
            errFile.write(k + ":\n")
            errFile.write(json.dumps(v) + "\n")
            errFile.write("\n")
            errFile.write("\n")


# 绑定设备
def bundDeviceAndLogic(bundDic, bunderrfilePath):
    print "================="
    errDic = {}
    nameInt = 1
    timeStr = str(time.strftime('%Y%m%d%H%M%S', time.localtime()))
    for k, v in bundDic.items():

        nameStr = "StressTest-" + timeStr + str(nameInt)
        # 确定payload
        payloadDic = CONFIG.BUND_LOGIC_DEVICE["payload"]
        payloadDic["LogicDeviceID"] = k
        payloadDic["DeviceID"] = v
        payloadDic["DeviceName"] = nameStr

        # 调用接口
        response = requests.request(
            "POST", CONFIG.BUND_LOGIC_DEVICE["url"],
            data=json.dumps(payloadDic),
            headers=CONFIG.BUND_LOGIC_DEVICE["headers"])
        resDic = response.json()
        if resDic["Code"] != 1:
            resDic["device"] = v
            errDic[k] = resDic
        else:
            print "Bund %s to %s success. %d" % (v, k, nameInt)
        nameInt = nameInt + 1

    with open(bunderrfilePath, "w") as errFile:
        for m, n in errDic.items():
            errFile.write(m + ":\n")
            errFile.write(json.dumps(n) + "\n")
            errFile.write("\n")
            errFile.write("\n")


def run():
    # 获得逻辑设备列表和物理设备列表
    logicList = label_used_logic.label_logic()
    deviceList = get_device.getDeviceList(CONFIG.DEVICE_NUM, CONFIG.DEVICE_SOURCE_FILE, CONFIG.DEVICE_DES_FILE)

    # 获得逻辑设备和物理设备对应关系
    bundDic = dict(zip(logicList, deviceList))

    # 添加逻辑设备到设备组
    addLogicToGroup(logicList, CONFIG.ADD_LOGIC_TO_GROUP_ERRFILE)

    # 绑定逻辑设备和物理设备
    bundDeviceAndLogic(bundDic, CONFIG.DEVICE_BUND_ERRFILE)


if __name__ == '__main__':
    run()