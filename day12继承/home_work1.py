"""
============================
Author:小白31
Time:2020/7/26 17:23
E-mail:1359239107@qq.com
============================
"""
'''
1、通过继承定义如下三个类：PhoneV1,PhoneV2,PhoneV3
   PhoneV1：
        类属性：attr = "移动电话",  
             实例属性 name(品牌型号),price(价格),（year）生产年份
        方法：打电话
    
   PhoneV2：
        类属性：attr = "移动电话"，
        实例属性 name(品牌型号),price(价格),（year）生产年份， 摄像头像素(pixel)
             方法：打电话 ,听音乐，发短信，拍照
        
   PhoneV3：
        类属性：attr = "移动电话"
             实例属性 name(品牌型号),price(价格),（year）生产年份， 摄像头像素(pixel),屏幕大小(screen)
             方法：打电话 ,听音乐，发短信，拍照, 看视频
'''


class PhoneV1:
    attr = '移动电话'

    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year

    def call_phone(self):
        print("{}可以打电话".format(self.name))


class PhoneV2(PhoneV1):
    def __init__(self, name, price, year, pixel):
        super().__init__(name, price, year)
        # 实例属性赋值
        # 继承父类的__init__方法，拓展一个属性
        self.pixel = pixel

    # 方法：打电话, 听音乐，发短信，拍照
    def music(self):
        print(f"{self.name}可以听音乐")

    def send_msg(self):
        print(f"{self.name}可以发送短信")

    def picture(self):
        print(f"{self.name}可以拍照")


class PhoneV3(PhoneV2):
    def __init__(self, name, price, year, pixel, screen):
        super().__init__(name, price, year, pixel)
        self.screen = screen

    # 方法：打电话, 听音乐，发短信，拍照, 看视频

    def video(self):
        print(f"{self.name}可以看视频")

p1 = PhoneV1("小米1",1999,2008)
p2 = PhoneV2("小米2", 2999, 2009, 20000)
p3 = PhoneV3("小米3",3999,2010,50000,6)

p1.call_phone()
p2.music()
p3.send_msg()