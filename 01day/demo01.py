# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:18
# @Author  : guoyunfei.0603
# @File    : demo01.py

import keyword
# print(keyword.kwlist)

'''
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 
 'except', 'finally', 'for', 'from', 'global', 'if', 'import',
  'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
   'return', 'try', 'while', 'with', 'yield']

'''


name = input("请输入你的名字：")
sex = input("请输入你的性别：")
age = input("请输入你的年龄：")
print("*" * 20)

print("姓名：{0} \n性别：{1} \n年龄：{2} ".format(name,sex,int(age)))

print("*" * 20 )
