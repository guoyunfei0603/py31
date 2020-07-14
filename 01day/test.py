# -*- coding: utf-8 -*-
# @Time    : 2020/6/24 15:35
# @Author  : guoyunfei.0603
# @File    : day6笔记.py

# 创建一个学生测试类
class student:
    # 类变量
    new_age = 11
    '''
    类变量和实例变量的区别在于：类变量是所有对象共有，其中一个对象将它值改变，其他对象得到的就是改变后的结果；
    而实例变量则属对象私有，某一个对象将其值改变，不影响其他对象
    '''

    def __init__(self, stu_name, stu_sex, stu_age):
        # 实例变量 可以通过创建实例调用，也可以通过类名().
        self.stu_name = stu_name
        self.stu_sex = stu_sex
        self.stu_age = stu_age

    # 显示姓名，性别，年龄
    def show_info(self):
        return self.stu_name , self.stu_sex , self.stu_age

    def age(self):
        return int(self.stu_age) + int(student.new_age)

# 创建一个实例s1, 传入必要的参数
# 可以创建多个实例s1,s2,s3,,,  实例s1 相当于self

s1 = student("小白","男", 12)
s2 = student("小黑","男",17)

# 打印的结果是一个地址
print(s1) # 0x000001B888B73D08
print(s2) # 0x000001B888B73D88

# 打印类变量
print("类变量：",student.new_age)

# 打印实例变量
print("实例变量：",s1.stu_age)

# 打印s1的信息
print(s1.show_info())

# 打印年龄
print(s1.age())

print(s1.__dict__)