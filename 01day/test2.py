# -*- coding: utf-8 -*-
# @Time    : 2020/6/30 20:26
# @Author  : guoyunfei.0603
# @File    : test2.py

# a = 10
# b = 10
# print( a == b)

import random

# 生产131开通的手机号码
res = random.randint(100000000,900000000)
res2 = "131" + str(res)
print(res2)


# PHP is """the best" \tprogramming"language in 'the\norld
str1 = "PHP is \"\"\"the best\" \\tprogramming\"language in \'the\\norld"

print(str1)

# 100以内奇数和

sum1 = 0
for i in range(1,101):
    if i % 2 !=0:
        sum1 += i
print(sum1)

a = sum(range(1,100,2))
print(a)

# 替换 I 为 i
str2 = 'I love '
new_str = str2.replace('I','i')
print(new_str)

i = sum = 0

while i <= 4:
    sum += i
    i = i+1

print(sum)