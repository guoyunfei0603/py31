"""
============================
Author:小白31
Time:2020/7/30 6:47
E-mail:1359239107@qq.com
============================
"""
import unittest
from unittestreport import TestRunner
# 1. 创建测试用例套件
suite = unittest.TestSuite()

# 2. 创建一个加载器
loader = unittest.TestLoader()
# 2.1 第三种：指定用例所在文件路径去加载(用例文件要以test开头)
suite.addTest(loader.discover(r'D:\py31\git_code\py31\day13unittest初识\testcase'))
# 3. 运行用例
runner = TestRunner(suite,
                 filename="xbreport.html",
                 report_dir=".",
                 title='测试报告',
                 tester='小白',
                 desc="小白执行测试生产的报告",
                 templates=1)


runner.run()