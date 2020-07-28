"""
============================
Author:柠檬班-木森
Time:2020/7/28   20:32
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
unittest四大核心概念:

TestCase:测试用例
    测试用例类：测试用例以类的形式去定义，并且一定要继承unittest.TestCase
    测试用例方法：用例类里面每一个以test开头的方法，就是一条测试用例

TestSuite:测试套件(集合)

TestRunner:测试运行程序

fixture:测试夹具（测试的前置后置条件处理）
"""
import unittest
from py31_13day.login import login_check


class TestLogin(unittest.TestCase):
    """登录的测试用例类"""

    def test_login_pass(self):
        """登录成功的用例"""
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        data = {"username": "python31", "password": "lemonban"}
        # 1.2预期结果
        expected = {"code": 0, "msg": "登录成功"}

        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = login_check(**data)

        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_login_pwd_error(self):
        """密码错误"""
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        data = {"username": "python31", "password": "lemonban111"}
        # 1.2预期结果
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = login_check(**data)

        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_login_pwd_is_none(self):
        """密码为空"""
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        data = {"username": "python31", "password": ""}
        # 1.2预期结果
        expected = {"code": 1, "msg": "所以的参数不能为空"}
        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = login_check(**data)
        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_login_user_is_none(self):
        """账号为空"""
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        data = {"username": "", "password": "lemonban"}
        # 1.2预期结果
        expected = {"code": 1, "msg": "所以的参数不能为空"}
        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = login_check(**data)
        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_login_user_error(self):
        """账号错误"""
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        data = {"username": "pytho1111", "password": "lemonban"}
        # 1.2预期结果
        expected = {"code": 1, "msg": "账号或密码不正确"}
        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = login_check(**data)
        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()


# 大家先安装一下：pip install unittestreport （生成测试报告用的）