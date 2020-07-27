"""
============================
Author:小白31
Time:2020/7/27 22:10
E-mail:1359239107@qq.com
============================
"""
'''
1：简单题
    1、函数的形参有哪几种定义形式？
    3、函数的实参有哪几种形式？

2、利用上课讲的for循环嵌套的知识点，封装一个可以打印任意比列三角形的函数
(注意点：和上课的有区别，这个是倒三角)
* * * * * *
* * * * *
* * * *
* * * 
* * 
* 
'''


def test1(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end='')

        print()


# test1(6)
'''
3、定义一个可以完成任意个数字相加的函数（支持关键字传参和位置传参），并返回相加结果。
要求:调用函数传入1个数字，返回值为这个数字。                                      
        如：func(1) ---->   返回 1
    调用函数传入2个数字，返回值为2个数相加的结果。                            
        如：func(11,22) ---->   返回33
    调用函数传入3个数字，返回值为3个数相加的结果。                            
        如：func(11,22,33,) ----> 返回66
    调用函数传入n个数字，返回值为n个数相加的结果。                             
        如：func(1,2,3,4,5) ----> 返回 15
（提示：可以使用不定长参数来接收参数，对参数进行遍历再相加）
'''


def test2(*args, **kwargs):
    he = 0
    for i in args:
        he += i

    for j in kwargs.values():
        he += j
    print(he)


# test2(1, 2, 3, a=10)
#  获取字典中值大于30的键值对，放到一个新的字典中
def test3():
    dic = {"aa": 11, "bb": 22, "cc": 33, "dd": 44}

    new_dic = {}
    for k, v in dic.items():
        if v > 30:
            new_dic[k] = v
    print(new_dic)


#  获取列表值大于30的，放到一个新的列表中
def test4():
    li = [11, 22, 33, 44, 55, 66, 77, 88, 99]

    new_li = []
    for i in li:
        if i > 30:
            new_li.append(i)
    print(new_li)
    # lambda 简洁的代码
    res = filter(lambda x: x > 30, li)
    print(list(res))
test4()

# -----------------------学习 zip -------------------
def test5():
    pass
