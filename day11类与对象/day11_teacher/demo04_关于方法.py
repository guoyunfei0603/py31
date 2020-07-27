"""
============================
Author:柠檬班-木森
Time:2020/7/23   20:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
""" 
方法(类里面的函数):

    实例(对象)方法：
        方法的第一个参数是self，self代表的是对象自己
        只能通过对象去调用(注意：类不能调用对象方法)
        
        适用场景：方法中会用到实例的属性或者方法，适合定义为实例方法

    类方法：在定义的方法前面加一个@classmethod
        类方法的第一个参数，通常为定义为cls,cls代表的是类本身
        可以通过类去调用，也可以通过对象去调用
        类方法里面既不会使用到对象属性，也不会调用对象的方法
        
        适用场景：方法中不会用到实例的属性或者方法，
        有可能会用到类的属性或者方法，适合定义为类方法
        
    静态方法：在定义的方法前面加一个@staticmethod
    
    

    __init__方法：在创建对象的时候自动调用的


class Girl:
    sex = 女
    

    def __init__(self,name,age,height):
        passs
        
    def skill1(self):
        pass


"""


class Cat:
    attr = "喵喵喵"

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def skill1(self):
        """
        通过实例方法中会用到实例的属性或者方法
        :return:
        """
        self.move()
        print(f"{self.name}在抓老鼠")

    def skill2(self):
        # 行为2
        print(f"{self.name}会爬树")

    def move(self):
        print(f"{self.name}在移动")

    @classmethod
    def func_cls(cls):
        print(f"这个类有一个属性是{cls.attr}")


# 类名():创建对象(实例化)
kt = Cat("hello KT", 2)
dd = Cat("叮当猫", 5)

# 类不能调用
# Cat.skill1()
# kt.skill1()
# dd.skill1()

# 通过类调用类方法
Cat.func_cls()

# 通过对象调用类方法
dd.func_cls()


s = 'assa\taaa'
s2 = repr(s)
print(s2)