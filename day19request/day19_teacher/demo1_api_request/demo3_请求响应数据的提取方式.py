"""
============================
Author:柠檬班-木森
Time:2020/8/11   21:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
响应对象response：

一、http响应码：response.status_code

二、返回的数据提取：
1、text属性（str）:获取的是原生的json字符串
2、content属性(bytes)：可以使用decode指定编码转换为字符串
3、json()方法(dict)：获取到的是json转换的字典/列表

{"code":1001,
"msg":"账号信息错误",
"data":null,
"copyright":"Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"}


json类型的数据和  python中数据的对比
      json        python       
{}:  对象           字典
[]:  数组           列表
空    null         None
布尔  false        False
      true         True


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

print(response.json())








