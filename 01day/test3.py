# -*- coding: utf-8 -*-
# @Time    : 2020/7/2 16:59
# @Author  : guoyunfei.0603
# @File    : test3.py

# i = sum = 0
# while i <= 4:
#     sum += i # 当 i = 1 的时候，sum = 0 + 1
#     i = i+1
#
# print(sum)
#
# for char in 'PYTHON STRING':
#     if char == ' ':
#         break
#
#     print(char, end='')
#
#     if char == 'O':
#         continue

# print("test" ,end ="" )
import re
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配