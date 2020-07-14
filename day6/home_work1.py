# -*- coding: utf-8 -*-
# @Time    : 2020/7/10 9:48
# @Author  : guoyunfei.0603
# @File    : home_work1.py
'''
一、作业题（必做题）
'''
# 1、实现剪刀石头布游戏（），提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4）
# 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
# 运行如下图所示（提示：while循环加条件判断，做判断时建议先分析胜负的情况）
# user   random
# 1        2     1-2 =-1
# 2        3     2-3= -1
# 3        1     3- 1 = 2
print("-----------------------------第1题--------------------------")
import random

while True:
    user = int(input("请出拳：石头（1）／剪刀（2）／布（3）/退出（4）  :"))
    random_num = random.randint(1, 3)
    dic = {"石头": 1, "剪刀": 2, "步": 3, "退出": 4}

    if user in dic.values():
        # 退出
        if user == dic["退出"]:
            print("已退出")
            break
        # 用户胜
        elif user - random_num == -1 or user - random_num == 2:
            print("电脑随机出拳是：{}".format(random_num))
            print("用户胜！")
        # 用户负
        elif user - random_num == -2 or user - random_num == 1:
            print("电脑随机出拳是：{}".format(random_num))
            print("用户负")
        # 平局
        elif user - random_num == 0:
            print("电脑随机出拳是：{}".format(random_num))
            print("平局")
    else:
        print("输入有误~")

# 2、通过定义一个计算器，允许程序提示用户输入数字1，数字2，然后再提示用户选择 ：
#  加【1】    减【2】    乘【3】      除【4】，
# 根据不同的选择完成不同的计算 ，然后打印结果
print("-----------------------------第2题--------------------------")
num_1 = float(input("请输入第一个数字："))
num_2 = float(input("请输入第二个数字："))

operation = input("请选择 加【1】    减【2】    乘【3】    除【4】(例如：选择1作加法)：")
if operation == '1':
    print("加法运算：", num_1 + num_2)
elif operation == '2':
    print("减法运算：", num_1 - num_2)
elif operation == '3':
    print("乘法运算：", num_1 * num_2)
elif operation == '4':
    print("乘法运算：", num_1 / num_2)
else:
    print("只能输入1，2，3，4")

'''
第三题：请获取下面字典数据中的token，和reg_name
'''
print("-----------------------------第3题--------------------------")
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
print("token:", data["data"]["token_info"]["token"])
print("reg_name:", data["data"]["reg_name"])

# 第4题：当前有一个列表 li = [1,21,33,221,432,121,44,21,22,,44,1,221],请完成如下要求！
# 1、请先去除列表中的重复元素
print("-----------------------------第4题--------------------------")
li = [1, 21, 33, 221, 432, 121, 44, 21, 22, 44, 1, 221]
li1 = list(set(li))
print(li1)
# 2、对去重后的列表进行升序排序
li1.sort()
print("升序：", li1)
# 3、遍历排序后列表，将元素为偶数的元素，添加到一个新列表中
li2 = []
for i in li1:
    li2.append(i)
print("新列表:", li2)

# 第5题、运行程序，提示用户依次输入三个整数x,y,z，请把这三个数由小到大输出。
# print("-----------------------------第5题--------------------------")
x = int(input("请输入第一个整数x："))
y = int(input("请输入第一个整数y："))
z = int(input("请输入第一个整数z："))
#
t = []
t.extend([x, y, z])
t.sort()
print("从小到大：", t)

# 第6题、编写一个程序，使用for循环输出0-100（包括0和100）之间的偶数
print("-----------------------------第6题--------------------------")
# for item in range(0, 101):
#     if item % 2 == 0:
#         print(list(item))
li = []
for item in range(0, 101):
    if item % 2 == 0:
        li.append(item)
print(li)

# 第7题、当前有一个字典｛"a":1,"b":22,"c":3,"d":4,"e":5 },
# 请修改字典中所有键值对的值，新的值为原来的值乘10
print("-----------------------------第7题--------------------------")
d = {"a": 1, "b": 22, "c": 3, "d": 4, "e": 5}

# d["a"] = d["a"] * 10
# d["b"] = d["b"] * 10
# d["c"] = d["c"] * 10
# d["d"] = d["d"] * 10
# d["e"] = d["e"] * 10

for i in d.keys():
    d[i] = d[i] * 10

print(d)
