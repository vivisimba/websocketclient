# -*- coding: utf-8 -*-
"""
Created on 2018/5/16

@author: Simba
"""


import config as CONFIG


def getDeviceList(num, sourcePath, destinationPath):
    # 输入需要的设备数量，从文件中获取，被获取的设备行后增加*标记，标识该设备已被绑定。
    desList = []
    useList = []
    usedNum = 0
    with open(sourcePath, "r") as sourceFile:
        sourceList = sourceFile.readlines()
        for sourceLine in sourceList:
            if "*" in sourceLine:
                desList.append(sourceLine)
            else:
                if usedNum >= num:
                    desList.append(sourceLine)
                    # usedNum += 1
                else:
                    tempStr = sourceLine.strip()
                    useList.append(tempStr)
                    desList.append(tempStr + "\t" + "*" + "\n")
                    usedNum += 1

    with open(destinationPath, "w") as desFile:
        for desLine in desList:
            desFile.write(desLine)

    usrStr = ""
    for i in range(len(useList)):
        if i == (len(useList) - 1):
            usrStr = usrStr + useList[i]
        else:
            usrStr = usrStr + useList[i] + "|"
    print usrStr

    return useList


# 拿到指定数量的绑定物理设备字符串
if __name__ == '__main__':
    getDeviceList(CONFIG.DEVICE_NUM, CONFIG.DEVICE_SOURCE_FILE, CONFIG.DEVICE_DES_FILE)