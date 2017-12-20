
# -*- coding: utf-8 -*-
#加上上面这一句，可以让python识别文件中的utf-8字符，比如汉字
#如果不加，当文件中有汉字时会编译失败

#输出
print "Hello World !"

#运算 - 数字运算
print 4 + 5
print 4 - 5
print 4 * 5
#整形和整形进行运算的时候，结果也会是一个整形，所以下面结果会输出0
print 4 / 5
#如果想要输出浮点型，必须显示地指出参与运算的参数是浮点型，如
print 4.0 / 5
print 4 / 5.0
print 4.0 / 5.0

#字符串可以进行加法运算
print "aaa" + "bbb"
#字符串可以进行乘法运算
print "aaa" * 6

#输出一个十六进制的数字
#十六进制的数字是以0x开头的
print 0xAF

#输出一个八进制的数字
#八进制的数字是以0开头的
print 077

#如果以0开头的数字不是一个合法的八进制数字，则编译会失败
#print 0987

#变量赋值
#变量是没有类型的，赋值给它什么类型，它就是什么类型
x = 5
print x

y = "zhangsan"
print y

z = 998.0
print z

#获取输入的数字
#可以输入八进制、十进制、十六进制
#输入字符串会报错，暂时还不明白为什么
a = input("input you number:")
print a
print a * 2