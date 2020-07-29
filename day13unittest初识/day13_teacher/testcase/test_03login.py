"""
============================
Author:柠檬班-木森
Time:2020/7/28   21:15
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest
from day13unittest初识.day13_teacher.login import login_check


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