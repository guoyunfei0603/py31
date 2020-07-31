"""
============================
Author:小白31
Time:2020/7/31 23:54
E-mail:1359239107@qq.com
============================
"""
import unittest
import unittestreport
from day14ddt_opnpyxl.day14_work.testcase import test_register
suite = unittest.TestSuite()

loader = unittest.TestLoader()
# 模块加载用例
suite.addTest(loader.loadTestsFromModule(test_register))

runner = unittestreport.TestRunner(suite,filename="report.html",
                 report_dir=".",
                 title='测试报告',
                 tester='小白',
                 desc="小白执行测试生成的报告",
                 templates=1)
runner.run()

# 坑点！！
'''
1. __init__文件里面不要写代码，因为run文件执行的时候也会执行这里面的代码
2. 函数字典拆包是两个**
'''