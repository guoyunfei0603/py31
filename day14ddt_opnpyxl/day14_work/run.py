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

suite.addTest(loader.loadTestsFromModule(test_register))

runner = unittestreport.TestRunner(suite)
runner.run()