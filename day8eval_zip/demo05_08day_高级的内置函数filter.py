"""
============================
Author:柠檬班-木森
Time:2020/7/16   21:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
filter:过滤器函数

"""

#  获取字典中值大于30的键值对，放到一个新的字典中
dic = {"aa": 11, "bb": 22, "cc": 33, "dd": 44}

# new_dict = {}
# for k, v in dic.items():
#     if v > 30:
#         new_dict[k] = v
#
# print(new_dict)


# def func(x):
#     return x[1] > 30
# res = filter(func, dic.items())
# print(dict(list(res)))


li = [11, 22, 33, 44, 55, 66, 77, 88, 99]

# def func(x):
#     return 60 > x > 30
#
#
# res = filter(func, li)
# print(list(res))

# 匿名函数: lambda表达式（适用函数中只有一行代码的简单函数）

# lambda 参数:返回值
# ---------------------扩展知识点-------------------------
# res = filter(lambda x: 80 > x > 40, li)
# print(list(res))


# zip(): 聚合打包
# 现有数据如下
users_title = ["name", "age", "gender"]
users_info = [['小明', 18, '男'], ["小李", 19, '男'], ["小美", 17, '女']]

# 要求：将上述数据转换为以下格式
users = [{'name': '小明', 'age': 18, 'gender': '男'},
         {'name': '小李', 'age': 19, 'gender': '男'},
         {'name': '小美', 'age': 17, 'gender': '女'}]

'''优化版本'''
list1 = []
for item in users_info:
    dic = dict(zip(users_title,item))

    list1.append(dic)
print(list1)

'''旧版本 忽略'''
# list1 = []
# for item in users_info:
#     dic ={}
#     for i in range(len(users_title)):
#         dic[users_title[i]] = item[i]
#     list1.append(dic)
# print(list1)

a = ["name", "age", "gender","url","123"]
b = ['小明', 18, '男']
res = dict(zip(a,b))
print(res)


