"""
============================
Author:小白31
Time:2020/8/2 23:29
E-mail:1359239107@qq.com
============================
"""
import unittest
from tools.hand_excel import HandExcel
from day15excel优化和结果回写.day15home_work.register import register
from tools import myddt



@myddt.ddt
class TestLogin(unittest.TestCase):
    # 测试用例数据
    excel = HandExcel(r"D:\py31\git_code\py31\day15excel优化和结果回写\day15home_work\case_data.xlsx", "register")

    testdata = excel.read_excel()
    print(testdata)
    @myddt.data(*testdata)
    def test_register(self, item):
        # 测试数据
        data = eval(item["data"])
        # 预期结果
        expected = eval(item["expected"])
        # 实际结果
        res = register(**data)
        # 断言
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            self.excel.write_excel(row=item["case_id"] + 1, col=5, value="failed")
            print("{}: 用例执行失败，错误信息:{}".format(item["title"], e))
            raise e
        else:
            self.excel.write_excel(row=item["case_id"] + 1, col=5, value="pass")
            print("{}: 用例执行通过".format(item["title"]))


if __name__ == '__main__':
    unittest.main()