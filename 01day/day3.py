# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 9:38
# @Author  : guoyunfei.0603
# @File    : day3.py
# 1、现有字符串    str1 = "PHP is the best, programming, language in, the world! "
#       要求一：将给定字符串的PHP替换为Python
#       要求二：替换以后，将字符串以逗号为分割点进行分割得到一个列表
str1 = "PHP is the best, programming, language in, the world!"
str2 = str1.replace('PHP','python')
str3 = str2.split(',')

print(str3)


# 2、编写代码，提示用户输入1-7七个数字，分别代表周一到周日，打印输出“今天是周X”
# （要求：使用上课学过的知识点来做）
# 提示：周一到周日，可以保存到列表中，实现用到的知识点：输入、输出、列表索引取值
li = ['','周一','周二','周三','周四','周五','周六','周日']
user = int(input('请输入1-7的数字：'))
print(li[user])  #li[user-1]

# 3、用户输入一个数值，请使用比较运算符确认用户输入的是否为偶数？是偶数输出True,不是输出False
# （提示:input输入的不管是什么，都会被转换成字符串，自己扩展，想办法将字符串转换为数值类型，再进行算术运算和比较）
#
# 提示：用到的知识点：算术运算符、 比较运算符  、输入、输出
user2 = int(input('请输入一个数字：'))
print(user2 %2 == 0)    # 结果为True 或者 False

# 4、切片小练习

# 1、现在有一个字符串
s = 'abcdefghijk'

# 要求一：通过切片获取: defg
index_1 = s.find('d')
index_2 = s.find('h')

print(s[index_1:index_2])
# 要求二：通过切片获取：cgk
print(s[2::4])
# 2、通过切片获取 li = [2, 3, 1, 4, 6, 2, 5, 6, 7] 中的[1, 4, 6, 2]
li = [2, 3, 1, 4, 6, 2, 5, 6, 7]
print(li[2:6])

