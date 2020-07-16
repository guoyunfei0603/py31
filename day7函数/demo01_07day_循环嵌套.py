"""
============================
Author:柠檬班-木森
Time:2020/7/14   20:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
python之禅：扁平胜于嵌套


print()的参数：

end="\n"


"""
# while循环嵌套
# while True:
#     num = int(input("请输入数字："))
#     n = 0
#
#     while n <= num:
#         print(n)
#         n += 1


# for循环嵌套
"""
*
* *
* * *
* * * *
* * * * *
* * * * * *
"""


# for i in range(1, 7):
#     print(f"第{i}行",end="")
#     for j in range(i):
#         print("*",end="")
#
#     print()


# for i in range(1, 10):
#     for j in range(i):
#         print("* ", end="")
#     print()


for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={:<4}".format(i, j, i * j), end="")
    print("\n")
