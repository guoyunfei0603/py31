# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 9:44
# @Author  : guoyunfei.0603
# @File    : home_work5.py
# 1、有下面几个数据 ，t1 = ("aa",11)      t2= (''bb'',22)    li1 = [("cc",22)]
# 请通过学过的知识点，进行相关操作变为如下字典: {"aa":11,"cc":22,"bb":22}
t1 = ("aa", 11)
t2 = ("bb", 22)
li1 = [("cc", 22)]

li1.append(t1)
li1.append(t2)

print(dict(li1))
# 2、当前有一个列表 li = [11,22,33,22,22,44,55,77,88,99,11]，
#  要求一：去除列表中的重复元素，
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
res = set(li)

# 转为列表
li_res = list(res)
print(li_res)

#  要求二：去重后删除 77，88，99这三个元素
li_res.remove(77)
li_res.remove(88)
li_res.remove(99)
print(li_res)

# 3、利用random函数生成随机整数（范围1-9），然后用户输入一个数字，来进行比较：
# 如果大于随机数，则打印印大于随机数。
# 如果小于随机数，则打印小于随机数。
# 如果相等随机数，则打印等于随机数。
import random
random_num = random.randint(1,9)
user_num = int(input("请输入一个数字："))

if user_num > random_num:
    print("大于随机数")
elif user_num < random_num:
    print("小于随机数")
elif user_num == random_num:
    print("等于随机数")

print("随机数是:",random_num)

# 4、一家商场在降价促销。如果购买金额50-100元(包含50元和100元)之间，会给打九折，
# 如果购买金额大于100元会给打八折。编写一程序，询问购买价格，再打印出折扣和最终价格。
price = float(input("请问购买价格是？"))

if 50 <= price <= 100:
    print("打九折，最终价格是{:.2f}元".format(price * 0.9))
elif price > 100:
    print("打八折，最终价格是{:.2f}元".format(price * 0.8))

# 5、提示用户输入一个数（只考虑整数），判断这个数能同时被3和5整除，
# 能整除打印 :能整除
# 不能整除打印：不能整除
# 方式一：
num = int(input("请输入一个整数："))
if num % 3 == 0 and num % 5 == 0:
    print("能整除")
else:
    print("不能整除")

# 方式二：
# num = int(input("请输入一个整数："))
# if num % 3 ==0 :
#     print("可以整数3")
#     if num % 5 == 0:
#         print("能整除3和5")
#     else:
#         print("不能整除5")
# else:
#     print("不能整除")
