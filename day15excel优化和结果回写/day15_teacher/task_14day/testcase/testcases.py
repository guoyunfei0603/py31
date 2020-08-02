import unittest
import ddt
from py31_15day.task_14day.login import login_check
from py31_15day.task_14day.handle_excel import Excel


@ddt.ddt
class LoginTestCase(unittest.TestCase):
    excel = Excel("cases.xlsx", "login")
    case_data = excel.read_data()

    @ddt.data(*case_data)
    def test_login(self, case):
        # 第一步：准备用例的数据
        # 预期结果：
        excepted = eval(case["expected"])
        # 参数：data
        data = eval(case["data"])
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = login_check(**data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(excepted, res)


"""
编写测试用例类的思路和流程：
1、定义测试类，再定义一个测试方法
2、去excel中读取用例数据
3、通过DDT实现数据驱动
4、实现用例内部的逻辑

"""


# @ddt.ddt
# class RegisterTestCase(unittest.TestCase):
#     excel2 = Excel("cases.xlsx", "register")
#     register_data = excel2.read_data()
#
#     @ddt.data(*register_data)
#     def test_register(self, case):
#         # 第一步：准备用例数据
#         data = eval(case["data"])
#         expected = eval(case["expected"])
#         # 第二步：调用功能函数（请求接口），获取实际结果
#
#         # 第三步：比对预期结果和实际结果
