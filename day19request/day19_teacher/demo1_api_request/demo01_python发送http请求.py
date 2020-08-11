"""
============================
Author:柠檬班-木森
Time:2020/8/11   20:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
requests:
安装命令： pip install requests

"""
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
    "X-Lemonban-Media-Type":"lemonban.v2"
}


# 发送一个登录的请求
# 请求类型为 Content-Type：application/json,参数就应该使用json去传递
response = requests.post(url=url,json=params,headers =headers)

# 获取接口返回的数据
print(response.text)








