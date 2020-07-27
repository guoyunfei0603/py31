# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 10:50
# @Author  : guoyunfei.0603
# @File    : review_1.py
# 1、现有字符串    str1 = "PHP is the best, programming, language in, the world! "
#       要求一：将给定字符串的PHP替换为Python
#       要求二：替换以后，将字符串以逗号为分割点进行分割得到一个列表

# str1 = "PHP is the best, programming, language in, the world! "
# s1 = str1.replace("PHP","python")
# print(s1)
#
# s2 = s1.split(',')
# print(s2)

# # 1、现在有一个字符串
# s = 'abcdefghijk'
# # 要求一：通过切片获取: defg
# print(s[3:7])
#
# # 要求二：通过切片获取：cgk
# print(s[2::4])


# 1、现在有变量 a = ‘hello’ ,
# b = ‘python18’     c = ‘!’  ,通过相关操作变成一个字符串：'hello python18 !'
# （注意点:转换之后单词之间有空格）
#
# a = 'hello'
# b = 'python18'
# c = '!'
#
# print(' '.join([a,b,c]))
# print("{} {} {}".format(a,b,c))

# 3、请随机生成一个131开头的手机号码。
import random
phone = random.randint(13100000000,13199999999)
print(phone)

s = "PHP is the best\"\"\" \\tprogramming\"language in 'the\\norld"
print(s)