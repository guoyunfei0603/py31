"""
============================
Author:柠檬班-木森
Time:2020/8/11   21:51
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import requests
# 登录的接口地址
url = "http://api.lemonban.com/futureloan/member/login"

# 登录的参数
params = {
    "mobile_phone": "13367822221",
    "pwd": "lemonban11"
}

# 请求头
headers = {
    "X-Lemonban-Media-Type":"lemonban.v2"
}


# 发送请求
# 请求类型为 Content-Type：application/json,参数就应该使用json去传递
response = requests.post(url=url,json=params,headers =headers)
res = response.text
print(res)
# import json
# 把json字符串中转换为python对应的数据
# res = json.loads(res)
# print(res,type(res))


res2 = response.json()

