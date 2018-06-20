# -*- coding: utf-8 -*-
#Created by zhouzebing on 2018/5/20.

#获取输入的数字
#可以输入八进制、十进制、十六进制

#如果要输出字符串，必须带引号
#input : 输入的内容会当做一个表达式来执行，
# 所以可以输入数字，
# 如果要输入字符串，必须带上引号
a = input("input you number:")
print a
print a * 2

#raw_input : 输入的内容会当做一个字符串来处理
b = raw_input("input you name:")
print b
print b * 2