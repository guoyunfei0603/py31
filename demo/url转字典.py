# -*- coding: utf-8 -*-
# @Time    : 2020/7/14 17:36
# @Author  : guoyunfei.0603
# @File    : url转字典.py

# 有url = "http://127.0.0.1:5000/?name=lc&pwd=233&p=dhd&a=233&cropid=66876876767"
# 这样一个url，通过你的方式将携带的参数转化为字典的形式

url = "http://127.0.0.1:5000/?name=lc&pwd=233&p=dhd&a=233&cropid=66876876767"

index1 = url.find('?')
print(index1)

# 切片拿到 参数
res1 = url[23:-2]
print(res1)

# = 换成 ,
res2 = res1.replace('=',',')
print(res2)
# 根据 & 分割
res3 = res2.split('&')