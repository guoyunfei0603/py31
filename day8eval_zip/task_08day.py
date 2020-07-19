"""
============================
Author:柠檬班-木森
Time:2020/7/16   22:21
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""

第一题：请封装一个函数，按要求实现数据的格式转换
# 传入参数： data = ["{'a':11,'b':2}", "[11,22,33,44]"]
# 返回结果：res = [{'a': 11, 'b': 2}, [11, 22, 33, 44]]
# 通过代码将传入参数转换为返回结果所需数据，然后返回



第一题：请封装一个函数，完成如下数据格式转换
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



第三题：简单题
#  1、什么是全局变量？
#  2、什么是局部变量？
#  3、函数内部如何修改全局变量（声明全局变量 ）？

"""


def work1(data):
    # 创建一个新列表
    new_data = []
    # 遍历列表中的数据
    for i in data:
        # 将数据使用eval进行转换
        res = eval(i)
        # 将将转换后的数据放入新列表
        new_data.append(res)
    # 返回转换后的数据
    return new_data

data = ["{'a':11,'b':2}", "[11,22,33,44]"]
res = work1(data)
print(res)

def work2(cases):
    new_list = []
    title = cases[0]
    for i in cases[1:]:
        dic = dict(zip(title, i))
        new_list.append(dic)
    return new_list

cases = [
    ['case_id', 'case_title', 'url', 'data', 'excepted'],
    [1, '用例1', 'www.baudi.com', '001', 'ok'],
    [2, '用例2', 'www.baudi.com', '002', 'ok'],
    [3, '用例3', 'www.baudi.com', '002', 'ok'],
    [4, '用例4', 'www.baudi.com', '002', 'ok'],
    [5, '用例5', 'www.baudi.com', '002', 'ok'],
]
res2 = work2(cases)
print(res2)