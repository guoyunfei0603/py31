"""
============================
Author:小白31
Time:2020/7/30 6:50
E-mail:1359239107@qq.com
============================
"""
import unittest
from day13unittest初识.register import register

'''
   注册成功               返回结果：{"code": 1, "msg": "注册成功"}
   有参数为空，            返回结果 {"code": 0, "msg": "所有参数不能为空"}   
   两次密码不一致          返回结果：{"code": 0, "msg": "两次密码不一致"}
   账户已存在              返回结果：{"code": 0, "msg": "该账户已存在"}
   密码不在6-18位之间      返回结果：{"code": 0, "msg": "账号和密码必须在6-18位之间"}              
'''

'''为了控制用例执行顺序,以数字代替'''
class TestRegister(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_register_01(self):
        '''正确的注册'''
        # 第一步：准备用例数据
        # 1.1用例的输入数据（参数）
        # ------注意------参数名称要一一对应，否则函数拆包传入的参数有误！！
        data = {"username": "xiaobai", "password1": "lemonban", "password2": "lemonban"}

        # 1.2预期结果
        expected = {"code": 1, "msg": "注册成功"}
        # 第二步：调用被测的功能函数(请求接口)，传入参数
        res = register(**data)
        # 第三步：比对预期结果和实际结果（断言）
        self.assertEqual(expected, res)

    def test_register_02(self):
        '''账号为空'''
        data = {"username": "", "password1": "lemonban", "password2": "lemonban"}
        expected = {"code": 0, "msg": "所有参数不能为空"}
        res = register(**data)
        self.assertEqual(expected, res)

    def test_register_03(self):
        '''两次密码不一致'''
        data = {"username": "python02", "password1": "lemonban2", "password2": "lemonban"}
        expected = {"code": 0, "msg": "两次密码不一致"}
        res = register(**data)
        self.assertEqual(expected, res)

    def test_register_04(self):
        '''账号已存在'''
        data = {"username": "xiaobai", "password1": "lemonban", "password2": "lemonban"}
        expected = {"code": 0, "msg": "该账户已存在"}
        res = register(**data)
        self.assertEqual(expected, res)

    def test_register_05(self):
        '''密码不在6~18位'''
        data = {"username": "python03", "password1": "lem", "password2": "lem"}
        expected = {"code": 0, "msg": "账号和密码必须在6-18位之间"}
        res = register(**data)
        self.assertEqual(expected, res)



# if __name__ == '__main__':
#     unittest.main()
#     print()
