"""
============================
Author:柠檬班-木森
Time:2020/7/25   9:58
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
类属性：
    公有属性：
    私有属性:__开头 或者_开头的叫私有属性，不能再类外部使用，只能在类里面使用

私有方法：
    __开头 或者_开头
    
"""


class MyClass:
    attr = 100
    _attr = 200  # 在外部可以访问，但是不要在内外部使用
    __attr2 = 999  # 强制拒绝外部访问

    def __func(self):
        print('---func---')


print(MyClass.attr)
print(MyClass._attr)
m = MyClass()


# print(MyClass.__attr2)  # 不能再类外部使用
import  requests