"""
============================
Author:小白31
Time:2020/7/24 23:26
E-mail:1359239107@qq.com
============================
"""
'''
try：
    可能出现错误的代码
    1、涉及用户输入
    2、涉及到文件操作
    3、涉及到网络请求
except Exception as e:
    print(e)
finally:
    必定会执行的代码
 
'''

'''
类的定义：
class 类名：
    # 该类事物共有的行为和特征
       
特征：属性
    类属性：直接定义在类里面的变量
    
    对象(实例)属性：
        对象自己的一些属性
行为：方法（类里面的函数）

创建对象:类名()
'''

'''
类属性：直接定义在类里面的变量（该类事物共有的属性，所有对象属性值都是一样的）
    可以通过类直接去访问
    也可以通过对象去访问
    

对象(实例)属性：
    1、实例属性的定义：对象.属性名 = 属性值
    2、每个对象属性值有可能是不一样的
    3、每个对象自己的属性，只能通过对象自己去访问
    4、不能通过类去访问的
    

__init__方法：初始化方法：
    init方法定义了几个参数，创建对象的时候就要传几个参数(self除外)

self是什么：实例本身
'''
'''
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
'''