# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 16:10
# @Author  : guoyunfei.0603
# @File    : home_work.py
# 1：简单题
#     1、函数的形参有哪几种定义形式？
"""
三种：
1. 位置参数
2. 默认参数
3. 不定长参数（*args  **kwargs）

"""
#     3、函数的实参有哪几种形式？
'''
两种:
1、位置传参（位置参数）:按照参数定义的位置进行传递
2、关键字传参（关键字参数）:通过参数名字，指定传递
'''
# 2、利用上课讲的for循环嵌套的知识点，封装一个可以打印任意比列三角形的函数
# (注意点：和上课的有区别，这个是倒三角)
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

print("--------------第二题-------------")


def sanjiao(n):
    for i in range(n + 1):
        for j in range(n):
            print(" * ", end="")
        n -= 1
        print()


sanjiao(5)


# 3、定义一个可以完成任意个数字相加的函数（支持关键字传参和位置传参），并返回相加结果。
# 要求:调用函数传入1个数字，返回值为这个数字。
#         如：func(1) ---->   返回 1
#     调用函数传入2个数字，返回值为2个数相加的结果。
#         如：func(11,22) ---->   返回33
#     调用函数传入3个数字，返回值为3个数相加的结果。
#         如：func(11,22,33,) ----> 返回66
#     调用函数传入n个数字，返回值为n个数相加的结果。
#         如：func(1,2,3,4,5) ----> 返回 15
# （提示：可以使用不定长参数来接收参数，对参数进行遍历再相加）

# 方式一
def num_sum(*args, **kwargs):
    count = 0  # 记录总和
    for i in args:
        count += i

    for j in kwargs.values():
        count += j

    print(count)


num_sum(10, 20, a=1, b=2, c=3)

# 方式二
# def num_sum2(*args, **kwargs):
#     a = sum(args) + sum(kwargs.values())
#
#     print("结果：",a)
# num_sum2(1,2,a=1,b=2)

import random
random.random()
