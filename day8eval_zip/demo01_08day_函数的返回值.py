"""
============================
Author:柠檬班-木森
Time:2020/7/16   20:16
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
函数的返回值：通过关键字return来定义
不写return或者return后面不写内容:返回None
return后面返回1个值：返回就是该数据
return后面返回1个以上值: 返回的是一个元组

注意点：函数执行到return就会结束函数的运行，并返回结果



"""


# li = [11, 22, 33]
# st1= "12345"
# 为什么append这个方法调用的之后，用变量接收不到结果（原因是因为append这个方法没有定义返回值）
# res = li.append(11)
# res2 = li.copy()
# st1.split()
# print(res)
# print(res2)


def add(a, b):
    """计算两个数相加并返回结果"""
    c = a + b
    # return c


#     return
#
#
# result = add(11, 22)
# print("函数调用之后的返回结果：", result)


def func(a, b):
    """计算两个数相加并返回结果"""
    c = a + b
    d = a - b
    return c, d


# result = func(11, 22)
# print("函数调用之后的返回结果：", result)


# ---------------------
# res1, res2 = func(11, 22)
# print(res1)
# print(res2)


# --------------------函数执行到return就会结束函数的运行，并返回结果---------------------------


def demo1(a, b):
    """计算两个数相加并返回结果"""
    c = a + b
    d = a - b
    print("-------------1-------------")
    if c == d:
        return c, d
    print("-------------2-------------")
    print("-------------3-------------")
    print("-------------4-------------")
    return 1111


res = demo1(11, 11)
