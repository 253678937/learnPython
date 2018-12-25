# -*- coding: utf-8 -*-
# Created by Administrator on 2018-12-25.

import os,sys
import string
import time


def visitPath(arg, dirname, names):
    print arg
    print dirname
    print names
    print "-------------------"


def renameInAllFile(all_src_path):
    list = os.listdir(all_src_path)
    for i in range(0, len(list)):
        path = os.path.join(all_src_path, list[i])
        if os.path.isfile(path):
            print path
        if os.path.isdir(path):
            renameInAllFile(path)

renameInAllFile("d:\\WorkSpace\\DingDing\\Bohu\\BoHuDebug\\frameworks\\cocos2d-x\\cocos")