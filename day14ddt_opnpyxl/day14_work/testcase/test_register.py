"""
============================
Author:小白31
Time:2020/7/31 23:12
E-mail:1359239107@qq.com
============================
"""
import unittest
from day14ddt_opnpyxl.day14_work.register1 import register
from day14ddt_opnpyxl.day14_teacher.demo02_excel的操作.demo5_read_excel封装2 import Excel
import ddt

# 从excel读取的测试数据
testdata = Excel(r"D:\py31\git_code\py31\day14ddt_opnpyxl\day14_work\testdata.xlsx", "register").read_data()
print("测试数据：",testdata)
# testdata = [
#     {"expected": {"code": 1, "msg": "注册成功"}, "data": ('python3', '123456', '123456')},
#     {"expected": {"code": 0, "msg": "两次密码不一致"}, "data": ('python4', '1234567', '123456')},
#     {"expected": {"code": 0, "msg": "该账户已存在"}, "data": ('python31', '123456', '123456')},
# ]


# for item in testdata:
#     print(item["data"])

@ddt.ddt
class TestRegister(unittest.TestCase):
    @ddt.data(*testdata)
    def test_case(self,item):
        """测试标题"""
        # title = item["title"]

        # 测试数据
        data = eval(item["data"])
        # 预期结果
        expected = eval(item["expected"])
        # 调用被测方法，获取实际结果
        res = register(**data)
        # 比对
        self.assertEqual(expected,res)

if __name__ == '__main__':
    unittest.main()