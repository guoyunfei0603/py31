# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 15:49
# @Author  : guoyunfei.0603
# @File    : day6笔记.py
# encoding:UTF-8
# for 循环，当数字为4时 跳过
# var = 10
# while var >0:
#     var -=1
#     if var == 4:
#         continue
#     print(var)

# 使用内置 enumerate 函数进行遍历:
# li = [332,1,99,10,5]
# for i,j in enumerate(li):
#     print(i,j)

# for 循环 1-100 所有整数的和
# s = 0
# for i in range(101):
#     s += i
# print(s)

# 使用循环嵌套来实现99乘法法则:
'''
1 * 1 = 1
1 * 2 = 2  2 * 2 = 4
1 * 3 = 3  2 * 3 = 6  3 * 3 = 9

'''
# for j in range(1,10):
#     for k in range(1,j+1):
#
#         print("{} * {} = {}  ".format(j, k, j * k),end='')
#     print("")

# for row in range(1,10):
#     for col in range(1,row+1): # 因为row 只会到9，所以col要+1  变成9 * 9
#         print("{}*{}={}\t".format(col,row,col*row),end=" ")
#
#     print("")

# for i in range(5): # 0 1 2 3 4
#     print(i)

# 冒泡 ：两个相邻数值依次比较



def bubble_sort(li):
    n = len(li)
    # 遍历列表长度减1次
    for i in range(1, n):
        # 创建一个变量，用来记录本轮冒泡，是否有数据交换位置
        status = False
        # 每次遍历都获取第一个元素，依次和后面的元素进行比较
        for j in range(n - i):
            # 判断前元素，和后一个元素的值
            if li[j] > li[j + 1]:
                # 交换当前元素和后一个元素的值
                li[j], li[j + 1] = li[j + 1], li[j]
                # 只要由数据交换位置，则修改statusd的值
                status = True
        # 每一轮冒泡结束之后，判断当前status是否为Flase,
        # 如果为Flase，则说明上一轮冒泡没有修改任何数据的顺序（即数据是有序的）
        if not status:
            return li
    return li
li = [45,23,15,350,999,1]

res = bubble_sort(li)
print(res)
# a = 5
# b = 10
#
# a,b = b,a # 交换两个位置
# print(a,b)# 10 5