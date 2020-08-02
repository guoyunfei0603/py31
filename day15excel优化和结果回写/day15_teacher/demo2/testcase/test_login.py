"""
============================
Author:柠檬班-木森
Time:2020/8/1   10:17
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from py31_15day.demo2 import myddt
from py31_15day.demo2.handle_excel import Excel
from py31_15day.demo2.login import login_check


"""
unittest：是通过用例执行是否出现 断言异常 来评判用例是否通过
"""

@myddt.ddt
class TestLogin(unittest.TestCase):
    excel = Excel(r"C:\project\py31_class\py31_15day\demo2\cases.xlsx", "login")
    cases = excel.read_data()

    @myddt.data(*cases)
    def test_login(self, item):
        # 准备数据
        data = eval(item["data"])
        expected = eval(item["expected"])
        # 获取用例所在表单的行号
        case_row = item["case_id"]+1
        # 调用功能函数
        res = login_check(**data)
        print("用例入参：{}".format(data))
        print("实际结果：{}".format(res))
        print("预期结果：{}".format(expected))
        try:
            # 断言
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_data(row=case_row, column=5, value="失败")
            self.excel.write_data(row=case_row, column=6, value=str(res))
            print("{}:用例执行失败，失败的信息如下：".format(item['title']))
            raise e
        else:
            self.excel.write_data(row=case_row, column=5, value="通过")
            self.excel.write_data(row=case_row, column=6, value=str(res))
            print("{}:用例测试执行通过！！！".format(item['title']))
