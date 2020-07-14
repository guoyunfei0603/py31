# -*- coding: utf-8 -*-
# @Time    : 2020/7/9 20:36
# @Author  : guoyunfei.0603
# @File    : day6笔记.py

'''
while 循环：
定义：
while 循环条件：
    循环体

'''

'''
需求 实现一个注册的小程序代码：
1. 用户输入账号id，密码pwd，再次确认密码pwd
2. 判断该账号是否已经注册，已注册，打印账号被注册
3. 判断两次的密码是否一致，不一致，打印两次密码不一致
4. 上面两个判断都通过则注册成功（注册成功之后需要将账号和密码保存到列表中）
'''

user = [{"id": "py01", "pwd": "123456"},
        {"id": "py02", "pwd": "123456"},
        {"id": "py03", "pwd": "123456"}]

id = input("请输入账号：")
pwd = input("请输入密码：")
pwd2 = input("请再次确认密码：")


for i in user: # 遍历的结果是字典
        if id == i['id']:
                print("账号已被注册！")
                break
else:
        if pwd == pwd2:
                print("注册成功！")
                user.append({"id":id,"pwd":pwd})
        else:
                print("两次密码不一致！")
print(user)
