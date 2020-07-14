# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 14:31
# @Author  : guoyunfei.0603
# @File    : test3.py

# a = [{"name": "张三", "age": 18},
#      {"name": "李四", "age": 20}]

# a = [[11, 22, 333, 4444],
#      ['q', 'qwe', 'weqqe']]
#
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])

# data = (
#     ("江金莲","女",28,"高级软件测试工程师"),
#     ("王旭婷","女",22,"中级软件测试工程师"),
#     ("郭云飞","男",22,"中级软件测试工程师")
#     )
#
# for i in range(len(data)):
#     for j in range(len(data[i])):
#         print(data[i][j])

# q = ['a','b','c']
# for i,j in enumerate(q):
#     print(i,j)

# li = ['method','p2','pn','p1','p3']
# li.sort() # 升序
# print(li)
body = {
    "username": "test",
    "password": "123456",
    "mail": ""
}

# 列表生成式，生成key=value格式
a = ["".join(i) for i in body.items() if i[1] ]
print(a)
strA = "".join(sorted(a))
print(strA)

# # 把字典里面的键值对 拼接成字符串
