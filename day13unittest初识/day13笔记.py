"""
============================
Author:小白31
Time:2020/7/30 7:35
E-mail:1359239107@qq.com
============================
"""
'''
多继承，不常用
一个类同时继承多个父类
'''
#---------------------------重点-----------------------------------
'''
unittest四大核心概念:

TestCase:测试用例
    测试用例类：测试用例以类的形式去定义，并且一定要继承unittest.TestCase
    测试用例方法：用例类里面每一个以test开头的方法，就是一条测试用例

TestSuite:测试套件(集合)

TestRunner:测试运行程序

fixture:测试夹具（测试的前置后置条件处理）

测试步骤：
    def test_login_pass(self):
        """登录成功的用例"""
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        data = {"username": "python31", "password": "lemonban"}
        # 1.2预期结果
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = login_check(**data)

        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)
'''

# 用例执行顺序：
"""
1、模块按照ASCII排序
2、类名按照ASCII排序
3、方法名按照ASCII排序
"""