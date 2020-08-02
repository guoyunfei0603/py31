import unittest
from unittestreport import TestRunner

#  实际工作中可以通过这个方式来加载
suite = unittest.defaultTestLoader.discover(r"C:\project\py31_class\py31_15day\task_14day\testcase")

# 生成html文件的的测试报告
runner = TestRunner(suite)
runner.run()
