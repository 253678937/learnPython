# -*- coding: utf-8 -*-
# Created by Administrator on 2018-12-25.

#遍历目录下的所有文件
#foreach
    #读取文件内容，替换当前文件中所有可以替换的字符串，然后保存
    #修改当前文件的文件名
#读取工程文件，并替换工程文件中所有可以替换的字符串，然后保存

import os,sys

#将一个文本内容转换为词典
def readFileToDict(filePath):
    dict = {}
    if not os.path.exists(filePath):
        print "file not exist %s" %(filePath)
        return
    f = open(filePath);
    lines = f.readlines();
    for i in range(0, len(lines)):
        text = lines[i]
        arr = text.split(",")
        if len(arr) >= 1:
            key = arr[0]
            value = key
            if "CC" in key:
                value = key.replace("CC", "CCX")
            if not "CC" in key:
                value = "DT" + key
            dict[key] = value

    #对KEY进行去重处理，假设有两个key,分别是 aaa, aaaBC, 那么aaa就不能要，会影响到后面的aaaBC
    for key in dict:
        for key2 in dict:
            if len(key2) > len(key) and (key in key2):
                print "pop key, key = %s, key2 = %s" %(key, key2)
                dict.pop(key)
    return dict


#处理单个文件
def dealFile(fileName, filePath, dict):
    #读取文件内容，替换字符串
    with open(filePath, "r") as fileObj:
        all_text = fileObj.read()
        fileObj.close()

    newFileName = ""

    for key in dict:
        value = dict[key]
        all_text = all_text.replace(key, value)
        if key in fileName:
            newFileName = fileName.replace(key, value)

    with open(filePath, "w") as fileObj:
        fileObj.write(all_text)
        fileObj.close()

    if len(newFileName) > 0:
        newFilePath = filePath.replace(fileName, newFileName)
        os.rename(filePath, newFilePath)

    return True


#遍历目录下的所有文件，并逐个进行处理
def visitPath(dir, dict):
    list = os.listdir(dir)
    for i in range(0, len(list)):
        path = os.path.join(dir, list[i])
        if os.path.isfile(path):
            dealFile(list[i], path, dict)
        if os.path.isdir(path):
            visitPath(path, dict)

#脚本入口
def main():
    src_path = "d:\\WorkSpace\\DingDing\\Bohu\\BoHuDebug\\frameworks\\cocos2d-x\\cocos"
    src_path_2 = "d:\\WorkSpace\\DingDing\\Bohu\\BoHuDebug\\frameworks\\cocos2d-x\\extensions"
    proj_file_path = "d:\\WorkSpace\\DingDing\\Bohu\\BoHuDebug\\frameworks\\cocos2d-x\\build\\cocos2d_libs.xcodeproj\\project.pbxproj"
    config_file_path = "d:\\config.txt"

    dictConfig = readFileToDict(config_file_path)

    print dictConfig

    #处理代码
    visitPath(src_path, dictConfig)

    visitPath(src_path_2, dictConfig)

    #处理工程文件
    dealFile(proj_file_path, proj_file_path, dictConfig)

    print "finish !!"

    return True

main()






