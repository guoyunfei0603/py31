"""
============================
Author:柠檬班-木森
Time:2020/7/23   20:44
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类的定义：
class 类名：
    # 该类事物共有的行为和特征
    
    
特征：属性
    类属性：直接定义在类里面的变量（该类事物共有的特征，所有对象特征值都是一样的）
    
    对象(实例)属性：
        对象自己的一些属性(和类里面的其他对象属性值有可能是不一样的)
    
    
    
行为：方法（类里面的函数）


创建对象:类名()
  
# 字符串、列表




万物皆对象：
a = "python"  # a保存的是一个字符串对象  str
b = [11,22,33,44],  b保存的是一个列表对象  list





"""


class Cat:
    # 猫的相关特征
    attr1 = "喵喵叫"
    attr2 = "有尾巴"
    attr3 = "爱吃鱼"

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def skill1(self):
        # 行为2
        print("抓老鼠")

    def skill2(self):
        # 行为2
        print("会爬树")


# 类名():创建对象(实例化)
kt = Cat("hello KT", 2)

dd = Cat("叮当猫", 5)
