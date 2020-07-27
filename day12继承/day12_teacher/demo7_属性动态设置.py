"""
============================
Author:柠檬班-木森
Time:2020/7/25   11:08
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
# 动态设置属性
setattr(obj,属性名,属性值)：在代码执行的过程中给 类/对象 设置属性（属性不存在就是添加，存在就是修改）

getattr(obj,属性名,默认值):在代码执行的过程中获取 类/对象 属性

delattr(obj,属性名) :在代码执行的过程中删除 类/对象 属性


__dict__:获取所有的属性
"""


class BaseClass(object):

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age


# 动态设置类属性
# BaseClass.attr = 18
# BaseClass.attr2 = "木森"
# setattr(BaseClass,"attr",18)

# 如何将变量的值设置为类属性名？
# var = input("请输入属性名：")
# value = 8890
# setattr(BaseClass,var,value)
# 可以查看所有的属性
# print(BaseClass.__dict__)
# b1 = BaseClass("木木", "男")
# ------------------设置属性----------------
# # 给对象设置属性
# setattr(b1, "age", 999)
# print(b1.__dict__)

# ------------------访问属性----------------
# b1 = BaseClass("木木", "男")
# # 需求：根据用户的输入的属性名，获取对应的属性值
# item = input("请输入属性名：")
# res = getattr(b1, item,None)
# print(res)

# ——-------------属性删除-----------
b1 = BaseClass("木木", "男",18)
# 需求：根据用户的输入的属性名，删除对应的属性值
item = input("请输入属性名：")
delattr(b1, item)
print(b1.__dict__)


# b1 = BaseClass("木木", "男", 18)
# b1.aa = 11
# b1.bb = 99
# print(b1.__dict__)


# # 需求：打印name之外的所有属性
# keys = b1.__dict__.keys()
# for key in keys:
#     if key != "name":
#         print(getattr(b1, key))
#
# print(b1.__dict__)
