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

#str3 = "".join(arr)
#print "str3 = ", str3       # 没有输出


# ====================== 修改序列中的值 =====================

arr = [0,1,2,3,4,5,6,7,8,9]

#修改指定位置的值
arr = [0,1,2,3,4,5,6,7,8,9]
arr[0] = 999
print "arr = ", arr         # arr =  [999, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#使用片段修改多个值
arr = [0,1,2,3,4,5,6,7,8,9]
arr[0:3] = ["a", "b", "c", "d"]
print "arr = ", arr         # arr =  ['a', 'b', 'c', 'd', 3, 4, 5, 6, 7, 8, 9]

#使用片段插入一段值
arr = [0,1,2,3,4,5,6,7,8,9]
arr[3:3] = ["a", "b", "c", "d"]
print "arr = ", arr         # arr =  [0, 1, 2, 'a', 'b', 'c', 'd', 3, 4, 5, 6, 7, 8, 9]

#删除指定的数据
arr = [0,1,2,3,4,5,6,7,8,9]
del arr[3]
print "arr = ", arr         # arr =  [0, 1, 2, 4, 5, 6, 7, 8, 9]

#删除指定的片段
arr = [0,1,2,3,4,5,6,7,8,9]
del arr[3:7]
print "arr = ", arr         # arr =  [0, 1, 2, 7, 8, 9]

#删除指定的片段 + 步长
arr = [0,1,2,3,4,5,6,7,8,9]
del arr[::2]
print "arr = ", arr         # arr =  [1, 3, 5, 7, 9]


# ====================== 列表方法 ======================

# append 在末尾添加新的对象,只能添加单个数据，不能添加列表
arr1 = [0,1,2,3,4]
arr1.append("a")
print "arr1 = ", arr1         # arr1 =  [0, 1, 2, 3, 4, 'a']

# extend 在末尾添加新的列表
arr2 = [0,1,2,3,4]
arr3 = ["a","b","c"]
arr2.extend(arr3)
print "arr2 = ", arr2       # arr2 =  [0, 1, 2, 3, 4, 'a', 'b', 'c']

# insert 在列表中插入数据
arr4 = [0,1,2,3,4]
arr4.insert(3, "aaaa")
print "arr4 = ", arr4       # arr4 =  [0, 1, 2, 'aaaa', 3, 4]

# count 统计数据出现的次数
arr5 = [0,1,2,3,4,0,1,2,0,1,2,3,4]
num = arr5.count(4)
print "num = ", num         # num =  2

# index 从列表中查找某个值，返回其第一次出现的位置的索引,如果找不到，则会出现异常
arr6 = [0,1,2,3,4,0,1,2,0,1,2,3,4]
idx = arr6.index(4)
print "idx = ", idx         # idx =  4

#idx = arr.index(5)
#print "idx = ", idx


# pop 移除列表的一个元素，并返回该值，如果不指定位置，则默认是最后一个
arr7 = [0,1,2,3]
num1 = arr7.pop()
print "num1 = ", num1       # num1 =  3
print "arr7 = ", arr7       # arr7 =  [0, 1, 2]

arr8 = [0,1,2,3]
num2 = arr8.pop(2)
print "num2 = ", num2       # num2 =  2
print "arr8 = ", arr8       # arr8 =  [0, 1, 3]

# remove 移除列表中某个值的第一个匹配项
arr9 = [0,1,2,3,2,4,5,]
arr9.remove(2)
print "arr9 = ", arr9       # arr9 =  [0, 1, 3, 2, 4, 5]

# reverse 将列表中的值反向存放
print " --------- reverse --------- "
arr = [0,1,2,3]
arr.reverse();
print "arr = ", arr         # arr =  [3, 2, 1, 0]

# sort 排序
print " --------- sort --------- "
arr = [0,1,2,3,2,4,5,]
arr.sort()
print "arr = ", arr         # arr =  [0, 1, 2, 2, 3, 4, 5]

# 排序是直接改变原来的列表，排序完成后原来的列表的数据就变化了
# 如果想要对一个列表排序，完了之后还想要原来的列表的数据
# 就需要先拷贝一份数据，对拷贝的数据进行排序

arr1 = [0,1,2,3,2,4,5,]
arr2 = arr1[:]      # 如果直接使用 arr2 = arr1, 那么两者表示的是同一个对象，改变一个另一个也会受影响
arr2.sort()
print "arr1 = ", arr1
print "arr2 = ", arr2

# sorted 对一个列表进行排序，并返回一个已排序的列表,原来的列表也被改变，但是新的列表和原来的列表是两个对象
print " --------- sorted --------- "
arr1 = [0,1,2,3,2,4,5]
arr2 = sorted(arr1)
print "arr1 = ", arr1
print "arr2 = ", arr2