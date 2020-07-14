# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 18:01
# @Author  : guoyunfei.0603
# @File    : dict_json.py
import json
dic = {"name":"丁香","age":22,"job":"teacher"}

# 字典转成json格式
new_json = json.dumps(dic)
print(new_json,'类型是：',type(new_json)) # 类型是： <class 'str'>  json在python中是一个字符串

# json转字典
new_dic = json.loads(new_json)
print(new_dic,'类型是：',type(new_dic))

# 字典转字符串
s = str(dic)
print(s,type(s))

# eval
s1 = '{"age":22,"job":"teacher"}'
s2 = eval(s1)   # 字符串 eval为字典

print(s2,type(s2))