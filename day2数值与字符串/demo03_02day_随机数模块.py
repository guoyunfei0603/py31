"""
============================
Author:柠檬班-木森
Time:2020/6/30   20:09
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
"""
随机数模块

需求1：随机生产一个1，1000之间的整数

需求2：随机生产一个0-1之间的小数

需求3：如何生产指定范围的小数？1，1000
"""

import random

# 随机生产一个整数
number = random.randint(1, 1000)
# print(number)

# 随机生产一个0-1之间的小数
number2 = random.random()
# print(number2)

# 随机生产一个1-1000之间的小数
res = random.randint(1, 999) + random.random()

# print(res)


#  思考：如何生产一个8位的整数?
res2 = random.randint(10000000, 99999999)
print(res2)


# 作业：随机生产一个131开头的手机号码？

# 13100000000


"""
[1,100] :1-100这个区间，包含1和100的
(1,100] :1-100这个区间，不包含1，包含100的
(1,100) :1-100这个区间，不包含1，不包含100的
[1,100) : 1-100这个区间，包含1，不包含100的

"""
