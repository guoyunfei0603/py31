"""
============================
Author:柠檬班-木森
Time:2020/7/25   10:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
重写父类方法：在子类中定义一个和父类同名的方法

在子类的方法中调用被重新过的父类方法：
     方式一：父类名.方法名(self)
     # 方式二：super().base_func()

# 父类是不能使用子类的方法和属性的


"""


class Base(object):

    def base_func(self):
        print("----Base--------base__func-------------")


class A(Base):

    def base_func(self):
        # 方式一：父类名.方法名(self)
        Base.base_func(self)
        # 方式二：super().base_func()
        super().base_func()
        print("____A___-----base__func----")


a = A()

a.base_func()