"""
============================
Author:柠檬班-木森
Time:2020/7/28   21:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest
from unittestreport import TestRunner,HTMLTestRunner

# 第一步：创建一个测试套件
suite = unittest.TestSuite()

# 第二步：将测试用例添加到测试套件中
# 2.1 创建加载器
loader = unittest.TestLoader()

# 2.2加载用例到套件
# 第一种：通过测试用例类去加载
from py31_13day.testcase.test_03login import TestLogin

suite.addTest(loader.loadTestsFromTestCase(TestLogin))

# 第三步：执行测试用例
# runner = unittest.TextTestRunner()
# runner.run(suite)

#  生成测试报告
runner = TestRunner(suite,
                    filename="musen.html",
                    report_dir=r"C:\project\py31_class\py31_01day",
                    title='python31的测试报告',
                    tester='小简老师',
                    desc="小简执行测试生产的报告",
                    templates=2)
runner.run()

# 生产HTMLTestRunnerNew风格的报告
# runner = HTMLTestRunner(stream=open("py31.html","wb"))
# runner.run(suite)



