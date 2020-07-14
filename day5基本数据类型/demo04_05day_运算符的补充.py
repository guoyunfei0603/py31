"""
============================
Author:柠檬班-木森
Time:2020/7/7   20:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
逻辑运算符： 
    or: 假假为假   
    and: 真真为真  
    not: 非  

成员运算符： in  not in  结合字符串进行讲解

身份运算符 is   is not(了解)



内置的函数:id()

"""
# 1,逻辑运算符
# print(8 > 5 and 9 > 88)

#  去比较：张三的年龄比李四大，并且钱比李四多
zs = {"age": 18, "money": 10000}
ls = {"age": 115, "money": 15000}

# print(zs["age"] > ls["age"] and zs["money"] > ls["money"])

# 比较：张三的年龄比李四大，或者钱比李四多
# print(zs["age"] > ls["age"] or zs["money"] > ls["money"])
# print(not 8 < 5)


# 2,成员运算符
# students = ['流年', '向日葵', "Zing", "丽"]
# name = "流年"
# name2 = "张三"
# print(name2 not in students)


# str1 = "12345678o"
# s = "123"
# print(s in str1)

# 字典成员运算
# dic = {"name": "木森", "age": 18, "sex": "男", "aa": 99}
# d = {"name": "木森"}

# 错误示范
# print(d in dic)

# 键
# print("name" in dic.keys())
#
# # 值
# print(18 in dic.values())


# 身份运算符 is   is not
# is:比较数据的id是否一致
# is not:比较数据的id是否不一致

# is  ==


n = [11, 22]
n1 = [11, 22]

n2 = n
print(id(n))
print(id(n1))
print(id(n2))

print(n == n1)
print(n is n1)
print(n is n2)
