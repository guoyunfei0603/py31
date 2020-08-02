"""
============================
Author:小白31
Time:2020/8/2 23:01
E-mail:1359239107@qq.com
============================
"""
import unittest
import unittestreport
# 创建一个测试套件
suite = unittest.TestSuite()
# 创建一个加载器
loader =unittest.TestLoader()
# 把testcase下面的测试用例添加到suite
suite.addTest(loader.discover(r"D:\py31\git_code\py31\day15excel优化和结果回写\day15home_work\testcase"))

runner = unittestreport.TestRunner(suite)
runner.run()
