"""
============================
Author:柠檬班-木森
Time:2020/7/9   20:48
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
需求：实现一个注册的小程序代码，
    1、用户输入账号id，密码pwd，再次确认密码pwd,
    2、判断该账号是否已注册，已注册，打印账号被注册，
    3、判断两次的密码是否一致，不一致，打印两次密码不一致
    4、上面两个判断都通过则注册成功（注册成功之后需要将账号和密码保存到列表中）
    
输入，条件判断，for循环，输出，列表的操作

for 

for —— else:

for i in range(100):
    循环体
else:
    for对应的else语句，for循环正常遍历结束的时候回执行，
    (如果for是通过break来结束循环的则不会执行对应else)


"""
users = [
    {"uid": "py01", "pwd": "lmb01"},
    {"uid": "py02", "pwd": "lmb02"},
    {"uid": "py03", "pwd": "lmb02"},
    {"uid": "py04", "pwd": "lmb02"},
    {"uid": "py05", "pwd": "lmb02"}
]

id = input("请输入账号：")
pwd = input("请输入密码：")
pwd2 = input("请再次确认密码：")
# 遍历所有的账号
for u in users:
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
        # 帮输入的账号密码已字典的形式加入道users中
        users.append({"uid": id, "pwd": pwd})
    else:
        print("两次输入的密码不一致")

# u = {"uid": "py01", "pwd": "lmb01"}
# res = u['pwd']
# print(res)
