"""
============================
Author:柠檬班-木森
Time:2020/7/25   10:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
在子类的方法中调用被重新过的父类方法：
     # 方式一：父类名.方法名(self)
     # 方式二：super().base_func()
     
应用场景：
    父类中原有的方法不能满足当前的需求，需要对父类中的方法进行扩展


"""


class BaseClass(object):

    def __init__(self, name,sex):
        self.name = name
        self.sex = sex


class MyClass(BaseClass):

    def __init__(self, name, sex,age):
        # 调用父类的方法
        super().__init__(name,sex)
        # 重写之后扩展的功能代码
        self.age = age

    def func(self):
        pass


a = MyClass("木森",'男', 18)

print(a)

"""
开放封闭原则：
已经实现的功能不要进行修改（对修改是封闭的）
对功能的扩展是开放的




"""