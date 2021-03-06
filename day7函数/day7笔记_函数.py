# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 17:14
# @Author  : guoyunfei.0603
# @File    : day7笔记_函数.py

# for i in range(1, 7):
#     print(f"第{i}行",end="")
#     for j in range(i):
#         print("*",end="")
#
#     print()

#
# for i in range(1, 10):
#     for j in range(i):
#         print("* ", end="")
#     print()





'''
函数的定义： 关键字def
函数：可以用对重复使用的功能代码进行封装，提高代码的复用性，提高工作效率，降低代码的耦合性

def 函数的名字():
    函数的功能代码


函数名命名规范：
    1、变量只能使用数字、字母、下划线组成
    2、变量不能使用数字开头
    3、不能使用python中的关键字(内置函数，官方库，第三库的名字统统不要用)
命名风格：
    推荐使用下划线命名法


# 定义好的函数，不会执行运行，需要调用才会执行函数内部的代码

已经学过的内置函数：
print():输出
input():输入
id():获取数据的内存地址
type():获取数据的类型
'''

def fun1(n):
    for i in range(n):
        for j in range(i+1):
            print("* ", end="")
        print()

fun1(5)

'''
函数的参数：定义函数的时候，可以在后面的括号中定义参数 
函数的参数类型：

形参：定义的参数称为：形参
    三种定义形式：
        1、必需参数（必备参数）：定义了就一定(必须)要传，不能多也不能少
        2、默认参数（缺省参数）：定义的时候可以设置默认值,调用的时候可以传，也可以不传，不传使用默认值
        3、不定长参数（动态\可变参数）：可以接受0个或者多个参数
            *args:只能接收位置传参，以元组的形式保存
            **kwargs:只能接受关键字传参，以字典的形式保存
            
实参：调用实际的传递的为：实参
    两种形式：
        1、位置传参（位置参数）:按照参数定义的位置进行传递
        2、关键字传参（关键字参数）:通过参数名字，指定传递

注意点：如果使用两种形式混合传递参数：先写位置参数，再写关键字参数（不然就会报错）

'''

def add_fun(a,b,c=10):
    print(a+b+c)
add_fun(10,11)

'''函数拆包

*: 
    *加在形参前面（定义函数参数的时候使用），接收不定长的位置参数，转换为元祖
    *加在实参前面（调用函数参数的时候使用），可以将元祖(列表)拆包成多个位置参数
**:
    **加在形参前面（定义函数参数的时候使用），接收不定长的关键字参数，转换为字典
    **加在实参前面（调用函数参数的时候使用），可以将字典拆包成多个关键字参数

'''
def fun1(*args,**kwargs):
    print(args)

tu = (111,222,333)
fun1(*tu)
def fun2(**kwargs):
    print(kwargs)

dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
fun2(**dic)