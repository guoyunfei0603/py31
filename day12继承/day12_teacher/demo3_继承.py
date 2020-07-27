"""
============================
Author:柠檬班-木森
Time:2020/7/25   10:07
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类的定义形式：

# 默认继承与object
class 类名：
    pass
    
    
class 类名(继承的父类):
    pass

object（基类）:python中所有类的祖宗（所有的类都继承于他）


继承：子类通过继承能够拥有父类的属性和方法（__开头的私有属性和方法除外）




"""


# class MyTest:
#     pass
#
#
# class MyClass(object):
#     pass

class BaseClass:
    attr = "base"

    def func(self):
        print("----base---func-")


class MyClass(BaseClass):

    def func2(self):
        print("------子类自己的方法-----")


m = MyClass()

print(m.attr)
m.func()
m.func2()




