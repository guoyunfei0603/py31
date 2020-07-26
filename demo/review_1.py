"""
============================
Author:小白31
Time:2020/7/26 20:20
E-mail:1359239107@qq.com
============================
"""


# 随机生成 10个131 开头的手机号
def test_1():
    import random

    li = []
    for i in range(1, 11):
        res = random.randint(13100000000, 13199999999)
        li.append(res)
    print(li)

# 列表反转
def test_2():
    t = [17,'hello',90,6611,99]
    t.reverse()

    print(t)
