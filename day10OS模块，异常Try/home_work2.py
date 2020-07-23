"""
============================
Author:小白31
Time:2020/7/23 0:11
E-mail:1359239107@qq.com
============================
"""

'''
2、优化之前作业的石头剪刀布游戏，用户输入时，如果输入非数字会引发异常，请通过异常捕获来处理这个问题。
'''
import random

while True:
    try:
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
    except ValueError :
        print("请输入数字！")