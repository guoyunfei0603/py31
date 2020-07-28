"""
============================
Author:柠檬班-木森
Time:2020/7/28   20:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
多继承：一个类同时继承多个父类


"""


class Base:
    attr = 100


class User:
    attr = 1000000
    attr2 = 2000000


class MyClass(Base, User):
    pass


print(MyClass.attr)
print(MyClass.attr2)
