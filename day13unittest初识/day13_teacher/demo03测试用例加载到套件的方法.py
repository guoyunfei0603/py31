"""
============================
Author:柠檬班-木森
Time:2020/7/28   21:39
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from unittestreport import TestRunner

# 第一步：创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例添加到测试套件中
# 2.1 创建加载器
loader = unittest.TestLoader()

# 2.2加载用例到套件
# 第一种：通过测试用例类去加载
# from py31_13day.testcase.test_login import TestLogin
# suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# 第二种：通过测试用例模块去加载
# from py31_13day.testcase import test_login
# suite.addTest(loader.loadTestsFromModule(test_login))

# 第三种：指定用例所在文件路径去加载(用例文件要以test开头)
"""
用例加载的的过程：
1、先找指定路径中test开头的python文件，
2、再找test开头文件中继承unittest.TestCase的用例类
3、再去找用例类中以test开头的方法
"""
suite.addTest(loader.discover(r"C:\project\py31_class\py31_13day\testcase"))

# 第三步：执行测试用例
runner = TestRunner(suite)
runner.run()
