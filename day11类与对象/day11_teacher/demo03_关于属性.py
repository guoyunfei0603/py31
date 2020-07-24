"""
============================
Author:柠檬班-木森
Time:2020/7/23   20:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类属性：直接定义在类里面的变量（该类事物共有的属性，所有对象属性值都是一样的）
    可以通过类直接去访问
    也可以通过对象去访问
    

对象(实例)属性：
    1、实例属性的定义：对象.属性名 = 属性值
    2、每个对象属性值有可能是不一样的
    3、每个对象自己的属性，只能通过对象自己去访问、
    4、不能通过类去访问的
    

__init__方法：初始化方法：
    init方法定义了几个参数，创建对象的时候就要传几个参数(self除外)
  


self是什么：代表对象自己，那个对象调用方法，就代码那个


"""


class Cat:
    # 猫的相关特征
    attr1 = "喵喵叫"
    attr2 = "有尾巴"
    attr3 = "爱吃鱼"

    def __init__(self, name, age, sex):
        # 给对象初始化属性
        self.name = name
        self.age = age
        self.sex = sex


# --------------------类属性-----------------------
# tom = Cat()
# dd = Cat()
# # 通过类去访问类属性
# print(Cat.attr1)
#
# # 通过对象去访问类属性
# print(tom.attr2)
# print(dd.attr2)


# ---------------实例属性----------------
# tom.name ="汤姆"
# tom.age = 18
# tom.sex = "公"
#
# dd.name = "叮当"
# dd.age = 5
# dd.sex = "母"
tom = Cat("汤姆", 18, "公")
dd = Cat("叮当", 5, "母")
print(dd.name, dd.age, dd.sex)
print(tom.name, tom.age, tom.sex)


