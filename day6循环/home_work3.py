# -*- coding: utf-8 -*-
# @Time    : 2020/7/13 10:14
# @Author  : guoyunfei.0603
# @File    : home_work2类.py

# 3、打印99乘法表，结果如下：
'''
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
'''
print()
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,j*i),end=" ")
    print()


# 4、小明有100块钱 ，需要买100本书（钱要刚好花完），a类数5元一本，b类书3元一本，c类书 1元2本。请写一段代码计算小明有多少种购买的方式？
# 思路提示：穷举法，使用技术点：for循环嵌套
print()