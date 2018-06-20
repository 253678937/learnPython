# -*- coding: utf-8 -*-
# Created by zebing.zhou on 2018-06-20.

#列表即数组

#列表可以相加,也可以和数字相乘，将原来的序列重复多次

a = ["zhang", "san", 10]
b = ["li", "si", 12]
c = [["aa", "bb"],["111", "222", "333"]]

print a
print a + b
print a + c
print a * 2


#取值
#列表可以通过索引的方式取值, 下标的取值范围是[0, size-1]

print a[1]


#分片
#分片是指提取序列中指定的部分数据
#格式 ：arr[begin : end, step]
#解释 ：从序列的 begin 开始，到 end 结束，但不包含 end，步长为 step
# begin 和 end 可以取值为负数，表示倒数的意思
# 如果 begin 没有指定，则表示从第一个开始
# 如果 end 没有指定，则表示到最后一个
#其中 step 可以不指定，默认为1
arr = [10,11,12,13,14,15,16,17,18,19]

#从第三个开始，到第6个结束，但不包含第6个
arr1 = arr[3:6]
print "arr1 = ", arr1   # arr1 =  [13, 14, 15]

#从第0个开始，到第1个结束，但不包含第1个
arr2 = arr[0:1]
print "arr2 = ", arr2   # arr2 =  [10]

#从倒数第三个开始，到倒数第一个，但是不包含倒数第一个
arr3 = arr[-3:-1]
print "arr3 = ", arr3   # arr3 =  [17, 18]

#从第一个开始，到第三个，但是不包含第三个
arr4 = arr[:3]
print "arr4 = ", arr4   # arr4 =  [10, 11, 12]

#从第7个开始，到最后一个
arr5 = arr[7:]
print "arr5 = ", arr5   # arr5 =  [17, 18, 19]

#步长
arr6 = arr[::2]
print "arr6 = ", arr6   # arr6 =  [10, 12, 14, 16, 18]

#反向
arr7 = arr[-1::-1]
print "arr7 = ", arr7   # arr7 =  [19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

#判断某个值是否在序列中
ret1 = 10 in arr
print "ret1 = ", ret1   # True

ret2 = 88 in arr
print "ret2 = ", ret2   # False

#获取序列的长度
len = len(arr)
print "len = ", len         # len =  10

#获取序列中的最大值
nMax = max(arr)
print "nMax = ", nMax       # nMax =  19

nMin = min(arr)
print "nMin = ", nMin       # nMin =  10

arrString = ["aaa", "a222", "sdfsa", "bddd", "zzdfa"];
nMax = max(arrString)
print "nMax = ", nMax       # nMax =  zzdfa

nMin = min(arrString)
print "nMin = ", nMin       # nMin =  a222

#字符串也是序列，但是是一个比较特殊的序列
#可以将字符串转化为一个普通的全是字符串序列
str = "zhangsan"
arrStr = list(str)
print "arrStr = ", arrStr   # arrStr =  ['z', 'h', 'a', 'n', 'g', 's', 'a', 'n']

#也可以将一个普通的全是字符串序列转化为一个字符串
str2 = "".join(arrStr)
print "str2 = ", str2       # str2 =  zhangsan

str3 = "".join(arr)
print "str3 = ", str3       # 没有输出



