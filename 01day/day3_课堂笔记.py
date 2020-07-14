# -*- coding: utf-8 -*-
# @Time    : 2020/7/3 10:46
# @Author  : guoyunfei.0603
# @File    : day3_课堂笔记.py
# 5.课堂笔记

# 1. 字符串格式化小数长度（四舍五入）
# format
a = 3.1415926
print("结果：{:.3f}".format(a))

# 2. 格式字符串的长度
a1 = "小白"
a2 = "小小白"
a3 = "小小拜拜"

# >右对齐     <左对齐     ^中间对齐
print("我的名字是{:<8},今年18岁".format(a1))
print("我的名字是{:<8},今年18岁".format(a2))
print("我的名字是{:<8},今年18岁".format(a3))

# 3. 格式化百分比
b = 0.568
print("百分比的数值为：{:.2%}".format(b))

print("======================华丽的分割线===================")

# 1、find：查找字符串,返回的是字符串的索引（下标）,找不到返回的是-1 # 注意：如果存在多个，返回的是第一个
s1 = "python java"
print(s1.find('j'))
print(s1.find('d')) # 找不到，返回-1

# 2、count：计算字符的个数
s2 = 'aaa,bbbb,cccc'
print(s2.count('b'))

# 3、replace:替换字符串的内容 # 默认所有符合要求的都替换，可以通过第三个参数指定替换的次数
s3 = '不想努力了~~'
# 把不想 改为继续
res = s3.replace('不想','继续')
print(res)

# 4、split：字符串分割
s4 = '抓包:charles,接口:jmeter,数据库:mysql'
print(s4.split(','))

# 5、upper:把小写的字母转换为大写
s5 = 'teacher'
print(s5.upper())

# 6、lower：把大写的字母转换为小写
s6 = 'TEACHER'
print(s6.lower())

# 7、strip:去除字符串首尾的空格
s7 = '  student  '
print(s7.strip())

# 8、join:字符串拼接
str1 = 'python'
str2 = 'java'
str3 = 'go'
str4 = '!!!'

print(" ".join([str1,str2,str3,str4])) # 注意是空格

# 9.字符串格式化 format