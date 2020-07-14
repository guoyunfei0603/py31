"""
============================
Author:柠檬班-木森
Time:2020/6/30   20:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
1、字符串拼接？
方式1：直接使用+进行拼接


2、字符串格式化输出
    1、format格式化输出:
    2、字符串的F表达式:
    3、%号格式化输出：
        %s: 表示为任意的类型占位
        %f: 为浮点数占位
        %d: 为数值类型占位
"""

# name = "我的名字叫木森,"
# age = "我今年18岁,"
# sex = "性别男"

# 方式1：直接使用+进行拼接
# user_info = name + age + sex
# print(user_info)

# 方式2：使用format格式化
# user_info2 = "{}{}{}".format(name, age, sex)
# print(user_info2)


# 需求1：编写一个自动生产收据的程序，
# 用户输入，姓名，费用类别，金额就可以输出如下格式的收据：
# 格式样本： 今天收到XXX同学，交来XXX费用，金额XXX，开此收据为凭证！
# name = input("请输入姓名：")
# info = input("请输入费用类别：")
# money = input("请输入金额：")

# 方式一:
# desc = "今天收到{}同学，交来{}费用，金额{}，开此收据为凭证！".format(name, info, money)
# print(desc)


# 方式二:
# desc2 = F"今天收到{name}同学，交来{info}费用，金额{money}，开此收据为凭证！"
# print(desc2)


# 方式三：
# desc3 = "今天收到%s同学，交来%s费用，金额%s，开此收据为凭证！" % (name, info, money)
# print(desc3)

# 方式四
# 不推荐
# desc4 = "今天收到" + name + "同学，交来" + info + "费用，金额" + money + "，开此收据为凭证！"
# print(desc2)


# 需求2：随机生产的小数，如何指定保留两位小数来显示在字符串中

# import random
#
# n1 = random.random()
# print("随机生产的小数为:{:.2f}".format(n1))
# print("随机生产的小数为:%.2f" % n1)


# 关于：input输入的注意点
#
# number = input("请输入数值:")
#
# print(number,type(number))

# 如何将input输入得内容转换为数值

number = int(input("请输入数值:"))

print(number,type(number))



# 作业题：随机生产一个数值，和用户输入的数值  进行乘法运算




