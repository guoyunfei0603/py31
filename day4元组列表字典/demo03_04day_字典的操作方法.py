"""
============================
Author:柠檬班-木森
Time:2020/7/4   10:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
字典的增删查改:

1、添加：通过键直接进行赋值（无则增，有则改）

2、修改：通过键直接进行赋值（无则增，有则改）

3、查找：
    # 方式一，直接通过键去获取
    # print(dic['name'])
    # 该方式如果键不存在，会报错KeyError


    # 方式二：get:直接通过键去获取,如果键不存在，返回None

4、删除：
    pop:通过指定键删除对应的键值对
    popitem:
    clear:清空字典


注意点：字符串，列表、元祖，支持下标操作，可以下标取值课切片
字典不支持下标取值和切片



None：空



"""

dic = {"name": "musen", "name1": "cmq", "name2": "FENG"}

# # 1、添加：通过键直接进行赋值 # 无则增，有则改
# dic["name3"] = "小白"
#
# # 2、修改：通过键直接进行赋值  # 无则增，有则改
# dic["name"] = "女子"
# print(dic)

# 3、查询
# 方式一，直接通过键去获取
# print(dic['name'])
# 该方式如果键不存在，会报错KeyError


# 方式二：get:直接通过键去获取,如果键不存在，返回None
# print(dic.get("name111"))

# 4、删除
# 方法一：通过指定键删除对应的键值对
# dic.pop('name')


# 方法二：popitem：删除最近一个添加到字典的键值对（3.5以前的pyhton是随机的）
# print(dic.popitem())








