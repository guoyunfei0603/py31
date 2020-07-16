"""
============================
Author:柠檬班-木森
Time:2020/7/14   20:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
函数：可以用对重复使用的功能代码进行封装，提高代码的复用性，提高工作效率，降低代码的耦合性


"""


# for i in range(1, 10):
#     for j in range(i):
#         print("* ", end="")
#     print()
#
# print("-----------------------------")
#
# for i in range(1, 5):
#     for j in range(i):
#         print("* ", end="")
#     print()
#
# print("-----------------------------")
#
# for i in range(1, 8):
#     for j in range(i):
#         print("* ", end="")
#     print()


def func(n):
    for i in range(1, n + 1):
        for j in range(i):
            print("* ", end="")
        print()


func(3)
func(4)
func(5)
func(20)
