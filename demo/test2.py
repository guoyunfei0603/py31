# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 11:28
# @Author  : guoyunfei.0603
# @File    : test2.py
# 二、定义一个空列表user = [], 分别提示用户输入，姓名，年龄，身高，用户输入完之后，
# 将输入的信息作为添加的列表中保存，然后按照一下格式输出：
# 用户的姓名为：xxx, 年龄为：xxx, 身高为：xxx, 请仔细核对
# user = []
# name = input('请输入你的姓名:')
# age = input('请输入你的年龄：')
# height = input('请输入你的身高：')

# user.extend([name,age,height])  # 方式一
# user.append(name) # 方式二
# user.append(age)
# user.append(height)
#
# print("用户的姓名为：{}, 年龄为：{}, 身高为：{}".format(user[0],user[1],user[2]))
# 三、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
# （提示：通过字符串分割，拼接，列表反序等知识点来实现）
# s1 = 'hello xiao mi'
# s2 = s1.split(" ")
# # s2.reverse()
#
# s3 = s2[::-1]
# print(s3)
# print('{} {} {}'.format(s2[0],s2[1],s2[2]))

#
# 四、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
# 1、运行时分别提醒输入
# 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
# 2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
# 3、平台需要补足您的身高和联系方式；（分别输入身高和联系方式添加到字典中）
# 4、平台为了保护你的隐私，需要你删除你的联系方式（删除字典中的联系方式）；


# dic = {"name": '张三', "age": 18, "sal": 99999}
# print(len(dic))  3
# for key,value in dic.items():
#     print(key,value)
# for i in dic.items():
#     print(i[1])
# print('-------------------------------------')

t = [[11, 22, 33], ['aa', 'bb', 'cc']]
# for i in t:
#     # print(i,type(i))
#     for j in i:
#         print(j, type(j))
