"""
============================
Author:柠檬班-木森
Time:2020/7/28   21:16
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

import unittest


class TestRegister(unittest.TestCase):

    def test_01(self):
        """比对1和100"""
        print("-----------执行test_01------------")
        self.assertEqual(100, 100)

    def test_02(self):
        """比对1000和1000"""
        print("-----------执行test_02------------")
        self.assertEqual(1000, 1000)

    def setUp(self):
        # 每条测试用例执行之前都会调用该方法（有多少用例执行多少次）
        print("-------------setup----------")

    def tearDown(self):
        # 每条测试用例执行之后都会调用该方法（有多少用例执行多少次）
        print("-------------tearDown----------")

    @classmethod
    def setUpClass(cls):
        # 测试类里面的用例执行之前会调用该方法（只会执行一次）
        print("-------------setUpClass----------")

    @classmethod
    def tearDownClass(cls):
        # 测试类里面的用例执行之后会调用该方法（只会执行一次）
        print("-------------tearDownClass----------")

if __name__ == '__main__':
    unittest.main()