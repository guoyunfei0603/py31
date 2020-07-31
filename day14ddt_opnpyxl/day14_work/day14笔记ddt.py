"""
============================
Author:小白31
Time:2020/8/1 0:26
E-mail:1359239107@qq.com
============================
"""
'''
ddt 是第三方模块，需安装， pip install ddt

DDT包含类的装饰器ddt和两个方法装饰器data（直接输入测试数据）

通常情况下，data中的数据按照一个参数传递给测试用例，如果data中含有多个数据，以元组，列表，字典等数据，需要自行在脚本中对数据进行分解或者使用unpack分解数据。
'''
# import ddt
# @ddt.ddt
# class RegisterTestCase(unittest.TestCase):
#     @ddt.data(*case_data)
#     def test_register(self, case):
# li = [111, 222, 333]
#
# @ddt.data(*li)
# def test_register(self, case):
#     """正常注册"""
#     print("-----测试用例-----case:{}---".format(case))