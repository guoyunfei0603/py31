"""
============================
Author:柠檬班-木森
Time:2020/7/14   22:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
1：简答题
    1、函数的形参有哪几种定义形式？
        必需参数：
        默认参数：
        不定长参数：*args  和 **kwargs
    2、函数的实参有哪几种形式？
        位置传参
        关键字传参
"""

"""
2、利用上课讲的for循环嵌套的知识点，封装一个可以打印任意比列三角形的函数
(注意点：和上课的有区别，这个是倒三角)

* * * * * *
* * * * *
* * * *
* * * 
* * 
* 

"""


def print_triangle(n):
    for i in range(n, 0, -1):
        for j in range(i):
            print("* ", end="")
        print()


print_triangle(6)
"""
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


"""


def add_number(*args, **kwargs):
    # 定义一个初始变量为零
    s = 0
    # 遍历参数进行累加
    for n in args:
        s += n
    for n in kwargs.values():
        s += n
    print(s)



add_number(1, 2, 3, a=4, b=5, c=99, d=100)
