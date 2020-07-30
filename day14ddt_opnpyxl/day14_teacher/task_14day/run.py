import unittest
from unittestreport import TestRunner

# # 创建测试套件
# suite = unittest.TestSuite()
#
# # 添加一个模块中所有的测试用例
# loader = unittest.TestLoader()
#
# suite.addTest(loader.discover(r"C:\project\py31_class\py31_14day\task_14day\testcase"))


#  实际工作中可以通过这个方式来加载
suite = unittest.defaultTestLoader.discover(r"C:\project\py31_class\py31_14day\task_14day\testcase")

# 生成html文件的的测试报告
runner = TestRunner(suite)
runner.run()
