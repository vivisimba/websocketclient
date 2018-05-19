# -*- coding: utf-8 -*-
"""
Created on 2018/5/17

@author: Simba
"""


import subprocess
import os
import sys
import time


# 查看的时间间隔
deltaTime = 2


# 本机执行命令，返回shell执行结果
def runShell(cmd):
    returnDic = {}
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    p.wait()
    outStrList = p.stdout.readlines()
    errStrList = p.stderr.readlines()
    returnDic['outStrList'] = outStrList
    returnDic['errStrList'] = errStrList
    return returnDic


# 获得GPU总信息
def getGPUtotal(infoStr):
    infoList = []
    tempList = infoStr.split("|")
    for i in range(len(tempList)):
        # 显存使用率Memory Usage
        if i == 2:
            temtStr1 = tempList[i].replace(" ", "")
            alist = temtStr1.split("MiB")
            usedStr = alist[0]
            totalStr = alist[1].replace("/", "")
            usePercentStr = "%.2f%%" % (float(usedStr)/float(totalStr)*100)
            rankerMemoryTotalStr = temtStr1 + "=" + usePercentStr
            infoList.append(rankerMemoryTotalStr)
        # GPU利用率
        if i == 3:
            bList = tempList[i].split("%")
            gpuTotalUsageStr = bList[0].replace(" ", "") + "%"
            infoList.append(gpuTotalUsageStr)
    return infoList


# 处理比对库和聚类库信息
def getRegAndCls(regAndClsStr):
    newList = regAndClsStr.split(" ")
    lastList = []
    for i in newList:
        if "MiB" in i:
            lastList.append(i)
    return lastList[0]




# 处理获得的GPU信息,获得字典
def getGpuInfoDic(shellDic):
    infoList = []
    tempList = []
    for i in range(len(shellDic["outStrList"])):
        # if i in (8, 11, 18, 19 ,20, 21,22):
        if i in (8, 11, 18, 19):
            tempList.append(shellDic["outStrList"][i])

    # ranker total
    infoList.append(getGPUtotal(tempList[0]))
    # matrix total
    infoList.append(getGPUtotal(tempList[1]))
    # register ranker GPU Memort usage
    infoList.append(getRegAndCls(tempList[2]))
    # cluster ranker GPU Memort usage
    infoList.append(getRegAndCls(tempList[3]))


    nameList = [
        "rankerTotal",
        "matrixTotal",
        "registerRanker",
        "clusterRanker",
        # "matrix1",
        # "matrix2",
        # "matrix3"
    ]
    infoDic = dict(zip(nameList, infoList))
    return infoDic


# 写文件infoDic, fileName
def makeFile(infoDic, fileName):
    fileDir = os.path.abspath(os.path.join(os.path.dirname(__file__), "."))
    filePath = os.path.join(fileDir, fileName)
    line = "rankerTotalGpuMemUsage: %s " \
           "rankerTotalGpuUsage %s " \
           "matrixTotalGpuMemUsage: %s " \
           "matrixTotalGpuUsage %s " \
           "registerRankerUsedMem %s " \
           "clusterRankerUsedMem %s\n" \
           % (
               infoDic["rankerTotal"][0],
               infoDic["rankerTotal"][1],
               infoDic["matrixTotal"][0],
               infoDic["matrixTotal"][1],
               infoDic["registerRanker"],
               infoDic["clusterRanker"]
           )
    timeStr = str(int(round(time.time() * 1000)))
    line = timeStr + " " + line
    # print line
    with open(filePath, "a") as f:
        f.write(line)



def run():
    resDic = runShell("nvidia-smi")
    infoDic = getGpuInfoDic(resDic)
    fileName = sys.argv[1]
    makeFile(infoDic, fileName)






if __name__ == '__main__':

    while True:
        run()
        time.sleep(deltaTime)