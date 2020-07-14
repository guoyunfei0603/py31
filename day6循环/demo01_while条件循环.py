"""
============================
Author:柠檬班-木森
Time:2020/7/9   20:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
while循环：

语法：

while 条件:
    循环体
    
    
break：强制性的跳出循环

continue: 中止当前本轮循环，开启下一轮循环(执行到continue，直接回到条件判断的地方)


pass:没有任何语义，执行带pass直接通过，通常用来占位


"""
#  案例一：
# num = input("请输入是否考上清华：是请输入1，否请输入2:")
# while num == "2":
#     print("继续考......")
#     num = input("请输入是否考上清华：是请输入1，否请输入2:")
#
# print("从循环中出来了")


# 案例二：打印100遍hello python

# n = 1
# while n <= 100:
#     print(f"这个是第{n}遍:hello python")
#     n = n + 1
#
# print("从循环中出来了")


# 案例三：登录
# user = "py31"
# pwd = "lemonban"
#
# while True:
#     username = input("请输入账户名：")
#     password = input("请输入密码：")
#
#     if user == username and pwd == password:
#         print("恭喜：登录成功！")
#         # 使用break跳出循环
#         break
#
#     else:
#         print("账号或者密码错误！")
#
# print("-----------------while循环外面的代码------------------")


#  案例四：通过循环去打印1-10，其中5不用打印
#
# n = 0
# while n < 10:
#     n = n + 1
#
#     if n == 5:
#         pass
#     else:
#         print(n)

n = 0
while n < 10:
    n = n + 1

    if n == 5:
        continue

    print(n)
    print(f"--{n}--{n}-")





