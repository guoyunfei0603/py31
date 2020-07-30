import unittest
import ddt
from py31_14day.task_14day.register import register

case_data = [
    {"excepted": {"code": 1, "msg": "注册成功"}, "data": ('python3', '123456', '123456')},
    {"excepted": {"code": 0, "msg": "两次密码不一致"}, "data": ('python4', '1234567', '123456')},
    {"excepted": {"code": 0, "msg": "该账户已存在"}, "data": ('python31', '123456', '123456')},
]


@ddt.ddt
class RegisterTestCase(unittest.TestCase):
    @ddt.data(*case_data)
    def test_register(self, case):
        """正常注册"""
        # 第一步：准备用例的数据
        # 预期结果：
        excepted = case["excepted"]
        # 参数：data
        data = case["data"]
        # 第二步：调用被测试的功能函数，传入参数，获取实际结果：
        res = register(*data)
        # 第三步：断言（比对预期结果和实际结果）
        self.assertEqual(excepted, res)

    # li = [111, 222, 333]
    #
    # @ddt.data(*li)
    # def test_register(self, case):
    #     """正常注册"""
    #     print("-----测试用例-----case:{}---".format(case))


if __name__ == '__main__':
    unittest.main()
