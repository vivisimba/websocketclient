# -*- coding: utf-8 -*-
"""
Created on 2018/5/16

@author: Simba
"""


import os
import time


# person文件路径
personFileDir = unicode("F:\\压力测试相关\\05181729-05181759-250\\testMessage","utf-8")


# 获得所有文件绝对路径列表
def getFilePathList(personFileDir):
    fileNameList = os.listdir(personFileDir)
    filePathList = []
    for i in fileNameList:
        filePathList.append(os.path.join(personFileDir, i))
    return filePathList


# 获得每个文件名对应文件内容的字典，键为文件名（personid），值为文件内容的列表
def getFileDic(filePathList):
    fileDic = {}
    for i in filePathList:
        pathList = i.split("\\")
        fileName = pathList[len(pathList) - 1]
        with open(i, "r") as f:
            fileContentList = f.readlines()
        fileDic[fileName] = fileContentList
    return fileDic


filePathList = getFilePathList(personFileDir)
getFileDic(filePathList)


# 检查单个人的所有消息，是否存在超时
def checkTimeOutSingleFile(personid, fileContentList):
    timeOutDic = {}
    timeOutList = []
    allDeltaTimeList = []
    for i in fileContentList:
        lineToList = i.split(",")
        tempdeltTimeList = []
        for j in lineToList:
            if "Time" in j:
                tempdeltTimeList.append(int(j.replace('"Time":', '')))
        # print tempdeltTimeList[0]
        # upTime = float(str(tempdeltTimeList[0]))
        upTime = tempdeltTimeList[0]

        #lineToList
        messageTimeList = lineToList[0].split(" ")
        messageTimeStr = messageTimeList[0]
        # messageTime = time.mktime(time.strptime(messageTimeStr,'%Y-%m-%d-%H-%M-%S'))
        messageTime = int(messageTimeStr)

        deltaTime = messageTime - upTime

        allDeltaTimeList.append(deltaTime)
        if deltaTime >= 10000:
            timeOutList.append(deltaTime)

    timeOutDic[personid] = {
        "deltaTimeTimeoutList": timeOutList,
        "messageNum": len(fileContentList),
        "allDeltaTimeList": allDeltaTimeList
    }
    return timeOutDic


# 获得所有person的所有消息的时间差，如果有时间差大于10秒的记录，返回字典列表[{"personid": {"deltaTimeList": 超时时间差列表, "messageNum": 消息条数}}]
def checkTimeOutPerson(fileDic):
    # 所有文件的所有消息总数
    messageNumOfAllFile = 0
    # 超时消息数量
    messageNumOfTimeout = 0
    # 超时列表
    timeoutList = []
    #
    allDeltaTimeList = []

    for k, v in fileDic.items():
        singleFileTimeoutDic = checkTimeOutSingleFile(k, v)
        if len(singleFileTimeoutDic[k]["deltaTimeTimeoutList"]) != 0:
            timeoutList.append(singleFileTimeoutDic)
            messageNumOfTimeout = messageNumOfTimeout + len(singleFileTimeoutDic[k]["deltaTimeTimeoutList"])
        messageNumOfAllFile = messageNumOfAllFile + len(v)
        allDeltaTimeList = allDeltaTimeList + singleFileTimeoutDic[k]["allDeltaTimeList"]

    # 返回超时列表, 消息总数, 超时消息数, 所有消息时间差列表
    return timeoutList, messageNumOfAllFile, messageNumOfTimeout, allDeltaTimeList



def run():
    filePathList = getFilePathList(personFileDir)
    fileDic = getFileDic(filePathList)

    #获得超时列表，总消息条数，超时消息条数
    print checkTimeOutPerson(fileDic)


if __name__ == '__main__':
    run()

