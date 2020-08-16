"""
============================
Author:小白31
Time:2020/8/12 22:13
E-mail:1359239107@qq.com
============================
"""
# 1、必做题：使用requests请求接口文档中的接口(任选6个接口进行请求)，
# 提交代码（请求头使用X-Lemonban-Media-Type":"lemonban.v1）这种不需要鉴权的方式

import requests
from jsonpath import jsonpath


class test_api:
    # 域名
    url = 'http://api.lemonban.com/futureloan'

    # 请求头
    def headers_v1(self):
        headers_v1 = {"X-Lemonban-Media-Type": "lemonban.v1",
                      "content-type": "application/json"}

        return headers_v1

    # 注册接口
    def register(self):
        register_url = self.url + "/member/register"
        data = {"mobile_phone": "13012341230", "pwd": "lemon123456"}
        res = requests.post(url=register_url, json=data, headers=self.headers_v1())
        return res

    # 登录接口
    def login(self):
        login_url = self.url + "/member/login"
        data = {"mobile_phone": "13012341230", "pwd": "lemon123456"}
        res = requests.post(url=login_url, json=data, headers=self.headers_v1())
        id = jsonpath(res.json(), '$..id')
        return id[0]  # 取到登录后json数据里面的id字段

    # 充值接口
    def recharge(self):
        recharge_url = self.url + "/member/recharge"
        data = {"member_id": self.login(), "amount": "1080"}
        res = requests.post(url=recharge_url, json=data, headers=self.headers_v1())

        return res

    # 提现接口
    def withdraw(self):
        withdraw_url = self.url + "/member/withdraw"
        data = {"member_id": self.login(), "amount": "500"}
        res = requests.post(url=withdraw_url, json=data, headers=self.headers_v1())

        return res

    # 更新昵称
    def update_name(self):
        update_url = self.url + "/member/update"
        data = {"member_id": self.login(), "reg_name": "小白"}
        res = requests.patch(url=update_url, json=data, headers=self.headers_v1())

        return res

    # 用户信息
    def get_userinfo(self):
        update_url = self.url + "/member/2074984/info"
        res = requests.get(url=update_url,headers = self.headers_v1())
        return res

test = test_api()
# reg = test.register()
# print(reg.json())# {'code': 0, 'msg': 'OK', 'data': {'id': 2074984, 'reg_name': '小柠檬', 'mobile_phone': '13012341230'}, 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
# login = test.login()
# print(login)
# rec = test.recharge()
# print(rec.json())
# print(test.withdraw().json())
# print(test.update_name().json())
print(test.get_userinfo().json())













# res = {'code': 0, 'msg': 'OK', 'data': {'id': 2074984, 'leave_amount': 0.0, 'mobile_phone': '13012341230', 'reg_name': '小柠檬', 'reg_time': '2020-08-12 22:28:00.0', 'type': 1}, 'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
# r = jsonpath(res,"$..id"[0])
# print(r[0],type(r[0]))
