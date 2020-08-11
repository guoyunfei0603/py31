"""
============================
Author:柠檬班-木森
Time:2020/8/11   20:30
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
常见的接口请求参数类型：


1、查询字符串参数：常用于get请求（其他的请求方法用的少），参数会直接拼接在url地址后面
    requests发送请求，传递查询字符串参数，要使用params

2、json类型的参数：
     请求参数类型为 Content-Type：application/json,
     requests发送请求，传递json参数，就应该使用json去传递

3、表单类型的参数
    请求参数类型：content-type: application/x-www-form-urlencoded
    requests发送请求，传递表单参数，就应该使用data去传递

4、文件上传：
    请求参数类型：content-type: multipart/form-data
    文件参数要使用files进行传递
    文件参数的组装：
        {"参数名": ("文件名", open以rb模式打开文件, "文件类型")}
        [("参数名", ("文件名", open以rb模式打开文件, "文件类型"))]
"""

import requests
# --------------------查询字符串参数传递-----------------------------
# # 查询字符串参数的传递：
# url = "http://api.lemonban.com/futureloan/loans"
#
# # 请求参数
# params = {
#     "pageIndex": 1,
#     "pageSize": 20
# }
# # 请求头
# headers = {
#     "X-Lemonban-Media-Type": "lemonban.v2"
# }
#
# response = requests.get(url=url, params=params, headers=headers)
#
# print(response.text)


# ----------------------json格式的参数传递------------------------------
# # 注册的接口地址
# url = "http://api.lemonban.com/futureloan/member/register"
# # 参数
# params = {
#     "mobile_phone": "13367822666",
#     "pwd": "lemonban"
# }
# # 请求头
# headers = {
#     "X-Lemonban-Media-Type": "lemonban.v2"
# }
#
# response = requests.post(url=url,json=params,headers=headers)
# print(response.text)


# ------------------------表单类型参数的传递----------------------------------
# # 接口地址
# url = "https://www.ketangpai.com/UserApi/login"
# # 参数
# params = {
#     "email": "3247119728@qq.com",
#     "password": "nmb123321",
#     "remember": 0
# }
#
# response = requests.post(url=url, data=params)
#
# print(response.json())


# -----------------------文件上传---------------------------------
# 上传文件的接口地址（老师本地的，你们无法访问）
# url = "http://127.0.0.1:5000/upload"
# # 请求的参数
# params = {
#     "nickname": "1122",
#     "age": 18,
#     "sex": "男"
# }
# file = {
#     "pic": ("jiayouya.gif", open("jiayouya.gif", "rb"), "image/gif")
# }
# #
# res = requests.post(url=url, data=params, files=file)
# print(res.json())
