# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 17:12
# @Author  : guoyunfei.0603
# @File    : test_requests.py

import requests

url = 'http://api.juheapi.com/japi/toh'
data = {'key': '57d46b7258fc47e14290c33537f23d36', 'v': '1.0', 'month': 10, 'day': 1}

r = requests.get(url,data)
print(r.json())
