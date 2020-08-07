"""
============================
Author:柠檬班-木森
Time:2020/8/4   10:01
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import unittest

from py31_16day.demo2 import myddt
from py31_16day.demo2.handle_excel import Excel
from py31_16day.demo2.register import register
# from py31_16day.demo2.handle_log import create_logger
# log = create_logger()

from py31_16day.demo2.handle_log import log

@myddt.ddt
class RegisterTestCase(unittest.TestCase):
    excel = Excel(r"C:\project\py31_class\py31_16day\work_15day\cases.xlsx", "register")
    cases = excel.read_data()

    @myddt.data(*cases)
    def test_register(self, item):
        # 1、准备用例参数
        expected = eval(item["expected"])
        data = eval(item["data"])
        case_row = item["case_id"] + 1
        res = register(*data)
        print("用例入参：{}".format(data))
        print("实际结果：{}".format(res))
        print("预期结果：{}".format(expected))
        try:
            # 断言
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_data(row=case_row, column=5, value="失败")
            self.excel.write_data(row=case_row, column=6, value=str(res))
            log.error("用例--{}--执行失败".format(item['title']))
            log.exception(e)
            raise e
        else:
            self.excel.write_data(row=case_row, column=5, value="通过")
            self.excel.write_data(row=case_row, column=6, value=str(res))
            log.info("用例--{}--执行通过".format(item['title']))