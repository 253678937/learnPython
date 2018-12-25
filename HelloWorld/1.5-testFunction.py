# -*- coding: utf-8 -*-
# Created by zebing.zhou on 2018-06-19.

#全局的函数，可以直接使用

#获取绝对值
print abs(1.8)

#取四舍五入
print round(1.8)

#转换为int 型数据
print int(1.8)


print '============= 分割线 ============='


#某些模块提供的函数，如果要使用，首先需要导入对应的模块

#导入模块
import math

#向下取整
print math.floor(1.8)

#向上取整
print math.ceil(1.8)

print '============= 分割线 ============='

#列表作为参数传递
def append(args = []):
    args.append(0)
    print(args)

append()
append([1])
append()

print '============= 分割线 ============='

#传递可变参数
def func(*args):
    print args
    print args[0]
    print args[1]

func([1,2,3], "name")

print '============= 分割线 ============='

#词典作为参数传递
def func2(*t, **d):
    keys = d.keys()
    print keys

    for key in keys:
        print key


func2("aa", "bb", one="1", two="2'", three="3")

