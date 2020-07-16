"""
============================
Author:柠檬班-木森
Time:2020/7/14   14:11
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import random

"""
1、实现剪刀石头布游戏，提示用户输入要出的拳 ：石头（1）／剪刀（2）／布（3）/退出（4） 电脑随机出拳比较胜负，显示 用户胜、负还是平局。
（提示：while循环加条件判断，做判断时建议先分析胜负的情况）
user   random
1        2     1-2  = -1 
2        3     2-3  = -1
3        1     3- 1 =  2

"""
# 第一题
print('---石头剪刀布游戏开始----')
print('请按下面提示出拳：')
# 创建一个列表来存储 石头 剪刀 布
li = ['石头', '剪刀', '布']
while True:
    print('石头【1】 剪刀【2】 布【3】 结束游戏【4】')
    # 用户输入数字
    user_num = int(input('请输入你的选项：'))
    # 电脑随机生成数字
    r_num = random.randint(1, 3)
    if 1 <= user_num <= 3:
        # 判断用户和电脑是否相等
        if r_num == user_num:
            info = '您的出拳为:{}，电脑出拳:{}，平局'.format(li[user_num - 1], li[r_num - 1])
            print(info)
        # 判断用户胜利的情况
        elif (user_num - r_num) == -1 or (user_num - r_num) == 2:
            info = '您的出拳为:{}，电脑出拳:{}，您赢了'.format(li[user_num - 1], li[r_num - 1])
            print(info)
        else:
            info = '您的出拳为:{}，电脑出拳:{}，您输了\n'.format(li[user_num - 1], li[r_num - 1])
            print(info)
        # 比较胜负
    elif user_num == 4:
        # 用户输入4，游戏结束
        print('游戏结束')
        break
    else:
        print('您出拳有误，请按规矩出拳')

print("--------------------第2题-------------------------------")
"""
2、通过定义一个计算器，运行程序提示用户输入数字1，数字2，然后再提示用户选择 ：  
 加【1】    减【2】    乘【3】      除【4】，
根据不同的选择完成不同的计算 ，然后打印结果

"""
print('欢迎使用计算器')
a = int(input('请输入数字1:'))
b = int(input('请输入数字2:'))
print('功能提示:【1】加 【2】减【3】乘 【4】除')
num = input('请选择：')
if num == '1':
    print("相加的结果为：{}".format(a + b))
elif num == '2':
    print("相减的结果为：{}".format(a - b))
elif num == '3':
    print("相乘的结果为：{}".format(a * b))
elif num == '4':
    print("相除的结果为：{}".format(a / b))
else:
    print('没有此选项！')

print("-------------------------第3题---------------------------")
# 3、请获取下面数据中的token，和reg_name
data = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 74711,
        "leave_amount": 29600.0,
        "mobile_phone": "13367899876",
        "reg_name": "小柠檬666",
        "reg_time": "2019-12-13 11:12:53.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2019-12-30 22:28:57",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjc0NzExLCJleHAiOjE1Nzc3MTYxMzd9.eNMtnEWr57iJoZRf2IRsGDWm2GKj9LZc1J2SGRprAwOk7EPoJeXSjJwdh0pcVVJygHmsbh1TashWqFv1bvCVZQ"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2019 湖南省零檬信息技术有限公司 All Rights Reserved"
}
# 获取token
token = data["data"]["token_info"]["token"]
# 获取reg_name
reg_name = data["data"]["reg_name"]
print(token)
print(reg_name)
print("-------------------------第4题---------------------------")
"""
第4题：当前有一个列表 li = [1,21,33,221,432,121,44,21,22,44,1,221],请完成如下要求！
    1、请先去除列表中的重复元素
    2、对去重后的列表进行升序排序
    3、遍历排序后列表，将元素为偶数的元素，添加到一个新列表中
"""
li = [1, 21, 33, 221, 432, 121, 44, 21, 22, 44, 1, 221]
# 1、去重
li = list(set(li))

# 2、排序
li.sort()

# 3、找偶数
new_list = []
for i in li:
    if i % 2 == 0:
        new_list.append(i)

print(new_list)

print("-------------------------第5题---------------------------")
"""
第5题、运行程序，提示用户依次输入三个整数x,y,z，请把这三个数由小到大输出。
"""
x = int(input('输入数字x：'))
y = int(input('输入数字y：'))
z = int(input('输入数字z：'))
num_list = [x, y, z]
# 从小到大排序
num_list.sort()
# 遍历输出
for num in num_list:
    print(num)

print("-------------------------第6题---------------------------")
"""
第6题、编写一个程序，使用for循环输出0-100（包括0和100）之间的偶数
"""
for i in range(101):
    if i % 2 == 0:
        print(i)

print("-------------------------第7题---------------------------")
"""
第7题、当前有一个字典｛"a":1,"b":22,"c":3,"d":4,"e":5 },
    请修改字典中所有键值对的值，新的值为原来的值乘10
"""
dic = {"a": 1, "b": 22, "c": 3, "d": 4, "e": 5}
for i in dic:
    dic[i] = dic[i] * 10

print(dic)
