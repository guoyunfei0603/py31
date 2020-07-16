# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 21:05
# @Author  : guoyunfei.0603
# @File    : test.py

data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}

for i, j in data.items():

    if i == 'data':

        for a, b in j.items():

            if a == 'reg_name':

                print(a, b)

            elif a == 'token_info':

                for c, d in b.items():

                    if c == 'token':
                        print(c, d)
