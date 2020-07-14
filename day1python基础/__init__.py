# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 10:18
# @Author  : guoyunfei.0603
# @File    : __init__.py.py

# s = "'abcd'"
# print(s[0:2])       #'a

# 三、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
# （提示：通过字符串分割，拼接，列表反序等知识点来实现）
s = "hello xiao mi"
s1 = s.split(' ')

t = s1[::-1] # 方式一
# print(t,type(t))  是一个列表  ，最后还要拼接成字符串！！
new_str = ' '.join(t)
print(new_str,type(new_str))


# s1.reverse() # 方式二
# print(s1)