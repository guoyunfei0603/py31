# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 15:09
# @Author  : guoyunfei.0603
# @File    : 练习题_字符串.py
# 编写程序，用户输入一段英文，然后输出这段英文中所有长度为3个字母的单词。

str1 = "Are you a big shot? abc"
r1 = str1.split(" ")

for i in r1:
    if len(i) == 3:
        print(i)