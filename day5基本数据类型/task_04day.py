"""
============================
Author:柠檬班-木森
Time:2020/7/4   11:50
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""

"""
一、现在有一个列表 li2=[1，2，3，4，5]
     第一步：请通过三行代码将上面的列表，改成这个样子 li2 = [0，1，2，3，66，5，11，22，33]，
     第二步：对列表进行升序排序 （从小到大）
     第三步：将列表复制一份进行降序排序（从大到小）
"""
li2 = [1, 2, 3, 4, 5]
# 第一步
li2.insert(0, 0)  # 在最前面加入0
li2[4] = 66
li2.extend([11, 22, 33])  # 在最后加入三个元素

print(li2)
# 第二步：从小到大排序
li2.sort()
print(li2)
# 第三步：从大到小排序
li3 = li2.copy()
li3.sort(reverse=True)
print(li3)

"""
二、定义一个空列表user=[],   分别提示用户输入，姓名，年龄，身高，用户输入完之后，
    将输入的信息作为添加的列表中保存，然后按照一下格式输出：
    用户的姓名为：xxx,年龄为：xxx,  身高为：xxx  ,请仔细核对
"""
user = []
name = input("请输入姓名：")
age = input("请输入年龄：")
height = input("请输入身高：")
user.extend([name, age, height])
print('用户的姓名为：{},年龄为：{},身高为：{:.2f},请仔细核对'.format(name, age, float(height)))

"""
三、 将字符串中的单词位置反转，“hello xiao mi” 转换为 “mi xiao hello”
（提示：通过字符串分割，拼接，列表反序等知识点来实现）
"""
s1 = "hello xiao mi"
li = s1.split(" ")
li.reverse()
s2 = " ".join(li)
print(s2)

"""
四、字典的增删查改操作： 某比赛需要获取你的个人信息，编写一段代码要求如下：
        1、运行时分别提醒输入 姓名、性别、年龄 ，输入完了，请将数据通过字典存储起来，
        2、数据存储完了，然后输出个人介绍，格式如下: 我的名字XXX，今年XXX岁，性别XX，喜欢敲代码
        3、平台需要补足您的身高和联系方式；（分别输入身高和联系方式添加到字典中） 
        4、平台为了保护你的隐私，需要你删除你的联系方式（删除字典中的联系方式）；
"""
# 1、
name = input('请输入姓名：')
gender = input('请输入性别:')
age = input('请输入年龄：')
user_info = {"name": name, "gender": gender, "age": age}

# 2、
print('我的名字:{}，今年{}岁，性别:{}，喜欢敲代码'.format(user_info["name"], user_info["age"], user_info["gender"]))

# 3、
user_info['height'] = input('请输入身高：')
user_info['mobile_phone'] = input('请输入联系方式：')

# 4、
user_info.pop('mobile_phone')

# print(user_info)

