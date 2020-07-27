"""
============================
Author:柠檬班-木森
Time:2020/7/25   10:18
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
需求V1：实现一个初始版的手机类（大哥大）
      只能打电话

需求V2：实现一个定义功能机类
     打电话，听音乐，发短信

需求V3：实现一个智能手机类
     打电话，听音乐，发短信,看视频，玩游戏、手机支付、视频通话）


"""


# # 1995
# class BasePhone:
#
#     def __init__(self, name):
#         self.name = name
#
#     def call_phone(self):
#         print(f"{self.name}使用了打电话的功能")
#
#
# # 2002
# class PhoneV2(object):
#     def __init__(self, name):
#         self.name = name
#
#     def call_phone(self):
#         print(f"{self.name}使用了打电话的功能")
#
#     def music(self):
#         print(f"{self.name}使用了打听音乐的功能")
#
#     def send_msg(self):
#         print(f"{self.name}使用了打发短信的功能")
#
#
# # 2009
# class PhoneV3(object):
#     def __init__(self, name):
#         self.name = name
#
#     def call_phone(self):
#         print(f"{self.name}使用了打电话的功能")
#
#     def music(self):
#         print(f"{self.name}使用了打听音乐的功能")
#
#     def send_msg(self):
#         print(f"{self.name}使用了打发短信的功能")
#
#     def pay(self):
#         print(f"{self.name}使用了打支付的功能")
#
#     def game(self):
#         print(f"{self.name}使用了玩游戏的功能")

# ---------------------继承模式-----------------------------

class BasePhone(object):

    def __init__(self, name):
        self.name = name

    def call_phone(self):
        print(f"{self.name}使用了打电话的功能")


class PhoneV2(BasePhone):

    def music(self):
        print(f"{self.name}使用了打听音乐的功能")

    def send_msg(self):
        print(f"{self.name}使用了打发短信的功能")


# 2009
class PhoneV3(PhoneV2):
    def pay(self):
        print(f"{self.name}使用了打支付的功能")

    def game(self):
        print(f"{self.name}使用了玩游戏的功能")


# PhoneV3 --->  PhoneV2  --> BasePhone  --->object
p1 = BasePhone("大哥大")
p1.call_phone()

p2 = PhoneV2("老人机")
p2.call_phone()
p2.send_msg()
p2.music()


p3 = PhoneV3('huawei')
p3.pay()
p3.call_phone()
p3.send_msg()
p3.music()
p3.game()
