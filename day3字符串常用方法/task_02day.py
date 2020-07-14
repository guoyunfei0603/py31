"""
============================
Author:柠檬班-木森
Time:2020/7/1   13:40
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
import random

# 第一题：现在有变量 a = ‘hello’,b = ‘python18’  c = ‘!’
# 通过相关操作变成一个字符串：'hello python18 !'（注意点:转换之后单词之间有空格）
a = 'hello'
b = 'python18'
c = '!'
str1 = '{} {} {}'.format(a, b, c)
print(str1)

# 第二题：卖橘子的计算器：写一段代码，提示用户输入橘子的价格（整数）
# 然后随机生成购买的斤数（5到10斤之间的整数），最后打印出应该支付的金额！
#
price = int(input("请输入橘子价格:"))
num = random.randint(5, 10)
print('购买{}斤橘子的金额为：{}'.format(num, price * num))

# 第三题: 请随机生成一个131开头的手机号码。
phone = random.randint(13100000000, 13199999999)
# 生成的是数值类型，也可以转换为字符串
print(phone, str(phone))

# 第四题 ：请定义一个字符串，并通过print打印字符串，打印出来字符串的内容如下
# PHP is the best""" \tprogramming"language in 'the\norld


str4 = 'PHP is the best""" \\tprogramming"language in \'the\\norld'
print(str4)
