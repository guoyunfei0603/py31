"""
============================
Author:小白31
Time:2020/7/19 21:40
E-mail:1359239107@qq.com
============================
"""
'''
第三题：之前上课讲了一个注册功能的案例，再之前案例的功能上进行升级，
要求：把所有用户数据放到文件中进行保存，数据存储的格式不限，原来的案例代码如下

提示：
每次运行程序，先去文件中读取所有注册过的用户数据，
程序运行完之后，将所有的用户数据再次写入到文件
可以把保存账号的列表转为字符串直接写入文件，读出来的时候，再把字符串转换为列表
'''
# users = [
#     {"uid": "py01", "pwd": "lmb01"},
#     {"uid": "py02", "pwd": "lmb02"},
# ]
from day9文件操作和模块导入.home_work2类 import test_data

id = input("请输入账号：")
pwd = input("请输入密码：")
pwd2 = input("请再次确认密码：")

read_data = test_data().read_data('data3.txt')
# print(read_data)

# 遍历所有的账号
for u in read_data:
    # 判断账号是否已经被注册
    if id == u["uid"]:
        print("该账号已经被注册！")
        break
else:
    # 如果账号没有注册，那么for循环中的break不会执行。则会执行for对应的else语句
    print("该账号可以注册，继续判断密码！")
    # 判断两次密码是否一致
    if pwd == pwd2:
        print("注册成功！")
    # 写到data3.txt里面
    #     todo 格式有点问题，，后期优化吧
        with open('data3.txt','a',encoding='utf-8') as f:
            f.write(str({"uid": id, "pwd": pwd}))
    else:
        print("两次输入的密码不一致")
