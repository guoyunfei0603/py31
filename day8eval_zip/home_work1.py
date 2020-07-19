# -*- coding: utf-8 -*-
# @Time    : 2020/7/16 21:05
# @Author  : guoyunfei.0603
# @File    : home_work1.py

# 第一题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回
print("-------------------------第一题--------------------------\n")


def type_func(n):
    li = []
    for i in n:
        li.append(eval(i))  # 遍历出每个元素，然后eval，添加到列表里面
    return li


data = ["{'a':11,'b':2}", "[11,22,33,44]"]
#
res = type_func(data)
print(res)

'''
第二题：请封装一个函数，完成如下数据格式转换
传入参数：
cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
# 返回结果
cases02 = [
    {'case_id': 1, 'case_title': '用例1', 'url': 'www.baudi.com', 'data': '001', 'excepted': 'ok'},
    {'case_id': 2, 'case_title': '用例2', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 3, 'case_title': '用例3', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 4, 'case_title': '用例4', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'},
    {'case_id': 5, 'case_title': '用例5', 'url': 'www.baudi.com', 'data': '002', 'excepted': 'ok'}
]
'''

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]

print('*************************************草稿*************************************')
li = []
for i in range(1, 6):
    res1 = zip(cases[0], cases[i])
    # res2 = zip(cases[0],cases[2])
    # res3 = zip(cases[0],cases[3])
    # res4 = zip(cases[0],cases[4])
    # res5 = zip(cases[0],cases[5])

    li.append(list(res1))
# li.append(list(res2))
# li.append(list(res3))
# li.append(list(res4))
# li.append(list(res5))

print(li)
print('*************************************草稿*************************************')

print("------------------------第二题------------------------------\n")


#
# def fun2(cases, n):
#     li = []
#
#     for i in range(1, n):
#         res1 = zip(cases[0], cases[i])
#         li.append(list(res1))
#     return li
#
#
# result = fun2(cases, 6)
# print(result)


print("------------------------------第3题---------------------------------")
# 第三题：简单题
#  1、什么是全局变量？
#  2、什么是局部变量？
#  3、函数内部如何修改全局变量（声明全局变量 ）？
print('''
1. 全局变量：python中直接定义在模块（py文件中的变量），叫做全局变量,在该文件中任何地方都可以使用
2. 局部变量：定义在函数中的变量，叫做局部变量,只能在该函数内部使用
3. global
    例如：
        global name
        name == '小白'
''')
