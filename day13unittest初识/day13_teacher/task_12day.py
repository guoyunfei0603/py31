"""
============================
Author:柠檬班-木森
Time:2020/7/25   11:53
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
1、通过继承定义如下三个类：PhoneV1,PhoneV2,PhoneV3
   PhoneV1：
        类属性：attr = "移动电话",  
        实例属性 name(品牌型号),price(价格),（year）生产年份
        方法：打电话
    
   PhoneV2：
        类属性：attr = "移动电话"，
        实例属性 name(品牌型号),price(价格),（year）生产年份， 摄像头像素(pixel)
        方法：打电话 ,听音乐，发短信，拍照
        
   PhoneV2：
        类属性：attr = "移动电话"
        实例属性 name(品牌型号),price(价格),（year）生产年份， 摄像头像素(pixel),屏幕大小(screen)
        方法：打电话 ,听音乐，发短信，拍照, 看视频
    
2、有一组数据，如下格式：
{'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过','excepted': '通过'},

定义一个如下的类，
请通过setattr将上面字典中的键值对，分别设置为类的属性和属性值，
键作为属性名，对应的值作为属性值
class CaseData:
    pass
    
3、复习面向对象的知识点（整理笔记）
    
"""


# 第一题
class PhoneV1(object):
    attr = "移动电话"

    def __init__(self, name, price, year):
        # 调用父类的方法，进行初始化
        self.name = name
        self.price = price
        self.year = year

    def call_phone(self):
        print(f"{self.name}使用了打电话的功能")


class PhoneV2(PhoneV1):

    def __init__(self, pixel, name, price, year):
        # 调用父类的方法，进行初始化
        super().__init__(name, price, year)
        self.pixel = pixel

    def music(self, ):
        print(f"{self.name}使用了打听音乐的功能")

    def send_msg(self):
        print(f"{self.name}使用了发短信的功能")

    def photograph(self):
        print(f"{self.name}使用了拍照的功能")


class PhoneV3(PhoneV2):
    def __init__(self, screen, pixel, name, price, year):
        # 调用父类的方法，进行初始化
        super().__init__(pixel, name, price, year)
        self.screen = screen

    def video(self):
        print(f"{self.name}使用了看视频的功能")


# ==================第二题========================

data = {'case_id': 1, 'method': 'post', 'url': '/member/login', 'data': '123', 'actual': '不通过', 'excepted': '通过'}


class CaseData:
    pass


# 答案一：设置为类属性和属性值
for k, v in data.items():
    setattr(CaseData, k, v)
# 打印类的所有属性
print(CaseData.__dict__)

# 答案二：创建一个对象，设置为对象的属性和属性值
case = CaseData()
for k, v in data.items():
    setattr(case, k, v)
# 打印对象的所有属性
print(case.__dict__)












# 以上两种解答方法都给分哈
"""
git init
git add ./*
git commit -m "first commit"
git remote add origin https://github.com/musen123/unittestreport.git
git push -u origin master
  
git config --global user.name "Lemon-Test-Official"             

"""