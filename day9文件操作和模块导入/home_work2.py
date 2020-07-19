"""
============================
Author:小白31
Time:2020/7/19 20:58
E-mail:1359239107@qq.com
============================
"""
'''
# 文件中数据
url:www.baidu.com,mobilephone:13760246701,pwd:123456
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
url:www.baidu.com,mobilephone:15678934551,pwd:234555
​
# 要求一： 请把这些数据读取出来，到并且存到list中，格式如下
[
{'url': 'www.baidu.com', 'mobilephone': '13760246701', 'pwd': '123456'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'},
{'url': 'www.baidu.com', 'mobilephone': '15678934551', 'pwd': '234555'}
]
'''
with open('data2.txt','r',encoding='utf-8')as file:
    # 处理 \n
    f = file.readlines()
    new_list = []

    for i in f:
        new_str = i.replace('\n', '')

        new_list.append(new_str)
    print(new_list)

t1 = []
for i in new_list:
    s1 = i.split(',')
    t1.append(s1)

print(t1)

t2 = []
for item in t1:
    for j in item:
        s2 = i.split(',')
        t2.append(s2)
print(t2)

dic = t2[0][]