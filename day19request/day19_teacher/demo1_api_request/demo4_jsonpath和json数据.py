"""
============================
Author:柠檬班-木森
Time:2020/8/11   21:38
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
jsonpath提取数据
安装：pip install  jsonpath



{
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 2071424,
        "leave_amount": 0,
        "mobile_phone": "13367822221",
        "reg_name": "小柠檬",
        "reg_time": "2020-08-08 11:20:10.0",
        "type": 1,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2020-08-11 20:32:47",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIwNzE0MjQsImV4cCI6MTU5NzE0OTE2N30.NVNAp3nSgU_EdVnJXdEetFir5_hBGMaYrKjYozqTX7Mlp2MwpiDQotvNeaHtrFCIMZPDJ-H3EI76M6EtdBmpoA"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}






"""
from jsonpath import jsonpath
import requests

# 登录的接口地址
url = "http://api.lemonban.com/futureloan/member/login"

# 登录的参数
params = {
    "mobile_phone": "13367822221",
    "pwd": "lemonban"
}

# 请求头
headers = {
    "X-Lemonban-Media-Type": "lemonban.v2"
}

# 发送请求
# 请求类型为 Content-Type：application/json,参数就应该使用json去传递
response = requests.post(url=url, json=params, headers=headers)
res = response.json()

# 通过字典键值对的方式获取
# token = res["data"]["token_info"]["token"]
# print(token)

# 通过jsonpath提取
# token = jsonpath(res,"$..token")
# print(token)

# token = jsonpath(res, "$[code]")
# print(token)
