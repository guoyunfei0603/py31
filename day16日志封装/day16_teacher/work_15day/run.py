"""
============================
Author:柠檬班-木森
Time:2020/8/1   10:23
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from unittestreport import TestRunner

# 加载套件
suite = unittest.defaultTestLoader.discover(r"C:\project\py31_class\py31_16day\work_15day\testcase")

# 执行用例
runner = TestRunner(suite)
runner.run()
