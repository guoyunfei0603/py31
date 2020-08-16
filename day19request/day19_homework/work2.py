"""
============================
Author:小白31
Time:2020/8/12 23:10
E-mail:1359239107@qq.com
============================
"""
# 2、选做题：尝试（请求头使用X-Lemonban-Media-Type":"lemonban.v2），
# 去请求需要鉴权的充值接口（提示：要先登录，提取token，按接口文档要求加上token才能通过鉴权）

import requests
from jsonpath import jsonpath


class test_api2():
    # 域名
    url = 'http://api.lemonban.com/futureloan'

    # 请求头
    def headers_v2(self):
        headers_v2 = {"X-Lemonban-Media-Type": "lemonban.v2",
                      "content-type": "application/json"
                      }

        return headers_v2

    # 登录接口
    def login(self):
        login_url = self.url + "/member/login"
        data = {"mobile_phone": "13012341230", "pwd": "lemon123456"}

        res = requests.post(url=login_url, json=data, headers=self.headers_v2())
        return res
        # return jsonpath(res.json(), "$..token")
        # return res.json()["data"]["token_info"]["token"]

    # 充值接口
    def recharge(self):
        recharge_url = self.url + "/member/recharge"
        # 获取登录后的id也就是member_id
        id = jsonpath(self.login().json(),"$..id")
        # 测试数据
        data = {"member_id": id[0], "amount": "50000.00"}
        # token
        token = jsonpath(self.login().json(),"$..token")
        auth = {"Authorization": "Bearer {}".format(token[0])}

        header = self.headers_v2()
        header.update(auth) # 添加一个字典auth
        res = requests.post(url=recharge_url, json=data, headers=header)

        return res.json()

t = test_api2()
# print(t.login().json())
print(t.recharge())

# print(t.recharge())
# {'code': 0, 'msg': 'OK',
#  'data': {'id': 2074984, 'leave_amount': 1580.0, 'mobile_phone': '13012341230', 'reg_name': '小白',
#           'reg_time': '2020-08-12 22:28:00.0', 'type': 1,
#           'token_info': {'token_type': 'Bearer', 'expires_in': '2020-08-12 23:21:10',
#                          'token': 'eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwNzQ5ODQsImV4cCI6MTU5NzI0NTY3MH0.Cs2qobmeH9A1fBo2OXOelbuJGgz1Askgx47-xUg3mOugCJ3KW8cG4MXoAydyDMEveU-Ha8_x0GluijZUuIrTWQ'}},
#  'copyright': 'Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved'}
