"""
============================
Author:小白31
Time:2020/7/26 20:32
E-mail:1359239107@qq.com
============================
"""
# 一、现在有一个列表 li2=[1，2，3，4，5]，
#
#      第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
li2 =[1,2,3,4,5]
li2.insert(0,0)
li2[4] = 66
li2.extend([11,22,33])
# print(li2)

#      第二步：对列表进行升序排序 （从小到大）
li2.sort()
# print(li2)
#      第三步：将列表复制一份进行降序排序（从大到小）
li3 = li2.copy()
li3.sort(reverse=True)
# print(li3)

# 三、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
# （提示：通过字符串分割，拼接，列表反序等知识点来实现）

str1 = 'hello xiao mi'
res = str1.split(" ")
res.reverse()
r = ' '.join(res)
print(r)
# 四、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
#         1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
#         2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
#         3、平台需要补足您的身高和联系方式；（分别输入身高和联系方式添加到字典中）
#         4、平台为了保护你的隐私，需要你删除你的联系方式（删除字典中的联系方式）；
dic ={}
dic["name"] = input("请输入你的名字：")
dic["sex"] = input("请输入你的性别：")
dic["age"] = input("请输入你的年龄：")
print(dic)

dic.pop('name')
print(dic)