"""
============================
Author:小白31
Time:2020/8/2 22:43
E-mail:1359239107@qq.com
============================
"""
import unittest
from tools.hand_excel import HandExcel
from day15excel优化和结果回写.day15home_work.login import login_check
from tools import myddt


@myddt.ddt
class TestLogin(unittest.TestCase):
    # 测试用例数据
    excel = HandExcel(r"D:\py31\git_code\py31\day15excel优化和结果回写\day15home_work\case_data.xlsx", "login")

    testdata = excel.read_excel()
    @myddt.data(*testdata)
    def test_login(self, item):
        # 测试数据
        data = eval(item["data"])
        # 预期结果
        expected = eval(item["expected"])
        # 实际结果
        res = login_check(**data)
        # 断言
        try:
            self.assertEqual(expected, res)
        except AssertionError as e:
            '''
            类属性：直接定义在类里面的变量（该类事物共有的属性，所有对象属性值都是一样的）
                    可以通过类直接去访问
                    也可以通过对象去访问 
            所以可以 self.excel调用
            '''
            self.excel.write_excel(row=item["case_id"] + 1, col=5, value="failed")
            print("{}: 用例执行失败，错误信息:{}".format(item["title"], e))
            raise e
        else:
            self.excel.write_excel(row=item["case_id"] + 1, col=5, value="pass")
            print("{}: 用例执行通过".format(item["title"]))


if __name__ == '__main__':
    unittest.main()
