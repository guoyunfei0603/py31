"""
============================
Author:柠檬班-木森
Time:2020/7/7   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
控制流程

# 1,逻辑运算符
# print(8 > 5 and 9 > 88)

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

"""

# 去判断：张三的年龄比李四大，并且钱比李四多,如果成立,打印张三比李四有钱,如果不成立打印张三很穷
# zs = {"age": 18, "money": 10000}
# ls = {"age": 115, "money": 15000}
#
# if zs["age"] > ls["age"] and zs["money"] > ls["money"]:
#     print("张三比李四有钱")
# else:
#     print("张三很穷")

# 判断流年是否是咱们半的学员
students = ['流年', '向日葵', "Zing", "丽"]
name = "流年"

if name in students:
    print("赶紧坐下上课")
else:
    print("出门左转,不送")
