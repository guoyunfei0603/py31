"""
============================
Author:柠檬班-木森
Time:2020/8/1   9:49
E-mail:3247119728@qq.com
Company:湖南零檬信息技术有限公司
============================
"""
#需求1、生成列表[0,1,2,3,4...9]
li = []
for i in range(10):
    li.append(i)

# print(li)
# print(list(range(10)))
# 需求生成列表：['page1','page2','page3'.......'page100']

li2 = []
for i in range(1, 101):
    li2.append("page{}".format(i))

# print(li2)

print("----------------li3------------------")
# 列表推导式实现
li3 =["page{}".format(i) for i in range(1,101)]
print(li3)


print("----------------li4------------------")
li4 =["musen" for i in range(1,101)]
print(li4)